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
and edges, and reports cycles. Cycles composed entirely of reviewed metadata are
errors; cycles involving unreviewed heuristic edges are warnings for later
semantic review.

## Responsive interaction model

Desktop starts with a left-to-right flow from prerequisites through the current
knowl to dependent concepts. An orientation control switches to a vertical
view with dependents above the current concept and prerequisites below it. The
selected knowl remains open in a side pane, and knowl links within that pane
refocus the graph rather than navigating away.

Mobile starts in that vertical view, with dependents above and prerequisites
below. Selecting a node opens the definition in a bottom sheet, preserving the
full screen for the graph when the sheet is closed. The initial mobile radius
is one step; deeper exploration proceeds naturally by refocusing. The same
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
