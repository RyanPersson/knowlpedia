#!/usr/bin/env python3
"""Validate, export, and query the sparse mathematical object catalogue."""

from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from pathlib import Path

COMPILER_DIR = Path(__file__).resolve().parents[1] / "packages" / "compiler"
sys.path.insert(0, str(COMPILER_DIR))
import catalog  # noqa: E402


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("--database", type=Path, default=Path("public-imported/indexes/catalog.sqlite"))
    commands = result.add_subparsers(dest="command", required=True)
    for name in ("validate", "export"):
        sub = commands.add_parser(name, help=f"{name.capitalize()} authored JSON shards")
        sub.add_argument("--content-package", type=Path,
                         default=Path(__file__).resolve().parents[2] / "knowlpedia-content")
        if name == "export":
            sub.add_argument("--output-dir", type=Path, required=True, help="Directory for catalog.json and catalog.sqlite")
    commands.add_parser("counts", help="Count stored records, not unrecorded pairs")
    objects = commands.add_parser("objects", help="List objects with optional indexed filters")
    objects.add_argument("--category")
    objects.add_argument("--kind")
    objects.add_argument("--family")
    get = commands.add_parser("get", help="Retrieve a complete record")
    get.add_argument("collection", choices=catalog.COLLECTIONS)
    get.add_argument("id")
    views = commands.add_parser("views", help="List category views of an object")
    views.add_argument("object")
    common = commands.add_parser("common", help="List common categories of two objects")
    common.add_argument("source")
    common.add_argument("target")
    neighbors = commands.add_parser("neighbors", help="Find authored relationship arrows incident to an object")
    neighbors.add_argument("object")
    neighbors.add_argument("--direction", choices=("both", "outgoing", "incoming"), default="both")
    neighbors.add_argument("--category")
    neighbors.add_argument("--kind")
    hom = commands.add_parser("hom", help="Look up recorded Hom information between category view IDs")
    hom.add_argument("source_view")
    hom.add_argument("target_view")
    for name in ("end", "aut"):
        sub = commands.add_parser(name, help=f"Look up recorded {name.capitalize()} information for a category view ID")
        sub.add_argument("view")
    return result


def run(args: argparse.Namespace) -> object:
    if args.command in {"validate", "export"}:
        import knowl_compile as compiler
        root = args.content_package.resolve()
        package = compiler.read_toml(root / "knowlpack.toml")
        knowls, roots = compiler.discover_package_knowls(root, package, compiler.BUILD_PROFILES["production"])
        registry, _ = compiler.build_registry(knowls)
        data = catalog.discover_catalog((path for path, visibility in roots if visibility == "production"), registry)
        if data is None:
            return {"status": "absent", "counts": {}}
        if args.command == "export":
            catalog.export_catalog(data, args.output_dir)
        return {"status": "valid", "counts": data["counts"]}
    with catalog.CatalogQuery(args.database) as query:
        if args.command == "counts":
            return query.counts()
        if args.command == "objects":
            return query.objects(category_id=args.category, kind=args.kind, family=args.family)
        if args.command == "get":
            return query.get(args.collection, args.id)
        if args.command == "views":
            return query.views(args.object)
        if args.command == "common":
            return query.common_categories(args.source, args.target)
        if args.command == "neighbors":
            return query.neighbors(args.object, direction=args.direction, category_id=args.category, kind=args.kind)
        if args.command == "hom":
            return query.morphisms(args.source_view, args.target_view)
        return query.morphisms(args.view, args.view, args.command)


def main() -> int:
    args = parser().parse_args()
    try:
        result = run(args)
    except (OSError, ValueError, KeyError, sqlite3.Error) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
