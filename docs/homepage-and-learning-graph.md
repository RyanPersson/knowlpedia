# Homepage and learning-graph direction

## Product goal

Knowlpedia should make it easy to enter mathematics through one concept and
then retain context while moving through its dependencies. The homepage is an
orientation layer, not the exhaustive corpus index.

The initial information architecture is:

- `/` — search-first introduction, featured subject gateways, and an honest
  preview of the dependency-graph direction;
- `/library/` — the complete expandable index of production knowls;
- individual knowl pages — compact definitions with deeper sections disclosed
  on demand;
- `/indexes/dependencies.json` — authored prerequisite graph for future graph
  mode and learning-path generation;
- `/indexes/links.json` — all structural and incidental links, including
  mentions, proof uses, relations, and prerequisite metadata.

## Why dependencies are explicit metadata

A textual link is not automatically a prerequisite. It may be an example, a
comparison, a consequence, a citation, or a related concept. Inferring a
learning order from every wikilink would create noisy and frequently backward
edges.

A knowl may therefore declare a conservative list in its TOML front matter:

```toml
prerequisites = [
  "linear-algebra/vector-space",
  "linear-algebra/norm",
]
```

These edges are authored claims that the target concepts should normally be
understood before the current knowl. The compiler:

1. validates that every target exists;
2. rejects cycles in the authored prerequisite graph;
3. exposes the list on each registry item;
4. adds typed prerequisite records to the general link index; and
5. emits `/indexes/dependencies.json`, whose edges point from prerequisite to
   dependent concept, matching a learner's forward direction.

The metadata should remain sparse and trustworthy. Absence of an edge means
"not yet classified," not "no prerequisite relationship exists."

## Responsive interaction model

Desktop has enough room to establish orientation and show spatial structure:

- a prominent search action and concise explanation above the fold;
- a multi-column subject gateway;
- a visible dependency-graph preview;
- generous separation between orientation, exploration, and explanatory
  content.

Mobile prioritizes reachability and linear reading:

- the hero, explanation, and calls to action stack in reading order;
- subject cards become a single-column list on narrow screens;
- graph nodes become a compact two-column progression rather than relying on
  a tiny free-form canvas;
- search, theme, and library navigation remain available in the sticky header;
- interactive targets remain at least 44 CSS pixels high where practical.

## Learning-path roadmap

The dependency index is infrastructure, not yet a claim that the corpus has a
complete learning order. A useful graph mode should be built in stages:

1. Expand prerequisite metadata in reviewed subject-sized batches.
2. Add edge provenance and strength when the simple prerequisite relation is
   no longer expressive enough (for example required, recommended, or one-of).
3. Audit cycles, disconnected concepts, unusually broad nodes, and concepts
   whose prerequisites are much more advanced than the concept itself.
4. Build a graph view that can focus on a local neighborhood rather than
   attempting to display thousands of nodes at once.
5. On desktop, pair the graph with a knowl viewer and highlight the currently
   open knowl. On mobile, alternate between a focused graph neighborhood and a
   full-width knowl sheet instead of squeezing both panes side by side.
6. Generate candidate learning paths by topological order and prerequisite
   closure, then have subject-matter review determine pedagogical ordering,
   optional branches, and appropriate entry assumptions.

Algorithmic ordering can enforce dependency constraints, but it should not be
treated as a substitute for pedagogy. Motivation, examples, pacing, and the
choice between equivalent routes remain editorial decisions.

