#!/usr/bin/env python3
"""Build canonical index of knowls from filesystem content."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
from typing import Dict, List

from knowl_diff_lib import (
    build_term_map,
    default_content_root,
    frontmatter_terms,
    list_markdown_files,
    load_json,
    parse_frontmatter,
    repo_root_from_script,
    sort_unique,
    write_json,
)


def compute_fingerprint(files: List[Path], content_root: Path) -> str:
    hasher = hashlib.sha256()
    for path in files:
        rel = str(path.relative_to(content_root))
        stat = path.stat()
        hasher.update(rel.encode("utf-8"))
        hasher.update(b"\0")
        hasher.update(str(stat.st_mtime_ns).encode("utf-8"))
        hasher.update(b"\0")
        hasher.update(str(stat.st_size).encode("utf-8"))
        hasher.update(b"\n")
    return hasher.hexdigest()


def parse_args() -> argparse.Namespace:
    script = Path(__file__).resolve()
    repo_root = repo_root_from_script(script)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--content-root",
        type=Path,
        default=default_content_root(repo_root),
        help="Root directory containing section folders with *.md knowls.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=repo_root / "data" / "knowl-index.json",
        help="Where to write the generated corpus index JSON.",
    )
    parser.add_argument(
        "--allow-duplicate-slugs",
        action="store_true",
        help="Allow duplicate slug collisions across sections.",
    )
    parser.add_argument(
        "--force-rebuild",
        action="store_true",
        help="Ignore fingerprint cache and rebuild index payload.",
    )
    return parser.parse_args()


def build_entries(content_root: Path, files: List[Path]) -> List[Dict[str, object]]:
    entries = []
    for path in files:
        rel = path.relative_to(content_root)
        section = rel.parts[0]
        slug = path.stem
        text = path.read_text(encoding="utf-8")
        frontmatter = parse_frontmatter(text)
        title, aliases = frontmatter_terms(frontmatter)
        entries.append(
            {
                "slug": slug,
                "title": title,
                "section": section,
                "path": str(rel),
                "aliases": aliases,
            }
        )
    entries.sort(key=lambda item: (item["slug"], item["section"], item["path"]))
    return entries


def duplicate_collisions(entries: List[Dict[str, object]]) -> Dict[str, List[str]]:
    slug_to_paths: Dict[str, List[str]] = {}
    for entry in entries:
        slug_to_paths.setdefault(str(entry["slug"]), []).append(str(entry["path"]))
    collisions = {slug: sort_unique(paths) for slug, paths in slug_to_paths.items() if len(set(paths)) > 1}
    return dict(sorted(collisions.items()))


def main() -> int:
    args = parse_args()
    content_root = args.content_root.resolve()
    output_path = args.output.resolve()

    if not content_root.exists():
        raise SystemExit(f"Content root does not exist: {content_root}")

    files = list_markdown_files(content_root)
    fingerprint = compute_fingerprint(files, content_root)

    if output_path.exists() and not args.force_rebuild:
        try:
            existing = load_json(output_path)
            if (
                existing.get("schema_version") == 1
                and existing.get("content_root") == str(content_root)
                and existing.get("scan_fingerprint") == fingerprint
            ):
                print(f"Index is up to date: {output_path}")
                return 0
        except Exception:
            pass

    entries = build_entries(content_root, files)
    collisions = duplicate_collisions(entries)
    if collisions and not args.allow_duplicate_slugs:
        print("Duplicate slug collisions detected:")
        for slug, paths in collisions.items():
            joined = ", ".join(paths)
            print(f"- {slug}: {joined}")
        print("Re-run with --allow-duplicate-slugs to emit index anyway.")
        return 2

    term_map = build_term_map(entries)
    slug_to_entries: Dict[str, List[Dict[str, object]]] = {}
    for entry in entries:
        slug_to_entries.setdefault(str(entry["slug"]), []).append(entry)
    slug_to_entries = {k: sorted(v, key=lambda e: (e["section"], e["path"])) for k, v in sorted(slug_to_entries.items())}

    payload = {
        "schema_version": 1,
        "content_root": str(content_root),
        "scan_fingerprint": fingerprint,
        "allow_duplicate_slugs": bool(args.allow_duplicate_slugs),
        "entries": entries,
        "slug_to_entries": slug_to_entries,
        "term_map": term_map,
        "duplicate_slug_collisions": collisions,
    }
    write_json(output_path, payload)
    print(f"Wrote index with {len(entries)} entries: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
