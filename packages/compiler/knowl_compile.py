#!/usr/bin/env python3
"""Compile a knowl package into static pages, fragments, and indexes.

Typed source files become a validated graph and a set of static publishing
artifacts.
"""

from __future__ import annotations

import argparse
import atexit
import base64
import functools
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


WIKILINK_RE = re.compile(
    r"\[\[([A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*(?:#[^\]|]+)?)(?:\|((?:[^\]]|\](?=\]\])|\](?!\]))*?))?\]\](?!\])"
)
MARKDOWN_LINK_RE = re.compile(r"\[([^\]\n]+)\]\(([^)\n]+)\)")
INLINE_CODE_RE = re.compile(r"(?<!`)`([^`\n]+)`(?!`)")
FENCED_CODE_RE = re.compile(r"^```[^\n]*\n.*?^```[ \t]*$", re.MULTILINE | re.DOTALL)
MATH_RE = re.compile(
    r"(?s)(\$\$(.+?)\$\$|\\\[(.+?)\\\]|\\\((.+?)\\\)|(?<!\\)\$(?!\$)(.+?)(?<!\\)\$)"
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
]

GRAPH_DEFAULT_FOCUS = "linear-algebra/vector-space"
DIRECTORY_EXCLUDED_SUBJECTS = frozenset({"search"})
SOURCE_COLLECTIONS = {
    "langlands-letter": "Langlands's letter",
    "shale-paper": "Shale's paper",
    "knowlification": "Source expansion guides",
    "posts": "Long-form documents",
}
SUBJECT_TITLES = {
    "algebra-category-theory": "Category theory",
    "algebra-coalgebras": "Coalgebras",
    "algebra-commutative": "Commutative algebra",
    "algebra-fields-galois": "Fields and Galois theory",
    "algebra-groups": "Groups",
    "algebra-homological": "Homological algebra",
    "algebra-hyperstructures": "Hyperstructures, semirings, and blueprints",
    "algebra-modules": "Modules",
    "algebra-representation-theory": "Representation theory",
    "algebra-rings": "Rings",
    "algebra-topological": "Topological algebra",
    "algebraic-geometry-foundations": "Algebraic geometry",
    "analysis": "Analysis: geometric and quantitative tools",
    "formal-groups": "Formal groups",
    "nonassociative-algebra": "Nonassociative and Jordan algebras",
    "shared-foundations": "Foundations",
    "stat-mech-quantum": "Quantum statistical mechanics",
}

PROFILE_NAMES = ("development", "production")


@dataclass(frozen=True)
class BuildProfile:
    name: str
    include_development_content: bool
    show_testing_ui: bool

    @property
    def features(self) -> dict[str, bool]:
        return {
            "developmentContent": self.include_development_content,
            "testingUi": self.show_testing_ui,
        }


BUILD_PROFILES = {
    "development": BuildProfile("development", True, True),
    "production": BuildProfile("production", False, False),
}


def resolve_profile(explicit: str | None = None, environment: dict[str, str] | None = None) -> BuildProfile:
    environment = os.environ if environment is None else environment
    name = explicit or environment.get("KNOWLPEDIA_PROFILE") or "development"
    if name not in BUILD_PROFILES:
        choices = ", ".join(PROFILE_NAMES)
        raise ValueError(f"Unknown Knowlpedia profile {name!r}; expected one of: {choices}")
    return BUILD_PROFILES[name]

# Small pages embed their direct knowl fragments for instant offline expansion.
# Large indexes use the runtime's visible-link preloader and fetch fragments on
# demand, avoiding multi-megabyte HTML pages and a request for every linked knowl.
INLINE_PRELOAD_TEMPLATE_LIMIT = 64


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


@functools.lru_cache(maxsize=1)
def runtime_asset_version() -> str:
    """Return a stable cache key for the browser runtime shipped by this build."""
    runtime_dir = Path(__file__).resolve().parents[1] / "static-runtime"
    digest = hashlib.sha256()
    for filename in ("knowl.css", "knowl.js", "graph.js", "knowl-testing.js"):
        path = runtime_dir / filename
        if not path.is_file():
            continue
        digest.update(filename.encode("utf-8"))
        digest.update(path.read_bytes())
    return digest.hexdigest()[:12]


def find_node() -> Path | None:
    node = shutil.which("node")
    if node:
        return Path(node)
    for node in sorted(Path.home().glob(".vscode-server/cli/servers/*/server/node"), reverse=True):
        if node.is_file():
            return node
    return None


def find_katex_module() -> Path | None:
    local_module = repo_root() / "node_modules" / "katex" / "dist" / "katex.js"
    if local_module.is_file():
        return local_module
    for module in sorted(Path.home().glob(".vscode-server/cli/servers/*/server/node_modules/katex/dist/katex.js"), reverse=True):
        if module.is_file():
            return module
    return None


def find_katex_assets_dir() -> Path | None:
    repo_dir = repo_root()
    local_assets = repo_dir / "node_modules" / "katex" / "dist"
    if (local_assets / "katex.min.css").is_file():
        return local_assets
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
        self._png_engine = executable("pdflatex")
        self._png_converter = executable("gs")
        self._converter = executable("dvisvgm") or executable("pdftocairo")
        if self._converter and Path(self._converter).name == "dvisvgm" and executable("latex"):
            self._engine = executable("latex")
            self._engine_output = "dvi"
        else:
            self._engine = executable("tectonic") or executable("pdflatex")
            self._engine_output = "pdf"
        self._cache: dict[tuple[str, str], str] = {}
        self._disk_cache_dir: Path | None = None
        self._prebuilt_dir: Path | None = None
        self._refresh_prebuilt = False

    @property
    def backend(self) -> str:
        if self._png_engine and self._png_converter:
            return "image"
        if self._engine and self._converter:
            return "svg"
        return "source"

    def configure_cache(self, cache_dir: Path | None) -> None:
        self._disk_cache_dir = cache_dir
        if self._disk_cache_dir:
            self._disk_cache_dir.mkdir(parents=True, exist_ok=True)

    def configure_prebuilt(self, prebuilt_dir: Path | None, *, refresh: bool = False) -> None:
        self._prebuilt_dir = prebuilt_dir
        self._refresh_prebuilt = refresh
        self._cache.clear()
        if self._prebuilt_dir:
            self._prebuilt_dir.mkdir(parents=True, exist_ok=True)

    def disable_local_rendering(self) -> None:
        self._png_engine = None
        self._png_converter = None
        self._engine = None
        self._converter = None
        self._cache.clear()

    def render(self, source: str, kind: str = "tikz") -> str:
        source = source.strip()
        cache_key = (kind, source)
        if cache_key in self._cache:
            return self._cache[cache_key]

        prebuilt_path = self._prebuilt_path(source, kind)
        if not self._refresh_prebuilt and prebuilt_path and prebuilt_path.is_file():
            rendered = prebuilt_path.read_text(encoding="utf-8")
            self._cache[cache_key] = rendered
            return rendered

        disk_cache_path = self._disk_cache_path(source, kind)
        if disk_cache_path and disk_cache_path.is_file():
            rendered = disk_cache_path.read_text(encoding="utf-8")
            self._cache[cache_key] = rendered
            return rendered

        rendered: str | None = None
        if self._png_engine and self._png_converter:
            rendered = self._render_png(source, kind)
        elif self._engine and self._converter:
            rendered = self._render_svg(source, kind)

        if rendered is None:
            rendered = self._render_source(source, kind)
        self._cache[cache_key] = rendered
        if disk_cache_path and "diagram-error" not in rendered and "diagram-source" not in rendered:
            disk_cache_path.parent.mkdir(parents=True, exist_ok=True)
            disk_cache_path.write_text(rendered, encoding="utf-8")
        if (
            self._refresh_prebuilt
            and prebuilt_path
            and "diagram-error" not in rendered
            and "diagram-source" not in rendered
        ):
            prebuilt_path.write_text(rendered, encoding="utf-8")
        return rendered

    def _prebuilt_path(self, source: str, kind: str) -> Path | None:
        if not self._prebuilt_dir:
            return None
        payload = {
            "version": 1,
            "kind": kind,
            "source": source,
            "document": self._document(source, kind),
        }
        digest = hashlib.sha256(json.dumps(payload, sort_keys=True).encode("utf-8")).hexdigest()
        return self._prebuilt_dir / f"{digest}.html"

    def _disk_cache_path(self, source: str, kind: str) -> Path | None:
        if not self._disk_cache_dir or self.backend == "source":
            return None
        payload = {
            "version": 1,
            "backend": self.backend,
            "kind": kind,
            "source": source,
            "document": self._document(source, kind),
            "png_engine": self._png_engine,
            "png_converter": self._png_converter,
            "engine": self._engine,
            "engine_output": self._engine_output,
            "converter": self._converter,
        }
        digest = hashlib.sha256(json.dumps(payload, sort_keys=True).encode("utf-8")).hexdigest()
        return self._disk_cache_dir / self.backend / f"{digest}.html"

    def _render_png(self, source: str, kind: str) -> str | None:
        with tempfile.TemporaryDirectory(prefix="knowl-diagram-") as tmp:
            tmp_path = Path(tmp)
            tex_path = tmp_path / "diagram.tex"
            pdf_path = tmp_path / "diagram.pdf"
            png_path = tmp_path / "diagram.png"
            tex_path.write_text(self._document(source, kind), encoding="utf-8")

            try:
                compile_result = subprocess.run(
                    [
                        self._png_engine,
                        "-halt-on-error",
                        "-interaction=nonstopmode",
                        tex_path.name,
                    ],
                    cwd=tmp_path,
                    text=True,
                    capture_output=True,
                    timeout=30,
                    check=False,
                )
            except Exception as exc:
                return self._render_error(source, kind, str(exc))

            if compile_result.returncode != 0 or not pdf_path.is_file():
                log = (compile_result.stdout + "\n" + compile_result.stderr).strip()
                return self._render_error(source, kind, log)

            try:
                convert_result = subprocess.run(
                    [
                        self._png_converter,
                        "-dSAFER",
                        "-dBATCH",
                        "-dNOPAUSE",
                        "-sDEVICE=pngalpha",
                        "-r220",
                        "-dTextAlphaBits=4",
                        "-dGraphicsAlphaBits=4",
                        f"-sOutputFile={png_path}",
                        str(pdf_path),
                    ],
                    cwd=tmp_path,
                    text=True,
                    capture_output=True,
                    timeout=30,
                    check=False,
                )
            except Exception as exc:
                return self._render_error(source, kind, str(exc))

            if convert_result.returncode != 0 or not png_path.is_file():
                log = (convert_result.stdout + "\n" + convert_result.stderr).strip()
                return self._render_error(source, kind, log)

            diagram_hash = hashlib.sha256(source.encode("utf-8")).hexdigest()[:12]
            encoded = base64.b64encode(png_path.read_bytes()).decode("ascii")
            return (
                f'<figure class="diagram diagram-image diagram-{escape_attr(kind)}" '
                f'data-diagram-hash="{diagram_hash}">'
                '<div class="diagram-frame">'
                f'<img src="data:image/png;base64,{encoded}" alt="Rendered {escape_attr(kind)} diagram" loading="lazy">'
                "</div>"
                "</figure>"
            )

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
        node = find_node()
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
    progressive_sections: bool = True
    prerequisites: list[str] = field(default_factory=list)
    dependency_heuristic: str | None = None
    dependency_review_count: int = 0
    core_data: list[dict[str, Any]] = field(default_factory=list)
    core_axioms: list[dict[str, Any]] = field(default_factory=list)
    sections: list[dict[str, Any]] = field(default_factory=list)
    relations: list[dict[str, Any]] = field(default_factory=list)
    knowls_open: bool = False
    visibility: str = "production"
    anchors: set[str] = field(default_factory=set)
    content_hash: str = ""
    redirect_to: str | None = None
    redirect_sections: dict[str, str] = field(default_factory=dict)


class AliasRegistry(dict[str, Knowl]):
    """Canonical knowls with legacy IDs resolving through the mapping."""

    def __init__(self, canonical: dict[str, Knowl], aliases: dict[str, str], redirects: dict[str, Knowl] | None = None):
        super().__init__(canonical)
        self.aliases = aliases
        self._redirects = redirects or {}

    def canonical_id(self, knowl_id: str) -> str:
        seen: set[str] = set()
        while knowl_id in self.aliases and knowl_id not in seen:
            seen.add(knowl_id)
            knowl_id = self.aliases[knowl_id]
        return knowl_id

    def __contains__(self, key: object) -> bool:
        return dict.__contains__(self, key) or (isinstance(key, str) and key in self.aliases)

    def __getitem__(self, key: str) -> Knowl:
        return dict.__getitem__(self, self.canonical_id(key))

    def get(self, key: str, default: Knowl | None = None) -> Knowl | None:
        return dict.get(self, self.canonical_id(key), default)

    def canonical_target(self, target: str) -> str:
        base, anchor = split_target(target)
        current = base
        seen: set[str] = set()
        while current in self.aliases and current not in seen:
            seen.add(current)
            redirect = self._redirects.get(current)
            if redirect and anchor:
                prefix = "section." if anchor.startswith("section.") else ""
                section = anchor.removeprefix("section.")
                anchor = prefix + redirect.redirect_sections.get(section, section)
            current = self.aliases[current]
        return current + (f"#{anchor}" if anchor else "")


def read_toml(path: Path) -> dict[str, Any]:
    with path.open("rb") as f:
        return tomllib.load(f)


def slug_to_relpath(knowl_id: str) -> Path:
    # Hugo lowercased legacy page paths. Keep generated URLs lowercase even
    # when an imported knowl id contains notation-specific capitals, so old
    # public URLs continue to resolve on GitHub Pages' case-sensitive host.
    return Path(*(part.lower() for part in knowl_id.split("/")))


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


def section_fragment_href(knowl_id: str, section_id: str) -> str:
    return (
        "/fragments/"
        + str(slug_to_relpath(knowl_id)).replace("\\", "/")
        + f"/sections/{section_id}.html"
    )


def escape_attr(value: str) -> str:
    return html.escape(value, quote=True)


def canonical_target(registry: dict[str, Knowl], target: str) -> str:
    if isinstance(registry, AliasRegistry):
        return registry.canonical_target(target)
    base, anchor = split_target(target)
    return base + (f"#{anchor}" if anchor else "")


def render_redirect_page(redirect: Knowl, destination: str, profile: BuildProfile, section_map: dict[str, str] | None = None) -> str:
    """A static fallback for a retired page URL, with a crawlable canonical link."""
    mapping = json.dumps(section_map or redirect.redirect_sections, separators=(",", ":")).replace("</", "<\\/")
    body = (
        '<main class="page-shell redirect-page" id="main-content">'
        f'<p>This knowl moved to <a href="{escape_attr(destination)}">the canonical page</a>.</p>'
        f'<script>(function(){{var m={mapping},h=location.hash.slice(1),k=h.indexOf("section.")==0?h.slice(8):h;location.replace({json.dumps(destination)}+(m[k]?"#section."+encodeURIComponent(m[k]):location.hash));}}());</script>'
        '</main>'
    )
    return html_document(
        f"Moved: {redirect.title}",
        body,
        preload_mode="none",
        profile=profile,
        canonical_url=destination,
        redirect_url=destination,
    )


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


def protect_inline_code(text: str) -> tuple[str, dict[str, str]]:
    replacements: dict[str, str] = {}

    def replace(match: re.Match[str]) -> str:
        token = f"@@KNOWL_CODE_{len(replacements)}@@"
        replacements[token] = f"<code>{html.escape(match.group(1))}</code>"
        return token

    return INLINE_CODE_RE.sub(replace, text), replacements


def restore_math(text: str, replacements: dict[str, str]) -> str:
    for token, rendered in replacements.items():
        text = text.replace(token, rendered)
    return text


def is_agent_status_line(line: str) -> bool:
    return bool(AGENT_STATUS_RE.match(line.strip()))


def section_id_from_title(title: str) -> str:
    normalized = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-z0-9]+", "-", normalized.lower()).strip("-")
    return slug or "section"


def split_single_file_sections(body: str) -> tuple[str, list[dict[str, Any]]]:
    """Split pedagogical H2 and standalone Examples blocks from a compact knowl.

    Text before the first H2 remains the canonical inline core. If a document
    starts with an H2, its first section becomes the core so a knowl never opens
    as an empty shell. Subsequent H2 blocks become progressively disclosed
    sections. A standalone ``**Examples:**`` label receives the same treatment.
    """

    lines = body.splitlines()
    headings: list[tuple[int, str]] = []
    in_fence = False
    for index, line in enumerate(lines):
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = re.match(r"^##\s+(.+?)\s*$", line)
        if match:
            headings.append((index, match.group(1).strip()))

    sections: list[dict[str, Any]] = []
    core = body.strip()
    if headings:
        first_index = headings[0][0]
        core = "\n".join(lines[:first_index]).strip()
        start_at = 0
        if not core:
            start_at = 1
            first_end = headings[1][0] if len(headings) > 1 else len(lines)
            core = "\n".join(lines[first_index + 1 : first_end]).strip()

        used_ids: set[str] = set()
        for offset in range(start_at, len(headings)):
            line_index, title = headings[offset]
            end = headings[offset + 1][0] if offset + 1 < len(headings) else len(lines)
            markdown = "\n".join(lines[line_index + 1 : end]).strip()
            if not markdown:
                continue
            base_id = section_id_from_title(title)
            section_id = base_id
            suffix = 2
            while section_id in used_ids:
                section_id = f"{base_id}-{suffix}"
                suffix += 1
            used_ids.add(section_id)
            sections.append(
                {
                    "id": section_id,
                    "title": title,
                    "kind": "markdown",
                    "markdown": markdown,
                }
            )

    # The migrated corpus often uses a standalone bold Examples label rather
    # than an H2. Split only the exact label so prose such as "Example." stays
    # part of the mathematical core.
    core_lines = core.splitlines()
    for index, line in enumerate(core_lines):
        match = re.match(r"^\*\*(Examples?):\*\*\s*$", line.strip(), re.IGNORECASE)
        if not match:
            continue
        example_markdown = "\n".join(core_lines[index + 1 :]).strip()
        if example_markdown:
            title = "Example" if match.group(1).lower() == "example" else "Examples"
            base_id = section_id_from_title(title)
            section_id = base_id
            existing_ids = {section["id"] for section in sections}
            suffix = 2
            while section_id in existing_ids:
                section_id = f"{base_id}-{suffix}"
                suffix += 1
            sections.insert(
                0,
                {
                    "id": section_id,
                    "title": title,
                    "kind": "markdown",
                    "markdown": example_markdown,
                },
            )
            core = "\n".join(core_lines[:index]).strip()
        break

    return core, sections


def uses_progressive_sections(meta: dict[str, Any]) -> bool:
    mode = str(meta.get("section_mode", "auto")).lower()
    if mode == "progressive":
        return True
    if mode == "continuous":
        return False
    return str(meta.get("kind", "")).lower() not in {"document", "index", "page", "section"}


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
    if uses_progressive_sections(meta):
        core_markdown, sections = split_single_file_sections(body)
    else:
        core_markdown, sections = body, []
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
    redirect_to = meta.get("redirect_to")
    redirect_sections = meta.get("redirect_sections", {})
    if redirect_to is not None and (not isinstance(redirect_to, str) or not redirect_to.strip()):
        raise ValueError(f"{source_path}: redirect_to must be a nonempty string")
    if not isinstance(redirect_sections, dict) or not all(
        isinstance(key, str) and isinstance(value, str) and key and value
        for key, value in redirect_sections.items()
    ):
        raise ValueError(f"{source_path}: redirect_sections must map nonempty strings to nonempty strings")

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
        progressive_sections=uses_progressive_sections(meta),
        prerequisites=list(meta.get("prerequisites", [])),
        dependency_heuristic=meta.get("dependency_heuristic"),
        dependency_review_count=meta.get("dependency_review_count", 0),
        core_data=list(core_meta.get("data", [])),
        core_axioms=list(core_meta.get("axioms", [])),
        sections=sections or [],
        relations=list(meta.get("relations", [])),
        knowls_open=bool(meta.get("knowls_open", False)),
        redirect_to=redirect_to,
        redirect_sections=dict(redirect_sections),
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
            "prerequisites": knowl.prerequisites,
            "dependency_heuristic": knowl.dependency_heuristic,
            "dependency_review_count": knowl.dependency_review_count,
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


def discover_knowls(content_dir: Path, *, visibility: str = "production") -> list[Knowl]:
    knowls = []
    for path in sorted(content_dir.rglob("*.knowl.md")):
        knowl = parse_single_file(path)
        knowl.visibility = visibility
        knowls.append(knowl)
    return sorted(knowls, key=lambda k: k.id)


def package_content_roots(
    package_dir: Path,
    package: dict[str, Any],
    profile: BuildProfile,
) -> list[tuple[Path, str]]:
    roots = [(package_dir / package.get("content_dir", "content"), "production")]
    if profile.include_development_content:
        configured = package.get("development_content_dirs", [])
        if not isinstance(configured, list) or not all(isinstance(item, str) for item in configured):
            raise ValueError("development_content_dirs must be a list of paths")
        roots.extend((package_dir / item, "development") for item in configured)
    return roots


def discover_package_knowls(
    package_dir: Path,
    package: dict[str, Any],
    profile: BuildProfile,
) -> tuple[list[Knowl], list[tuple[Path, str]]]:
    roots = package_content_roots(package_dir, package, profile)
    knowls = [
        knowl
        for content_dir, visibility in roots
        for knowl in discover_knowls(content_dir, visibility=visibility)
    ]
    return sorted(knowls, key=lambda knowl: knowl.id), roots


def render_inline(text: str, registry: dict[str, Knowl]) -> str:
    text, code_replacements = protect_inline_code(text)
    text, math_replacements = protect_math(text)
    escaped = html.escape(text)

    def replace_wikilink(match: re.Match[str]) -> str:
        target = html.unescape(match.group(1).strip())
        label = html.unescape(match.group(2).strip()) if match.group(2) else target_label(target)
        base, _ = split_target(target)
        canonical_target_value = canonical_target(registry, target)
        canonical, _ = split_target(canonical_target_value)
        class_name = "knowl"
        attrs = ""
        if canonical in registry:
            target = canonical_target_value
            attrs = f' data-knowl="{escape_attr(fragment_href(canonical))}"'
        else:
            class_name = "missing-knowl"
        return (
            f'<a class="{class_name}" href="{escape_attr(target_href(target))}"'
            f'{attrs} aria-expanded="false">{html.escape(label)}</a>'
        )

    def replace_markdown_link(match: re.Match[str]) -> str:
        label = html.unescape(match.group(1))
        href = html.unescape(match.group(2)).strip()
        if not (href.startswith("https://") or href.startswith("http://") or href.startswith("/")):
            return match.group(0)
        return (
            f'<a class="page-link" href="{escape_attr(href)}">'
            f"{html.escape(label)}</a>"
        )

    escaped = MARKDOWN_LINK_RE.sub(replace_markdown_link, escaped)
    escaped = WIKILINK_RE.sub(replace_wikilink, escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", escaped)
    escaped = restore_math(escaped, math_replacements)
    for token, rendered in code_replacements.items():
        escaped = escaped.replace(token, rendered)
    return escaped


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


def split_markdown_table_row(line: str) -> list[str]:
    # Split a pipe table row without treating wikilink label pipes as cells.
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]

    cells: list[str] = []
    cell: list[str] = []
    wikilink_depth = 0
    index = 0
    while index < len(stripped):
        pair = stripped[index : index + 2]
        if pair == "[[":
            wikilink_depth += 1
            cell.append(pair)
            index += 2
            continue
        if pair == "]]" and wikilink_depth:
            wikilink_depth -= 1
            cell.append(pair)
            index += 2
            continue
        if stripped[index] == "|" and wikilink_depth == 0:
            cells.append("".join(cell).strip())
            cell = []
        else:
            cell.append(stripped[index])
        index += 1
    cells.append("".join(cell).strip())
    return cells


def is_markdown_table_separator(line: str) -> bool:
    cells = split_markdown_table_row(line)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)


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

        if stripped in {"\\[", "$$", "$"}:
            close_list()
            delimiter = "\\]" if stripped == "\\[" else stripped
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

        callout = re.match(r"^\*\*(Warning|Remark|Interpretation)\.\*\*\s*(.*)$", stripped, re.IGNORECASE)
        if callout:
            close_list()
            label = callout.group(1).capitalize()
            callout_lines = [callout.group(2)] if callout.group(2) else []
            i += 1
            while i < len(lines):
                next_line = lines[i].strip()
                if not next_line:
                    break
                if next_line.startswith("#") or next_line.startswith("```") or next_line in {"\\[", "$$", "$"}:
                    break
                callout_lines.append(next_line)
                i += 1
            callout_body = " ".join(callout_lines).strip()
            out.append(
                f'<aside class="callout callout-{label.lower()}"><p class="callout-label">{label}</p>'
                f'<div>{render_paragraph(callout_body, registry)}</div></aside>'
            )
            continue

        heading = re.match(r"^(#{1,4})\s+(.+)$", stripped)
        if heading:
            close_list()
            level = len(heading.group(1))
            out.append(f"<h{level}>{render_inline(heading.group(2), registry)}</h{level}>")
            i += 1
            continue

        if (
            stripped.startswith("|")
            and i + 1 < len(lines)
            and is_markdown_table_separator(lines[i + 1])
        ):
            close_list()
            headers = split_markdown_table_row(line)
            i += 2
            rows: list[list[str]] = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                row = split_markdown_table_row(lines[i])
                if len(row) != len(headers):
                    break
                rows.append(row)
                i += 1
            head_html = "".join(f"<th>{render_inline(cell, registry)}</th>" for cell in headers)
            body_html = "".join(
                "<tr>"
                + "".join(f"<td>{render_inline(cell, registry)}</td>" for cell in row)
                + "</tr>"
                for row in rows
            )
            out.append(
                "<div class=\"table-scroll\"><table><thead><tr>"
                + head_html
                + "</tr></thead><tbody>"
                + body_html
                + "</tbody></table></div>"
            )
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
                or next_line in {"\\[", "$$", "$"}
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


def without_redundant_leading_h1(markdown: str) -> str:
    """Remove a source-document title when the knowl shell already supplies H1."""

    lines = markdown.splitlines()
    for index, line in enumerate(lines):
        if not line.strip():
            continue
        if re.match(r"^#\s+", line):
            return "\n".join(lines[:index] + lines[index + 1 :]).strip()
        break
    return markdown


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
            selected = "true" if idx == 0 else "false"
            tab_index = "0" if idx == 0 else "-1"
            parts.append(
                f'<button type="button" class="switcher-tab{active}" '
                f'id="tab-{escape_attr(item["id"])}" role="tab" aria-selected="{selected}" tabindex="{tab_index}" '
                f'aria-controls="panel-{escape_attr(item["id"])}" '
                f'data-switch-target="{escape_attr(item["id"])}">{html.escape(item.get("label", item["id"]))}</button>'
            )
        parts.append("</div>")
        parts.append('<div class="tfae-items">')
        for idx, item in enumerate(items):
            hidden_attr = "" if idx == 0 else " hidden"
            parts.append(
                f'<article class="tfae-item" id="panel-{escape_attr(item["id"])}" role="tabpanel" '
                f'aria-labelledby="tab-{escape_attr(item["id"])}" data-switch-panel="{escape_attr(item["id"])}"{hidden_attr}>'
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
            f'<span class="relation-type">{html.escape(humanize_identifier(relation["type"]))}</span> '
            f'{render_ref(relation["target"], registry)}'
            f'{": " + render_inline(note, registry) if note else ""}'
            "</li>"
        )
    parts.append("</ul></section>")
    return "\n".join(parts)


def humanize_identifier(value: str) -> str:
    return value.replace("_", " ").replace("-", " ").strip().capitalize()


def render_section_title(title: str, registry: dict[str, Knowl]) -> str:
    """Render math in a heading while flattening wikilinks to their labels.

    A section title sits inside a button or summary, so nesting an anchor there
    would be invalid and confusing. The section body still retains the link.
    """

    def flatten(match: re.Match[str]) -> str:
        return match.group(2).strip() if match.group(2) else target_label(match.group(1).strip())

    return render_inline(WIKILINK_RE.sub(flatten, title), registry)


def display_kind(kind: str) -> str:
    """Return a reader-facing kind without exposing the generic storage type."""

    return "" if kind.lower() == "knowl" else humanize_identifier(kind)


def core_heading_for_kind(kind: str) -> str | None:
    normalized = kind.lower()
    if normalized in {"knowl", "definition", "example"}:
        return None
    if normalized in {"theorem", "lemma", "proposition", "corollary"}:
        return "Statement"
    return "Core idea"


def render_section_links(knowl: Knowl, registry: dict[str, Knowl]) -> str:
    if not knowl.sections:
        return ""
    buttons = []
    for section in knowl.sections:
        buttons.append(
            f'<button type="button" class="section-chip" '
            f'data-section-id="{escape_attr(section["id"])}" '
            f'data-section-url="{escape_attr(section_fragment_href(knowl.id, section["id"]))}" '
            f'aria-expanded="false">{render_section_title(section["title"], registry)}</button>'
        )
    return (
        '<nav class="knowl-section-links" aria-label="More about this concept">'
        + "".join(buttons)
        + "</nav>"
    )


def render_knowl_core(knowl: Knowl, registry: dict[str, Knowl]) -> str:
    title_text = knowl.title
    compact_core_attr = ' data-compact-core="true"' if knowl.progressive_sections else ""
    body = [
        f'<div class="knowl-content" data-knowl-id="{escape_attr(knowl.id)}" '
        f'data-knowl-title="{escape_attr(title_text)}" data-knowl-kind="{escape_attr(display_kind(knowl.kind))}" '
        f'data-knowl-visibility="{escape_attr(knowl.visibility)}">',
        f'<div class="knowl-body"{compact_core_attr}>',
        render_markdown(without_redundant_leading_h1(knowl.core_markdown), registry),
        render_structured_core(knowl, registry),
        "</div>",
        '<div class="knowl-controls">',
        render_section_links(knowl, registry),
        f'<a class="knowl-page-link" href="{escape_attr(target_href(knowl.id))}" '
        f'aria-label="Open {escape_attr(title_text)} as a full page" title="Open full page">&#8599;</a>',
        f'<button type="button" class="knowl-close" aria-label="Collapse {escape_attr(title_text)}" '
        f'title="Collapse">&times;</button>',
        "</div>",
        '<div class="knowl-section-slot" aria-live="polite"></div>',
        "</div>",
    ]
    return "\n".join(body)


def preload_template_targets(knowl: Knowl, registry: dict[str, Knowl]) -> list[str]:
    targets: list[str] = []

    def add(target: str) -> None:
        base, _ = split_target(target)
        if isinstance(registry, AliasRegistry):
            base = registry.canonical_id(base)
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
    targets: list[str] | None = None,
) -> str:
    targets = targets if targets is not None else preload_template_targets(knowl, registry)
    if len(targets) > INLINE_PRELOAD_TEMPLATE_LIMIT:
        return ""
    templates = []
    for target in targets:
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
    profile: BuildProfile = BUILD_PROFILES["development"],
) -> str:
    knowls_open_attr = ' data-knowls-open="true"' if knowl.knowls_open else ""
    preload_targets = preload_template_targets(knowl, registry)
    preload_mode = "visible" if len(preload_targets) > INLINE_PRELOAD_TEMPLATE_LIMIT else "eager"
    section_html = []
    for section in knowl.sections:
        open_attr = " open" if section.get("default_open") else ""
        section_html.append(
            f'<details class="knowl-section" id="section.{escape_attr(section["id"])}"{open_attr}>'
            f'<summary><span>{render_section_title(section["title"], registry)}</span><span class="section-state" aria-hidden="true">Open</span></summary>'
            f'<div class="section-body">{render_section(section, registry)}</div>'
            "</details>"
        )

    kind = display_kind(knowl.kind)
    compact_core_attr = ' data-compact-core="true"' if knowl.progressive_sections else ""
    kind_html = f'<p class="kind">{html.escape(kind)}</p>' if kind else ""
    core_heading = core_heading_for_kind(knowl.kind)
    core_heading_html = (
        f'<h2 class="core-heading">{html.escape(core_heading)}</h2>' if core_heading else ""
    )
    development_banner = (
        '<aside class="development-banner" role="note"><strong>Testing content</strong>'
        '<span>This page is included in development previews and excluded from production.</span></aside>'
        if knowl.visibility == "development"
        else ""
    )

    return html_document(
        title=f"{knowl.title} - {package['title']}",
        body="\n".join(
            [
                '<main class="page-shell" id="main-content">',
                f'<nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Knowlpedia</a><span aria-hidden="true">/</span><span>{html.escape(humanize_identifier(knowl.id.split("/", 1)[0]))}</span></nav>',
                development_banner,
                f'<article class="knowl-page" data-knowl-id="{escape_attr(knowl.id)}" data-knowl-visibility="{escape_attr(knowl.visibility)}"{knowls_open_attr}>',
                f'<header class="page-header">{kind_html}<h1>{render_inline(knowl.title, registry)}</h1><p class="page-summary">{render_inline(knowl.summary, registry)}</p></header>',
                f'<section class="core-section" id="section.core"{compact_core_attr}>',
                core_heading_html,
                render_markdown(without_redundant_leading_h1(knowl.core_markdown), registry),
                render_structured_core(knowl, registry),
                "</section>",
                "\n".join(section_html),
                render_relations(knowl, registry),
                "</article>",
                render_preload_templates(knowl, registry, fragment_cache, preload_targets),
                "</main>",
            ]
        ),
        preload_mode=preload_mode,
        profile=profile,
    )


def html_document(
    title: str,
    body: str,
    preload_mode: str = "eager",
    profile: BuildProfile = BUILD_PROFILES["development"],
    page_script: str | None = None,
    canonical_url: str | None = None,
    redirect_url: str | None = None,
) -> str:
    asset_version = runtime_asset_version()
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
    profile_config = json.dumps(
        {"profile": profile.name, "features": profile.features},
        separators=(",", ":"),
    ).replace("</", "<\\/")
    config_script = f"""  <script>
    (function () {{
      var config = {profile_config};
      config.features = Object.freeze(config.features);
      window.KNOWLPEDIA_CONFIG = Object.freeze(config);
    }}());
  </script>"""
    palette_script = """
        var palette = localStorage.getItem("knowl-palette");
        var palettes = ["current", "original", "washi", "sumi", "aizome"];
        if (palettes.indexOf(palette) === -1) palette = "current";
        document.documentElement.dataset.palette = palette;""" if profile.show_testing_ui else ""
    theme_script = """  <script>
    (function () {
      try {
        var theme = localStorage.getItem("knowl-theme");
        if (theme !== "dark" && theme !== "light") {
          theme = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
        }
        document.documentElement.dataset.theme = theme;
__PALETTE_SCRIPT__
      } catch (error) {}
    }());
  </script>""".replace("__PALETTE_SCRIPT__", palette_script)
    testing_button = """
    <button type="button" id="testing-open" class="header-action testing-trigger" aria-haspopup="dialog" aria-controls="testing-panel" aria-expanded="false"><span aria-hidden="true">◫</span><span class="testing-label">Testing</span></button>""" if profile.show_testing_ui else ""
    testing_panel = """
<aside id="testing-panel" class="testing-panel" role="dialog" aria-modal="false" aria-labelledby="testing-title" hidden>
  <div class="testing-heading">
    <div><p class="kind">Visual lab</p><h2 id="testing-title">Test site styles</h2></div>
    <button type="button" id="testing-close" class="icon-button" aria-label="Close testing panel">&times;</button>
  </div>
  <p class="testing-intro">Compare temporary site-wide CSS settings. Your selection is saved in this browser.</p>
  <p class="testing-content-link"><a href="/testing/">Browse development-only documents</a></p>
  <fieldset class="testing-fieldset">
    <legend>Color palette</legend>
    <div class="palette-options" role="radiogroup" aria-label="Color palette">
      <button type="button" class="palette-option" data-palette-value="current" role="radio" aria-checked="false"><span class="palette-swatch" aria-hidden="true"><i></i><i></i></span><span><strong>Current</strong><small>Pine green baseline</small></span></button>
      <button type="button" class="palette-option" data-palette-value="original" role="radio" aria-checked="false"><span class="palette-swatch" aria-hidden="true"><i></i><i></i></span><span><strong>Original</strong><small>Pre-refactor PaperMod</small></span></button>
      <button type="button" class="palette-option" data-palette-value="washi" role="radio" aria-checked="false"><span class="palette-swatch" aria-hidden="true"><i></i><i></i></span><span><strong>Washi</strong><small>Warm paper and charcoal</small></span></button>
      <button type="button" class="palette-option" data-palette-value="sumi" role="radio" aria-checked="false"><span class="palette-swatch" aria-hidden="true"><i></i><i></i></span><span><strong>Sumi mist</strong><small>Cool ink and fog</small></span></button>
      <button type="button" class="palette-option" data-palette-value="aizome" role="radio" aria-checked="false"><span class="palette-swatch" aria-hidden="true"><i></i><i></i></span><span><strong>Aizome</strong><small>Indigo mountain haze</small></span></button>
    </div>
  </fieldset>
</aside>""" if profile.show_testing_ui else ""
    testing_script = f'  <script defer src="/assets/knowl-testing.js?v={asset_version}"></script>' if profile.show_testing_ui else ""
    page_script_html = (
        f'  <script defer src="/assets/{escape_attr(page_script)}?v={asset_version}"></script>'
        if page_script
        else ""
    )
    canonical_tags = (f'  <link rel="canonical" href="{escape_attr(canonical_url)}">\n' if canonical_url else "")
    redirect_script = (f'  <noscript><meta http-equiv="refresh" content="0;url={escape_attr(redirect_url)}"></noscript>\n' if redirect_url else "")
    return f"""<!doctype html>
<html lang="en" data-knowlpedia-profile="{escape_attr(profile.name)}" data-knowlpedia-development-content="{str(profile.include_development_content).lower()}" data-knowlpedia-testing-ui="{str(profile.show_testing_ui).lower()}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
{canonical_tags}{redirect_script}
{config_script}
{theme_script}
  <link rel="stylesheet" href="/assets/katex.min.css?v={asset_version}">
  <link rel="stylesheet" href="/assets/knowl.css?v={asset_version}">
  <script defer src="/assets/knowl.js?v={asset_version}"></script>
{testing_script}
{page_script_html}
{math_script.rstrip()}
</head>
<body data-knowl-preload="{escape_attr(preload_mode)}">
<a class="skip-link" href="#main-content">Skip to content</a>
<header class="site-header">
  <div class="site-identity">
    <a class="site-brand" href="/" aria-label="Knowlpedia home"><span class="brand-mark" aria-hidden="true">K</span><span>Knowlpedia</span></a>
    <nav class="site-nav" aria-label="Primary"><a href="/graph/">Graph</a><a href="/index/">Index</a></nav>
  </div>
  <div class="site-actions">
    <button type="button" id="search-open" class="header-action" aria-haspopup="dialog" aria-controls="search-dialog"><span class="header-action-icon" aria-hidden="true">⌕</span><span>Search</span><kbd>⌘K</kbd></button>
{testing_button}
    <button type="button" id="theme-toggle" class="header-action theme-toggle" aria-label="Use dark theme" aria-pressed="false"><span class="theme-icon header-action-icon" aria-hidden="true">◐</span><span class="theme-label">Dark</span></button>
  </div>
</header>
{testing_panel}
<div id="search-dialog" class="search-dialog" role="dialog" aria-modal="true" aria-labelledby="search-title" hidden>
  <div class="search-surface">
    <div class="search-heading"><div><p class="kind">Find a concept</p><h2 id="search-title">Search Knowlpedia</h2></div><button type="button" id="search-close" class="icon-button" aria-label="Close search">&times;</button></div>
    <label class="search-label" for="search-input">Search by name, alias, or description</label>
    <input id="search-input" class="search-input" type="search" autocomplete="off" spellcheck="false" placeholder="Try “étale topology” or “compact”…" aria-controls="search-results">
    <p id="search-status" class="search-status" aria-live="polite">Start typing to search the mathematical index.</p>
    <ul id="search-results" class="search-results" role="listbox"></ul>
  </div>
</div>
{body}
</body>
</html>
"""


def directory_title(subject_id: str) -> str:
    return SOURCE_COLLECTIONS.get(subject_id, SUBJECT_TITLES.get(subject_id, humanize_identifier(subject_id)))


def directory_groups(registry: dict[str, Knowl]) -> dict[str, list[Knowl]]:
    grouped: dict[str, list[Knowl]] = {}
    for knowl in registry.values():
        subject_id = knowl.id.split("/", 1)[0]
        if knowl.visibility == "production" and not knowl.redirect_to and subject_id not in DIRECTORY_EXCLUDED_SUBJECTS:
            grouped.setdefault(subject_id, []).append(knowl)
    return dict(sorted(grouped.items(), key=lambda item: directory_title(item[0]).casefold()))


def render_homepage(
    registry: dict[str, Knowl],
    package: dict[str, Any],
    profile: BuildProfile = BUILD_PROFILES["development"],
) -> str:
    grouped = directory_groups(registry)
    knowl_count = sum(len(knowls) for knowls in grouped.values())
    subject_links = []
    collection_links = []
    for subject_id, knowls in grouped.items():
        title = directory_title(subject_id)
        links = collection_links if subject_id in SOURCE_COLLECTIONS else subject_links
        links.append(
            f'<li><a href="/index/#subject-{escape_attr(subject_id)}">'
            f'<span>{render_inline(title, registry)}</span><small>{len(knowls):,}</small></a></li>'
        )

    body = "\n".join(
        [
            '<main class="start-shell" id="main-content">',
            '<section class="start-intro" aria-labelledby="home-title">',
            '<h1 id="home-title">Knowlpedia</h1>',
            f'<p>A linked library of {knowl_count:,} mathematical concepts and reading guides.</p>',
            '<button type="button" class="start-search" data-open-search><span aria-hidden="true">⌕</span><span>Search the mathematical library</span><kbd>⌘K</kbd></button>',
            '</section>',
            '<nav class="start-actions" aria-label="Ways to explore">',
            '<a href="/graph/"><strong>Dependency graph</strong><small>Explore prerequisites and dependents</small><span aria-hidden="true">&#8594;</span></a>',
            f'<a href="/index/"><strong>Complete index</strong><small>Browse all {knowl_count:,} knowls</small><span aria-hidden="true">&#8594;</span></a>',
            '</nav>',
            '<section class="start-subjects" aria-labelledby="subjects-title">',
            '<div class="start-section-heading"><h2 id="subjects-title">Subjects</h2><p>Compact definitions first; examples, proofs, and references when needed.</p></div>',
            '<ul>' + "".join(subject_links) + '</ul>',
            '</section>',
            '<section class="start-subjects start-collections" aria-labelledby="collections-title">'
            '<div class="start-section-heading"><h2 id="collections-title">Sources and collections</h2>'
            '<p>Read through a paper or explore a connected collection.</p></div><ul>'
            + "".join(collection_links) + '</ul></section>' if collection_links else "",
            '</main>',
        ]
    )
    return html_document(
        "Knowlpedia — Mathematical knowledge, connected",
        body,
        preload_mode="none",
        profile=profile,
    )


def render_graph_page(
    registry: dict[str, Knowl],
    package: dict[str, Any],
    profile: BuildProfile = BUILD_PROFILES["development"],
) -> str:
    default = registry.get(GRAPH_DEFAULT_FOCUS)
    default_title = default.title if default else "a concept"
    body = "\n".join(
        [
            '<main class="graph-shell" id="main-content" data-dependency-graph '
            f'data-default-focus="{escape_attr(GRAPH_DEFAULT_FOCUS)}">',
            '<section class="graph-workspace" aria-label="Dependency map">',
            '<div class="graph-toolbar">',
            '<div class="graph-find">',
            '<label for="graph-search">Find a concept</label>',
            f'<input id="graph-search" type="search" autocomplete="off" spellcheck="false" placeholder="Try {escape_attr(default_title)}" aria-controls="graph-search-results">',
            '<div id="graph-search-results" class="graph-search-results" hidden></div>',
            '</div>',
            '<label class="graph-depth-label" for="graph-depth">Depth<select id="graph-depth"><option value="1">1 step</option><option value="2" selected>2 steps</option><option value="3">3 steps</option></select></label>',
            '<label class="graph-review-filter-label" for="graph-review-filter"><input id="graph-review-filter" type="checkbox">Reviewed links only</label>',
            '<button type="button" id="graph-orientation" class="graph-tool-button" aria-label="Switch to vertical layout">Vertical</button>',
            '<button type="button" id="graph-fit" class="graph-tool-button">Fit</button>',
            '</div>',
            '<div class="graph-stage" id="graph-stage">',
            '<div class="graph-status" id="graph-status" role="status">Loading dependency data…</div>',
            '<svg id="dependency-map" class="dependency-map" role="img" aria-labelledby="graph-map-title graph-map-description">',
            '<title id="graph-map-title">Knowlpedia dependency graph</title>',
            '<desc id="graph-map-description">Prerequisites flow toward concepts they unlock.</desc>',
            '<defs><marker id="graph-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z"></path></marker></defs>',
            '<g class="graph-edge-layer"></g><g class="graph-node-layer"></g>',
            '</svg>',
            '<div class="graph-legend" aria-label="Graph legend"><span><i class="legend-edge"></i> prerequisite flow</span><span><i class="legend-edge unreviewed"></i> unreviewed heuristic</span><span><i class="legend-node"></i> current knowl</span></div>',
            '</div>',
            '</section>',
            '<aside class="graph-viewer" id="graph-viewer" aria-live="polite">',
            '<header class="graph-viewer-header"><div><p class="kind">Selected knowl</p><h1 id="graph-viewer-title">Choose a node</h1></div><button type="button" id="graph-viewer-close" class="icon-button" aria-label="Close knowl viewer">&times;</button></header>',
            '<p id="graph-viewer-summary" class="graph-viewer-summary">Select a node to inspect its definition and redraw the map around it.</p>',
            '<div id="graph-review-state" class="graph-review-state"></div>',
            '<div id="graph-viewer-content" class="graph-viewer-content"></div>',
            '</aside>',
            '</main>',
        ]
    )
    return html_document(
        f"Dependency graph - {package['title']}",
        body,
        preload_mode="visible",
        profile=profile,
        page_script="graph.js",
    )


def render_index(
    registry: dict[str, Knowl],
    package: dict[str, Any],
    profile: BuildProfile = BUILD_PROFILES["development"],
) -> str:
    grouped = directory_groups(registry)

    knowl_count = sum(len(items) for items in grouped.values())
    parts = [
        '<main class="page-shell index-shell" id="main-content">',
        '<header class="page-header index-hero">',
        '<p class="index-kicker">Mathematical knowledge, connected</p>',
        f'<h1>Browse all {knowl_count:,} knowls by subject</h1>',
        '<p class="index-summary">Open a definition without losing your place, then follow its prerequisites as deeply as you need.</p>',
        "</header>",
        '<div class="index-tools">',
        '<label class="index-subject-filter" for="subject-filter"><span class="header-action-icon" aria-hidden="true">⌕</span><input id="subject-filter" type="search" autocomplete="off" spellcheck="false" placeholder="Filter subjects and collections" aria-describedby="subject-filter-status"></label>',
        f'<p id="subject-filter-status" class="index-filter-status" role="status">{len(grouped)} subjects and collections</p>',
        '</div>',
        '<p class="index-instruction">Expand any term in place.</p>',
    ]
    previous_collection = None
    ordered_groups = sorted(grouped.items(), key=lambda item: (item[0] in SOURCE_COLLECTIONS, directory_title(item[0]).casefold()))
    for group, knowls in ordered_groups:
        collection = group in SOURCE_COLLECTIONS
        if collection != previous_collection:
            parts.append('<h2 class="index-group-heading">' + ("Sources and collections" if collection else "Subjects") + '</h2>')
            previous_collection = collection
        label = directory_title(group)
        parts.append(
            f'<details class="index-section" id="subject-{escape_attr(group)}" data-directory-kind="{"collection" if collection else "subject"}" data-subject-name="{escape_attr(label + " " + group)}"><summary><span>{html.escape(label)}</span>'
            f'<span class="index-count">{len(knowls)} knowls</span></summary><ul class="index-list">'
        )
        for knowl in sorted(knowls, key=lambda k: k.title.lower()):
            parts.append(
                f'<li class="index-item"><a class="knowl index-knowl" href="{escape_attr(target_href(knowl.id))}" '
                f'data-knowl="{escape_attr(fragment_href(knowl.id))}" aria-expanded="false">{render_inline(knowl.title, registry)}</a> '
                f'<span class="summary">{render_inline(knowl.summary, registry)}</span></li>'
            )
        parts.append("</ul></details>")
    parts.append("</main>")
    return html_document(f"Index - {package['title']}", "\n".join(parts), preload_mode="visible", profile=profile)


def render_testing_hub(
    registry: dict[str, Knowl],
    package: dict[str, Any],
    profile: BuildProfile,
) -> str:
    testing_knowls = sorted(
        (knowl for knowl in registry.values() if knowl.visibility == "development"),
        key=lambda knowl: knowl.title.lower(),
    )
    items = []
    for knowl in testing_knowls:
        items.append(
            '<li class="testing-index-item">'
            f'<a href="{escape_attr(target_href(knowl.id))}">{html.escape(knowl.title)}</a>'
            '<span class="testing-badge">Testing</span>'
            f'<p>{html.escape(knowl.summary)}</p></li>'
        )
    body = "\n".join(
        [
            '<main class="page-shell testing-index" id="main-content">',
            '<nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Knowlpedia</a><span aria-hidden="true">/</span><span>Testing</span></nav>',
            '<header class="page-header"><p class="kind">Development only</p><h1>Testing content</h1>',
            '<p class="page-summary">Drafts, performance fixtures, and rendering labs included in local previews but excluded from production.</p></header>',
            f'<ul class="testing-index-list">{"".join(items)}</ul>',
            "</main>",
        ]
    )
    return html_document(
        f"Testing content - {package['title']}",
        body,
        preload_mode="none",
        profile=profile,
    )


def render_old_topics_page(
    package: dict[str, Any],
    profile: BuildProfile = BUILD_PROFILES["development"],
) -> str:
    links = "\n".join(
        f'    <li><a href="{escape_attr(href)}">{html.escape(label)}</a></li>'
        for label, href in OLD_HUGO_TOPIC_LINKS
    )
    body = "\n".join(
        [
            '<main class="home-content" id="main-content">',
            "  <h1>Topics</h1>",
            "",
            '  <ul class="home-links">',
            links,
            "  </ul>",
            "</main>",
        ]
    )
    return html_document(f"Topics - {package['title']}", body, preload_mode="none", profile=profile)


def validate(registry: dict[str, Knowl]) -> list[ValidationMessage]:
    messages: list[ValidationMessage] = []
    aliases: dict[str, str] = {}
    for knowl in registry.values():
        if (
            isinstance(knowl.dependency_review_count, bool)
            or not isinstance(knowl.dependency_review_count, int)
            or knowl.dependency_review_count < 0
        ):
            messages.append(
                ValidationMessage(
                    "error",
                    knowl.id,
                    "dependency_review_count must be a nonnegative integer",
                )
            )
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

        for target in knowl.prerequisites:
            validate_target(messages, registry, knowl.id, target, "prerequisite")

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

    validate_prerequisite_cycles(messages, registry)
    return messages


def validate_prerequisite_cycles(
    messages: list[ValidationMessage], registry: dict[str, Knowl]
) -> None:
    """Reject authored prerequisite loops while allowing ordinary links to cycle."""

    state: dict[str, int] = {}
    path: list[str] = []
    reported: set[frozenset[str]] = set()

    def visit(knowl_id: str) -> None:
        state[knowl_id] = 1
        path.append(knowl_id)
        for target in registry[knowl_id].prerequisites:
            base, _ = split_target(target)
            if base not in registry:
                continue
            if state.get(base, 0) == 0:
                visit(base)
                continue
            if state.get(base) != 1:
                continue
            cycle_start = path.index(base)
            cycle = path[cycle_start:] + [base]
            cycle_key = frozenset(cycle)
            if cycle_key in reported:
                continue
            reported.add(cycle_key)
            severity = (
                "error"
                if all(registry[item].dependency_review_count > 0 for item in cycle_key)
                else "warning"
            )
            messages.append(
                ValidationMessage(
                    severity,
                    knowl_id,
                    "prerequisite cycle"
                    + (" survived review: " if severity == "error" else " in unreviewed metadata: ")
                    + " -> ".join(cycle),
                )
            )
        path.pop()
        state[knowl_id] = 2

    for knowl_id in registry:
        if state.get(knowl_id, 0) == 0:
            visit(knowl_id)


def wikilinks_in_text(text: str) -> list[str]:
    text = FENCED_CODE_RE.sub("@@KNOWL_CODE_BLOCK@@", text)
    text, _ = protect_inline_code(text)
    protected, _ = protect_math(text)
    return [match.group(1).strip() for match in WIKILINK_RE.finditer(protected)]


def collect_links(knowl: Knowl, registry: dict[str, Knowl] | None = None) -> list[dict[str, str]]:
    links: list[dict[str, str]] = []

    def add(target: str, source_part: str, link_type: str = "mentions") -> None:
        if registry is not None:
            target = canonical_target(registry, target)
        links.append(
            {
                "source": knowl.id,
                "source_part": source_part,
                "type": link_type,
                "target": target,
            }
        )

    for target in knowl.prerequisites:
        add(target, "metadata.prerequisites", "prerequisite")
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
    base, anchor = split_target(canonical_target(registry, target))
    if base not in registry:
        messages.append(ValidationMessage("error", source, f"{context}: missing target {target}"))
        return
    knowl = registry[base]
    if anchor and anchor not in knowl.anchors:
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


def write_compact_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )


def discovery_aliases(knowl: Knowl, registry: dict[str, Knowl]) -> list[str]:
    result = list(knowl.aliases)
    if isinstance(registry, AliasRegistry):
        for alias in registry.aliases:
            if registry.canonical_id(alias) == knowl.id:
                retired = registry._redirects.get(alias)
                result.extend([alias, retired.title, *retired.aliases] if retired else [alias])
    return list(dict.fromkeys(result))


def registry_json(registry: dict[str, Knowl]) -> dict[str, Any]:
    return {
        knowl.id: {
            "id": knowl.id,
            "title": knowl.title,
            "kind": knowl.kind,
            "summary": knowl.summary,
            "aliases": discovery_aliases(knowl, registry),
            "domains": knowl.domains,
            "prerequisites": list(dict.fromkeys(canonical_target(registry, target) for target in knowl.prerequisites)),
            "dependency_heuristic": knowl.dependency_heuristic,
            "dependency_review_count": knowl.dependency_review_count,
            "visibility": knowl.visibility,
            "href": target_href(knowl.id),
            "fragment": fragment_href(knowl.id),
            "anchors": sorted(knowl.anchors),
            "sections": [
                {
                    "id": section["id"],
                    "title": section["title"],
                    "kind": section.get("kind", "markdown"),
                    "fragment": section_fragment_href(knowl.id, section["id"]),
                }
                for section in knowl.sections
            ],
            "content_hash": knowl.content_hash,
        }
        for knowl in registry.values()
    }


def search_json(registry: dict[str, Knowl]) -> list[dict[str, Any]]:
    return [
        {
            "id": knowl.id,
            "title": knowl.title,
            "kind": display_kind(knowl.kind) or "Concept",
            "summary": knowl.summary,
            "aliases": discovery_aliases(knowl, registry),
            "domains": knowl.domains,
            "dependency_review_count": knowl.dependency_review_count,
            "href": target_href(knowl.id),
            "visibility": knowl.visibility,
        }
        for knowl in registry.values()
    ]


def relations_json(registry: dict[str, Knowl]) -> list[dict[str, Any]]:
    relations = []
    for knowl in registry.values():
        for relation in knowl.relations:
            item = {"source": knowl.id, **relation}
            item["target"] = canonical_target(registry, item["target"])
            relations.append(item)
    return relations


def links_json(registry: dict[str, Knowl]) -> list[dict[str, Any]]:
    links = []
    for knowl in registry.values():
        for link in collect_links(knowl, registry):
            links.append(link)
    return links


def dependency_graph_json(registry: dict[str, Knowl]) -> dict[str, Any]:
    """Return the authored learning graph, distinct from incidental wikilinks.

    Edges point from a prerequisite toward the concept it unlocks, matching the
    direction a learner would move through a topological ordering.
    """

    nodes = [
        {
            "id": knowl.id,
            "title": knowl.title,
            "kind": display_kind(knowl.kind) or "Concept",
            "summary": knowl.summary,
            "domains": knowl.domains,
            "dependency_heuristic": knowl.dependency_heuristic,
            "dependency_review_count": knowl.dependency_review_count,
            "href": target_href(knowl.id),
            "fragment": fragment_href(knowl.id),
            "visibility": knowl.visibility,
        }
        for knowl in registry.values()
    ]
    edges = []
    for knowl in registry.values():
        for prerequisite in knowl.prerequisites:
            source, _ = split_target(canonical_target(registry, prerequisite))
            if source not in registry:
                continue
            edges.append(
                {
                    "source": source,
                    "target": knowl.id,
                    "type": "prerequisite",
                    "authored": True,
                    "dependency_review_count": knowl.dependency_review_count,
                    "reviewed": knowl.dependency_review_count > 0,
                    "provenance": knowl.dependency_heuristic or "authored",
                }
            )
    return {
        "version": 1,
        "edge_direction": "prerequisite-to-dependent",
        "nodes": nodes,
        "edges": edges,
    }


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


def copy_runtime_assets(out_dir: Path, profile: BuildProfile) -> None:
    runtime_dir = Path(__file__).resolve().parents[1] / "static-runtime"
    assets_dir = out_dir / "assets"
    assets_dir.mkdir(parents=True, exist_ok=True)
    for filename in ("knowl.css", "knowl.js", "graph.js"):
        shutil.copyfile(runtime_dir / filename, assets_dir / filename)
    if profile.show_testing_ui:
        shutil.copyfile(runtime_dir / "knowl-testing.js", assets_dir / "knowl-testing.js")

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


def write_site(
    package_dir: Path,
    out_dir: Path,
    allow_validation_errors: bool = False,
    profile: BuildProfile = BUILD_PROFILES["development"],
    only_ids: set[str] | None = None,
) -> int:
    return write_site_for_ids(
        package_dir,
        out_dir,
        only_ids=only_ids,
        allow_validation_errors=allow_validation_errors,
        profile=profile,
    )


def write_site_for_ids(
    package_dir: Path,
    out_dir: Path,
    only_ids: set[str] | None = None,
    allow_validation_errors: bool = False,
    profile: BuildProfile = BUILD_PROFILES["development"],
) -> int:
    package_path = package_dir / "knowlpack.toml"
    package = read_toml(package_path)
    knowls, content_roots = discover_package_knowls(package_dir, package, profile)
    all_by_id = {knowl.id: knowl for knowl in knowls}
    if len(all_by_id) != len(knowls):
        duplicates = sorted({knowl.id for knowl in knowls if sum(k.id == knowl.id for k in knowls) > 1})
        raise ValueError("Duplicate knowl ids: " + ", ".join(duplicates))
    redirects = {knowl.id: knowl for knowl in knowls if knowl.redirect_to}
    canonical = {knowl.id: knowl for knowl in knowls if not knowl.redirect_to}
    aliases: dict[str, str] = {}
    resolving: set[str] = set()
    def resolve_redirect(old_id: str) -> str | None:
        if old_id in canonical:
            return old_id
        if old_id in resolving:
            return None
        redirect = redirects.get(old_id)
        if not redirect or not redirect.redirect_to:
            return None
        resolving.add(old_id)
        result = resolve_redirect(redirect.redirect_to)
        resolving.remove(old_id)
        if result:
            aliases[old_id] = redirect.redirect_to
        return result
    for old_id in redirects:
        resolve_redirect(old_id)
    # Lexical aliases are search terms; only explicit redirect IDs resolve as
    # IDs, avoiding accidental hijacking of a real canonical ID.
    registry = AliasRegistry(canonical, aliases, redirects)
    messages = validate(registry)
    for old_id, redirect in redirects.items():
        target = redirect.redirect_to
        if not target or target not in all_by_id:
            messages.append(ValidationMessage("error", old_id, f"redirect target missing: {target}"))
        elif target == old_id or resolve_redirect(old_id) is None:
            messages.append(ValidationMessage("error", old_id, f"redirect target is cyclic or unresolved: {target}"))
        for old_section, new_section in redirect.redirect_sections.items():
            resolved_target = resolve_redirect(target) if target in redirects else target
            if resolved_target in canonical:
                mapped = split_target(registry.canonical_target(f"{old_id}#{old_section}"))[1]
                if not mapped or f"section.{mapped}" not in canonical[resolved_target].anchors:
                    messages.append(ValidationMessage("error", old_id, f"redirect section target missing: {new_section}"))
    errors = [msg for msg in messages if msg.severity == "error"]
    if only_ids:
        missing = sorted(knowl_id for knowl_id in only_ids if knowl_id not in registry)
        if missing:
            for knowl_id in missing:
                messages.append(ValidationMessage("error", knowl_id, "only target not found"))
            errors = [msg for msg in messages if msg.severity == "error"]

    if not only_ids and out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    copy_runtime_assets(out_dir, profile)

    if only_ids:
        target_knowls = [registry[knowl_id] for knowl_id in sorted(only_ids) if knowl_id in registry]
        fragment_cache: dict[str, str] = {}
        for knowl in target_knowls:
            fragment_cache[knowl.id] = render_knowl_core(knowl, registry)
            for target in preload_template_targets(knowl, registry):
                fragment_cache.setdefault(target, render_knowl_core(registry[target], registry))
    else:
        target_knowls = list(registry.values())
        fragment_cache = {knowl.id: render_knowl_core(knowl, registry) for knowl in registry.values()}

        (out_dir / "index.html").write_text(
            render_homepage(registry, package, profile), encoding="utf-8"
        )
        index_path = out_dir / "index" / "index.html"
        index_path.parent.mkdir(parents=True, exist_ok=True)
        index_path.write_text(render_index(registry, package, profile), encoding="utf-8")
        graph_path = out_dir / "graph" / "index.html"
        graph_path.parent.mkdir(parents=True, exist_ok=True)
        graph_path.write_text(render_graph_page(registry, package, profile), encoding="utf-8")
        topics_path = out_dir / "topics" / "index.html"
        topics_path.parent.mkdir(parents=True, exist_ok=True)
        topics_path.write_text(render_old_topics_page(package, profile), encoding="utf-8")
        if profile.include_development_content:
            testing_path = out_dir / "testing" / "index.html"
            testing_path.parent.mkdir(parents=True, exist_ok=True)
            testing_path.write_text(render_testing_hub(registry, package, profile), encoding="utf-8")

    for knowl in target_knowls:
        page_path = out_dir / slug_to_relpath(knowl.id) / "index.html"
        page_path.parent.mkdir(parents=True, exist_ok=True)
        page_path.write_text(render_page(knowl, registry, package, fragment_cache, profile), encoding="utf-8")

        fragment_path = out_dir / "fragments" / slug_to_relpath(knowl.id) / "core.html"
        fragment_path.parent.mkdir(parents=True, exist_ok=True)
        fragment_path.write_text(fragment_cache[knowl.id], encoding="utf-8")

        for section in knowl.sections:
            section_path = out_dir / "fragments" / slug_to_relpath(knowl.id) / "sections" / f'{section["id"]}.html'
            section_path.parent.mkdir(parents=True, exist_ok=True)
            section_path.write_text(render_section(section, registry), encoding="utf-8")

    if not only_ids or redirects.keys() & only_ids:
        for old_id, redirect in redirects.items():
            if only_ids and old_id not in only_ids:
                continue
            target = redirect.redirect_to
            if target not in registry:
                continue
            canonical_id = registry.canonical_id(old_id)
            destination = target_href(canonical_id)
            section_map = {
                old_section: split_target(registry.canonical_target(f"{old_id}#{old_section}"))[1]
                for old_section in redirect.redirect_sections
            }
            redirect_html = render_redirect_page(redirect, destination, profile, section_map)
            page_path = out_dir / slug_to_relpath(old_id) / "index.html"
            page_path.parent.mkdir(parents=True, exist_ok=True)
            page_path.write_text(redirect_html, encoding="utf-8")
            old_fragment = out_dir / "fragments" / slug_to_relpath(old_id) / "core.html"
            old_fragment.parent.mkdir(parents=True, exist_ok=True)
            old_fragment.write_text(fragment_cache[canonical_id], encoding="utf-8")
            for old_section, new_section in section_map.items():
                section = next((item for item in registry[canonical_id].sections if item["id"] == new_section), None)
                if section is not None:
                    section_path = old_fragment.parent / "sections" / f"{old_section}.html"
                    section_path.parent.mkdir(parents=True, exist_ok=True)
                    section_path.write_text(render_section(section, registry), encoding="utf-8")

    if not only_ids:
        write_json(out_dir / "indexes" / "registry.json", registry_json(registry))
        write_compact_json(out_dir / "indexes" / "search.json", search_json(registry))
        write_json(out_dir / "indexes" / "relations.json", relations_json(registry))
        write_json(out_dir / "indexes" / "links.json", links_json(registry))
        write_compact_json(out_dir / "indexes" / "dependencies.json", dependency_graph_json(registry))
        write_json(out_dir / "indexes" / "proofs.json", proofs_json(registry))
        write_json(out_dir / "reports" / "validation.json", [msg.__dict__ for msg in messages])
        write_json(
            out_dir / "reports" / "build.json",
            {
                "profile": profile.name,
                "features": profile.features,
                "content_roots": [
                    {
                        "path": str(path.relative_to(package_dir)),
                        "visibility": visibility,
                    }
                    for path, visibility in content_roots
                ],
                "knowl_count": len(registry),
                "development_knowl_ids": sorted(
                    knowl.id for knowl in registry.values() if knowl.visibility == "development"
                ),
            },
        )
        print(f"Compiled {len(registry)} knowls into {out_dir}")
    else:
        print(f"Compiled {len(target_knowls)} selected knowls into {out_dir}")

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
        "--profile",
        choices=PROFILE_NAMES,
        default=None,
        help="Build profile. Defaults to KNOWLPEDIA_PROFILE, then development.",
    )
    parser.add_argument(
        "--allow-validation-errors",
        action="store_true",
        help="Write artifacts and return success even when semantic validation reports errors",
    )
    parser.add_argument(
        "--only",
        action="append",
        default=[],
        metavar="KNOWL_ID",
        help="Rewrite only the selected knowl page and fragments. Index artifacts are left untouched.",
    )
    parser.add_argument(
        "--diagram-cache-dir",
        type=Path,
        default=Path(".knowl-cache/diagrams"),
        help="Directory for persistent rendered diagram cache entries",
    )
    parser.add_argument(
        "--no-diagram-cache",
        action="store_true",
        help="Disable the persistent rendered diagram cache for this run",
    )
    parser.add_argument(
        "--prebuilt-diagram-dir",
        type=Path,
        default=Path("prebuilt/diagrams"),
        help="Directory containing portable checked-in rendered diagram fragments",
    )
    parser.add_argument(
        "--refresh-prebuilt-diagrams",
        action="store_true",
        help="Render diagrams locally and replace portable checked-in diagram fragments",
    )
    parser.add_argument(
        "--prebuilt-only-diagrams",
        action="store_true",
        help="Disable local TeX rendering and use only portable prebuilt diagram fragments",
    )
    args = parser.parse_args()
    try:
        profile = resolve_profile(args.profile)
    except ValueError as exc:
        parser.error(str(exc))
    DIAGRAM_RENDERER.configure_cache(None if args.no_diagram_cache else args.diagram_cache_dir)
    DIAGRAM_RENDERER.configure_prebuilt(
        args.prebuilt_diagram_dir,
        refresh=args.refresh_prebuilt_diagrams,
    )
    if args.prebuilt_only_diagrams:
        DIAGRAM_RENDERER.disable_local_rendering()
    return write_site_for_ids(
        args.package_dir,
        args.out,
        only_ids=set(args.only) or None,
        allow_validation_errors=args.allow_validation_errors,
        profile=profile,
    )


if __name__ == "__main__":
    raise SystemExit(main())
