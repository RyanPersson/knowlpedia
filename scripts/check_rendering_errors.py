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
from urllib.parse import unquote, urlsplit


IGNORED_TAGS = {"script", "style", "noscript", "svg", "math", "annotation", "pre", "code", "title"}
VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}
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
ERROR_CLASSES = {"math-render-error", "diagram-error", "knowl-error", "missing-knowl"}
ALLOWED_RAW_SHORTCODE_PATHS = {
    "fragments/posts/semigroup-quasigroup-structure/core.html",
    "posts/semigroup-quasigroup-structure/index.html",
}
LOCAL_TARGET_ATTRIBUTES = {"href", "src", "data-knowl", "data-section-url", "data-knowl-fragment"}
KNOWL_TARGET_ATTRIBUTES = {"data-knowl", "data-section-url", "data-knowl-fragment"}
HUGO_PLACEHOLDER_RE = re.compile(r"HUGOSHORTCODE\d+[A-Za-z0-9]*")
WIKILINK_RE = re.compile(r"\[\[(?:[A-Za-z0-9_.-]+/[^\]\n]+|[^\]\n]+\|[^\]\n]+)\]\]")
SHORTCODE_RE = re.compile(r"\{\{<\s*[^>]+>\}\}")
DISPLAY_DELIMITER_RE = re.compile(r"(\\\[|\\\]|\$\$)")
INLINE_MATH_RE = re.compile(r"(?<!\\)\$(?!\$)([^$\n]{1,500}?)(?<!\\)\$")
RAW_LATEX_COMMAND_RE = re.compile(r"\\(?:lhd|cdots|triangleleft|cong|subseteq|mathbb|mathcal|frac|to|in)\b")


@dataclass
class Issue:
    severity: str
    kind: str
    file: str
    line: int
    snippet: str


class RenderedHtmlChecker(HTMLParser):
    def __init__(self, path: Path, root: Path, *, require_rendered_diagrams: bool = False) -> None:
        super().__init__(convert_charrefs=True)
        self.path = path.resolve()
        self.root = root.resolve()
        self.issues: list[Issue] = []
        self._ignore_stack: list[bool] = []
        self._ignored_depth = 0
        self._require_rendered_diagrams = require_rendered_diagrams

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        classes = set()
        for name, value in attrs:
            if name == "class" and value:
                classes.update(value.split())

        if tag not in VOID_TAGS:
            ignored = tag in IGNORED_TAGS or bool(classes.intersection(IGNORED_CLASSES))
            self._ignore_stack.append(ignored)
            if ignored:
                self._ignored_depth += 1

        for class_name in sorted(classes.intersection(ERROR_CLASSES)):
            self._add_issue("error", class_name, f"<{tag} class=\"{class_name}\">")
        if self._require_rendered_diagrams and "diagram-source" in classes:
            self._add_issue("error", "diagram-source", f"<{tag} class=\"diagram-source\">")

        for name, value in attrs:
            if name in LOCAL_TARGET_ATTRIBUTES and value:
                self._check_local_target(name, value)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        if tag.lower() not in VOID_TAGS:
            self.handle_endtag(tag)

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
            try:
                relative_path = str(self.path.relative_to(self.root))
            except ValueError:
                relative_path = str(self.path)
            if relative_path not in ALLOWED_RAW_SHORTCODE_PATHS:
                self._add_issue("error", "raw_shortcode", match.group(0))

        for match in WIKILINK_RE.finditer(text):
            self._add_issue("error", "raw_wikilink", match.group(0))

        for match in DISPLAY_DELIMITER_RE.finditer(text):
            raw_math_spans.append((match.start(), match.end()))
            self._add_issue("error", "raw_display_math_delimiter", context(text, match.start(), match.end()))

        for match in INLINE_MATH_RE.finditer(text):
            if any(match.start() < end and match.end() > start for start, end in raw_math_spans):
                continue
            raw_math_spans.append((match.start(), match.end()))
            self._add_issue("error", "raw_inline_math", context(text, match.start(), match.end()))

        for match in re.finditer(r"\$", text):
            if any(start <= match.start() < end for start, end in raw_math_spans):
                continue
            self._add_issue("error", "raw_dollar", context(text, match.start(), match.end()))

        for match in RAW_LATEX_COMMAND_RE.finditer(text):
            if any(start <= match.start() < end for start, end in raw_math_spans):
                continue
            self._add_issue("error", "raw_latex_command", context(text, match.start(), match.end()))

    def _check_local_target(self, attribute: str, value: str) -> None:
        parsed = urlsplit(value)
        if parsed.scheme or parsed.netloc or value.startswith("//"):
            return
        if not parsed.path:
            return

        decoded_path = unquote(parsed.path)
        if decoded_path.startswith("/"):
            candidate = self.root / decoded_path.lstrip("/")
        else:
            candidate = self.path.parent / decoded_path

        candidate = candidate.resolve()
        try:
            candidate.relative_to(self.root)
        except ValueError:
            self._add_issue("error", "local_target_outside_build", f'{attribute}="{value}"')
            return

        candidates = [candidate]
        if decoded_path.endswith("/") or candidate.is_dir():
            candidates.append(candidate / "index.html")
        elif not candidate.suffix:
            candidates.append(candidate / "index.html")

        if any(path.is_file() for path in candidates):
            return

        kind = "broken_knowl_target" if attribute in KNOWL_TARGET_ATTRIBUTES else "broken_local_link"
        self._add_issue("error", kind, f'{attribute}="{value}"')

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


def scan_file(path: Path, root: Path, *, require_rendered_diagrams: bool = False) -> list[Issue]:
    checker = RenderedHtmlChecker(path, root, require_rendered_diagrams=require_rendered_diagrams)
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


def scan_tree(
    root: Path,
    fragments_only: bool = False,
    *,
    require_rendered_diagrams: bool = False,
) -> list[Issue]:
    issues: list[Issue] = []
    scan_root = root / "fragments" if fragments_only else root
    if not scan_root.exists():
        return issues
    for html_file in sorted(scan_root.rglob("*.html")):
        issues.extend(scan_file(html_file, root, require_rendered_diagrams=require_rendered_diagrams))
    return issues


def check_build_profile(root: Path, required_profile: str) -> list[Issue]:
    issues: list[Issue] = []
    report_path = root / "reports" / "build.json"
    try:
        report = json.loads(report_path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return [Issue("error", "missing_build_report", "reports/build.json", 1, "Build metadata is missing")]
    except json.JSONDecodeError as exc:
        return [Issue("error", "invalid_build_report", "reports/build.json", 1, str(exc))]

    actual_profile = report.get("profile")
    if actual_profile != required_profile:
        issues.append(
            Issue(
                "error",
                "wrong_build_profile",
                "reports/build.json",
                1,
                f"expected {required_profile}, found {actual_profile}",
            )
        )

    if required_profile != "production":
        return issues

    if report.get("development_knowl_ids"):
        issues.append(
            Issue(
                "error",
                "development_content_in_production",
                "reports/build.json",
                1,
                ", ".join(report["development_knowl_ids"][:10]),
            )
        )
    development_roots = [
        item.get("path", "")
        for item in report.get("content_roots", [])
        if item.get("visibility") == "development"
    ]
    if development_roots:
        issues.append(
            Issue(
                "error",
                "development_root_in_production",
                "reports/build.json",
                1,
                ", ".join(development_roots),
            )
        )

    forbidden_paths = [root / "testing", root / "assets" / "knowl-testing.js"]
    for path in forbidden_paths:
        if path.exists():
            issues.append(
                Issue(
                    "error",
                    "testing_artifact_in_production",
                    str(path.relative_to(root)),
                    1,
                    "Development-only artifact exists in production output",
                )
            )

    forbidden_markup = ("id=\"testing-open\"", "id=\"testing-panel\"", "knowl-testing.js")
    for html_file in sorted(root.rglob("*.html")):
        source = html_file.read_text(encoding="utf-8", errors="ignore")
        for marker in forbidden_markup:
            if marker in source:
                issues.append(
                    Issue(
                        "error",
                        "testing_ui_in_production",
                        str(html_file.relative_to(root)),
                        1,
                        marker,
                    )
                )
                break
        production_dataset = (
            'data-knowlpedia-profile="production"',
            'data-knowlpedia-development-content="false"',
            'data-knowlpedia-testing-ui="false"',
        )
        if "<html" in source and any(marker not in source for marker in production_dataset):
            issues.append(
                Issue(
                    "error",
                    "wrong_html_profile",
                    str(html_file.relative_to(root)),
                    1,
                    "Expected production profile and feature flags in the HTML dataset",
                )
            )
    return issues


def print_text_report(issues: list[Issue], max_issues: int) -> None:
    if not issues:
        print("No rendered HTML errors found.")
        return

    print(f"Rendered HTML errors found: {len(issues)}")
    by_kind: dict[str, int] = {}
    files_by_kind: dict[str, set[str]] = {}
    for issue in issues:
        by_kind[issue.kind] = by_kind.get(issue.kind, 0) + 1
        files_by_kind.setdefault(issue.kind, set()).add(issue.file)
    for kind, count in sorted(by_kind.items()):
        affected = len(files_by_kind[kind])
        noun = "file" if affected == 1 else "files"
        print(f"  {kind}: {count} in {affected} {noun}")

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
    parser.add_argument(
        "--fragments-only",
        action="store_true",
        help="Scan canonical knowl fragments only, avoiding copies embedded in pages and indexes.",
    )
    parser.add_argument(
        "--require-rendered-diagrams",
        action="store_true",
        help="Report source-panel diagram fallbacks as rendering errors",
    )
    parser.add_argument(
        "--require-profile",
        choices=("development", "production"),
        help="Require build metadata and reject artifacts that do not match this profile",
    )
    parser.add_argument("--max-issues", type=int, default=80, help="Maximum issues to print in text mode.")
    args = parser.parse_args()

    root = args.root.resolve()
    if not root.exists():
        print(f"error: generated HTML directory does not exist: {root}", file=sys.stderr)
        return 2

    issues = scan_tree(
        root,
        fragments_only=args.fragments_only,
        require_rendered_diagrams=args.require_rendered_diagrams,
    )
    if args.require_profile:
        issues.extend(check_build_profile(root, args.require_profile))
    if args.json:
        print(json.dumps([asdict(issue) for issue in issues], indent=2))
    else:
        print_text_report(issues, args.max_issues)
    return 1 if any(issue.severity == "error" for issue in issues) else 0


if __name__ == "__main__":
    raise SystemExit(main())
