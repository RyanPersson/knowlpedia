#!/usr/bin/env python3
"""Validate knowl targets and source fidelity of a knowlified Markdown file."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

from inventory_knowls import inventory


WIKILINK = re.compile(r"\[\[([A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)+)(?:#[^|\]]+)?\|((?:(?!\]\]).)*)\]\]", re.DOTALL)
VALID_MATH = re.compile(r"\\\[.*?\\\]|\\\(.*?\\\)|\$\$.*?\$\$|(?<!\$)\$(?!\$).*?(?<!\$)\$(?!\$)", re.DOTALL)
PSEUDO_MATH = re.compile(r"(?<!\\)\([A-Za-z]\)")


def body_without_frontmatter(text: str) -> str:
    if not text.startswith("+++\n"):
        return text
    end = text.find("\n+++\n", 4)
    if end < 0:
        raise ValueError("missing closing TOML front matter")
    body = text[end + 5 :]
    return body[1:] if body.startswith("\n") else body


def strip_links(text: str) -> str:
    return WIKILINK.sub(lambda match: match.group(2), text)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--content-root", type=Path, required=True)
    parser.add_argument("--document", type=Path, required=True)
    parser.add_argument("--original", type=Path)
    parser.add_argument("--extra-document", type=Path, action="append", default=[])
    parser.add_argument("--check-pseudo-math", action="store_true")
    args = parser.parse_args()

    records = inventory(args.content_root)
    known = {record["id"] for record in records}
    source = args.document.read_text(encoding="utf-8")
    body = body_without_frontmatter(source)
    documents = [(args.document, body)] + [
        (path, body_without_frontmatter(path.read_text(encoding="utf-8")))
        for path in args.extra_document
    ]
    matches = [match for _, document_body in documents for match in WIKILINK.finditer(document_body)]
    counts = Counter(match.group(1) for match in matches)
    missing = sorted(target for target in counts if target not in known)

    print(f"links: {len(matches)}")
    print(f"distinct targets: {len(counts)}")
    print(f"missing targets: {len(missing)}")
    for target in missing:
        print(f"  {target}")

    pseudo_math: list[tuple[Path, str]] = []
    if args.check_pseudo_math:
        for path, document_body in documents:
            without_math = VALID_MATH.sub("", document_body)
            pseudo_math.extend((path, match.group(0)) for match in PSEUDO_MATH.finditer(without_math))
        print(f"pseudo-math candidates: {len(pseudo_math)}")
        for path, candidate in pseudo_math:
            print(f"  {path}: {candidate}")

    fidelity_ok = True
    if args.original:
        original = args.original.read_text(encoding="utf-8")
        fidelity_ok = strip_links(body) == original
        print(f"source fidelity: {'pass' if fidelity_ok else 'FAIL'}")

    return 0 if not missing and fidelity_ok and not pseudo_math else 1


if __name__ == "__main__":
    raise SystemExit(main())
