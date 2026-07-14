# Knowl Diff Contract (MVP)

This document defines the deterministic, filesystem-backed contract for missing-knowl planning across:

- explicit knowl list generation
- subject+level planning
- paper-driven extraction

## Inputs

1. `data/knowl-index.json` built from corpus filesystem.
2. `data/knowl-aliases.json` for explicit synonym/canonical mappings.
3. `data/knowl-prereq-graph.json` for prerequisite expansion.
4. Requested term list (`.txt` or `.json`).

## Index Build

Command:

```bash
python3 scripts/build-knowl-index.py \
  --content-root content \
  --output data/knowl-index.json
```

Behavior:

- Scans `*.md` knowls under section directories.
- Extracts `slug`, `title`, `section`, `path`, and `aliases/synonyms` if present.
- Fails on duplicate slug collisions unless `--allow-duplicate-slugs` is set.
- Uses a fingerprint cache (`scan_fingerprint`) to skip unchanged rebuilds.

## Term Resolution

Command:

```bash
python3 scripts/resolve-knowl-terms.py \
  --index data/knowl-index.json \
  --aliases data/knowl-aliases.json \
  --terms-file tmp/requested.txt
```

Normalization rules are deterministic:

- lowercase
- remove apostrophes/backticks
- replace punctuation/whitespace with `-`
- collapse repeated `-`
- apply simple singularization for matching variants

Resolution order:

1. alias map
2. corpus term map (slug/title/frontmatter aliases)
3. unresolved fallback to normalized slug proposal

Ambiguous matches are surfaced explicitly and never auto-selected.

## Planner / Manifest

Command:

```bash
python3 scripts/plan-knowl-diff.py \
  --index data/knowl-index.json \
  --aliases data/knowl-aliases.json \
  --prereq-graph data/knowl-prereq-graph.json \
  --terms-file tmp/requested.json \
  --output tmp/missing_manifest.json \
  --summary-output tmp/missing_manifest.summary.json \
  --max-ambiguous 0
```

Required manifest shape (`missing_manifest.json`):

```json
{
  "schema_version": 1,
  "requested": [],
  "already_present": [],
  "missing_primary": [],
  "missing_prerequisites": [],
  "ambiguous_matches": [],
  "unresolved_terms": [],
  "validation": {}
}
```

Field meaning:

- `requested`: each input term and per-term resolution status.
- `already_present`: canonical slugs already in corpus index.
- `missing_primary`: requested concepts absent from corpus.
- `missing_prerequisites`: prerequisite slugs absent from corpus and required by missing primary/prereq nodes.
- `ambiguous_matches`: terms with >1 canonical candidate; must be reviewed.
- `unresolved_terms`: terms not matched by alias or corpus term map.
- `validation`: gate outcomes and collision checks.

## Validation Gates

Pre-generation gate:

- Planner exits non-zero if `ambiguous_matches` count exceeds `--max-ambiguous` unless `--allow-ambiguous` is set.

Post-generation gate:

- Optionally pass `--generated-slugs-file`.
- Planner validates no duplicate generated slug in batch.
- Planner validates no generated slug already exists in corpus index.
- Non-zero exit on collision failures.

## Determinism Requirements

Given identical inputs and identical corpus state:

- identical index payload (except file system mtime-dependent fingerprint only when corpus changed)
- identical manifest categories and ordering
- no model-memory dependency (filesystem + JSON inputs only)

Generation batches must consume `missing_manifest.json` as the single source of truth.
