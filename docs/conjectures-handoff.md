# Conjectures knowlification handoff

## Branches and scope

Work is on the local `conjectures` branch in both repositories:

- `/home/codex/code/knowlpedia-root/knowlpedia`
- `/home/codex/code/knowlpedia-root/knowlpedia-content`

The content branch adds axiom-first pages for the twelve conjectures selected from the personalized formal-conjectures catalog. The compiler branch contains this handoff; no compiler or runtime behavior needed to change.

## Public entry point

The collection entry point is `content/conjectures.knowl.md`, rendered at `/conjectures/`. It divides the collection into the eight primary and four secondary selections.

Primary pages:

1. Hilbert–Smith conjecture, \(p\)-adic formulation
2. Erdős problem 727
3. Inverse Galois problem
4. Pierce–Birkhoff conjecture
5. Banach–Mazur rotation problem
6. Maximum number of mutually unbiased bases
7. Smooth four-dimensional Poincaré conjecture
8. Existence of SIC-POVMs

Secondary pages:

1. Complex structure on the six-sphere
2. Kaplansky zero-divisor conjecture
3. Invariant subspace problem
4. Pretriangulated but non-triangulated category

Each page defines its ambient objects and exact hypotheses before its conjecture/open-problem section, records known boundaries, and names the corresponding Lean file under `google-deepmind/formal-conjectures`.

## Dependency work

The pre-change content inventory contained 2,140 knowls. The completed branch contains 2,195:

- 12 conjecture pages;
- 41 supporting definitions;
- 1 public conjecture index;
- 1 temporary review/glossary index.

Pass one introduced 33 missing prerequisites. Pass two recursively examined those definitions and added eight more: initial object, closed manifold, orthogonal complement, orthogonal projection, positive semidefinite operator, holomorphic map, integrable almost-complex structure, and mapping cone.

New definitions are linked from their normal domain indexes in addition to the temporary index. Existing knowls were reused when semantically suitable, even across domain boundaries.

## Reproducibility artifacts

Workflow artifacts are under `knowlpedia-content/content/knowlification/conjectures/`:

- `sources/`: frozen, unlinked first-pass page bodies;
- `frontmatter/`: page metadata;
- `term-map.json`: deterministic first semantic-link pass;
- `coverage-table.md`: per-page dependency coverage;
- `semantic-dependency-audit.md`: first- and second-pass audit summary;
- `candidate-link-adjudication.json` and JSONL ledgers: candidate decisions;
- `new-knowls-index.knowl.md`: clickable review index.

The candidate matcher surfaced one important wrong-sense risk: “separable” in a Galois extension must not link to topological separability. The adjudication also records rejected false matches for inverse limits and tangent-bundle endomorphisms.

## Validation completed

- Full compiler build: 2,195 knowls compiled.
- Validation report: 27 warnings, identical to the 27-warning baseline; all are pre-existing duplicate aliases.
- New validation errors or warnings: 0.
- Rendered HTML scan: no raw wikilinks, malformed math markers, or other detected rendering errors.
- Source fidelity: all twelve conjecture pages pass exact comparison against their frozen sources after frontmatter and semantic-link markup are removed.
- Link resolution: every link on every conjecture page resolves.
- Candidate review: 63 conjecture-page candidates adjudicated, 28 applied, no unreviewed residual candidate; 22 high-confidence links added across 19 new definition files.
- Browser QA: index title and all 12 links present; KaTeX rendered on representative category and quantum pages; inline dependency expansion worked; no browser console errors; no horizontal overflow at a 390×844 viewport.

## Review preview

A persistent preview is served by `devserver-knowlpedia-conjectures.service` on port 8012. On the OptiPlex it is `http://127.0.0.1:8012/conjectures/`; over Tailscale it is `http://100.69.17.72:8012/conjectures/`.

Useful review order:

1. Read the conjecture index and choose a domain of interest.
2. Check whether the object-building paragraphs are sufficient without being encyclopedic.
3. Expand several inline definitions to judge granularity and link density.
4. Compare the formal-source paragraph with the named Lean source when exact scope is important.
5. Use the temporary new-knowl index to review the 41 supporting definitions independently.

## Deferred follow-up

The requested `leanknowl`/automation feasibility study is intentionally deferred until the editorial feedback cycle on these manually produced knowls is complete. That later study should treat this collection, its source/final pairs, term map, coverage table, and decision ledgers as a small gold-standard dataset for comparing Lean declarations and metadata against publishable knowl output.
