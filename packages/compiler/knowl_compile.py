#!/usr/bin/env python3
"""Compile a knowl package into static pages, fragments, and indexes.

This is a deliberately small prototype compiler. It proves the architectural
shape: typed source files become a validated graph, then static artifacts.
"""

from __future__ import annotations

import argparse
import atexit
import hashlib
import html
import json
import os
import re
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import tomllib
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


WIKILINK_RE = re.compile(
    r"\[\[([A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)+(?:#[^\]|]+)?)(?:\|([^\n]*?))?\]\]"
)
MATH_RE = re.compile(
    r"(?s)(\$\$(.+?)\$\$|\\\[(.+?)\\\]|\\\((.+?)\\\)|(?<!\\)\$(?!\s)(.+?)(?<!\\)\$)"
)
DISPLAY_MATH_RE = re.compile(r"(?s)(\\\[(.+?)\\\]|\$\$(.+?)\$\$)")
DIAGRAM_ENV_RE = re.compile(r"\\begin\{(tikzpicture|tikzcd|CD)\}")
AGENT_STATUS_RE = re.compile(r"^\d+[smhd]\d+[smhd]\s+·\s+gpt-[^·]+·.*[↑↓↻Δ]")
OLD_HUGO_TOPIC_LINKS = [
    ("Analysis", "/analysis/"),
    ("Convex Analysis", "/convex-analysis/"),
    ("Foundations", "/shared-foundations/"),
    ("Linear Algebra", "/linear-algebra/"),
    ("Groups", "/algebra-groups/"),
    ("Rings", "/algebra-rings/"),
    ("Modules", "/algebra-modules/"),
    ("Fields & Galois Theory", "/algebra-fields-galois/"),
    ("Commutative Algebra", "/algebra-commutative/"),
    ("Category Theory", "/algebra-category-theory/"),
    ("Homological Algebra", "/algebra-homological/"),
    ("Representation Theory", "/algebra-representation-theory/"),
    ("Fiber Bundles", "/fiber-bundles/"),
    ("Lie Groups", "/lie-groups/"),
    ("Langlands Letter", "/langlands-letter/"),
    ("Shale's Paper", "/shale-paper/"),
    ("Posts", "/posts/"),
]


def find_vscode_node() -> Path | None:
    for node in sorted(Path.home().glob(".vscode-server/cli/servers/*/server/node"), reverse=True):
        if node.is_file():
            return node
    return None


def find_katex_module() -> Path | None:
    for module in sorted(Path.home().glob(".vscode-server/cli/servers/*/server/node_modules/katex/dist/katex.js"), reverse=True):
        if module.is_file():
            return module
    return None


def find_katex_assets_dir() -> Path | None:
    repo_dir = Path(__file__).resolve().parents[2]
    old_site_assets = repo_dir.parent / "knowlpedia" / "static" / "css"
    if (old_site_assets / "katex.min.css").is_file():
        return old_site_assets
    for assets_dir in sorted(Path.home().glob(".vscode-server/cli/servers/*/server/node_modules/katex/dist"), reverse=True):
        if (assets_dir / "katex.min.css").is_file():
            return assets_dir
    return None


def executable(name: str) -> str | None:
    return shutil.which(name)


def contains_diagram_environment(tex: str) -> bool:
    return bool(DIAGRAM_ENV_RE.search(tex))


def diagram_kind_from_fence(info: str) -> str | None:
    normalized = info.strip().lower()
    if normalized in {"tikz", "tikzpicture"}:
        return "tikz"
    if normalized in {"tikz-cd", "tikzcd"}:
        return "tikz-cd"
    if normalized in {"cd", "amscd"}:
        return "cd"
    return None


def diagram_kind_from_begin(line: str) -> str | None:
    if line.startswith(r"\begin{tikzpicture}"):
        return "tikz"
    if line.startswith(r"\begin{tikzcd}"):
        return "tikz-cd"
    return None


def diagram_end_for_kind(kind: str) -> str:
    if kind == "tikz-cd":
        return r"\end{tikzcd}"
    if kind == "cd":
        return r"\end{CD}"
    return r"\end{tikzpicture}"


class DiagramRenderer:
    def __init__(self) -> None:
        self._converter = executable("dvisvgm") or executable("pdftocairo")
        if self._converter and Path(self._converter).name == "dvisvgm" and executable("latex"):
            self._engine = executable("latex")
            self._engine_output = "dvi"
        else:
            self._engine = executable("tectonic") or executable("pdflatex")
            self._engine_output = "pdf"
        self._cache: dict[tuple[str, str], str] = {}

    @property
    def backend(self) -> str:
        if self._engine and self._converter:
            return "svg"
        return "source"

    def render(self, source: str, kind: str = "tikz") -> str:
        source = source.strip()
        cache_key = (kind, source)
        if cache_key in self._cache:
            return self._cache[cache_key]

        rendered: str | None = None
        if self._engine and self._converter:
            rendered = self._render_svg(source, kind)

        if rendered is None:
            rendered = self._render_source(source, kind)
        self._cache[cache_key] = rendered
        return rendered

    def _render_svg(self, source: str, kind: str) -> str | None:
        with tempfile.TemporaryDirectory(prefix="knowl-diagram-") as tmp:
            tmp_path = Path(tmp)
            tex_path = tmp_path / "diagram.tex"
            compiled_path = tmp_path / f"diagram.{self._engine_output}"
            svg_path = tmp_path / "diagram.svg"
            tex_path.write_text(self._document(source, kind), encoding="utf-8")

            if self._engine and Path(self._engine).name == "tectonic":
                command = [self._engine, "--outdir", str(tmp_path), str(tex_path)]
            else:
                command = [
                    self._engine,
                    "-halt-on-error",
                    "-interaction=nonstopmode",
                    tex_path.name,
                ]
            try:
                compile_result = subprocess.run(
                    command,
                    cwd=tmp_path,
                    text=True,
                    capture_output=True,
                    timeout=30,
                    check=False,
                )
            except Exception as exc:
                return self._render_error(source, kind, str(exc))

            if compile_result.returncode != 0 or not compiled_path.is_file():
                log = (compile_result.stdout + "\n" + compile_result.stderr).strip()
                return self._render_error(source, kind, log)

            try:
                if self._converter and Path(self._converter).name == "dvisvgm":
                    convert_command = [self._converter, "--bbox=min", str(compiled_path), "-o", str(svg_path)]
                    if compiled_path.suffix == ".pdf":
                        convert_command.insert(1, "--pdf")
                else:
                    convert_command = [self._converter, "-svg", str(compiled_path), str(svg_path)]
                convert_result = subprocess.run(
                    convert_command,
                    cwd=tmp_path,
                    text=True,
                    capture_output=True,
                    timeout=30,
                    check=False,
                )
            except Exception as exc:
                return self._render_error(source, kind, str(exc))

            if convert_result.returncode != 0 or not svg_path.is_file():
                log = (convert_result.stdout + "\n" + convert_result.stderr).strip()
                return self._render_error(source, kind, log)

            svg = svg_path.read_text(encoding="utf-8")
            svg = re.sub(r"<\?xml[^>]*>\s*", "", svg).strip()
            svg = re.sub(r"<!DOCTYPE[^>]*>\s*", "", svg).strip()
            diagram_hash = hashlib.sha256(source.encode("utf-8")).hexdigest()[:12]
            return (
                f'<figure class="diagram diagram-svg diagram-{escape_attr(kind)}" '
                f'data-diagram-hash="{diagram_hash}">'
                f'<div class="diagram-frame">{svg}</div>'
                "</figure>"
            )

    def _document(self, source: str, kind: str) -> str:
        body = source
        if kind == "tikz" and r"\begin{tikzpicture}" not in source:
            body = "\\begin{tikzpicture}\n" + source + "\n\\end{tikzpicture}"
        elif kind in {"tikz-cd", "tikzcd"} and r"\begin{tikzcd}" not in source:
            body = "\\begin{tikzcd}\n" + source + "\n\\end{tikzcd}"
        elif kind == "cd":
            if r"\begin{CD}" not in source:
                body = "\\begin{CD}\n" + source + "\n\\end{CD}"
            if not body.lstrip().startswith((r"\[", "$$")):
                body = "\\(\n\\displaystyle\n" + body + "\n\\)"

        return "\n".join(
            [
                r"\documentclass[tikz,border=8pt]{standalone}",
                r"\usepackage{amsmath,amssymb,amscd}",
                r"\usepackage{tikz}",
                r"\usepackage{tikz-cd}",
                r"\usetikzlibrary{arrows.meta,calc,cd,decorations.pathmorphing,matrix,positioning}",
                r"\begin{document}",
                body,
                r"\end{document}",
                "",
            ]
        )

    def _render_source(self, source: str, kind: str) -> str:
        return (
            f'<figure class="diagram diagram-source diagram-{escape_attr(kind)}">'
            "<figcaption>Diagram source</figcaption>"
            f"<pre><code>{html.escape(source)}</code></pre>"
            "</figure>"
        )

    def _render_error(self, source: str, kind: str, log: str) -> str:
        if not log:
            log = "Diagram renderer failed without diagnostic output."
        return (
            f'<figure class="diagram diagram-error diagram-{escape_attr(kind)}">'
            "<figcaption>Diagram render failed</figcaption>"
            f"<pre><code>{html.escape(source)}</code></pre>"
            "<details><summary>Render log</summary>"
            f"<pre><code>{html.escape(log[-6000:])}</code></pre>"
            "</details>"
            "</figure>"
        )


DIAGRAM_RENDERER = DiagramRenderer()


class MathRenderer:
    def __init__(self) -> None:
        self.backend = "tex"
        self._worker: subprocess.Popen[str] | None = None
        self._cache: dict[tuple[str, bool], str] = {}
        self._convert = None
        self._start_katex_worker()
        if self.backend == "katex":
            return

        try:
            from latex2mathml.converter import convert
        except Exception:
            return
        else:
            self.backend = "mathml"
            self._convert = convert

    def _start_katex_worker(self) -> None:
        node = find_vscode_node()
        katex_module = find_katex_module()
        worker = Path(__file__).with_name("katex_worker.cjs")
        if not node or not katex_module or not worker.is_file():
            return

        env = dict(os.environ)
        env["KATEX_MODULE"] = str(katex_module)
        try:
            self._worker = subprocess.Popen(
                [str(node), str(worker)],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
                text=True,
                encoding="utf-8",
                env=env,
            )
        except Exception:
            self._worker = None
            return
        self.backend = "katex"
        atexit.register(self.close)

    def close(self) -> None:
        if not self._worker:
            return
        try:
            self._worker.terminate()
        except Exception:
            pass
        self._worker = None

    def render(self, tex: str, display: bool) -> str:
        tex = tex.strip()
        if display and contains_diagram_environment(tex):
            kind = "cd" if "\\begin{CD}" in tex else "tikz-cd" if "\\begin{tikzcd}" in tex else "tikz"
            return DIAGRAM_RENDERER.render(tex, kind)

        cache_key = (tex, display)
        if cache_key in self._cache:
            return self._cache[cache_key]

        if self.backend == "katex":
            rendered = self._render_katex(tex, display)
            if rendered:
                self._cache[cache_key] = rendered
                return rendered

        if self.backend != "mathml" or self._convert is None:
            delimiter = "$$" if display else "$"
            rendered = html.escape(f"{delimiter}{tex}{delimiter}")
            self._cache[cache_key] = rendered
            return rendered

        try:
            mathml = self._convert(tex, display="block" if display else "inline")
        except Exception:
            delimiter = "$$" if display else "$"
            rendered = f'<span class="math-render-error">{html.escape(f"{delimiter}{tex}{delimiter}")}</span>'
            self._cache[cache_key] = rendered
            return rendered
        class_name = "math-display" if display else "math-inline"
        wrapper = "div" if display else "span"
        rendered = f'<{wrapper} class="{class_name} math-mathml">{mathml}</{wrapper}>'
        self._cache[cache_key] = rendered
        return rendered

    def _render_katex(self, tex: str, display: bool) -> str | None:
        if not self._worker or not self._worker.stdin or not self._worker.stdout:
            self.backend = "mathml" if self._convert else "tex"
            return None
        try:
            self._worker.stdin.write(json.dumps({"tex": tex, "display": display}) + "\n")
            self._worker.stdin.flush()
            line = self._worker.stdout.readline()
        except Exception:
            self.close()
            self.backend = "mathml" if self._convert else "tex"
            return None
        if not line:
            self.close()
            self.backend = "mathml" if self._convert else "tex"
            return None
        try:
            payload = json.loads(line)
        except json.JSONDecodeError:
            return None
        if "html" not in payload:
            return None
        class_name = "math-display math-katex" if display else "math-inline math-katex"
        wrapper = "div" if display else "span"
        return f'<{wrapper} class="{class_name}">{payload["html"]}</{wrapper}>'


MATH_RENDERER = MathRenderer()


@dataclass
class ValidationMessage:
    severity: str
    source: str
    message: str


@dataclass
class Knowl:
    id: str
    title: str
    kind: str
    summary: str
    aliases: list[str]
    domains: list[str]
    source_path: Path
    core_markdown: str
    core_data: list[dict[str, Any]] = field(default_factory=list)
    core_axioms: list[dict[str, Any]] = field(default_factory=list)
    sections: list[dict[str, Any]] = field(default_factory=list)
    relations: list[dict[str, Any]] = field(default_factory=list)
    anchors: set[str] = field(default_factory=set)
    content_hash: str = ""


def read_toml(path: Path) -> dict[str, Any]:
    with path.open("rb") as f:
        return tomllib.load(f)


def slug_to_relpath(knowl_id: str) -> Path:
    return Path(*knowl_id.split("/"))


def split_target(target: str) -> tuple[str, str | None]:
    if "#" not in target:
        return target, None
    base, anchor = target.split("#", 1)
    return base, anchor or None


def target_label(target: str) -> str:
    return target.split("#", 1)[0].split("/")[-1].replace("-", " ")


def target_href(target: str) -> str:
    base, anchor = split_target(target)
    href = "/" + str(slug_to_relpath(base)).replace("\\", "/") + "/"
    if anchor:
        href += "#" + anchor
    return href


def fragment_href(knowl_id: str) -> str:
    return "/fragments/" + str(slug_to_relpath(knowl_id)).replace("\\", "/") + "/core.html"


def escape_attr(value: str) -> str:
    return html.escape(value, quote=True)


def protect_math(text: str) -> tuple[str, dict[str, str]]:
    replacements: dict[str, str] = {}

    def replace(match: re.Match[str]) -> str:
        token = f"@@KNOWL_MATH_{len(replacements)}@@"
        if match.group(2) is not None:
            tex = match.group(2)
            display = True
        elif match.group(3) is not None:
            tex = match.group(3)
            display = True
        elif match.group(4) is not None:
            tex = match.group(4)
            display = False
        else:
            tex = match.group(5)
            display = False
        replacements[token] = MATH_RENDERER.render(tex, display)
        return token

    return MATH_RE.sub(replace, text), replacements


def restore_math(text: str, replacements: dict[str, str]) -> str:
    for token, rendered in replacements.items():
        text = text.replace(token, rendered)
    return text


def is_agent_status_line(line: str) -> bool:
    return bool(AGENT_STATUS_RE.match(line.strip()))


def parse_single_file(path: Path) -> Knowl:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("+++\n"):
        raise ValueError(f"{path} is missing TOML front matter")
    end = text.find("\n+++\n", 4)
    if end == -1:
        raise ValueError(f"{path} has unterminated TOML front matter")

    front_matter = text[4:end]
    body = text[end + 5 :].strip()
    meta = tomllib.loads(front_matter)
    return knowl_from_meta(meta, path, body)


def parse_bundle(path: Path) -> Knowl:
    meta = read_toml(path)
    bundle_dir = path.parent
    core_meta = meta.get("core", {})
    core_source = core_meta.get("source", "core.md")
    core_markdown = (bundle_dir / core_source).read_text(encoding="utf-8").strip()

    sections = []
    for section in meta.get("sections", []):
        section = dict(section)
        source_name = section.get("source")
        if not source_name:
            raise ValueError(f"{path}: section {section.get('id')} is missing source")
        source_path = bundle_dir / source_name
        section["source_path"] = str(source_path)
        if section.get("kind") == "tfae":
            section["payload"] = read_toml(source_path)
        elif section.get("kind") == "proof":
            section["payload"] = read_toml(source_path)
        else:
            section["markdown"] = source_path.read_text(encoding="utf-8").strip()
        sections.append(section)

    return knowl_from_meta(meta, path, core_markdown, sections=sections)


def knowl_from_meta(
    meta: dict[str, Any],
    source_path: Path,
    core_markdown: str,
    sections: list[dict[str, Any]] | None = None,
) -> Knowl:
    required = ["id", "title", "kind", "summary"]
    missing = [field_name for field_name in required if not meta.get(field_name)]
    if missing:
        raise ValueError(f"{source_path}: missing required fields: {', '.join(missing)}")

    core_meta = meta.get("core", {})
    knowl = Knowl(
        id=meta["id"],
        title=meta["title"],
        kind=meta["kind"],
        summary=meta["summary"],
        aliases=list(meta.get("aliases", [])),
        domains=list(meta.get("domains", [])),
        source_path=source_path,
        core_markdown=core_markdown,
        core_data=list(core_meta.get("data", [])),
        core_axioms=list(core_meta.get("axioms", [])),
        sections=sections or [],
        relations=list(meta.get("relations", [])),
    )
    knowl.anchors.add("section.core")
    for item in knowl.core_data:
        knowl.anchors.add(f"data.{item['id']}")
    for item in knowl.core_axioms:
        knowl.anchors.add(f"axiom.{item['id']}")
    for section in knowl.sections:
        section_id = section["id"]
        knowl.anchors.add(f"section.{section_id}")
        if section.get("kind") == "proof":
            proof = section["payload"]
            proof_id = proof["id"]
            knowl.anchors.add(f"proof.{proof_id}")
            for step in proof.get("steps", []):
                knowl.anchors.add(f"proof.{proof_id}.step.{step['id']}")

    hash_input = json.dumps(
        {
            "id": knowl.id,
            "title": knowl.title,
            "summary": knowl.summary,
            "core": knowl.core_markdown,
            "data": knowl.core_data,
            "axioms": knowl.core_axioms,
            "sections": serializable_sections(knowl.sections),
            "relations": knowl.relations,
        },
        sort_keys=True,
    ).encode("utf-8")
    knowl.content_hash = hashlib.sha256(hash_input).hexdigest()[:16]
    return knowl


def serializable_sections(sections: list[dict[str, Any]]) -> list[dict[str, Any]]:
    result = []
    for section in sections:
        item = {
            key: value
            for key, value in section.items()
            if key not in {"source_path"} and not isinstance(value, Path)
        }
        result.append(item)
    return result


def discover_knowls(content_dir: Path) -> list[Knowl]:
    knowls = []
    for path in sorted(content_dir.rglob("*.knowl.md")):
        knowls.append(parse_single_file(path))
    for path in sorted(content_dir.rglob("knowl.toml")):
        knowls.append(parse_bundle(path))
    return sorted(knowls, key=lambda k: k.id)


def render_inline(text: str, registry: dict[str, Knowl]) -> str:
    text, math_replacements = protect_math(text)
    escaped = html.escape(text)

    def replace_wikilink(match: re.Match[str]) -> str:
        target = html.unescape(match.group(1).strip())
        label = html.unescape(match.group(2).strip()) if match.group(2) else target_label(target)
        base, _ = split_target(target)
        class_name = "knowl"
        attrs = ""
        if base in registry:
            attrs = f' data-knowl="{escape_attr(fragment_href(base))}"'
        else:
            class_name = "missing-knowl"
        return (
            f'<a class="{class_name}" href="{escape_attr(target_href(target))}"'
            f'{attrs} aria-expanded="false">{html.escape(label)}</a>'
        )

    escaped = WIKILINK_RE.sub(replace_wikilink, escaped)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", escaped)
    return restore_math(escaped, math_replacements)


def render_paragraph(text: str, registry: dict[str, Knowl]) -> str:
    blocks: list[str] = []
    cursor = 0
    for match in DISPLAY_MATH_RE.finditer(text):
        before = text[cursor : match.start()].strip()
        if before:
            blocks.append(f"<p>{render_inline(before, registry)}</p>")
        blocks.append(MATH_RENDERER.render(match.group(2) or match.group(3), display=True))
        cursor = match.end()

    after = text[cursor:].strip()
    if after:
        blocks.append(f"<p>{render_inline(after, registry)}</p>")
    return "\n".join(blocks)


def render_markdown(markdown: str, registry: dict[str, Knowl]) -> str:
    lines = markdown.splitlines()
    out: list[str] = []
    i = 0
    list_mode: str | None = None
    in_code = False
    code_lines: list[str] = []

    def close_list() -> None:
        nonlocal list_mode
        if list_mode:
            out.append(f"</{list_mode}>")
            list_mode = None

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if is_agent_status_line(stripped):
            i += 1
            continue

        if in_code:
            if stripped.startswith("```"):
                out.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
                code_lines = []
                in_code = False
            else:
                code_lines.append(line)
            i += 1
            continue

        code_fence = re.match(r"^```\s*([A-Za-z0-9_-]+)?", stripped)
        if code_fence:
            diagram_kind = diagram_kind_from_fence(code_fence.group(1) or "")
            if diagram_kind:
                close_list()
                i += 1
                diagram_lines = []
                while i < len(lines) and not lines[i].strip().startswith("```"):
                    diagram_lines.append(lines[i])
                    i += 1
                if i < len(lines):
                    i += 1
                out.append(DIAGRAM_RENDERER.render("\n".join(diagram_lines), diagram_kind))
                continue

            close_list()
            in_code = True
            code_lines = []
            i += 1
            continue

        if not stripped:
            close_list()
            i += 1
            continue

        if stripped in {"\\[", "$$"}:
            close_list()
            delimiter = "\\]" if stripped == "\\[" else "$$"
            i += 1
            math_lines = []
            while i < len(lines) and lines[i].strip() != delimiter:
                math_lines.append(lines[i])
                i += 1
            if i < len(lines):
                i += 1
            out.append(MATH_RENDERER.render("\n".join(math_lines), display=True))
            continue

        single_line_display = re.match(r"^(?:\\\[(.+)\\\]|\$\$(.+)\$\$)$", stripped)
        if single_line_display:
            close_list()
            out.append(MATH_RENDERER.render(single_line_display.group(1) or single_line_display.group(2), display=True))
            i += 1
            continue

        raw_diagram_kind = diagram_kind_from_begin(stripped)
        if raw_diagram_kind:
            close_list()
            diagram_lines = [line]
            end_marker = diagram_end_for_kind(raw_diagram_kind)
            i += 1
            while i < len(lines):
                diagram_lines.append(lines[i])
                if lines[i].strip().startswith(end_marker):
                    i += 1
                    break
                i += 1
            out.append(DIAGRAM_RENDERER.render("\n".join(diagram_lines), raw_diagram_kind))
            continue

        heading = re.match(r"^(#{1,4})\s+(.+)$", stripped)
        if heading:
            close_list()
            level = len(heading.group(1))
            out.append(f"<h{level}>{render_inline(heading.group(2), registry)}</h{level}>")
            i += 1
            continue

        bullet = re.match(r"^-\s+(.+)$", stripped)
        if bullet:
            if list_mode != "ul":
                close_list()
                out.append("<ul>")
                list_mode = "ul"
            i += 1
            item_lines = [bullet.group(1)]
            while i < len(lines):
                continuation = lines[i]
                continuation_stripped = continuation.strip()
                if not continuation_stripped:
                    break
                if re.match(r"^-\s+", continuation_stripped) or re.match(r"^\d+\.\s+", continuation_stripped):
                    break
                if continuation.startswith(" ") or continuation.startswith("\t"):
                    item_lines.append(continuation_stripped)
                    i += 1
                    continue
                break
            out.append(f"<li>{render_inline(' '.join(item_lines), registry)}</li>")
            continue

        ordered = re.match(r"^\d+\.\s+(.+)$", stripped)
        if ordered:
            if list_mode != "ol":
                close_list()
                out.append("<ol>")
                list_mode = "ol"
            i += 1
            item_lines = [ordered.group(1)]
            while i < len(lines):
                continuation = lines[i]
                continuation_stripped = continuation.strip()
                if not continuation_stripped:
                    break
                if re.match(r"^-\s+", continuation_stripped) or re.match(r"^\d+\.\s+", continuation_stripped):
                    break
                if continuation.startswith(" ") or continuation.startswith("\t"):
                    item_lines.append(continuation_stripped)
                    i += 1
                    continue
                break
            out.append(f"<li>{render_inline(' '.join(item_lines), registry)}</li>")
            continue

        close_list()
        paragraph = [stripped]
        i += 1
        while i < len(lines):
            next_line = lines[i].strip()
            if (
                not next_line
                or next_line.startswith("#")
                or next_line.startswith("```")
                or next_line in {"\\[", "$$"}
                or is_agent_status_line(next_line)
                or re.match(r"^-\s+", next_line)
                or re.match(r"^\d+\.\s+", next_line)
            ):
                break
            paragraph.append(next_line)
            i += 1
        out.append(render_paragraph(" ".join(paragraph), registry))

    if in_code:
        out.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
    close_list()
    return "\n".join(out)


def render_ref(target: str, registry: dict[str, Knowl], label: str | None = None) -> str:
    base, _ = split_target(target)
    text = label or (registry[base].title if base in registry else target_label(target))
    attrs = ""
    class_name = "knowl"
    if base in registry:
        attrs = f' data-knowl="{escape_attr(fragment_href(base))}"'
    else:
        class_name = "missing-knowl"
    return (
        f'<a class="{class_name}" href="{escape_attr(target_href(target))}"'
        f'{attrs} aria-expanded="false">{html.escape(text)}</a>'
    )


def render_structured_core(knowl: Knowl, registry: dict[str, Knowl]) -> str:
    parts: list[str] = []
    if knowl.core_data:
        parts.append('<section class="semantic-block"><h3>Data</h3><ol>')
        for item in knowl.core_data:
            parts.append(
                f'<li id="data.{escape_attr(item["id"])}">'
                f'{render_inline(item["text"], registry)}'
                f'{render_refs(item.get("refs", []), registry)}</li>'
            )
        parts.append("</ol></section>")
    if knowl.core_axioms:
        parts.append('<section class="semantic-block"><h3>Axioms</h3><ol>')
        for item in knowl.core_axioms:
            parts.append(
                f'<li id="axiom.{escape_attr(item["id"])}">'
                f'{render_inline(item["text"], registry)}'
                f'{render_refs(item.get("refs", []), registry)}</li>'
            )
        parts.append("</ol></section>")
    return "\n".join(parts)


def render_refs(refs: list[str], registry: dict[str, Knowl]) -> str:
    if not refs:
        return ""
    links = ", ".join(render_ref(ref, registry) for ref in refs)
    return f' <span class="uses">uses {links}</span>'


def render_tfae(payload: dict[str, Any], registry: dict[str, Knowl]) -> str:
    parts = [f'<div class="tfae"><h3>{html.escape(payload.get("title", "Equivalent characterizations"))}</h3>']
    hypotheses = payload.get("hypotheses", [])
    if hypotheses:
        parts.append("<p><strong>Hypotheses.</strong> " + html.escape("; ".join(hypotheses)) + "</p>")

    items = payload.get("items", [])
    if items:
        parts.append('<div class="definition-switcher" role="tablist">')
        for idx, item in enumerate(items):
            active = " active" if idx == 0 else ""
            parts.append(
                f'<button type="button" class="switcher-tab{active}" '
                f'data-switch-target="{escape_attr(item["id"])}">{html.escape(item.get("label", item["id"]))}</button>'
            )
        parts.append("</div>")
        parts.append('<div class="tfae-items">')
        for idx, item in enumerate(items):
            hidden_attr = "" if idx == 0 else " hidden"
            parts.append(
                f'<article class="tfae-item" data-switch-panel="{escape_attr(item["id"])}"{hidden_attr}>'
                f'<h4>{html.escape(item.get("label", item["id"]))}</h4>'
                f'<p>{render_inline(item["statement"], registry)}</p>'
                f'{render_refs(item.get("refs", []), registry)}'
                "</article>"
            )
        parts.append("</div>")

    implications = payload.get("implications", [])
    if implications:
        parts.append("<h4>Implication notes</h4><ol>")
        for implication in implications:
            parts.append(
                "<li>"
                f'<code>{html.escape(implication["from"])}</code> '
                f'&rarr; <code>{html.escape(implication["to"])}</code>: '
                f'{render_inline(implication.get("proof", ""), registry)}'
                "</li>"
            )
        parts.append("</ol>")
    parts.append("</div>")
    return "\n".join(parts)


def render_proof(payload: dict[str, Any], registry: dict[str, Knowl]) -> str:
    proof_id = payload["id"]
    parts = [
        f'<article class="proof" id="proof.{escape_attr(proof_id)}">',
        f'<h3>{html.escape(payload["title"])}</h3>',
        f'<p>{render_inline(payload.get("summary", ""), registry)}</p>',
    ]
    if payload.get("proves"):
        parts.append(f'<p class="proof-proves">Proves {render_ref(payload["proves"], registry)}</p>')
    parts.append('<ol class="proof-steps">')
    for step in payload.get("steps", []):
        step_anchor = f'proof.{proof_id}.step.{step["id"]}'
        parts.append(f'<li class="proof-step" id="{escape_attr(step_anchor)}">')
        parts.append(f'<div class="proof-assertion">{render_inline(step["assertion"], registry)}</div>')
        justifications = step.get("justifications", [])
        if justifications:
            parts.append('<div class="proof-justifications">')
            for justification in justifications:
                target = justification["target"]
                if target.startswith("step:"):
                    step_id = target.split(":", 1)[1]
                    href = f"#proof.{escape_attr(proof_id)}.step.{escape_attr(step_id)}"
                    link = f'<a href="{href}">step {html.escape(step_id)}</a>'
                else:
                    link = render_ref(target, registry)
                parts.append(
                    f'<span class="justification">{html.escape(justification.get("type", "uses"))}: {link}</span>'
                )
            parts.append("</div>")
        parts.append("</li>")
    parts.append("</ol></article>")
    return "\n".join(parts)


def render_section(section: dict[str, Any], registry: dict[str, Knowl]) -> str:
    kind = section.get("kind")
    if kind == "tfae":
        return render_tfae(section["payload"], registry)
    if kind == "proof":
        return render_proof(section["payload"], registry)
    return render_markdown(section.get("markdown", ""), registry)


def render_relations(knowl: Knowl, registry: dict[str, Knowl]) -> str:
    if not knowl.relations:
        return ""
    parts = ['<section class="relations"><h2>Relations</h2><ul>']
    for relation in knowl.relations:
        note = relation.get("note")
        parts.append(
            "<li>"
            f'<code>{html.escape(relation["type"])}</code> '
            f'{render_ref(relation["target"], registry)}'
            f'{": " + render_inline(note, registry) if note else ""}'
            "</li>"
        )
    parts.append("</ul></section>")
    return "\n".join(parts)


def render_knowl_core(knowl: Knowl, registry: dict[str, Knowl]) -> str:
    body = [
        f'<div class="knowl-content" data-knowl-id="{escape_attr(knowl.id)}">',
        '<div class="knowl-header">',
        f'<strong>{html.escape(knowl.title)}</strong>',
        f'<a class="full-page-link" href="{escape_attr(target_href(knowl.id))}">full page</a>',
        '<button type="button" class="knowl-close" aria-label="Close">&times;</button>',
        "</div>",
        '<div class="knowl-body">',
        render_markdown(knowl.core_markdown, registry),
        render_structured_core(knowl, registry),
        "</div>",
        "</div>",
    ]
    return "\n".join(body)


def preload_template_targets(knowl: Knowl, registry: dict[str, Knowl]) -> list[str]:
    targets: list[str] = []

    def add(target: str) -> None:
        base, _ = split_target(target)
        if base in registry and base not in targets:
            targets.append(base)

    for target in wikilinks_in_text(knowl.core_markdown):
        add(target)
    for item in knowl.core_data + knowl.core_axioms:
        for target in item.get("refs", []):
            add(target)
    for relation in knowl.relations:
        add(relation["target"])
    for section in knowl.sections:
        if section.get("kind") == "tfae":
            for item in section["payload"].get("items", []):
                for target in item.get("refs", []):
                    add(target)
        elif section.get("kind") == "proof":
            payload = section["payload"]
            add(payload["proves"])
            for step in payload.get("steps", []):
                for justification in step.get("justifications", []):
                    add(justification["target"])
        else:
            for target in wikilinks_in_text(section.get("markdown", "")):
                add(target)

    return targets


def render_preload_templates(
    knowl: Knowl,
    registry: dict[str, Knowl],
    fragment_cache: dict[str, str] | None = None,
) -> str:
    templates = []
    for target in preload_template_targets(knowl, registry):
        fragment_url = fragment_href(target)
        fragment_html = fragment_cache[target] if fragment_cache else render_knowl_core(registry[target], registry)
        templates.append(
            f'<template data-knowl-fragment="{escape_attr(fragment_url)}">'
            f"{fragment_html}"
            "</template>"
        )
    return "\n".join(templates)


def render_page(
    knowl: Knowl,
    registry: dict[str, Knowl],
    package: dict[str, Any],
    fragment_cache: dict[str, str] | None = None,
) -> str:
    section_html = []
    for section in knowl.sections:
        open_attr = " open" if section.get("default_open") else ""
        section_html.append(
            f'<details class="knowl-section" id="section.{escape_attr(section["id"])}"{open_attr}>'
            f'<summary>{html.escape(section["title"])}</summary>'
            f'<div class="section-body">{render_section(section, registry)}</div>'
            "</details>"
        )

    return html_document(
        title=f"{knowl.title} - {package['title']}",
        body="\n".join(
            [
                '<main class="page-shell">',
                f'<nav class="breadcrumb"><a href="/">Index</a> / {html.escape(knowl.id)}</nav>',
                f'<article class="knowl-page" data-knowl-id="{escape_attr(knowl.id)}">',
                f'<header class="page-header"><p class="kind">{html.escape(knowl.kind)}</p><h1>{html.escape(knowl.title)}</h1><p>{html.escape(knowl.summary)}</p></header>',
                '<section class="core-section" id="section.core">',
                render_markdown(knowl.core_markdown, registry),
                render_structured_core(knowl, registry),
                "</section>",
                "\n".join(section_html),
                render_relations(knowl, registry),
                "</article>",
                render_preload_templates(knowl, registry, fragment_cache),
                "</main>",
            ]
        ),
    )


def html_document(title: str, body: str, preload_mode: str = "eager") -> str:
    math_script = ""
    if MATH_RENDERER.backend == "tex":
        math_script = """  <script>
    window.MathJax = {
      tex: {
        inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
        displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
        processEscapes: true
      },
      options: {
        skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
      }
    };
  </script>
  <script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
"""
    theme_script = """  <script>
    (function () {
      try {
        var theme = localStorage.getItem("knowl-theme");
        if (theme === "dark" || theme === "light") {
          document.documentElement.dataset.theme = theme;
        }
      } catch (error) {}
    }());
  </script>"""
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
{theme_script}
  <link rel="stylesheet" href="/assets/katex.min.css">
  <link rel="stylesheet" href="/assets/knowl.css">
  <script defer src="/assets/knowl.js"></script>
{math_script.rstrip()}
</head>
<body data-knowl-preload="{escape_attr(preload_mode)}">
<button type="button" id="theme-toggle" class="theme-toggle" aria-label="Toggle dark mode" aria-pressed="false">Dark</button>
{body}
</body>
</html>
"""


def render_index(registry: dict[str, Knowl], package: dict[str, Any]) -> str:
    grouped: dict[str, list[Knowl]] = {}
    for knowl in registry.values():
        top = knowl.id.split("/", 1)[0]
        grouped.setdefault(top, []).append(knowl)

    parts = [
        '<main class="page-shell">',
        '<header class="page-header">',
        f'<p class="kind">knowl package</p><h1>{html.escape(package["title"])}</h1>',
        '<p>Generated from typed semantic source into static pages, fragments, and indexes.</p>',
        '<p class="index-alt-link"><a href="/topics/">Old Hugo-style topics page</a></p>',
        "</header>",
    ]
    for group, knowls in sorted(grouped.items()):
        parts.append(f'<section class="index-section"><h2>{html.escape(group.replace("-", " ").title())}</h2><ul class="index-list">')
        for knowl in sorted(knowls, key=lambda k: k.title.lower()):
            parts.append(
                f'<li class="index-item"><a class="knowl index-knowl" href="{escape_attr(target_href(knowl.id))}" '
                f'data-knowl="{escape_attr(fragment_href(knowl.id))}" aria-expanded="false">{html.escape(knowl.title)}</a> '
                f'<span class="summary">{html.escape(knowl.summary)}</span></li>'
            )
        parts.append("</ul></section>")
    parts.append("</main>")
    return html_document(package["title"], "\n".join(parts), preload_mode="visible")


def render_old_topics_page(package: dict[str, Any]) -> str:
    links = "\n".join(
        f'    <li><a href="{escape_attr(href)}">{html.escape(label)}</a></li>'
        for label, href in OLD_HUGO_TOPIC_LINKS
    )
    body = "\n".join(
        [
            '<main class="home-content">',
            "  <h1>Topics</h1>",
            "",
            '  <ul class="home-links">',
            links,
            "  </ul>",
            "</main>",
        ]
    )
    return html_document(f"Topics - {package['title']}", body, preload_mode="none")


def validate(registry: dict[str, Knowl]) -> list[ValidationMessage]:
    messages: list[ValidationMessage] = []
    aliases: dict[str, str] = {}
    for knowl in registry.values():
        for alias in knowl.aliases:
            normalized = alias.lower()
            if normalized in aliases:
                messages.append(
                    ValidationMessage(
                        "warning",
                        knowl.id,
                        f'Alias "{alias}" also appears on {aliases[normalized]}',
                    )
                )
            aliases[normalized] = knowl.id

        for target in wikilinks_in_text(knowl.core_markdown):
            validate_target(messages, registry, knowl.id, target, "core wikilink")

        for item in knowl.core_data + knowl.core_axioms:
            for target in item.get("refs", []):
                validate_target(messages, registry, knowl.id, target, f'{item["id"]} ref')

        for relation in knowl.relations:
            validate_target(messages, registry, knowl.id, relation["target"], f'relation {relation["type"]}')

        for section in knowl.sections:
            kind = section.get("kind")
            if kind == "tfae":
                validate_tfae(messages, registry, knowl, section["payload"])
            elif kind == "proof":
                validate_proof(messages, registry, knowl, section["payload"])
            else:
                for target in wikilinks_in_text(section.get("markdown", "")):
                    validate_target(messages, registry, knowl.id, target, f'section {section["id"]} wikilink')

    return messages


def wikilinks_in_text(text: str) -> list[str]:
    return [match.group(1).strip() for match in WIKILINK_RE.finditer(text)]


def collect_links(knowl: Knowl) -> list[dict[str, str]]:
    links: list[dict[str, str]] = []

    def add(target: str, source_part: str, link_type: str = "mentions") -> None:
        links.append(
            {
                "source": knowl.id,
                "source_part": source_part,
                "type": link_type,
                "target": target,
            }
        )

    for target in wikilinks_in_text(knowl.core_markdown):
        add(target, "core")
    for item in knowl.core_data:
        for target in item.get("refs", []):
            add(target, f'data.{item["id"]}', "uses")
    for item in knowl.core_axioms:
        for target in item.get("refs", []):
            add(target, f'axiom.{item["id"]}', "uses")
    for relation in knowl.relations:
        add(relation["target"], "relations", relation["type"])
    for section in knowl.sections:
        section_part = f'section.{section["id"]}'
        if section.get("kind") == "tfae":
            for item in section["payload"].get("items", []):
                for target in item.get("refs", []):
                    add(target, f'{section_part}.{item["id"]}', "uses")
        elif section.get("kind") == "proof":
            payload = section["payload"]
            add(payload["proves"], f'{section_part}.{payload["id"]}', "proves")
            for step in payload.get("steps", []):
                for justification in step.get("justifications", []):
                    add(justification["target"], f'{section_part}.{payload["id"]}.step.{step["id"]}', justification.get("type", "uses"))
        else:
            for target in wikilinks_in_text(section.get("markdown", "")):
                add(target, section_part)
    seen = set()
    deduped = []
    for link in links:
        key = (link["source"], link["source_part"], link["type"], link["target"])
        if key in seen:
            continue
        seen.add(key)
        deduped.append(link)
    return deduped


def validate_target(
    messages: list[ValidationMessage],
    registry: dict[str, Knowl],
    source: str,
    target: str,
    context: str,
) -> None:
    base, anchor = split_target(target)
    if base not in registry:
        messages.append(ValidationMessage("error", source, f"{context}: missing target {target}"))
        return
    if anchor and anchor not in registry[base].anchors:
        messages.append(ValidationMessage("error", source, f"{context}: missing anchor {target}"))


def validate_tfae(
    messages: list[ValidationMessage],
    registry: dict[str, Knowl],
    knowl: Knowl,
    payload: dict[str, Any],
) -> None:
    item_ids = {item["id"] for item in payload.get("items", [])}
    for item in payload.get("items", []):
        for target in item.get("refs", []):
            validate_target(messages, registry, knowl.id, target, f'tfae item {item["id"]}')
    for implication in payload.get("implications", []):
        for side in ("from", "to"):
            if implication[side] not in item_ids:
                messages.append(
                    ValidationMessage("error", knowl.id, f'tfae implication references missing item {implication[side]}')
                )


def validate_proof(
    messages: list[ValidationMessage],
    registry: dict[str, Knowl],
    knowl: Knowl,
    payload: dict[str, Any],
) -> None:
    validate_target(messages, registry, knowl.id, payload["proves"], f'proof {payload["id"]} proves')
    step_ids = {step["id"] for step in payload.get("steps", [])}
    for step in payload.get("steps", []):
        for justification in step.get("justifications", []):
            target = justification["target"]
            if target.startswith("step:"):
                step_id = target.split(":", 1)[1]
                if step_id not in step_ids:
                    messages.append(
                        ValidationMessage("error", knowl.id, f'proof step {step["id"]}: missing step {step_id}')
                    )
            else:
                validate_target(messages, registry, knowl.id, target, f'proof step {step["id"]}')


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def registry_json(registry: dict[str, Knowl]) -> dict[str, Any]:
    return {
        knowl.id: {
            "id": knowl.id,
            "title": knowl.title,
            "kind": knowl.kind,
            "summary": knowl.summary,
            "aliases": knowl.aliases,
            "domains": knowl.domains,
            "href": target_href(knowl.id),
            "fragment": fragment_href(knowl.id),
            "anchors": sorted(knowl.anchors),
            "content_hash": knowl.content_hash,
        }
        for knowl in registry.values()
    }


def relations_json(registry: dict[str, Knowl]) -> list[dict[str, Any]]:
    relations = []
    for knowl in registry.values():
        for relation in knowl.relations:
            item = {"source": knowl.id, **relation}
            relations.append(item)
    return relations


def links_json(registry: dict[str, Knowl]) -> list[dict[str, Any]]:
    links = []
    for knowl in registry.values():
        for link in collect_links(knowl):
            links.append(link)
    return links


def proofs_json(registry: dict[str, Knowl]) -> list[dict[str, Any]]:
    proofs = []
    for knowl in registry.values():
        for section in knowl.sections:
            if section.get("kind") == "proof":
                payload = section["payload"]
                proofs.append(
                    {
                        "knowl": knowl.id,
                        "section": section["id"],
                        "id": payload["id"],
                        "title": payload["title"],
                        "proves": payload["proves"],
                        "steps": payload.get("steps", []),
                    }
                )
    return proofs


def write_sqlite(path: Path, registry: dict[str, Knowl]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        path.unlink()
    conn = sqlite3.connect(path)
    try:
        conn.executescript(
            """
            create table knowls (
              id text primary key,
              title text not null,
              kind text not null,
              summary text not null,
              href text not null,
              fragment text not null,
              content_hash text not null
            );
            create table aliases (
              alias text not null,
              knowl_id text not null references knowls(id)
            );
            create table relations (
              source text not null references knowls(id),
              type text not null,
              target text not null,
              note text
            );
            create table links (
              source text not null references knowls(id),
              source_part text not null,
              type text not null,
              target text not null
            );
            create table proof_steps (
              knowl_id text not null references knowls(id),
              proof_id text not null,
              step_id text not null,
              assertion text not null
            );
            """
        )
        for knowl in registry.values():
            conn.execute(
                "insert into knowls values (?, ?, ?, ?, ?, ?, ?)",
                (
                    knowl.id,
                    knowl.title,
                    knowl.kind,
                    knowl.summary,
                    target_href(knowl.id),
                    fragment_href(knowl.id),
                    knowl.content_hash,
                ),
            )
            for alias in knowl.aliases:
                conn.execute("insert into aliases values (?, ?)", (alias, knowl.id))
            for relation in knowl.relations:
                conn.execute(
                    "insert into relations values (?, ?, ?, ?)",
                    (knowl.id, relation["type"], relation["target"], relation.get("note")),
                )
            for link in collect_links(knowl):
                conn.execute(
                    "insert into links values (?, ?, ?, ?)",
                    (link["source"], link["source_part"], link["type"], link["target"]),
                )
            for section in knowl.sections:
                if section.get("kind") == "proof":
                    payload = section["payload"]
                    for step in payload.get("steps", []):
                        conn.execute(
                            "insert into proof_steps values (?, ?, ?, ?)",
                            (knowl.id, payload["id"], step["id"], step["assertion"]),
                        )
        conn.commit()
    finally:
        conn.close()


def copy_runtime_assets(out_dir: Path) -> None:
    runtime_dir = Path(__file__).resolve().parents[1] / "static-runtime"
    assets_dir = out_dir / "assets"
    assets_dir.mkdir(parents=True, exist_ok=True)
    for filename in ("knowl.css", "knowl.js"):
        shutil.copyfile(runtime_dir / filename, assets_dir / filename)

    katex_assets = find_katex_assets_dir()
    if not katex_assets:
        (assets_dir / "katex.min.css").write_text("", encoding="utf-8")
        return

    css_source = katex_assets / "katex.min.css"
    if not css_source.is_file():
        css_source = katex_assets / "katex.css"
    if css_source.is_file():
        shutil.copyfile(css_source, assets_dir / "katex.min.css")

    fonts_source = katex_assets / "fonts"
    if fonts_source.is_dir():
        shutil.copytree(fonts_source, assets_dir / "fonts", dirs_exist_ok=True)


def write_site(package_dir: Path, out_dir: Path, allow_validation_errors: bool = False) -> int:
    package_path = package_dir / "knowlpack.toml"
    package = read_toml(package_path)
    content_dir = package_dir / package.get("content_dir", "content")
    knowls = discover_knowls(content_dir)
    registry = {knowl.id: knowl for knowl in knowls}
    if len(registry) != len(knowls):
        duplicates = sorted({knowl.id for knowl in knowls if sum(k.id == knowl.id for k in knowls) > 1})
        raise ValueError("Duplicate knowl ids: " + ", ".join(duplicates))

    messages = validate(registry)
    errors = [msg for msg in messages if msg.severity == "error"]

    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)
    copy_runtime_assets(out_dir)

    fragment_cache = {knowl.id: render_knowl_core(knowl, registry) for knowl in registry.values()}

    (out_dir / "index.html").write_text(render_index(registry, package), encoding="utf-8")
    topics_path = out_dir / "topics" / "index.html"
    topics_path.parent.mkdir(parents=True, exist_ok=True)
    topics_path.write_text(render_old_topics_page(package), encoding="utf-8")

    for knowl in registry.values():
        page_path = out_dir / slug_to_relpath(knowl.id) / "index.html"
        page_path.parent.mkdir(parents=True, exist_ok=True)
        page_path.write_text(render_page(knowl, registry, package, fragment_cache), encoding="utf-8")

        fragment_path = out_dir / "fragments" / slug_to_relpath(knowl.id) / "core.html"
        fragment_path.parent.mkdir(parents=True, exist_ok=True)
        fragment_path.write_text(fragment_cache[knowl.id], encoding="utf-8")

        for section in knowl.sections:
            section_path = out_dir / "fragments" / slug_to_relpath(knowl.id) / "sections" / f'{section["id"]}.html'
            section_path.parent.mkdir(parents=True, exist_ok=True)
            section_path.write_text(render_section(section, registry), encoding="utf-8")

    write_json(out_dir / "indexes" / "registry.json", registry_json(registry))
    write_json(out_dir / "indexes" / "relations.json", relations_json(registry))
    write_json(out_dir / "indexes" / "links.json", links_json(registry))
    write_json(out_dir / "indexes" / "proofs.json", proofs_json(registry))
    write_json(out_dir / "reports" / "validation.json", [msg.__dict__ for msg in messages])
    write_sqlite(out_dir / "indexes" / "knowls.sqlite", registry)

    print(f"Compiled {len(registry)} knowls into {out_dir}")
    if messages:
        for msg in messages:
            print(f"{msg.severity.upper()}: {msg.source}: {msg.message}", file=sys.stderr)
    if errors and not allow_validation_errors:
        return 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Compile a knowl package")
    parser.add_argument("package_dir", type=Path, help="Directory containing knowlpack.toml")
    parser.add_argument("--out", type=Path, default=Path("public"), help="Output directory")
    parser.add_argument(
        "--allow-validation-errors",
        action="store_true",
        help="Write artifacts and return success even when semantic validation reports errors",
    )
    args = parser.parse_args()
    return write_site(args.package_dir, args.out, allow_validation_errors=args.allow_validation_errors)


if __name__ == "__main__":
    raise SystemExit(main())
