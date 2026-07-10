#!/usr/bin/env python3
"""Resolve candidate knowl terms to canonical known slugs."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List

from knowl_diff_lib import (
    load_alias_map,
    load_json,
    normalize_term,
    term_variants,
    write_json,
)


def parse_term_inputs(raw_terms: List[str], terms_file: Path | None) -> List[str]:
    terms: List[str] = []
    terms.extend(t.strip() for t in raw_terms if t.strip())
    if terms_file:
        text = terms_file.read_text(encoding="utf-8").strip()
        if not text:
            return terms
        if terms_file.suffix.lower() == ".json":
            payload = json.loads(text)
            if isinstance(payload, list):
                terms.extend(str(item).strip() for item in payload if str(item).strip())
            elif isinstance(payload, dict) and isinstance(payload.get("requested"), list):
                terms.extend(str(item).strip() for item in payload["requested"] if str(item).strip())
            else:
                raise ValueError("JSON terms file must be an array or {\"requested\": [...]} object.")
        else:
            terms.extend(line.strip() for line in text.splitlines() if line.strip())
    return terms


def resolve_term(term: str, index: Dict[str, object], alias_map: Dict[str, str]) -> Dict[str, object]:
    variants = term_variants(term)
    term_map = index.get("term_map", {})
    slug_to_entries = index.get("slug_to_entries", {})

    for variant in variants:
        alias_slug = alias_map.get(variant)
        if alias_slug:
            entries = slug_to_entries.get(alias_slug, [])
            if entries:
                return {
                    "term": term,
                    "normalized": variant,
                    "status": "resolved",
                    "canonical_slug": alias_slug,
                    "match_type": "alias_map",
                    "candidate_paths": [e["path"] for e in entries],
                }
            return {
                "term": term,
                "normalized": variant,
                "status": "missing",
                "canonical_slug": alias_slug,
                "match_type": "alias_map_missing_target",
            }

    matches = []
    for variant in variants:
        matches.extend(term_map.get(variant, []))
    unique_matches = sorted(set(matches))
    if len(unique_matches) == 1:
        slug = unique_matches[0]
        entries = slug_to_entries.get(slug, [])
        return {
            "term": term,
            "normalized": normalize_term(term, singularize=False),
            "status": "resolved",
            "canonical_slug": slug,
            "match_type": "index_term_map",
            "candidate_paths": [e["path"] for e in entries],
        }
    if len(unique_matches) > 1:
        return {
            "term": term,
            "normalized": normalize_term(term, singularize=False),
            "status": "ambiguous",
            "candidate_slugs": unique_matches,
        }
    return {
        "term": term,
        "normalized": normalize_term(term, singularize=False),
        "status": "unresolved",
        "proposed_slug": normalize_term(term, singularize=True) or normalize_term(term, singularize=False),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index", type=Path, required=True, help="Path to knowl index JSON.")
    parser.add_argument("--aliases", type=Path, required=True, help="Path to alias mapping JSON.")
    parser.add_argument("--terms", nargs="*", default=[], help="Terms to resolve.")
    parser.add_argument("--terms-file", type=Path, help="Optional text/JSON file with terms.")
    parser.add_argument("--output", type=Path, help="Optional output JSON path.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    index = load_json(args.index.resolve())
    alias_map = load_alias_map(args.aliases.resolve())
    terms = parse_term_inputs(args.terms, args.terms_file.resolve() if args.terms_file else None)
    resolutions = [resolve_term(term, index, alias_map) for term in terms]
    payload = {
        "schema_version": 1,
        "index_path": str(args.index.resolve()),
        "aliases_path": str(args.aliases.resolve()),
        "resolutions": resolutions,
    }
    if args.output:
        write_json(args.output.resolve(), payload)
    else:
        json.dump(payload, sys.stdout, indent=2, sort_keys=True)
        sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
