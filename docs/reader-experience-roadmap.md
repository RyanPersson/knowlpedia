# Knowlpedia reader-experience roadmap

Started 2026-09-05 on `astra-refactor` in both repositories.
Starting commits: compiler `9c1e005`, content `ea7256bd`.
The preceding uncommitted SQLite/export cleanup and dependency-generator
preservation fix are part of this branch and must be retained.

## Outcome

A reader should be able to open a mathematical concept, understand its precise
statement, follow two unfamiliar prerequisites, and return to the original
argument without losing their place. A useful example should make the statement
concrete. The graph should distinguish editorially reviewed prerequisites from
unreviewed suggestions. Content correctness takes precedence over polish.

Keep the static architecture, stable IDs, compact cores, optional sections, and
ordinary link navigation. Improve existing content before adding more material.
Do not equate fewer words with easier reading, link coverage with prerequisite
coverage, or successful rendering with mathematical correctness.

## Milestone 1 — Establish a trustworthy reading baseline

Status: complete (2026-09-05). This is the first implementation batch, not a claim that
the whole corpus has been reviewed.

### Mathematical exposition

Exact content scope:

- `complex-analysis/subharmonic-function`: qualify the distributional
  characterization by the almost-everywhere representative and give the
  point-spike counterexample; check the zero-function convention in examples.
- `operator-algebras/gns-construction`: add one worked example that identifies
  the quotient, representation, and cyclic vector using the stated convention.
- `algebra-category-theory/group-object`: state the defining equations instead
  of requiring the reader to reconstruct unspecified diagrams.

Acceptance: source-supported statements, explicit notation, unchanged IDs and
math delimiters, intact links, and visual inspection of the changed sections.
Examples must perform a calculation or explain a mechanism, not merely name
another advanced object. No wholesale rewrites or compulsory section template.

### Reading interface

- Place expanded definitions after the complete compact core, keeping prose,
  displayed equations, and their continuation together. In continuous documents
  and optional sections use the paragraph boundary. Preserve nested-panel
  boundaries, list structure, and the special subject-index layout.
- Reduce mobile title and header space and remove a repeated core label when
  the page kind already supplies the same label.
- Preserve normal navigation, focus restoration, deepest-first Escape closing,
  full-page fallbacks, and access to optional sections.

Acceptance: desktop and 390px mobile reading checks; an opening GNS paragraph
remains intact when a linked term expands; nested expansion stays in its owner;
no new horizontal page overflow; closing returns to the relevant trigger.
Check a narrow 320px viewport and a long mathematical title as well. Browser
tests must exercise actual runtime behavior, not only compare generated markup.

### First dependency review

Review the complete direct prerequisite lists for `algebra-rings/ring`,
`ring-axioms`, `unital-ring`, and `commutative-ring`. Remove the false requirements
that the ring definition first needs its specializations or a second statement
of its own axioms. Retain useful textual links. Record the review rationale here
and increment only the four lists actually reviewed.

Acceptance: ring is a prerequisite of its unital and commutative specializations,
not the reverse; no reviewed-only cycle; a report/apply rerun preserves reviewed
lists. Remaining heuristic cycles are reported, not removed mechanically.
This review does not standardize the corpus-wide meaning of “ring.”

## Milestone 2 — Review complete mathematical reading paths

Status: complete (2026-09-05). Bounded paths and remaining assumptions are recorded in [refactor-reading-paths.md](refactor-reading-paths.md).

Start with two bounded neighborhoods: vector space → inner product space →
Hilbert space → a GNS reading path, and the ring foundations reviewed above.
For each, record the exact file manifest before edits and read the prerequisite
definitions as part of reviewing their dependent concepts.

- Check scalar fields, inner-product linearity, completeness, quotient objects,
  and unital/nonunital conventions across linked pages.
- Restore verbal explanations where compressed formulas hide the role of axioms.
- Add a worked example or a distinguishing non-example where it resolves a
  specific difficulty; do not require one in every short entry.
- Review actual prerequisite lists, including indispensable unlinked concepts,
  and record editorial provenance and the scope of each review.
- Pilot clearer graph copy and a reviewed-edge view. A node's reviewed list
  must not imply that every neighboring node or incoming use has been reviewed.

Acceptance: two documented end-to-end reading exercises, checked mathematical
conventions, reviewed direct dependencies, and explicit remaining boundary
assumptions. The graph must not present an unreviewed neighborhood as a syllabus.
Do not add path-generation algorithms at this stage.

## Milestone 3 — Organize discovery around readers

Status: complete (2026-09-05). Subject and source browsing remain separate presentations of stable IDs.

- Separate mathematical subject browsing from source/paper collections in the
  homepage and index presentation, without moving content or changing URLs.
- Replace mechanically derived labels such as “Algebra topological” with
  editorial subject names. Inspect overlaps among Analysis, Real Analysis,
  Convex Analysis, and neighboring collections before regrouping.
- Test search using concept names, standard aliases, and ambiguous terms.
  Check both successful retrieval and explanations when several results differ
  by convention or scope.

Acceptance: a reader can find a named concept and browse toward an unfamiliar
one on mobile and desktop. Source collections remain accessible. Classification
changes do not silently remove knowls from discovery or rename stable IDs.

## Milestone 4 — Consolidate duplicates and bundled records

Status: complete (2026-09-05). Two proven duplicates have compatibility redirects; the integration bundle links four atomic results.

- Build a small semantic manifest from known candidates: composition of
  functions, orthonormal frame bundles, and elementary Riemann-integral results.
- Choose canonical owners by mathematical scope and existing incoming uses.
- Implement the smallest alias/redirect model that preserves old page URLs,
  inline fragment requests, section links, and search discovery. Specify how
  dependency exports canonicalize IDs; test redirect loops and missing targets.
- Then merge proven duplicates and split the independently reusable additivity
  and linearity results. Preserve useful explanations and source references.

Acceptance: each old entry point still resolves to the intended mathematics;
no broken incoming links; search and graph do not double-count the same concept.
Do not batch-delete files merely because titles or formulas look similar.

## Milestone 5 — Consolidate the workflow

Status: complete (2026-09-05). Updated the existing batch workflow and content editorial guidance.

Update the existing authoring workflow with the successful reading exercises,
convention checks, and source-review expectations. Remove conflicting guidance
and redundant tooling rather than introducing another checklist system.
Keep mechanical rendering checks distinct from editorial and mathematical review.

Acceptance: one coherent workflow; no automation claiming to certify mathematical
truth; a future batch can reuse concrete examples and checks from this refactor.

## Verification and delivery

Each milestone ends with an updated progress record, relevant unit/browser
checks, source validation, and production rendering checks. Retain existing
preview services; use temporary browser interception for isolated checks rather
than launch duplicate servers. Publish or merge only under the user's deployment
instructions. Keep unrelated corpus transformations separate and explain known
warnings rather than presenting a green build as semantic certification.

Regenerate the side-by-side content review after each content batch. Before
committing, run `scripts/generate_content_review.py` with
`--content-repo ../knowlpedia-content --output public-imported/review/content-changes`
and omit ref arguments to compare HEAD with the working tree. The existing
`knowlpedia-astra-benchmark` preview serves this checkout on port 8015; the older
`.preview-server/state.json` port 8012 refers to a different checkout.

## Progress record

- Baseline: 92 Python tests pass; 3,491 production knowls compile; rendered-output
  checker reports no errors. Validation reports 583 unreviewed cycle warnings
  and 12 duplicate-alias warnings. These are warning counts, not a count of
  independent cycles or a complete semantic-duplicate inventory.
- Added mathematical examples and qualifications to the three specified knowls.
  The group-object operations and axioms use short displayed rows suitable for
  mobile reading. No IDs or delimiter conventions were changed.
- Reduced mobile page-heading space and omitted repeated Definition/Example
  core headings when the page kind already supplies that label.
- The first paragraph-only expansion attempt still separated GNS prose from a
  display equation. The final approach uses the compiler's existing reading-mode
  decision to mark compact cores explicitly. Continuous documents retain nearby
  paragraph expansion; no paragraph-length or punctuation heuristic is used.
- Added `npm run test:reading-ui` (standalone runtime fixtures) and
  `KNOWLPEDIA_SITE_DIR=tmp/refactor-production npm run test:reader-pages`
  (built pages at 320px, 390px, and 1440px). The latter saves inspection images
  in `tmp/reader-pages-smoke/` and checks reviewed ring edges.

### Mathematical review evidence

The subharmonic representative issue was checked against the distributional
discussion in [Harvey–Lawson](https://www.math.stonybrook.edu/~blaine/The-G-Paper-ArXiv.pdf).
The point-spike counterexample can also be checked directly: it is zero almost
everywhere, while its value at the spike exceeds every surrounding spherical
average. The GNS example was checked by computing the null ideal and evaluation
representation, alongside the GNS construction in
[C*-algebra notes hosted at Dartmouth](https://math.dartmouth.edu/~dana/bookspapers/cstar.pdf).
The group-object formulation uses the generalized-element interpretation in
[Vistoli's notes](https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/vistoli.pdf).
These checks support the bounded edits, not a certification of the full corpus.

### Ring dependency review (2026-09-05)

Reviewed the complete direct lists of four knowls, retaining their current
nonunital-ring convention. `ring` and `ring-axioms` each require binary operations
and abelian groups. The latter is an alternative statement of the same axioms,
not a prerequisite of the former. `unital-ring` and `commutative-ring` each
require `ring`; they specialize it and are not prerequisites of its definition.
The existing textual links to these variants remain useful and are unchanged.
Set the four review counters to 1 and removed the obsolete heuristic-ownership
marker. This is an AI editorial review of these lists, not a review of their
full transitive closure or a certification of every mathematical assertion.

The graph now counts reviewed and unreviewed displayed edges separately and
identifies the selected node's review as a review of its prerequisite list.
It does not claim the neighboring lists have received the same review.

### Milestone 1 verification (2026-09-05)

- 93 Python tests pass, including reading-mode overrides in both full pages
  and inline fragments.
- The standalone reading-flow browser test passes for compact prose/display/
  continuation sequences, nested definitions, continuous documents with later
  paragraphs, lists, index entries, table cells, Escape, and focus restoration.
- Built-page checks pass at 320px, 390px, and 1440px. The 390px GNS core starts
  at 285px; its complete statement precedes the expanded prerequisite. Group
  object core formulas need no horizontal scrolling even at 320px. Inspected
  generated screenshots, including the changed mathematical sections.
- Existing homepage, graph, and runtime browser suites pass against a freshly
  generated development site. The temporary test server was shut down.
- Production builds 3,491 knowls; development builds 3,501. Both have zero
  validation errors and 593 warnings: 581 heuristic-cycle warnings and 12
  duplicate-alias warnings. Two cycle warnings were removed by the bounded ring
  review; this is not a claim of corpus-wide graph correctness.
- The final production HTML scan passes, requiring rendered diagrams and the
  production profile. The source-section audit passes for all 3,491 production
  files; the external-reference audit passes for the three prose-edited knowls.
- Dependency generation reports four reviewed lists preserved, four existing
  authored lists preserved, and no changes. Direct apply checks leave the four
  reviewed ring files byte-identical.
- Both repository diffs pass whitespace checks. Work remains uncommitted on
  `astra-refactor`; no deployment or merge was performed.

The next planned batch is documented in [refactor-fanout.md](refactor-fanout.md).
Milestones 2–5 were completed in the subsequent batch described below.

Milestone 1 content review was regenerated and browser-checked: seven knowls,
including the four metadata-only edits. Live review:
http://100.69.17.72:8015/review/content-changes/ . Both panes use the current
renderer; this review compares content, not historical versions of the UI.


### Milestones 2–5 delivery (2026-09-05)

The functional and ring lanes reviewed 23 complete pages. Corrections include
scalar-field restrictions, the common additive identity in the vector-space
axioms, conjugation in polynomial inner products, almost-everywhere classes in
L², the zero-functional GNS case, and the hypotheses for the ideal
characterization of fields. The reading-path note records checked conventions,
source locators, and prerequisites outside this batch. Source review rejected
incorrect chapter citations and replaced them with substantive accessible
references. The ledger records AI editorial review, not independent certification.

The graph's reviewed-only checkbox filters edges before traversal, preserves
the selected concept, explains empty neighborhoods, and persists the mode in
the URL. Its review statement applies to a node's direct prerequisite list.

Homepage/index browsing now separates subjects from source collections, including
Langlands' letter, Shale's paper, historical expansion guides, and posts. Editorial
labels replace mechanical word order. The existing Analysis section mixes
absolute continuity with porosity and uncertainty geometry, Real Analysis covers
the introductory sequence, and Convex Analysis includes its own background
prerequisites. These are overlapping scopes, not interchangeable owners; they
were not mechanically merged. Discovery tests cover an exact title (Hilbert
space), a standard alias (Gelfand–Naimark–Segal construction), and distinct scope
descriptions for the ambiguous query “field.”

Composition of functions and the Riemannian orthonormal-frame specialization
now redirect to their canonical owners. Old page URLs, core fragments, and
historical example/remark fragments remain available; canonical search entries
retain retired titles and aliases. Chained redirects compose section mappings;
missing targets and cycles produce validation errors. Dependency exports use
canonical IDs. The cumulative diff shows the canonical mathematics beside the
historical source, instead of an empty redirect stub.

The former combined integration theorem is now a reading guide to Riemann and
Riemann–Stieltjes linearity and interval additivity. The two additivity results
are new atomic pages. The Stieltjes page distinguishes the local mesh-limit
definition from the cited upper/lower-sum formulation instead of assuming their
unqualified equivalence.

The existing authoring workflow now preserves supplied branches, keeps essential
hypotheses in the core, makes extra expansion indexes optional, and distinguishes
full, targeted, and dependency-only review. Progress is recorded in the content
repository's `reviews/refactor-ledger.json`; source hashes invalidate stale full
reviews. [Current statistics](refactor-progress.md): 18 starting knowls corrected,
23 fully reviewed, 3,468 still requiring full review, two compatibility redirects,
two new knowls, and 30 prerequisite lists with recorded reviews. These measures
overlap and must not be added together. The denominator remains the 3,491-source
starting corpus, including collections.

Verification:

- 101 Python tests pass, including real chained-redirect builds, selective old-ID
  builds, canonical dependency exports, review rendering, and stale-review counts.
- Homepage, graph, and runtime browser suites pass against the existing preview.
  Standalone reading-flow checks and built-page checks at 320/390/1440px pass.
  Final mobile spot checks include vector space, inner product space, field,
  positive functional, and Stieltjes additivity. Reviewed graph screenshots were
  inspected at all three widths.
- Production contains 3,491 canonical entries from 3,493 sources (two redirects).
  The existing development preview retains its optional conjecture collection
  and contains 4,677 canonical entries. Both builds have zero validation errors
  and 577 existing warnings: 567 unreviewed cycle warnings and ten alias warnings.
- The source-section audit passes for all 3,493 sources; the new external-reference
  syntax audit passes. The full production HTML scan passes with rendered
  diagrams and production-profile isolation required. This is separate from
  semantic review.
- The cumulative review contains 34 comparisons, including two additions.
  Browser checks cover filtering, sorting, both panes, consolidation destinations,
  both retired page URLs, and their historical example fragments.

Content baseline checkpoint: `4c48c37c`; milestone completion: `c1e30e06`.
Compiler baseline checkpoint: `4ee8847`. Work is committed to `astra-refactor`;
no production publication, push, or merge is part of this delivery. The existing
`knowlpedia-astra-benchmark` service continues to serve port 8015.

Live cumulative review: http://100.69.17.72:8015/review/content-changes/ .
It compares content `ea7256bd` to `c1e30e06` using the current renderer on both
sides. The next fan-out is a plan for 60 existing pending knowls in five lanes,
followed by independent cross-review; that larger batch has not been executed.

### Large batch and complete DAG repair (2026-09-05)

The larger fan-out completed 1,026 additional full reviews, bringing the
source-hashed total to 1,049 of the fixed 3,491 starting knowls. There are 54
recorded substantive corrections in total and 2,442 entries awaiting full
review. The exact 64 deferrals from this batch remain in the assignment
manifest. See [refactor-fanout.md](refactor-fanout.md) for scope and audit results.

All prerequisite cycles are now resolved, including the previously unreviewed
parts of the graph. The final canonical graph has 9,889 edges, zero cycles,
zero missing targets, and zero self-dependencies. Independent semantic checks
restored needed antecedents removed too aggressively; no graph algorithm
chooses which mathematical dependency to delete. Compiler validation now
rejects cycles regardless of review count and resolves redirected targets
before traversing them. Standard build targets no longer bypass errors.

The static architecture and reader interaction remain unchanged in this batch.
Ten existing duplicate-alias warnings remain; they are not prerequisite loops.
The refreshed cumulative diff compares content against `ea7256bd` using the
current renderer, at http://100.69.17.72:8015/review/content-changes/ .

Large-batch verification: 102 Python tests pass; source-section and external-link
checks pass for all 3,493 source files. The strict production build compiles
3,491 canonical knowls and its complete rendered HTML scan reports no errors.
The composed development preview compiles 4,677 knowls, including the existing
additional source collection. Homepage, runtime, graph, reading-flow and
320/390/1440px reader checks pass. The cumulative diff has 1,482 comparisons;
search and the rendered before/after axiom were browser-checked.

The narrowest development header exposed a one-pixel overflow. Reducing the
gap between navigation and actions keeps the larger mobile search target
while fitting the 320px viewport. The graph smoke test now
checks that unreviewed edges disappear, allowing nodes that remain connected
through reviewed paths to stay visible.

### Entire remaining corpus reviewed (2026-09-05)

Completed all 2,442 remaining entries: the fixed starting corpus now has
3,491 full current-source reviews, zero pending reviews, and zero stale hashes.
The two later additions also have full reviews. Cumulative content corrections
rose from 54 to 120; unchanged pages were retained. The final prerequisite graph
has 9,892 edges and remains acyclic, with no missing or self-referencing edges.
See [remainder-review-plan.md](remainder-review-plan.md) for the completed scope,
verification, and the corrections rejected during independent review.

The cumulative before/after page remains at
http://100.69.17.72:8015/review/content-changes/ on the existing persistent service.
