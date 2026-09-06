# Homepage and dependency-graph direction

## Product goal

Knowlpedia should make it easy to enter mathematics through one concept, read
its compact definition, and retain context while moving through prerequisites
and dependent concepts. The homepage is an entry surface, not the exhaustive
corpus index.

The current information architecture is:

- `/` — a restrained search-first entry with direct routes to graph and the
  index, followed by a compact subject directory;
- `/index/` — the complete expandable subject index of reader-facing knowls;
- `/graph/` — a focused dependency neighborhood paired with the selected knowl;
- individual knowl pages — compact definitions with deeper sections disclosed
  on demand;
- `/indexes/dependencies.json` — prerequisite graph data with provenance and
  review state;
- `/indexes/links.json` — all structural and incidental links, including
  mentions, proof uses, relations, and prerequisite metadata.

## What the Math Academy model contributes

Math Academy distinguishes a fine-grained topic graph from a compressed course
graph. The topic graph is the instructional source of truth: directed edges
record prerequisites, while a course graph is a human-facing summary. Its graph
is refined by domain experts, with software assisting rather than replacing
pedagogical judgment.

Knowlpedia adopts the structural lessons without attempting to render the whole
corpus at once:

- concepts, not courses or documents, are the graph nodes;
- edges point from prerequisite to dependent concept;
- the interface renders a bounded neighborhood around a selected node;
- selecting any node redraws the neighborhood and opens its knowl;
- omitted-neighbor counts make truncation explicit;
- unreviewed heuristic edges are visibly different from reviewed edges.

The free *Math Academy Way* PDF used for this design review is saved locally at
`docs/archive/the-math-academy-way.pdf`. The archive directory is gitignored;
the canonical public copy remains at
<https://www.justinmath.com/files/the-math-academy-way.pdf>.

## Dependency metadata

A textual link is not automatically a prerequisite. It may be an example, a
comparison, a consequence, or a merely related concept. Prerequisites are
therefore stored explicitly in TOML front matter:

```toml
prerequisites = [
  "linear-algebra/vector-space",
  "linear-algebra/norm",
]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
```

`dependency_review_count` is a nonnegative integer, not a boolean. Zero means
the list has not received a semantic dependency review. A reviewer increments
the count after checking the entire list in mathematical context, including
removing consequences and examples and adding prerequisites that were named
only through notation or prose.

The initial heuristic treats knowl links in the compact definition core as
candidate prerequisites. It deliberately ignores later expandable sections,
code, mathematics, self-links, and missing targets. The generator is
report-only by default, supports deterministic random samples and path
manifests, and never overwrites metadata whose review count is positive.
Heuristic-owned metadata is refreshed when the core changes; separately
authored prerequisites are retained.

Run a sample before a corpus-wide application:

```bash
.venv/bin/python scripts/generate_dependency_metadata.py \
  --content-root ../knowlpedia-content/content \
  --sample-size 40 \
  --seed 20260827 \
  --report tmp/dependency-sample.jsonl
```

After inspecting the sample, apply the selected scope:

```bash
.venv/bin/python scripts/generate_dependency_metadata.py \
  --content-root ../knowlpedia-content/content \
  --report tmp/dependency-full.jsonl \
  --apply
```

The compiler validates targets and review counters, exports provenance on nodes
and edges, and reports cycles. Every prerequisite cycle is an error, regardless of review count. Iterative
strongly connected component checks identify cycles without a recursion limit.
A cyclic dependency index is never exported, even with
`--allow-validation-errors`. Ordinary prose links may still form cycles.

## Responsive interaction model

Desktop starts with a left-to-right flow from prerequisites through the current
knowl to dependent concepts. An orientation control switches to a vertical
view with dependents above the current concept and prerequisites below it. The
selected knowl remains open in a side pane, and knowl links within that pane
refocus the graph rather than navigating away.

Mobile starts in that vertical view, with dependents above and prerequisites
below. Selecting a node opens the definition in a bottom sheet, preserving the
full screen for the graph when the sheet is closed. The initial radius is one
step on both desktop and mobile; mobile shows fewer neighbors to preserve
readable labels. Deeper exploration proceeds naturally by refocusing. The same
orientation control remains available when a horizontal view is useful.

Both layouts support search, pan, zoom, fit, URL-addressable focus, and visible
review state. High-degree concepts are capped per distance and direction so one
large adjacency list cannot collapse the entire visualization.

## Learning-path roadmap

The dependency index is infrastructure, not a claim that the corpus already has
an optimal learning order. A dependable learning-path system should proceed in
stages:

1. Review heuristic metadata in coherent subject-sized batches.
2. Audit cycles, disconnected nodes, unexpectedly broad prerequisites, and
   edges that point from an advanced consequence back to an elementary concept.
3. Add relation strength and alternatives when the binary prerequisite relation
   is insufficient, such as required, recommended, or one-of.
4. Compute prerequisite closure and candidate topological orderings.
5. Have subject-matter reviewers choose entry assumptions, optional branches,
   motivation, examples, and pacing.
6. Publish learning paths or lecture-note sequences only after those semantic
   and pedagogical reviews.

Algorithmic ordering can enforce dependency constraints, but it is not a
substitute for pedagogy.


## Graph views and validation

The View control offers a focused neighborhood, subject clusters (the canonical
ID namespace), and connected components (weak connectivity of prerequisite
edges). Cluster cards show exact corpus counts and open a bounded neighborhood
within the chosen group. They do not collapse subjects into directed supernodes:
such aggregation can introduce apparent cycles even when the concept graph is a
DAG. Hidden neighbors include links crossing the chosen cluster boundary.

All visible edges use the same prerequisite-to-dependent index. Display ranks
come from a topological longest-path pass over the visible subgraph, rather than
shortest distance from the selection. Shortcut edges therefore cannot turn
backward or share a rank with their target. Links that would cross a card route
around the map. Both orientations preserve arrow direction.

Focus, view, cluster, depth, and orientation are URL-addressable and survive
reload and browser navigation. Search supports keyboard selection; graph zoom
has touch-accessible buttons. Definitions load with a request counter so a slow
previous response cannot replace the current selection. Closed viewers are
inert to keyboard navigation.

Cycle repairs use `dependency_heuristic = "semantic-cycle-repair-v1"`. The
metadata generator preserves those lists unchanged, including on `--apply`.
This marker records targeted cycle repair, not a complete pedagogical review;
the original `dependency_review_count` remains unchanged.

Run a source audit before building either profile:

```bash
python3 scripts/audit_dependency_graph.py --profile development --report tmp/dag-development.json
python3 scripts/audit_dependency_graph.py --profile production --report tmp/dag-production.json
```

Audits include counts, missing targets, duplicate IDs, invalid sources, cycle
witnesses, and a complete topological ordering. They exit nonzero for invalid
graphs. The paired content repository records edge-level repair rationales in
`dependency-graph-audit.json`.

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
npm run test:graph-model
PREVIEW_URL=http://127.0.0.1:8016 npm run test:graph-ui
PREVIEW_URL=http://127.0.0.1:8016 npm run test:graph-views
```

The extended browser checks cover both orientations, all depths, cluster
browsing, history, keyboard search, responsive layouts, and rejection of empty
or cyclic indices. Rendered screenshots are written to `tmp/graph-screenshots`.

## Foundational semantic review

The paired content package records successive batches in
`dependency-foundations-review.json`, `dependency-curriculum-review.json`, and
`dependency-full-review.json`,
with companion Markdown reports. Run
`python3 scripts/check_learning_paths.py --coverage --report tmp/learning-path-review.json`
to check all batches, detect advanced concepts reintroduced as prerequisites of
their foundations (including acyclic direction errors), and report remaining
unreviewed dependencies. Repeat `--review PATH` to check selected batches.

The checker distinguishes reviewed lists from concepts whose entire prerequisite
closure has been reviewed. Coverage includes subject counts and the next
unreviewed inputs ranked by their direct dependents. Learning paths can specify
`max_unreviewed_prerequisites` to protect completed prerequisite reviews from
regressions. Historical batches remain readable; the latest review counter is
checked when a concept has been reviewed in multiple batches.

Fully checked lists use positive review counts and semantic review provenance
(`semantic-foundations-review-v1`, `semantic-curriculum-review-v1`, or
`semantic-full-review-v1`). The metadata generator preserves all positive-review
lists. The completed corpus review covers 3,509 development entries, including
eight added foundations; all their prerequisite closures are reviewed. The
production profile contains 3,499 entries. Both graphs are acyclic.

The full review contract sets `require_full_review: true`. The checker rejects
new unreviewed entries and prerequisite lists that differ from their latest
recorded review. To revise a list, review the complete definition or theorem,
increment its review count, and add a superseding contract record. Review
counters describe prerequisite review, not independent verification of every
proof or optimal pedagogical sequencing.

For future parallel reviews, `scripts/audit_review_proposals.py --directory DIR`
checks proposals before source edits. The directory contains a source registry,
numbered assignment packets and matching proposals, plus optional
`new_knowls.json` for already-reviewed added foundations. Source hashes and
complete assignment coverage are checked before the combined proposed graph is
audited. Cross-batch suggestions remain advisory until integrated into an actual
review row. Archive the successful audit before applying changes; afterward the
source audits and durable review contracts are the appropriate checks.
