#!/usr/bin/env python3
"""Scan generated knowl HTML for visible rendering errors.

This is the refactor-side equivalent of the old Hugo placeholder checks. It
looks at generated HTML pages and fragments, including <template> content that
becomes an opened knowl panel at runtime.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from html.parser import HTMLParser
from pathlib import Path


IGNORED_TAGS = {"script", "style", "noscript", "svg", "math", "annotation", "pre", "code", "title"}
IGNORED_CLASSES = {
    "katex",
    "katex-html",
    "katex-mathml",
    "math-inline",
    "math-display",
    "math-katex",
    "math-mathml",
    "diagram-source",
}
ERROR_CLASSES = {"math-render-error", "diagram-error", "knowl-error"}
IGNORED_FILES = {
    # Legacy Hugo shortcode with interactive SVG/JS. Keep the content source
    # intact until the shortcode is intentionally migrated into the refactor.
    "posts/semigroup-quasigroup-structure/index.html",
    "fragments/posts/semigroup-quasigroup-structure/core.html",
}

HUGO_PLACEHOLDER_RE = re.compile(r"HUGOSHORTCODE\d+[A-Za-z0-9]*")
WIKILINK_RE = re.compile(r"\[\[(?:[A-Za-z0-9_.-]+/[^\]\n]+|[^\]\n]+\|[^\]\n]+)\]\]")
SHORTCODE_RE = re.compile(r"\{\{<\s*[^>]+>\}\}")
DISPLAY_DELIMITER_RE = re.compile(r"(\\\[|\\\]|\$\$)")
INLINE_MATH_RE = re.compile(r"(?<!\\)\$(?!\$)([^$\n]{1,500}?)(?<!\\)\$")
LATEX_SIGNAL_RE = re.compile(
    r"(\\[A-Za-z]+|\\[{}]|[_^]\{?[A-Za-z0-9]+|[A-Za-z]\s*(?:[_^]\{?[A-Za-z0-9]+|\\)|"
    r"\\(?:in|to|lhd|cdots|cong|subset|subseteq|triangleleft))"
)
RAW_LATEX_COMMAND_RE = re.compile(r"\\(?:lhd|cdots|triangleleft|cong|subseteq|mathbb|mathcal|frac|to|in)\b")


@dataclass
class Issue:
    severity: str
    kind: str
    file: str
    line: int
    snippet: str


class RenderedHtmlChecker(HTMLParser):
    def __init__(self, path: Path, root: Path) -> None:
        super().__init__(convert_charrefs=True)
        self.path = path
        self.root = root
        self.issues: list[Issue] = []
        self._ignore_stack: list[bool] = []
        self._ignored_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        classes = set()
        for name, value in attrs:
            if name == "class" and value:
                classes.update(value.split())

        ignored = tag in IGNORED_TAGS or bool(classes.intersection(IGNORED_CLASSES))
        self._ignore_stack.append(ignored)
        if ignored:
            self._ignored_depth += 1

        for class_name in sorted(classes.intersection(ERROR_CLASSES)):
            self._add_issue("error", class_name, f"<{tag} class=\"{class_name}\">")

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if self._ignore_stack and self._ignore_stack.pop():
            self._ignored_depth -= 1

    def handle_data(self, data: str) -> None:
        if self._ignored_depth:
            return
        text = normalize(data)
        if not text:
            return

        self._check_text(text)

    def _check_text(self, text: str) -> None:
        raw_math_spans: list[tuple[int, int]] = []

        for match in HUGO_PLACEHOLDER_RE.finditer(text):
            self._add_issue("error", "hugo_shortcode_placeholder", match.group(0))

        for match in SHORTCODE_RE.finditer(text):
            self._add_issue("error", "raw_shortcode", match.group(0))

        for match in WIKILINK_RE.finditer(text):
            self._add_issue("error", "raw_wikilink", match.group(0))

        for match in DISPLAY_DELIMITER_RE.finditer(text):
            self._add_issue("error", "raw_display_math_delimiter", context(text, match.start(), match.end()))

        for match in INLINE_MATH_RE.finditer(text):
            inner = match.group(1)
            if LATEX_SIGNAL_RE.search(inner):
                raw_math_spans.append((match.start(), match.end()))
                self._add_issue("error", "raw_inline_math", context(text, match.start(), match.end()))

        for match in RAW_LATEX_COMMAND_RE.finditer(text):
            if any(start <= match.start() < end for start, end in raw_math_spans):
                continue
            self._add_issue("error", "raw_latex_command", context(text, match.start(), match.end()))

    def _add_issue(self, severity: str, kind: str, snippet: str) -> None:
        line, _ = self.getpos()
        try:
            display_path = str(self.path.relative_to(self.root))
        except ValueError:
            display_path = str(self.path)
        self.issues.append(
            Issue(
                severity=severity,
                kind=kind,
                file=display_path,
                line=line,
                snippet=normalize(snippet)[:240],
            )
        )


def normalize(text: str) -> str:
    return " ".join(text.split())


def context(text: str, start: int, end: int, radius: int = 90) -> str:
    return normalize(text[max(0, start - radius) : min(len(text), end + radius)])


def scan_file(path: Path, root: Path) -> list[Issue]:
    checker = RenderedHtmlChecker(path, root)
    try:
        checker.feed(path.read_text(encoding="utf-8", errors="ignore"))
    except Exception as exc:
        return [
            Issue(
                severity="error",
                kind="html_parse_error",
                file=str(path.relative_to(root)),
                line=1,
                snippet=str(exc),
            )
        ]
    return checker.issues


def scan_tree(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    for html_file in sorted(root.rglob("*.html")):
        if html_file.relative_to(root).as_posix() in IGNORED_FILES:
            continue
        issues.extend(scan_file(html_file, root))
    return issues


def print_text_report(issues: list[Issue], max_issues: int) -> None:
    if not issues:
        print("No rendered HTML errors found.")
        return

    print(f"Rendered HTML errors found: {len(issues)}")
    by_kind: dict[str, int] = {}
    for issue in issues:
        by_kind[issue.kind] = by_kind.get(issue.kind, 0) + 1
    for kind, count in sorted(by_kind.items()):
        print(f"  {kind}: {count}")

    print()
    for issue in issues[:max_issues]:
        print(f"{issue.severity}: {issue.kind}: {issue.file}:{issue.line}")
        print(f"  {issue.snippet}")
    if len(issues) > max_issues:
        print(f"\n... {len(issues) - max_issues} more issues not shown")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "root",
        nargs="?",
        default="public-imported",
        type=Path,
        help="Generated HTML directory to scan, usually public-imported or public.",
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of a text report.")
    parser.add_argument("--max-issues", type=int, default=80, help="Maximum issues to print in text mode.")
    args = parser.parse_args()

    root = args.root.resolve()
    if not root.exists():
        print(f"error: generated HTML directory does not exist: {root}", file=sys.stderr)
        return 2

    issues = scan_tree(root)
    if args.json:
        print(json.dumps([asdict(issue) for issue in issues], indent=2))
    else:
        print_text_report(issues, args.max_issues)
    return 1 if any(issue.severity == "error" for issue in issues) else 0


if __name__ == "__main__":
    raise SystemExit(main())
