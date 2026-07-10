#!/usr/bin/env python3
"""Inventory single-file Knowlpack knowls as JSON or TSV."""

from __future__ import annotations

import argparse
import json
import sys
import tomllib
from pathlib import Path


def read_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("+++\n"):
        raise ValueError("missing opening TOML front matter")
    end = text.find("\n+++\n", 4)
    if end < 0:
        raise ValueError("missing closing TOML front matter")
    return tomllib.loads(text[4:end])


def inventory(content_root: Path) -> list[dict]:
    records: list[dict] = []
    seen: dict[str, Path] = {}
    for path in sorted(content_root.rglob("*.knowl.md")):
        try:
            meta = read_frontmatter(path)
        except (OSError, ValueError, tomllib.TOMLDecodeError) as exc:
            raise ValueError(f"{path}: {exc}") from exc
        knowl_id = str(meta.get("id", "")).strip()
        title = str(meta.get("title", "")).strip()
        if not knowl_id or not title:
            raise ValueError(f"{path}: missing id or title")
        if knowl_id in seen:
            raise ValueError(f"duplicate id {knowl_id!r}: {seen[knowl_id]} and {path}")
        seen[knowl_id] = path
        records.append(
            {
                "id": knowl_id,
                "title": title,
                "aliases": [str(value) for value in meta.get("aliases", [])],
                "kind": str(meta.get("kind", "")),
                "summary": str(meta.get("summary", "")),
                "path": str(path.resolve()),
            }
        )
    return records


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("content_root", type=Path)
    parser.add_argument("--format", choices=("json", "tsv"), default="json")
    args = parser.parse_args()
    try:
        records = inventory(args.content_root)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 1
    if args.format == "json":
        print(json.dumps(records, ensure_ascii=False, indent=2))
    else:
        print("id\ttitle\taliases\tkind\tpath")
        for item in records:
            aliases = ";".join(item["aliases"])
            print(f'{item["id"]}\t{item["title"]}\t{aliases}\t{item["kind"]}\t{item["path"]}')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
