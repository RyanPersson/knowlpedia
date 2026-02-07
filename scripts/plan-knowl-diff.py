#!/usr/bin/env python3
"""Plan deterministic missing knowls manifest from requested terms and corpus index."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict, deque
from pathlib import Path
from typing import Dict, List, Sequence, Set

from knowl_diff_lib import (
    load_alias_map,
    load_json,
    normalize_term,
    sort_unique,
    term_variants,
    write_json,
)


def parse_terms(raw_terms: Sequence[str], terms_file: Path | None) -> List[str]:
    terms = [t.strip() for t in raw_terms if t.strip()]
    if not terms_file:
        return terms
    text = terms_file.read_text(encoding="utf-8").strip()
    if not text:
        return terms
    if terms_file.suffix.lower() == ".json":
        payload = json.loads(text)
        if isinstance(payload, list):
            terms.extend(str(item).strip() for item in payload if str(item).strip())
        elif isinstance(payload, dict):
            candidates = payload.get("requested") or payload.get("terms") or payload.get("definitions") or []
            if not isinstance(candidates, list):
                raise ValueError("JSON input object must include a list under requested/terms/definitions.")
            terms.extend(str(item).strip() for item in candidates if str(item).strip())
        else:
            raise ValueError("JSON input must be an array or object.")
    else:
        terms.extend(line.strip() for line in text.splitlines() if line.strip())
    return terms


def resolve_term(term: str, index: Dict[str, object], alias_map: Dict[str, str]) -> Dict[str, object]:
    term_map = index.get("term_map", {})
    slug_to_entries = index.get("slug_to_entries", {})
    variants = term_variants(term)

    for variant in variants:
        alias_slug = alias_map.get(variant)
        if alias_slug:
            if alias_slug in slug_to_entries:
                return {
                    "term": term,
                    "status": "already_present",
                    "canonical_slug": alias_slug,
                    "match_type": "alias_map",
                }
            return {
                "term": term,
                "status": "missing_primary",
                "canonical_slug": alias_slug,
                "match_type": "alias_map_missing_target",
            }

    matches = []
    for variant in variants:
        matches.extend(term_map.get(variant, []))
    unique_matches = sorted(set(matches))
    if len(unique_matches) == 1:
        return {
            "term": term,
            "status": "already_present",
            "canonical_slug": unique_matches[0],
            "match_type": "index_term_map",
        }
    if len(unique_matches) > 1:
        return {"term": term, "status": "ambiguous", "candidate_slugs": unique_matches}
    proposed = normalize_term(term, singularize=True) or normalize_term(term, singularize=False)
    return {"term": term, "status": "missing_primary", "canonical_slug": proposed, "match_type": "normalized_fallback"}


def load_prereq_graph(path: Path) -> Dict[str, object]:
    if not path.exists():
        return {"schema_version": 1, "knowl_prerequisites": {}, "section_default_prerequisites": {}}
    payload = load_json(path)
    payload.setdefault("knowl_prerequisites", {})
    payload.setdefault("section_default_prerequisites", {})
    return payload


def resolve_prereq_slug(
    prereq_term: str,
    index: Dict[str, object],
    alias_map: Dict[str, str],
) -> Dict[str, object]:
    slug_to_entries = index.get("slug_to_entries", {})
    candidate = normalize_term(prereq_term, singularize=False)
    if candidate in slug_to_entries:
        return {"status": "resolved", "slug": candidate}

    variants = term_variants(prereq_term)
    for variant in variants:
        alias_slug = alias_map.get(variant)
        if alias_slug:
            return {"status": "resolved", "slug": alias_slug}
    matches = []
    for variant in variants:
        matches.extend(index.get("term_map", {}).get(variant, []))
    unique = sorted(set(matches))
    if len(unique) == 1:
        return {"status": "resolved", "slug": unique[0]}
    if len(unique) > 1:
        return {"status": "ambiguous", "candidate_slugs": unique}
    fallback = normalize_term(prereq_term, singularize=True) or candidate
    return {"status": "unresolved", "proposed_slug": fallback}


def parse_generated_slugs(path: Path | None) -> List[str]:
    if not path:
        return []
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        return []
    if path.suffix.lower() == ".json":
        payload = json.loads(text)
        if isinstance(payload, list):
            items = payload
        elif isinstance(payload, dict):
            items = payload.get("generated") or payload.get("slugs") or []
        else:
            raise ValueError("Generated slug JSON must be an array or object with generated/slugs.")
        return [normalize_term(str(item), singularize=False) for item in items if normalize_term(str(item), singularize=False)]
    return [normalize_term(line, singularize=False) for line in text.splitlines() if normalize_term(line, singularize=False)]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index", type=Path, required=True, help="Path to knowl index JSON.")
    parser.add_argument("--aliases", type=Path, required=True, help="Path to alias map JSON.")
    parser.add_argument("--prereq-graph", type=Path, required=True, help="Path to prerequisite graph JSON.")
    parser.add_argument("--terms", nargs="*", default=[], help="Requested concepts.")
    parser.add_argument("--terms-file", type=Path, help="Optional text/JSON source of requested concepts.")
    parser.add_argument("--output", type=Path, default=Path("missing_manifest.json"), help="Output manifest path.")
    parser.add_argument("--summary-output", type=Path, help="Optional summary report JSON path.")
    parser.add_argument("--max-ambiguous", type=int, default=0, help="Max ambiguous matches before gate fails.")
    parser.add_argument("--allow-ambiguous", action="store_true", help="Proceed even if ambiguous gate fails.")
    parser.add_argument("--generated-slugs-file", type=Path, help="Optional generated slug list for post-check.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    index = load_json(args.index.resolve())
    alias_map = load_alias_map(args.aliases.resolve())
    graph = load_prereq_graph(args.prereq_graph.resolve())

    requested_terms = parse_terms(args.terms, args.terms_file.resolve() if args.terms_file else None)
    slug_to_entries = index.get("slug_to_entries", {})
    slug_primary_terms: Dict[str, List[str]] = defaultdict(list)

    requested_records = []
    already_present_slugs: Set[str] = set()
    missing_primary_slugs: Set[str] = set()
    ambiguous_matches = []
    unresolved_terms = []

    for term in requested_terms:
        result = resolve_term(term, index, alias_map)
        record = {"term": term, **result}
        requested_records.append(record)
        status = result["status"]
        if status == "already_present":
            slug = result["canonical_slug"]
            already_present_slugs.add(slug)
            slug_primary_terms[slug].append(term)
        elif status == "missing_primary":
            slug = result["canonical_slug"]
            missing_primary_slugs.add(slug)
            slug_primary_terms[slug].append(term)
        elif status == "ambiguous":
            ambiguous_matches.append({"term": term, "candidate_slugs": result["candidate_slugs"], "context": "requested"})
        else:
            unresolved_terms.append({"term": term, "context": "requested"})

    missing_prereq_reasons: Dict[str, Set[str]] = defaultdict(set)
    prereq_edges = graph.get("knowl_prerequisites", {})
    section_defaults = graph.get("section_default_prerequisites", {})
    queue = deque(sorted(missing_primary_slugs))
    visited_for_prereqs: Set[str] = set()

    while queue:
        slug = queue.popleft()
        if slug in visited_for_prereqs:
            continue
        visited_for_prereqs.add(slug)

        prerequisites = list(prereq_edges.get(slug, []))
        entries = slug_to_entries.get(slug, [])
        if entries:
            section = entries[0]["section"]
            prerequisites.extend(section_defaults.get(section, []))

        for prereq_term in sort_unique(prerequisites):
            resolved = resolve_prereq_slug(prereq_term, index, alias_map)
            if resolved["status"] == "resolved":
                prereq_slug = resolved["slug"]
                if prereq_slug in slug_to_entries:
                    already_present_slugs.add(prereq_slug)
                    continue
                if prereq_slug in missing_primary_slugs:
                    continue
                missing_prereq_reasons[prereq_slug].add(slug)
                queue.append(prereq_slug)
            elif resolved["status"] == "ambiguous":
                ambiguous_matches.append(
                    {
                        "term": prereq_term,
                        "candidate_slugs": resolved["candidate_slugs"],
                        "context": f"prerequisite_of:{slug}",
                    }
                )
            else:
                unresolved_terms.append(
                    {
                        "term": prereq_term,
                        "proposed_slug": resolved["proposed_slug"],
                        "context": f"prerequisite_of:{slug}",
                    }
                )

    already_present = []
    for slug in sorted(already_present_slugs):
        entries = slug_to_entries.get(slug, [])
        already_present.append(
            {
                "slug": slug,
                "paths": [entry["path"] for entry in entries],
                "sections": sort_unique([entry["section"] for entry in entries]),
                "requested_by_terms": sort_unique(slug_primary_terms.get(slug, [])),
            }
        )

    missing_primary = []
    for slug in sorted(missing_primary_slugs):
        missing_primary.append({"slug": slug, "requested_by_terms": sort_unique(slug_primary_terms.get(slug, []))})

    missing_prerequisites = []
    for slug in sorted(missing_prereq_reasons):
        missing_prerequisites.append({"slug": slug, "required_by": sorted(missing_prereq_reasons[slug])})

    ambiguous_matches = sorted(
        (
            {
                "term": item["term"],
                "candidate_slugs": sorted(set(item["candidate_slugs"])),
                "context": item["context"],
            }
            for item in ambiguous_matches
        ),
        key=lambda item: (item["term"], item["context"], ",".join(item["candidate_slugs"])),
    )
    unresolved_terms = sorted(
        (
            {
                "term": item["term"],
                "proposed_slug": item.get("proposed_slug", normalize_term(item["term"], singularize=True)),
                "context": item["context"],
            }
            for item in unresolved_terms
        ),
        key=lambda item: (item["term"], item["context"], item["proposed_slug"]),
    )

    generated_slugs = parse_generated_slugs(args.generated_slugs_file.resolve() if args.generated_slugs_file else None)
    generated_duplicates_in_batch = sorted(slug for slug in set(generated_slugs) if generated_slugs.count(slug) > 1)
    generated_slug_collisions_with_corpus = sorted(slug for slug in set(generated_slugs) if slug in slug_to_entries)

    ambiguous_gate_passed = len(ambiguous_matches) <= args.max_ambiguous
    post_generation_gate_passed = not generated_duplicates_in_batch and not generated_slug_collisions_with_corpus

    manifest = {
        "schema_version": 1,
        "requested": requested_records,
        "already_present": already_present,
        "missing_primary": missing_primary,
        "missing_prerequisites": missing_prerequisites,
        "ambiguous_matches": ambiguous_matches,
        "unresolved_terms": unresolved_terms,
        "validation": {
            "max_ambiguous": args.max_ambiguous,
            "ambiguous_count": len(ambiguous_matches),
            "ambiguous_gate_passed": ambiguous_gate_passed,
            "generated_slugs_checked": generated_slugs,
            "generated_duplicates_in_batch": generated_duplicates_in_batch,
            "generated_slug_collisions_with_corpus": generated_slug_collisions_with_corpus,
            "post_generation_gate_passed": post_generation_gate_passed,
        },
    }
    write_json(args.output.resolve(), manifest)

    summary = {
        "requested_count": len(requested_terms),
        "already_present_count": len(already_present),
        "missing_primary_count": len(missing_primary),
        "missing_prerequisites_count": len(missing_prerequisites),
        "ambiguous_count": len(ambiguous_matches),
        "unresolved_count": len(unresolved_terms),
        "ambiguous_gate_passed": ambiguous_gate_passed,
        "post_generation_gate_passed": post_generation_gate_passed,
    }
    if args.summary_output:
        write_json(args.summary_output.resolve(), summary)

    print(f"Wrote manifest: {args.output.resolve()}")
    print(
        "Summary: "
        f"present={summary['already_present_count']} "
        f"missing_primary={summary['missing_primary_count']} "
        f"missing_prereq={summary['missing_prerequisites_count']} "
        f"ambiguous={summary['ambiguous_count']} "
        f"unresolved={summary['unresolved_count']}"
    )

    if not ambiguous_gate_passed and not args.allow_ambiguous:
        print(
            f"Ambiguous match gate failed: {len(ambiguous_matches)} > max_ambiguous={args.max_ambiguous}. "
            "Re-run with --allow-ambiguous or increase threshold."
        )
        return 3
    if not post_generation_gate_passed:
        print("Post-generation collision gate failed; review generated slug collisions.")
        return 4
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
