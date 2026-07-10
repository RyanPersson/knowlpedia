#!/usr/bin/env python3
"""Insert semantic Knowlpack wikilinks from a literal term map."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


PROTECTED = re.compile(
    r"(\[\[(?:(?!\]\]).)*\]\]|```.*?```|`[^`\n]*`|\\\[.*?\\\]|\\\(.*?\\\)|\$\$.*?\$\$|(?<!\$)\$(?!\$).*?(?<!\$)\$(?!\$))",
    re.DOTALL,
)


def compile_terms(entries: list[dict]) -> tuple[re.Pattern[str], dict[str, str]]:
    lookup: dict[str, str] = {}
    for entry in entries:
        target = entry["target"]
        for term in entry["terms"]:
            key = term.casefold()
            if key in lookup and lookup[key] != target:
                raise ValueError(f"term {term!r} maps to multiple targets")
            lookup[key] = target
    alternatives = sorted(lookup, key=len, reverse=True)
    if not alternatives:
        raise ValueError("term map is empty")
    pattern = re.compile(
        r"(?<![\w-])(?:" + "|".join(re.escape(term) for term in alternatives) + r")(?![\w-])",
        re.IGNORECASE,
    )
    return pattern, lookup


def link_segment(text: str, pattern: re.Pattern[str], lookup: dict[str, str]) -> str:
    return pattern.sub(lambda match: f"[[{lookup[match.group(0).casefold()]}|{match.group(0)}]]", text)


def link_document(text: str, entries: list[dict]) -> str:
    math_terms: list[tuple[str, str]] = []
    for entry in entries:
        for term in entry.get("math_terms", []):
            math_terms.append((term, entry["target"]))
    for term, target in sorted(math_terms, key=lambda item: len(item[0]), reverse=True):
        text = text.replace(term, f"[[{target}|{term}]]")
    pattern, lookup = compile_terms(entries)
    pieces: list[str] = []
    position = 0
    for match in PROTECTED.finditer(text):
        pieces.append(link_segment(text[position : match.start()], pattern, lookup))
        pieces.append(match.group(0))
        position = match.end()
    pieces.append(link_segment(text[position:], pattern, lookup))
    return "".join(pieces)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--map", dest="term_map", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--frontmatter", type=Path)
    args = parser.parse_args()

    entries = json.loads(args.term_map.read_text(encoding="utf-8"))
    linked = link_document(args.input.read_text(encoding="utf-8"), entries)
    if args.frontmatter:
        linked = args.frontmatter.read_text(encoding="utf-8").rstrip() + "\n\n" + linked
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(linked, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
