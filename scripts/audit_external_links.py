#!/usr/bin/env python3
"""Audit source links and citation pointers outside References sections.

External links and source citations belong only in an H2 ``References``
section. With ``--fix``, external Markdown citations outside that section are
removed rather than converted to plain-text citations. Bibliographic links in
References are left unchanged.
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
PLAIN_BRACKET_RE = re.compile(r"(?<!\[)\[([^\[\]\n]{2,200})\](?![\[(])")
CITATION_SIGNAL_RE = re.compile(
    r"(?:"
    r"\b(?:chapter|chapters|lecture|lectures|section|sections|"
    r"theorem|lemma|proposition|corollary|definition|definitions|"
    r"example|examples|remark|remarks|page|pages|pp)\b"
    r"|§|doi\b|arxiv\b"
    r")",
    re.IGNORECASE,
)


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
    kind: str = "external link"


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
        label = text[start + 1 : label_end]
        # An unmatched mathematical interval opener such as ``[0,\infty)``
        # must not absorb a later Markdown link, possibly across sections.
        if "\n\n" in label or re.search(r"(?m)^##\s", label):
            cursor = start + 1
            continue
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
                label=label,
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


def plain_citation_positions(body: str) -> list[int]:
    """Return conservative matches for bracketed bibliographic pointers."""

    spans = reference_spans(body)
    positions: list[int] = []
    for match in PLAIN_BRACKET_RE.finditer(body):
        if position_in_spans(match.start(), spans):
            continue
        label = match.group(1).strip()
        if CITATION_SIGNAL_RE.search(label):
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
    violations: list[Violation] = []
    external_positions = [link.start for link in external_links_outside_references(body)]
    external_positions.extend(raw_external_positions(body, all_external))
    for position in sorted(set(external_positions)):
        line, excerpt = line_excerpt(body, position)
        prefix_lines = prefix.count("\n")
        violations.append(
            Violation(path, line + prefix_lines, excerpt, "external link")
        )
    for position in plain_citation_positions(body):
        line, excerpt = line_excerpt(body, position)
        prefix_lines = prefix.count("\n")
        violations.append(
            Violation(path, line + prefix_lines, excerpt, "plain-text citation")
        )
    return violations


def remove_inline_citations(body: str, links: list[MarkdownLink]) -> str:
    """Remove citation links and their source-attribution grammar."""

    marker = "\x00CITATION\x00"
    for link in reversed(links):
        body = body[: link.start] + marker + body[link.end :]

    group = rf"{marker}(?:\s*(?:,|;|and|or)\s*{marker})*"
    source_verb = (
        r"(?:develop(?:ed|s)?|treat(?:ed|s)?|discuss(?:ed|es)?|"
        r"record(?:ed|s)?|present(?:ed|s)?|giv(?:en|es)|stat(?:ed|es)|"
        r"explain(?:ed|s)?|formulat(?:ed|es)|describ(?:ed|es)|"
        r"analy[sz](?:ed|es)|work(?:ed|s)?\s+out|introduc(?:ed|es)|"
        r"review(?:ed|s)?|studi(?:ed|es)|deriv(?:ed|es)|prov(?:ed|es)|"
        r"establish(?:ed|es))"
    )
    author = r"(?:[A-Z][\w’'-]+(?:\s+(?:and|[A-Z][\w’'-]+)){0,4}\s+)"
    source_phrase = (
        rf"(?:{author})?{source_verb}\s+(?:in|by)\s*{group}|"
        rf"appears\s+in\s*{group}"
    )
    source_phrase = (
        rf"(?:{source_phrase}|(?:see|compare|consult|follow|follows|"
        rf"according\s+to|as\s+in)\s*{group}|"
        rf"{group}\s+(?:gives|give|proves|prove|states|state|develops|"
        rf"develop|treats|treat|discusses|discuss|records|record)|"
        rf"\b(?:in|by)\s*{group})"
    )

    # Remove a trailing attribution clause while preserving the mathematical
    # sentence before its semicolon or comma.
    body = re.sub(
        rf"\s*;\s*[^.!?\n]*?{source_phrase}[^.!?\n]*(?=[.!?])",
        "",
        body,
        flags=re.IGNORECASE,
    )
    body = re.sub(
        rf",\s*(?:a|an|the|this|that|these|those)\b[^.!?\n]*?"
        rf"{source_phrase}[^.!?\n]*(?=[.!?])",
        "",
        body,
        flags=re.IGNORECASE,
    )

    # Attribution-only sentences add no mathematical content once their
    # bibliography is kept in References.
    body = re.sub(
        rf"(?m)(?:^[ \t]*|(?<=[.!?])[ \t]+)"
        rf"[^.!?\n]*?{source_phrase}[^.!?\n]*[.!?][ \t]*",
        "",
        body,
        flags=re.IGNORECASE,
    )

    # Preserve the punctuation when a citation occupies its own final line.
    body = re.sub(rf"(?m)\n[ \t]*{group}([.!?])[ \t]*$", r"\1", body)

    # Remove remaining appended citations and citation-only lines.
    body = re.sub(group, "", body)
    body = re.sub(r"(?m)^[ \t]*(?:[.,;:]|and[ \t]*[.,;:]?)[ \t]*\n", "", body)
    body = re.sub(r"(?i)(?:\s*;\s*|\s*,\s*)see\s*(?=[.!?])", "", body)
    body = re.sub(r"(?i)(?<!\w)see\s*(?=[.!?])", "", body)
    body = re.sub(r"\(\s*(?:see\s*)?\)", "", body, flags=re.IGNORECASE)
    body = re.sub(r"\s+([,.;:!?])", r"\1", body)
    body = re.sub(r"([.!?])\1+", r"\1", body)
    body = re.sub(r"(?m)[ \t]+$", "", body)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body


def fix_path(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    prefix, body = split_front_matter(text)
    links = external_links_outside_references(body)
    if not links and not re.search(r"^## Reference\s*$", body, re.MULTILINE):
        return 0

    body = remove_inline_citations(body, links)
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
        help="Remove external citations outside References and normalize singular headings.",
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
                f"{violation.path}:{violation.line}: {violation.kind} outside References: "
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
