# Comparison against develop

Compared 2026-09-05. The refactor improves the sampled mathematical statements, dependency structure, and mobile reading flow. Most source-file changes are review metadata; the diff size must not be presented as thousands of rewritten definitions. This is a controlled branch comparison and a targeted editorial assessment, not an independent mathematical certification or user study.

## Revisions and controls

| Repository | develop | astra-refactor |
| --- | --- | --- |
| Application | `9c1e005a83f83ca431297424b83c311b44029de6` | `5ae5b4fb089a6fc4b8e6d2e578fcc8d04892c9b0` |
| Content | `ea7256bd661c30c54a817ea5e60dc9373119eaf6` | `e93d52ff04c7b3d6357beeda7ed9551c6dea252d` |

Both local develop branches match cached origin/develop. No fetch was performed. The application is six commits ahead and content five commits ahead, with no develop-only commits. The application revision above precedes this comparison report.

For content, the existing cumulative diff renders both revisions through the refactored renderer. For UI, both application revisions were built with exactly the develop content, production profile, and the existing prebuilt diagrams. Browser requests were routed to separate local build directories; no additional preview service was started. The refactored compiler needed `--allow-validation-errors` solely to render the historical cyclic content. That controlled build is not a passing validation result. The strict current-content production build is a separate check recorded in refactor-progress.md.

## Size and dependency structure

| Measure | develop | Refactor |
| --- | ---: | ---: |
| Source knowls | 3,491 | 3,493 |
| Canonical dependency nodes | 3,491 | 3,491 |
| Canonical prerequisite edges | 10,443 | 9,892 |
| Cyclic strongly connected components | 153 | 0 |

There are 2,948 changed existing source files and two additions, with no deleted source files. Of the existing files, 2,826 change only metadata; 2,334 change only review markers. The remaining 122 comprise 120 recorded content corrections and two compatibility redirects. A total of 518 prerequisite lists changed; this overlaps the other categories. Raw prerequisite lists lose 762 edges and gain 216, ending at 9,897 edges; redirect canonicalization merges five of those edges. Cyclic components are not a count of every individual cycle.

Body changes or changes to title, summary, core, core_data, core_axioms, redirect_to, or redirect_sections count as substantive in this source comparison. Metadata-only includes prerequisite changes, which can materially improve navigation. Review completion is a process statistic, not a quality score.

## Editorial assessment

Twelve deliberately selected examples span elementary definitions, advanced material, and research posts. They were selected to inspect different kinds of edits, not randomly sampled to estimate a corpus-wide error rate.

| Example | Assessment |
| --- | --- |
| Field | Explicit unity and hypotheses on the ideal characterization resolve ambiguity under this corpus's nonunital ring convention. |
| Vector space | Clarifies the shared additive zero and the role of the scalar field. Helpful exposition, although somewhat longer. |
| Inner product | Makes the linear/conjugate-linear argument convention explicit. |
| GNS construction | The point-evaluation example supplies a concrete model of the quotient construction; the zero-functional case is addressed. Added length earns its place here. |
| Subharmonic function | Distinguishes an almost-everywhere distributional condition from the choice of pointwise representative; the spike example explains why this matters. |
| Rational function | Separates finite rational expressions from the constant map to infinity when discussing sphere-valued maps. |
| Left Maurer–Cartan form | Aligns the displayed equation with an explicitly pointwise bracket convention. The old factor of one-half was appropriate for its wedge-bracket convention; this is convention alignment, not an inherently incorrect old formula. |
| Bundle of connections | Distinguishes the adjoint Lie algebra bundle from the adjoint group bundle in the affine model. |
| Tangent sheaf | Adds smoothness to the characteristic-zero claim identifying differential operators with the enveloping algebra. |
| Strong Morita equivalence | Requires an isomorphism with compact module operators, closing the gap left by an action whose image alone is the compact operators. |
| Research advice analysis | Removes unsupported quantitative and quotation claims. The result has less apparent empirical detail but a more defensible scope. |
| Semigroup/quasigroup post | Removes unsupported embedded material and clarifies the division conditions. |

The strongest gains come from corrected hypotheses, explicit conventions, concrete examples, and deletion of unsupported assertions. There is no evidence here that every longer passage is better, or that remaining unchanged knowls are error-free. This assessment is self-review; an independent blinded sample remains useful before making external quality claims.

## Controlled reader comparison

Playwright checked the homepage, vector-space page, and GNS page at 320, 390, and 1,440px in both renderers: 18 page/viewport combinations. All had no page-level horizontal overflow and no browser JavaScript errors. These are narrow checks, not exhaustive browser coverage.

At 390px, the GNS core starts at 403px in develop and 285px in the refactor (117px higher before rounding). Vector space starts at 304px versus 236px (68px higher). At 1,440px those core positions are unchanged. Both production renderers fit the tested widths; this experiment does not establish a baseline overflow regression.

Expanding “positive linear functional” in GNS on develop inserts the panel inside the definition paragraph, splitting the sentence and separating it from its formula. The refactor appends the panel after the compact core. Screenshots confirm the complete statement remains together. The tradeoff is that expansion may appear farther from the clicked term in a long core.

The homepage separates subject browsing from source collections. That distinction is clearer in the source structure; the captures do not measure whether readers find material faster. The reviewed-edge graph filter offers a useful inspection mode, but its metadata limitations below prevent interpreting it as an authoritative completion view. No performance or external benchmark scores were measured.

## Remaining issues and recommendation

1. Reconcile review metadata with the ledger: 496 nonempty prerequisite lists have no positive dependency_review_count; 62 positively marked entries still carry dependency_heuristic. Content review and prerequisite-list review are distinct concepts, so this needs an explicit policy rather than blindly setting every count to one.
2. Calibrate mathematical quality with an independent blinded sample, stratified by subject, difficulty, changed/unchanged status, and generation period. The targeted examples here cannot supply an unbiased quality percentage.
3. Freeze these revision identifiers, rendering conditions, and the evaluation rubric for external comparisons. Score correctness, clarity, examples, navigation, and unsupported claims separately; do not reward review-marker changes as editorial improvements.

Proceed with an exploratory external comparison now. Reconcile the review indicators before using them to select “reviewed” benchmark material or claiming corpus-wide quality from the completion statistics. This comparison made no application or mathematical-content changes.

## Artifacts

- [Visual comparison](http://100.69.17.72:8015/review/develop-comparison/)
- [Complete content diff: 2,950 comparisons](http://100.69.17.72:8015/review/content-changes/)
- [Browser measurements](http://100.69.17.72:8015/review/develop-comparison/measurements.json)
- [Source-change classification](http://100.69.17.72:8015/review/develop-comparison/source-comparison.json)

The existing persistent preview serves the artifacts. Generated files live under public-imported/review/develop-comparison and may be removed by a clean site rebuild. Build snapshots and the browser capture script are under tmp/develop-comparison; this report retains the methodology and conclusions.
