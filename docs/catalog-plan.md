# Category-aware object catalogue: initial batch

Both repositories use branch `catalog`, starting at application commit
`f6cbd9c45cc86faf369c61220a2cc4f729377140` and content commit
`d1ad541e` (the merged fiber-bundle repair). The batch adds object records,
atomic knowls, category conventions, selected relationships and Hom/End/Aut
examples, a navigable index, and validated indexed exports. It does not claim
to classify all morphisms or provide Lean proofs yet.

## Identity and authoring contract

Canonical data live in `knowlpedia-content/content/catalog/data/*.json`.
Each shard has `schema_version: 1` and arrays `objects`, `categories`, `views`,
`relationships`, `morphism_spaces` (unused arrays may be empty). Unique IDs
are global within each array type. Existing knowls should be reused when
they already own the exact object; generic family knowls do not substitute
for separate scalar-field and low-dimensional entries.

Object records have these fields:

```json
{
  "id": "lg-sl-2-c",
  "name": "SL(2,C)",
  "notation": "\\mathrm{SL}(2,\\mathbb C)",
  "kind": "lie-group",
  "family": "special-linear-group",
  "parameters": {"n": 2, "field": "C"},
  "knowl": "lie-groups/sl2-complex-as-real-and-complex-lie-group",
  "dimensions": {"real": 6, "complex": 3},
  "category_ids": ["real-lie-groups", "complex-lie-groups"],
  "constraints": [],
  "properties": {"connected": true},
  "status": "defined",
  "references": []
}
```

`dimensions` values can be nonnegative integers or formula strings.
`parameters`, `constraints`, `properties`, and `references` are explicit
metadata, never executable expressions. Symbolic families have
`status: "family"` and state parameter domains in `constraints`. A construction
outside a category's axioms can be an object with an appropriate broader
category, but must never be falsely assigned category membership.

The fields `id`, `name`, `notation`, `kind`, `family`, `parameters`, `knowl`,
`dimensions`, `category_ids`, `constraints`, `properties`, `status`, and
`references` are required on object records. References are objects containing
`url`, `title`, and `locator`, or an empty list for direct elementary reasoning.
Authors may add `description` and `related_ids`.

Views are explicit triples `{id, object_id, category_id}` with optional
`scalar`, `description`, `parameters`, and `constraints`. A default view ID is
`OBJECT_ID@CATEGORY_ID`. Objects list valid category memberships; the exporter
materializes these default views and indexes them. Multiple noncanonical
structures on one carrier require separately named views. Real and complex
objects keep distinct IDs even when scalar restriction connects them.

Categories have `{id, name, knowl, scalar, object_axioms, morphism_axioms,
unit_policy, regularity}`. Axioms are arrays of strings; other fields are
strings, and `scalar` may be null. Agreed category IDs include:

- `sets`, `groups`, `abelian-groups`, `rings`, `unital-rings`, `fields`;
- `topological-groups`, `topological-rings`, `topological-fields`;
- `real-lie-groups`, `complex-lie-groups`;
- `real-lie-algebras`, `complex-lie-algebras`;
- `real-vector-spaces`, `complex-vector-spaces`, `rational-vector-spaces`;
- `real-associative-algebras`, `complex-associative-algebras`,
  `rational-associative-algebras` (not necessarily unit-preserving maps);
- `real-unital-associative-algebras`, `complex-unital-associative-algebras`,
  `rational-unital-associative-algebras` (unit-preserving maps);
- `real-nonassociative-algebras`, `complex-nonassociative-algebras`;
- `jord-r`, `ujord-r`, `jord1-r`, and their `-c` counterparts.

Jord means Jordan algebras with arbitrary product-preserving linear maps.
UJord has unital objects but does not require maps to preserve units.
Jord1 requires both unital objects and unit-preserving maps. These labels
are explicit local conventions approved by the user. S means real sedenions.

Relationships have `{id, source, target, kind, category_id, statement, knowl,
conditions, evidence}`. `source` and `target` are object IDs, `category_id` is
a category ID or null for a construction rather than a morphism, and
`conditions` is an array of strings. `kind` may be `isomorphism`, `embedding`,
`quotient`, `covering`, `scalar-restriction`, `complexification`, `lie-algebra`,
`derivation-algebra`, `automorphism-group`, `construction`, or `representation`.
No inverse arrows or compositions are inferred without the appropriate
categorical justification. Evidence is `{status, method, references, lean}`;
status is `definition`, `proved-in-text`, `literature`, or `conjectural`,
references use the object-reference format, and `lean` is null until verified.

Morphism-space records have `{id, source_view, target_view, operation,
description, knowl, conditions, evidence}`. `operation` is `hom`, `end`, or
`aut`; source and target must be in the same category, and `end`/`aut` must
have identical view endpoints. A missing record means **not catalogued**,
never that the Hom-set is empty. No quadratic expansion of object pairs.

## Ownership and reserved ID patterns

- Lie groups: `lg-{gl,sl,o,so,pgl,psl,spin}-{1,2,3,n}-{r,c}`;
  `lg-{u,su,sp}-{1,2,3,n}` for compact groups. Further families reserve
  their IDs in their lane manifest before writing.
- Lie algebras: analogous `la-...` patterns. Compact symplectic `la-sp-k`
  means quaternionic size k; split real/complex symplectic names use
  `la-sp-2k-{r,c}` with explicit parameters to avoid size ambiguity.
- Exceptional groups/algebras: `lg-TYPE-{compact,split,complex}` and
  `la-TYPE-{compact,split,complex}`, TYPE in g2,f4,e6,e7,e8.
- Scalar and Jordan lane: `scalar-{r,c,h,o,s,split-c,split-h,split-o}`;
  matrix IDs `assoc-m-K-FIELD`, Hermitian IDs `j-herm-K-FIELD`, with
  K in 1,2,3,n. This lane owns real/complex scalars as objects.
- Arithmetic lane: `field-...`, `ring-...`, `group-ideles-...`; includes
  quaternion orders and rational quaternion algebras, and symbolic K/F.
- Magic-square lane: owns its composite output objects, construction and
  triality relationships, and the table. It reuses all existing input IDs.
- Root agent: category definitions, selected morphism-space examples,
  navigation indices, integration and final validation.
- Infrastructure agent: Python model/validator/exporter, compiler integration,
  JSON and SQLite indexes, query API, meaningful tests, and model docs.

Each mathematical lane must produce a reservation/reuse manifest and a
targeted review shard under `reviews/catalog/`; the root agent merges their
evidence into the existing refactor ledger. Each lane should browse substantive
sources, check its own definitions and mathematical edge cases, and report
unresolved facts instead of inventing classifications.

## Delivered batch

The content branch contains two separate commits:

- `5dc5548f`: transcript prerequisites — 43 new definitions plus the reading
  index, and seven expanded/corrected existing owners. Fraction fields and
  integral domains reuse their established knowls.
- `8ce039be`: catalogue — 521 new knowls/navigation pages, 514 objects,
  40 categories, 2,740 structure views, 622 relationships, 153 Hom/End/Aut
  records, and all 16 cells of the compact real Freudenthal magic square.

The catalogue includes the requested distinct real/complex entries, small
sizes and constrained symbolic families, split composition algebras, sedenions,
Heisenberg examples, local/global arithmetic objects and low-dimensional
identifications. Its selected morphism classifications carry explicit
conditions and complete/partial coverage. Missing records mean not catalogued;
no exhaustive classification or Lean proof is claimed.

Regenerate the seven catalogue navigation pages from the authored shards with
`python3 scripts/generate_catalog_indexes.py`. Its default baseline is the
pre-batch content commit `d1ad541e`. New object-bearing shard names must be
assigned navigation labels explicitly. The compiler validates references,
category membership, views, evidence shape and the construction table before
exporting indexed JSON and SQLite. `docs/catalog-model.md` documents the schema,
queries and measured performance.

The transcript source inventory and review evidence are in
`reviews/catalog/transcript-*` in the content repository. The other lane
manifests, source hashes, interlink decisions and independent adversarial review
are under `reviews/catalog/`; accepted reviews are also integrated into
`reviews/refactor-ledger.json` without changing its fixed baseline.

## Integration validation

- Catalogue validation passes with the counts above; the complete prerequisite
  graph is acyclic and all new links resolve.
- All 572 new/modified knowls preserve their source content under section
  splitting. The corpus-wide section audit still reports the unchanged
  `fiber-bundles/construction-splitting-of-atiyah-sequence-from-a-principal-connection`
  page; its source is byte-for-byte identical to the starting revision.
- The external-reference-placement audit passes. New-page scope findings were
  reviewed; specific link labels were clarified, and the quaternionic trace
  qualification and Z-order specialization were retained with explanations.
- `make build EXTRA_CONTENT_SOURCES=` compiles 4,739 development knowls;
  `make check-rendering` finds no rendered HTML errors.
- `make build-production OUTPUT_DIR=tmp/catalog-arithmetic-render` composes only
  the primary content package and compiles 4,727 knowls with prebuilt-only
  diagrams. Full rendering, diagram and production-profile checks pass.
- Browser checks reach all 153 recorded map descriptions by their exact views,
  distinguish unknown from empty/zero results, and exercise result-object
  links. Eighteen representative pages at 390px and 1440px pass math, missing
  resource, overflow, and inline-knowl checks, including the repaired adèle and
  idèle restricted-product displays.
- The existing `knowlpedia-astra-benchmark` service on port 8015 serves the final
  output at `https://optiplex.taildb538a.ts.net:8443/`. Catalogue pages, transcript
  index and exported JSON were verified over HTTPS against the local files.

The final application suite passes **212 tests**, including catalogue validation,
indexed queries, compiler integration, filtered added/deleted review selection,
and retrieval of evidence from the exact compared Git revision.

Generated reviews are served at `/review/catalog/` (521 additions) and
`/review/transcript-orders/` (44 additions and seven revisions). Every one of
their 572 comparisons has at least one recorded review matching the displayed
source hash. These are scoped author/adversarial reviews, not formal proofs.
The transcript review uses a path manifest against the final content revision,
so its links to catalogue objects resolve while its file list stays separate.
The review generator now imports the canonical refactor ledger, preserves
batch/entry provenance, displays structured source checks, and applies path
filters to added and deleted files as well as revisions.
