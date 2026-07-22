#!/usr/bin/env python3
"""Compose one canonical Knowlpack package with additional content sources."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import tempfile
import tomllib
from pathlib import Path


MANIFEST_NAME = ".knowl-source-manifest.json"


def read_package(path: Path) -> dict:
    metadata_path = path / "knowlpack.toml"
    if not metadata_path.is_file():
        raise ValueError(f"primary package has no knowlpack.toml: {path}")
    with metadata_path.open("rb") as handle:
        return tomllib.load(handle)


def contributor_content_dir(path: Path) -> Path:
    metadata_path = path / "knowlpack.toml"
    if metadata_path.is_file():
        with metadata_path.open("rb") as handle:
            metadata = tomllib.load(handle)
        content_dir = metadata.get("content_dir", "content")
        if not isinstance(content_dir, str):
            raise ValueError(f"content_dir must be a string in {metadata_path}")
        return path / content_dir
    return path / "content"


def iter_files(root: Path):
    if not root.is_dir():
        raise ValueError(f"content source does not exist: {root}")
    for path in sorted(root.rglob("*")):
        if path.is_file():
            yield path


def copy_tree_checked(
    source_root: Path,
    destination_root: Path,
    owner: str,
    claimed: dict[Path, str],
) -> int:
    count = 0
    for source_path in iter_files(source_root):
        relative = source_path.relative_to(source_root)
        previous = claimed.get(relative)
        if previous is not None:
            raise ValueError(
                f"content path collision at {relative}: supplied by both {previous} and {owner}"
            )
        claimed[relative] = owner
        destination_path = destination_root / relative
        destination_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_path, destination_path)
        count += 1
    return count


def compose(primary: Path, sources: list[Path], output: Path) -> dict:
    primary = primary.resolve()
    sources = [source.resolve() for source in sources]
    output = output.resolve()
    metadata = read_package(primary)
    content_dir_name = metadata.get("content_dir", "content")
    if not isinstance(content_dir_name, str):
        raise ValueError("primary content_dir must be a string")

    all_sources = [primary, *sources]
    if len(set(all_sources)) != len(all_sources):
        raise ValueError("the same content source was supplied more than once")
    for source in all_sources:
        if output == source or output.is_relative_to(source):
            raise ValueError(f"output directory must not be inside a content source: {source}")

    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix=f".{output.name}-", dir=output.parent))
    claimed: dict[Path, str] = {}
    entries = []
    try:
        shutil.copy2(primary / "knowlpack.toml", temporary / "knowlpack.toml")
        destination_content = temporary / content_dir_name
        for package in all_sources:
            source_content = contributor_content_dir(package)
            count = copy_tree_checked(
                source_content,
                destination_content,
                str(package),
                claimed,
            )
            entries.append(
                {
                    "source": str(package),
                    "content_root": str(source_content),
                    "file_count": count,
                }
            )

        development_dirs = metadata.get("development_content_dirs", [])
        if development_dirs and not isinstance(development_dirs, list):
            raise ValueError("primary development_content_dirs must be a list")
        for relative_name in development_dirs:
            if not isinstance(relative_name, str):
                raise ValueError("development content directory names must be strings")
            source_root = primary / relative_name
            if source_root.is_dir():
                shutil.copytree(source_root, temporary / relative_name)

        manifest = {
            "schema_version": 1,
            "primary": str(primary),
            "content_dir": content_dir_name,
            "sources": entries,
            "total_content_files": sum(entry["file_count"] for entry in entries),
        }
        (temporary / MANIFEST_NAME).write_text(
            json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        if output.exists():
            shutil.rmtree(output)
        os.replace(temporary, output)
        return manifest
    except Exception:
        shutil.rmtree(temporary, ignore_errors=True)
        raise


def verify_source_set(manifest: dict, expected_sources: list[Path]) -> None:
    actual = {Path(entry["source"]).resolve() for entry in manifest["sources"]}
    expected = {path.resolve() for path in expected_sources}
    if actual != expected:
        unexpected = sorted(str(path) for path in actual - expected)
        missing = sorted(str(path) for path in expected - actual)
        details = []
        if unexpected:
            details.append("unexpected: " + ", ".join(unexpected))
        if missing:
            details.append("missing: " + ", ".join(missing))
        raise ValueError("composed content source guard failed (" + "; ".join(details) + ")")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compose a primary Knowlpack package with additional content contributors"
    )
    parser.add_argument("--primary", type=Path, required=True)
    parser.add_argument("--source", type=Path, action="append", default=[])
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument(
        "--expect-source",
        type=Path,
        action="append",
        default=[],
        help="Require the composed manifest to contain exactly these sources",
    )
    args = parser.parse_args()
    try:
        manifest = compose(args.primary, args.source, args.out)
        if args.expect_source:
            verify_source_set(manifest, args.expect_source)
    except ValueError as error:
        parser.error(str(error))
    print(
        f"Composed {manifest['total_content_files']} files from "
        f"{len(manifest['sources'])} content sources into {args.out}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
