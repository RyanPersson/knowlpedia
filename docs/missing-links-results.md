# Production linking review results

The six stages in [the roadmap](missing-links-roadmap.md) are complete on
`missing-links`. The scope is mathematical linking and dependency coverage,
including checking new target definitions and preserving minimal opening cores.
This is not a certification of every mathematical claim in the corpus.

## Coverage

| Measure | Final count |
| --- | ---: |
| Canonical production entries reviewed | 3,515 |
| Non-container knowls | 3,458 |
| Production containers reviewed | 57 |
| Existing entries changed | 514 |
| New definitions added and reviewed | 16 |
| Entries reviewed without net changes | 2,985 |
| Stale reviews / blocked / remaining | 0 / 0 / 0 |
| Legacy redirects checked separately | 2 |

The initial scope had 3,442 non-container knowls. We expanded it to include
all 57 production containers and the 16 new definitions. Counts come from
`knowlpedia-content/reviews/missing-links/progress.json` and the accepted
source-hash ledger, not from agents' estimates or the number of phrase matches.
Three tentative source changes were fully reverted after final target review;
these count as unchanged.

## Work completed

- Calibrated across algebra, geometry, analysis, probability and physics, then
  reviewed the full production inventory in batches.
- Adjudicated all 768 original unknown-phrase groups. Most were existing
  concepts, local descriptions or false positives.
- Added faithful and fully faithful functors, quaternion and alternating groups,
  Poincaré disk, crossing form, volume form, sectional and Gaussian curvature,
  normal and uniform distributions, Calkin algebra, reduced cohomology,
  Schrödinger representation, rank-one operator and Borel measure.
- Reviewed callers again after adding those definitions. Kept Hilbert-module
  rank-one operators distinct from operators with one-dimensional range, and
  complex/holomorphic volume notions distinct from real oriented volume forms.
- Kept core statements minimal; moved equivalent formulas and consequences
  into expandable sections. Corrected the plane-wave Laplacian sign convention
  and the new reduced-cohomology explanation after checking their definitions.
- Used independent batch samples, separate new-definition checks, and a final
  review of every changed source's added link targets. Root resolved wrong-sense
  matches, dropped labels, duplicated words and extra brackets found in review.
- Removed 32 nested link wrappers from 26 edited sources. Compiler validation
  now rejects nested knowl links before rendering while preserving brackets in
  math and code; audit fence handling has regression coverage.

## Validation

- 157 Python tests passed, including audit, compiler and progress regressions.
- Production and development audits: no unresolved knowl or prerequisite IDs,
  and no compiler validation errors. Ten pre-existing alias warnings remain.
- Production dependency graph: 3,515 nodes, 10,953 edges, no cycles, invalid
  sources or missing targets.
- Production build and full HTML rendering scan passed with no errors,
  including rendered-diagram and production-profile requirements.
- Browser checks passed at 320, 390 and 1,440 pixels, including inline expansion
  and the preserved Research Advice article. All 16 new definitions separately
  passed at 390 and 1,440 pixels with collapsed details, working prerequisite
  expansion, no rendering errors and no page overflow. Mobile and desktop
  screenshots of new definitions were inspected.
- The existing development service was rebuilt, retaining its composed local
  content; no duplicate server was started.

## Interpreting discovery counts

The fresh production audit still reports 21,373 unlinked phrase candidates,
373 ambiguous occurrences and 739 possible unknown phrase groups. These are
heuristic discovery outputs, **not unresolved errors**. They include generic
words, compositional descriptions, repeated concepts and context-dependent
meanings. Review evidence records accepted and rejected matches. Future edits
invalidate a review when its source hash changes; rerun the audit and progress
commands in the roadmap to find those entries.

The development audit also checks ten development-only canonical entries for
structural errors. Neither those entries nor the external conjectures package
are included in the production manual-review count.

## Commits and comparison

Content commits: `dc8b68a6` (new definitions and focused corrections),
`dcd1babd` (corpus linking and review ledger). The application and content trees
remain on `missing-links`, based on `develop`.

[Rendered comparison against develop](https://optiplex.taildb538a.ts.net/review/missing-links/)
includes added definitions. The existing development service serves it; production
builds do not include this comparison artifact.
