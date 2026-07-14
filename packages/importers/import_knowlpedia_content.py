#!/usr/bin/env python3
"""Import the legacy knowlpedia-content markdown corpus into knowlpack format."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


SHORTCODE_ATTRS = r"(?:(?:\"[^\"]*\")|[^>])*"
KNOWL_SHORTCODE_RE = re.compile(r"\{\{<\s*knowl\s+(" + SHORTCODE_ATTRS + r")>\}\}")
ANY_SHORTCODE_RE = re.compile(r"\{\{<\s*([A-Za-z0-9_-]+)\b(" + SHORTCODE_ATTRS + r")>\}\}")
ATTR_RE = re.compile(r"([A-Za-z_][A-Za-z0-9_-]*)\s*=\s*\"([^\"]*)\"")


@dataclass
class ImportStats:
    source_files: int = 0
    imported_files: int = 0
    section_pages: int = 0
    root_pages: int = 0
    knowl_shortcodes: int = 0
    converted_shortcodes: int = 0
    malformed_knowl_shortcodes: list[dict[str, str]] = field(default_factory=list)
    unknown_shortcodes: dict[str, int] = field(default_factory=dict)


def toml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def toml_array(values: list[str]) -> str:
    return "[" + ", ".join(toml_string(value) for value in values) + "]"


def humanize_slug(slug: str) -> str:
    return slug.replace("-", " ").replace("_", " ").strip().title() or "Untitled"


def parse_front_matter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        return {}, text.strip()
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text.strip()

    raw = text[4:end]
    body = text[end + 5 :].strip()
    meta: dict[str, Any] = {}
    for line in raw.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or ":" not in stripped:
            continue
        key, raw_value = stripped.split(":", 1)
        key = key.strip()
        value = raw_value.strip()
        meta[key] = parse_front_matter_value(value)
    return meta, body


def parse_front_matter_value(value: str) -> Any:
    if value in {"true", "false"}:
        return value == "true"
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        items = []
        for item in inner.split(","):
            item = item.strip()
            if len(item) >= 2 and item[0] == item[-1] and item[0] in {"'", '"'}:
                item = item[1:-1]
            items.append(item)
        return items
    return value


def imported_id_for(rel_path: Path) -> str:
    if rel_path.name == "_index.md":
        if rel_path.parent == Path("."):
            return "index"
        return rel_path.parent.as_posix()
    return rel_path.with_suffix("").as_posix()


def output_path_for(out_content_dir: Path, rel_path: Path) -> Path:
    if rel_path.name == "_index.md":
        if rel_path.parent == Path("."):
            return out_content_dir / "index.knowl.md"
        return out_content_dir / (rel_path.parent.as_posix() + ".knowl.md")
    return (out_content_dir / rel_path).with_suffix(".knowl.md")


def namespace_for(rel_path: Path) -> str:
    if rel_path.name == "_index.md":
        return "" if rel_path.parent == Path(".") else rel_path.parent.as_posix()
    return "" if rel_path.parent == Path(".") else rel_path.parent.as_posix()


def kind_for(rel_path: Path) -> str:
    if rel_path.name == "_index.md":
        return "section"
    if rel_path.parent == Path(".") or rel_path.parts[0] in {"posts", "preview"}:
        return "page"
    if rel_path.parts[:2] == ("langlands-letter", "letter"):
        return "page"
    return "knowl"


def domains_for(rel_path: Path) -> list[str]:
    if rel_path.parent == Path("."):
        return []
    return [rel_path.parts[0]]


def parse_attrs(raw: str) -> dict[str, str]:
    return {match.group(1): match.group(2) for match in ATTR_RE.finditer(raw)}


def convert_shortcodes(markdown: str, current_namespace: str, source_path: str, stats: ImportStats) -> str:
    def replace_knowl(match: re.Match[str]) -> str:
        stats.knowl_shortcodes += 1
        attrs = parse_attrs(match.group(1))
        knowl_id = attrs.get("id")
        if not knowl_id:
            stats.malformed_knowl_shortcodes.append(
                {"source": source_path, "shortcode": match.group(0), "reason": "missing id"}
            )
            return match.group(0)

        section = attrs.get("section", current_namespace)
        target = f"{section}/{knowl_id}" if section else knowl_id
        label = attrs.get("text", knowl_id)
        stats.converted_shortcodes += 1
        return f"[[{target}|{label}]]"

    converted = KNOWL_SHORTCODE_RE.sub(replace_knowl, markdown)

    for match in ANY_SHORTCODE_RE.finditer(converted):
        name = match.group(1)
        if name == "knowl":
            continue
        stats.unknown_shortcodes[name] = stats.unknown_shortcodes.get(name, 0) + 1

    return converted


def write_imported_file(
    source_file: Path,
    rel_path: Path,
    out_content_dir: Path,
    source_root: Path,
    stats: ImportStats,
) -> dict[str, Any]:
    text = source_file.read_text(encoding="utf-8")
    meta, body = parse_front_matter(text)
    imported_id = imported_id_for(rel_path)
    output_path = output_path_for(out_content_dir, rel_path)
    current_namespace = namespace_for(rel_path)
    converted_body = convert_shortcodes(body, current_namespace, rel_path.as_posix(), stats)

    title = str(meta.get("title") or humanize_slug(imported_id.split("/")[-1]))
    summary = str(meta.get("description") or meta.get("summary") or title)
    kind = kind_for(rel_path)
    aliases = [imported_id.split("/")[-1]]
    if title.lower() != aliases[0].lower():
        aliases.append(title)
    aliases = dedupe_preserving_order(aliases)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    imported_text = "\n".join(
        [
            "+++",
            f"id = {toml_string(imported_id)}",
            f"title = {toml_string(title)}",
            f"kind = {toml_string(kind)}",
            f"summary = {toml_string(summary)}",
            f"aliases = {toml_array(aliases)}",
            f"domains = {toml_array(domains_for(rel_path))}",
            f"legacy_source_path = {toml_string(rel_path.as_posix())}",
            "+++",
            "",
            converted_body,
            "",
        ]
    )
    output_path.write_text(imported_text, encoding="utf-8")

    stats.imported_files += 1
    if rel_path.name == "_index.md":
        stats.section_pages += 1
    if rel_path.parent == Path("."):
        stats.root_pages += 1

    return {
        "id": imported_id,
        "source": str(source_file.relative_to(source_root)),
        "output": str(output_path),
        "title": title,
        "kind": kind,
    }


def dedupe_preserving_order(values: list[str]) -> list[str]:
    seen = set()
    result = []
    for value in values:
        normalized = value.lower()
        if normalized in seen:
            continue
        seen.add(normalized)
        result.append(value)
    return result


def write_package_file(out_dir: Path) -> None:
    package = "\n".join(
        [
            'id = "org.knowlpedia.imported-content"',
            'title = "Imported Knowlpedia Content"',
            'version = "0.1.0"',
            'authors = ["Ryan Persson"]',
            'license = "unknown-imported"',
            'content_dir = "content"',
            "",
            "[outputs]",
            "static_site = true",
            "json_indexes = true",
            "sqlite = true",
            "",
        ]
    )
    (out_dir / "knowlpack.toml").write_text(package, encoding="utf-8")


def import_corpus(source_dir: Path, out_dir: Path) -> int:
    source_dir = source_dir.resolve()
    if not source_dir.exists():
        raise FileNotFoundError(source_dir)
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_content_dir = out_dir / "content"
    out_content_dir.mkdir(parents=True)
    write_package_file(out_dir)

    stats = ImportStats()
    manifest = []
    markdown_files = sorted(source_dir.rglob("*.md"))
    stats.source_files = len(markdown_files)
    for source_file in markdown_files:
        rel_path = source_file.relative_to(source_dir)
        manifest.append(write_imported_file(source_file, rel_path, out_content_dir, source_dir, stats))

    report = {
        "source_dir": str(source_dir),
        "out_dir": str(out_dir),
        "stats": {
            "source_files": stats.source_files,
            "imported_files": stats.imported_files,
            "section_pages": stats.section_pages,
            "root_pages": stats.root_pages,
            "knowl_shortcodes": stats.knowl_shortcodes,
            "converted_shortcodes": stats.converted_shortcodes,
            "malformed_knowl_shortcodes": len(stats.malformed_knowl_shortcodes),
            "unknown_shortcodes": stats.unknown_shortcodes,
        },
        "malformed_knowl_shortcodes": stats.malformed_knowl_shortcodes,
        "manifest": manifest,
    }
    (out_dir / "import-report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Imported {stats.imported_files} markdown files into {out_dir}")
    print(f"Converted {stats.converted_shortcodes} knowl shortcodes")
    if stats.unknown_shortcodes:
        print("Unknown shortcodes left in markdown: " + json.dumps(stats.unknown_shortcodes, sort_keys=True))
    if stats.malformed_knowl_shortcodes:
        print(f"Malformed knowl shortcodes: {len(stats.malformed_knowl_shortcodes)}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Import legacy knowlpedia-content into knowlpack source")
    parser.add_argument("source_dir", type=Path)
    parser.add_argument("out_dir", type=Path)
    args = parser.parse_args()
    return import_corpus(args.source_dir, args.out_dir)


if __name__ == "__main__":
    raise SystemExit(main())
