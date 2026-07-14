#!/usr/bin/env python3
"""Render a single TikZ-like diagram block from a Knowlpack Markdown file."""

from __future__ import annotations

import argparse
import html
import re
import sys
from dataclasses import dataclass
from pathlib import Path

from knowl_compile import (
    DIAGRAM_RENDERER,
    contains_diagram_environment,
    copy_runtime_assets,
    diagram_end_for_kind,
    diagram_kind_from_begin,
    diagram_kind_from_fence,
    html_document,
)


@dataclass
class DiagramBlock:
    kind: str
    source: str
    line: int


def extract_diagrams(markdown: str) -> list[DiagramBlock]:
    lines = markdown.splitlines()
    diagrams: list[DiagramBlock] = []
    i = 0
    in_code = False
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if in_code:
            if stripped.startswith("```"):
                in_code = False
            i += 1
            continue

        code_fence = re.match(r"^```\s*([A-Za-z0-9_-]+)?", stripped)
        if code_fence:
            diagram_kind = diagram_kind_from_fence(code_fence.group(1) or "")
            start_line = i + 1
            i += 1
            block_lines: list[str] = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                block_lines.append(lines[i])
                i += 1
            if i < len(lines):
                i += 1
            if diagram_kind:
                diagrams.append(DiagramBlock(diagram_kind, "\n".join(block_lines), start_line))
            else:
                in_code = False
            continue

        if stripped in {"\\[", "$$"}:
            delimiter = "\\]" if stripped == "\\[" else "$$"
            start_line = i + 1
            i += 1
            math_lines: list[str] = []
            while i < len(lines) and lines[i].strip() != delimiter:
                math_lines.append(lines[i])
                i += 1
            if i < len(lines):
                i += 1
            source = "\n".join(math_lines)
            if contains_diagram_environment(source):
                kind = "cd" if "\\begin{CD}" in source else "tikz-cd" if "\\begin{tikzcd}" in source else "tikz"
                diagrams.append(DiagramBlock(kind, source, start_line))
            continue

        raw_diagram_kind = diagram_kind_from_begin(stripped)
        if raw_diagram_kind:
            start_line = i + 1
            block_lines = [line]
            end_marker = diagram_end_for_kind(raw_diagram_kind)
            i += 1
            while i < len(lines):
                block_lines.append(lines[i])
                if lines[i].strip().startswith(end_marker):
                    i += 1
                    break
                i += 1
            diagrams.append(DiagramBlock(raw_diagram_kind, "\n".join(block_lines), start_line))
            continue

        i += 1

    return diagrams


def write_preview(block: DiagramBlock, source_path: Path, out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    copy_runtime_assets(out_dir)
    rendered = DIAGRAM_RENDERER.render(block.source, block.kind)
    body = "\n".join(
        [
            '<main class="page-shell">',
            '<article class="knowl-page">',
            '<header class="page-header">',
            '<p class="kind">tikz preview</p>',
            f"<h1>{html.escape(source_path.name)} diagram {block.line}</h1>",
            f"<p>{html.escape(block.kind)} block starting at line {block.line}</p>",
            "</header>",
            '<section class="core-section">',
            rendered,
            "<details>",
            "<summary>Source</summary>",
            f"<pre><code>{html.escape(block.source)}</code></pre>",
            "</details>",
            "</section>",
            "</article>",
            "</main>",
        ]
    )
    preview_path = out_dir / "index.html"
    preview_path.write_text(html_document("TikZ diagram preview", body), encoding="utf-8")
    return preview_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Preview one TikZ diagram block from a Knowlpack Markdown file")
    parser.add_argument("source", type=Path, help="Markdown source file containing diagram blocks")
    parser.add_argument("--index", type=int, default=1, help="1-based diagram index to render")
    parser.add_argument("--out", type=Path, default=Path("tmp/tikz-preview"), help="Output preview directory")
    parser.add_argument(
        "--diagram-cache-dir",
        type=Path,
        default=Path(".knowl-cache/diagrams"),
        help="Directory for persistent rendered diagram cache entries",
    )
    parser.add_argument("--no-diagram-cache", action="store_true", help="Disable persistent diagram cache")
    parser.add_argument(
        "--prebuilt-diagram-dir",
        type=Path,
        default=Path("prebuilt/diagrams"),
        help="Directory containing portable checked-in rendered diagram fragments",
    )
    args = parser.parse_args()

    if args.index < 1:
        print("--index must be 1 or greater", file=sys.stderr)
        return 2
    if not args.source.is_file():
        print(f"Source file not found: {args.source}", file=sys.stderr)
        return 2

    DIAGRAM_RENDERER.configure_cache(None if args.no_diagram_cache else args.diagram_cache_dir)
    DIAGRAM_RENDERER.configure_prebuilt(args.prebuilt_diagram_dir)
    diagrams = extract_diagrams(args.source.read_text(encoding="utf-8"))
    if not diagrams:
        print(f"No TikZ diagram blocks found in {args.source}", file=sys.stderr)
        return 1
    if args.index > len(diagrams):
        print(f"Diagram index {args.index} is out of range; found {len(diagrams)} diagram blocks", file=sys.stderr)
        return 2

    block = diagrams[args.index - 1]
    preview_path = write_preview(block, args.source, args.out)
    print(f"Rendered diagram {args.index}/{len(diagrams)} ({block.kind}, line {block.line}) to {preview_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
