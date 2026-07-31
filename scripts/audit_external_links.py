#!/usr/bin/env python3
"""Audit external links outside References sections in knowl Markdown.

Knowl bodies may cite sources in prose, but clickable external links belong in
an H2 ``References`` section. With ``--fix``, Markdown links outside that
section are converted from ``[label](URL)`` to the non-clickable citation
``[label]``. Bibliographic links in References are left unchanged.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import re
import sys


H2_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)
RAW_EXTERNAL_RE = re.compile(r"(?:https?://|mailto:)")
REFERENCE_TITLES = {"reference", "references"}


@dataclass(frozen=True)
class MarkdownLink:
    start: int
    end: int
    label: str
    destination: str


@dataclass(frozen=True)
class Violation:
    path: Path
    line: int
    text: str


def split_front_matter(text: str) -> tuple[str, str]:
    if not text.startswith("+++\n"):
        return "", text
    end = text.find("\n+++\n", 4)
    if end == -1:
        return "", text
    boundary = end + len("\n+++\n")
    return text[:boundary], text[boundary:]


def reference_spans(body: str) -> list[tuple[int, int]]:
    headings = list(H2_RE.finditer(body))
    spans: list[tuple[int, int]] = []
    for index, heading in enumerate(headings):
        title = heading.group(1).strip().casefold()
        if title not in REFERENCE_TITLES:
            continue
        end = headings[index + 1].start() if index + 1 < len(headings) else len(body)
        spans.append((heading.start(), end))
    return spans


def position_in_spans(position: int, spans: list[tuple[int, int]]) -> bool:
    return any(start <= position < end for start, end in spans)


def markdown_links(text: str) -> list[MarkdownLink]:
    """Return Markdown links, accepting balanced parentheses in destinations."""

    links: list[MarkdownLink] = []
    cursor = 0
    while cursor < len(text):
        start = text.find("[", cursor)
        if start == -1:
            break
        if start > 0 and text[start - 1] == "!":
            cursor = start + 1
            continue

        label_end = text.find("]", start + 1)
        if label_end == -1:
            break
        destination_start = label_end + 1
        while destination_start < len(text) and text[destination_start] in " \t":
            destination_start += 1
        if destination_start >= len(text) or text[destination_start] != "(":
            cursor = start + 1
            continue

        depth = 1
        index = destination_start + 1
        escaped = False
        while index < len(text) and depth:
            character = text[index]
            if escaped:
                escaped = False
            elif character == "\\":
                escaped = True
            elif character == "(":
                depth += 1
            elif character == ")":
                depth -= 1
            index += 1
        if depth:
            cursor = start + 1
            continue

        destination = text[destination_start + 1 : index - 1].strip()
        if destination.startswith("<") and destination.endswith(">"):
            destination = destination[1:-1].strip()
        destination = destination.split(maxsplit=1)[0] if destination else ""
        links.append(
            MarkdownLink(
                start=start,
                end=index,
                label=text[start + 1 : label_end],
                destination=destination,
            )
        )
        cursor = index
    return links


def external_links_outside_references(body: str) -> list[MarkdownLink]:
    spans = reference_spans(body)
    return [
        link
        for link in markdown_links(body)
        if RAW_EXTERNAL_RE.match(link.destination)
        and not position_in_spans(link.start, spans)
    ]


def raw_external_positions(
    body: str,
    all_external_links: list[MarkdownLink],
) -> list[int]:
    spans = reference_spans(body)
    link_spans = [(link.start, link.end) for link in all_external_links]
    positions: list[int] = []
    for match in RAW_EXTERNAL_RE.finditer(body):
        if position_in_spans(match.start(), spans):
            continue
        if position_in_spans(match.start(), link_spans):
            continue
        positions.append(match.start())
    return positions


def line_excerpt(text: str, position: int) -> tuple[int, str]:
    line = text.count("\n", 0, position) + 1
    start = text.rfind("\n", 0, position) + 1
    end = text.find("\n", position)
    if end == -1:
        end = len(text)
    return line, text[start:end].strip()


def audit_path(path: Path) -> list[Violation]:
    text = path.read_text(encoding="utf-8")
    prefix, body = split_front_matter(text)
    all_external = [
        link for link in markdown_links(body) if RAW_EXTERNAL_RE.match(link.destination)
    ]
    positions = [link.start for link in external_links_outside_references(body)]
    positions.extend(raw_external_positions(body, all_external))
    violations: list[Violation] = []
    for position in sorted(set(positions)):
        line, excerpt = line_excerpt(body, position)
        prefix_lines = prefix.count("\n")
        violations.append(Violation(path, line + prefix_lines, excerpt))
    return violations


def fix_path(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    prefix, body = split_front_matter(text)
    links = external_links_outside_references(body)
    if not links and not re.search(r"^## Reference\s*$", body, re.MULTILINE):
        return 0

    for link in reversed(links):
        body = body[: link.start] + f"[{link.label}]" + body[link.end :]
    body = re.sub(r"^## Reference\s*$", "## References", body, flags=re.MULTILINE)
    path.write_text(prefix + body, encoding="utf-8")
    return len(links)


def knowl_paths(roots: list[Path]) -> list[Path]:
    paths: set[Path] = set()
    for root in roots:
        if root.is_dir():
            paths.update(root.rglob("*.knowl.md"))
        elif root.name.endswith(".knowl.md"):
            paths.add(root)
    return sorted(paths)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("roots", nargs="+", type=Path)
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Strip external destinations outside References and normalize singular headings.",
    )
    args = parser.parse_args()

    paths = knowl_paths(args.roots)
    changed_files = 0
    stripped_links = 0
    if args.fix:
        for path in paths:
            count = fix_path(path)
            if count:
                changed_files += 1
                stripped_links += count

    violations = [violation for path in paths for violation in audit_path(path)]
    if args.fix:
        print(f"Stripped {stripped_links} inline external links in {changed_files} files.")
    if violations:
        for violation in violations:
            print(
                f"{violation.path}:{violation.line}: external link outside References: "
                f"{violation.text}",
                file=sys.stderr,
            )
        print(
            f"Found {len(violations)} external-link violations in "
            f"{len({violation.path for violation in violations})} files.",
            file=sys.stderr,
        )
        return 1

    print(f"External-link audit passed: {len(paths)} knowl files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
