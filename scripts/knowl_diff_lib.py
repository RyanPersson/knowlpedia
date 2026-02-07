#!/usr/bin/env python3
"""Shared helpers for deterministic knowl index/resolution/diff planning."""

from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path
from typing import Dict, List, Sequence, Tuple


def repo_root_from_script(script_path: Path) -> Path:
    return script_path.resolve().parent.parent


def default_content_root(repo_root: Path) -> Path:
    local_content = repo_root / "content"
    sibling_corpus = repo_root.parent / "knowlpedia-content"
    if any(local_content.glob("**/*.md")):
        return local_content
    return sibling_corpus if sibling_corpus.exists() else local_content


def list_markdown_files(content_root: Path) -> List[Path]:
    files = []
    for path in content_root.rglob("*.md"):
        if path.name == "_index.md":
            continue
        rel = path.relative_to(content_root)
        if len(rel.parts) < 2:
            continue
        files.append(path)
    return sorted(files, key=lambda p: str(p.relative_to(content_root)))


def parse_frontmatter(text: str) -> Dict[str, object]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    block = text[4:end]
    lines = block.splitlines()
    data: Dict[str, object] = {}
    i = 0
    while i < len(lines):
        line = lines[i]
        key_match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not key_match:
            i += 1
            continue
        key = key_match.group(1).strip().lower()
        value = key_match.group(2).strip()
        if value:
            data[key] = _parse_scalar_or_inline_list(value)
            i += 1
            continue

        values: List[str] = []
        i += 1
        while i < len(lines):
            item = lines[i]
            m = re.match(r"^\s*-\s+(.*)$", item)
            if not m:
                break
            values.append(_strip_quotes(m.group(1).strip()))
            i += 1
        data[key] = values
    return data


def _parse_scalar_or_inline_list(value: str):
    value = value.strip()
    if value.startswith("[") and value.endswith("]"):
        raw = value[1:-1].strip()
        if not raw:
            return []
        parts = [p.strip() for p in raw.split(",")]
        return [_strip_quotes(p) for p in parts if p]
    return _strip_quotes(value)


def _strip_quotes(value: str) -> str:
    if len(value) >= 2 and (
        (value.startswith('"') and value.endswith('"'))
        or (value.startswith("'") and value.endswith("'"))
    ):
        return value[1:-1]
    return value


def frontmatter_terms(frontmatter: Dict[str, object]) -> Tuple[str, List[str]]:
    title_raw = str(frontmatter.get("title", "")).strip()
    aliases: List[str] = []
    for key in ("aliases", "synonyms"):
        value = frontmatter.get(key)
        if isinstance(value, str):
            aliases.append(value.strip())
        elif isinstance(value, list):
            aliases.extend(str(v).strip() for v in value if str(v).strip())
    aliases = sorted(set(a for a in aliases if a))
    return title_raw, aliases


def normalize_term(term: str, singularize: bool = False) -> str:
    cleaned = unicodedata.normalize("NFKD", term)
    cleaned = "".join(ch for ch in cleaned if not unicodedata.combining(ch))
    cleaned = cleaned.lower()
    cleaned = cleaned.replace("&", " and ")
    cleaned = re.sub(r"[`'’]", "", cleaned)
    cleaned = re.sub(r"[^a-z0-9]+", "-", cleaned)
    cleaned = re.sub(r"-{2,}", "-", cleaned).strip("-")
    if not singularize or not cleaned:
        return cleaned
    tokens = [_singularize_token(tok) for tok in cleaned.split("-") if tok]
    return "-".join(tokens)


def term_variants(term: str) -> List[str]:
    variants = []
    base = normalize_term(term, singularize=False)
    singular = normalize_term(term, singularize=True)
    if base:
        variants.append(base)
    if singular and singular != base:
        variants.append(singular)
    return variants


def _singularize_token(token: str) -> str:
    if len(token) <= 3:
        return token
    if token.endswith("ies") and len(token) > 4:
        return token[:-3] + "y"
    if token.endswith(("sses", "shes", "ches", "xes", "zes")) and len(token) > 4:
        return token[:-2]
    if token.endswith("ses") and len(token) > 4:
        return token[:-1]
    if token.endswith("s") and not token.endswith(("ss", "us", "is")):
        return token[:-1]
    return token


def build_term_map(entries: Sequence[Dict[str, object]]) -> Dict[str, List[str]]:
    term_map: Dict[str, set] = {}
    for entry in entries:
        slug = str(entry["slug"])
        terms = [slug]
        title = str(entry.get("title", "")).strip()
        if title:
            terms.append(title)
        terms.extend(entry.get("aliases", []))
        for term in terms:
            for variant in term_variants(str(term)):
                term_map.setdefault(variant, set()).add(slug)
    return {k: sorted(v) for k, v in sorted(term_map.items())}


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, sort_keys=True)
        fh.write("\n")


def load_alias_map(alias_path: Path) -> Dict[str, str]:
    if not alias_path.exists():
        return {}
    raw = load_json(alias_path)
    if isinstance(raw, dict) and isinstance(raw.get("aliases"), dict):
        alias_items = raw["aliases"]
    elif isinstance(raw, dict):
        alias_items = raw
    else:
        raise ValueError(f"Alias map at {alias_path} must be a JSON object.")

    normalized: Dict[str, str] = {}
    for term, canonical in alias_items.items():
        canonical_slug = normalize_term(str(canonical), singularize=False)
        if not canonical_slug:
            continue
        for variant in term_variants(str(term)):
            normalized[variant] = canonical_slug
    return normalized


def sort_unique(items: Sequence[str]) -> List[str]:
    return sorted(set(items))

