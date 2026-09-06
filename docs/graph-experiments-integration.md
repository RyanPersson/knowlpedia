# Graph experiments integration

Merged remote graph-experiments into astra-refactor in both repositories on 2026-09-06. Incoming application commit: ee64d878e038a648d89f7875a77b75f9c0be7373. Incoming content commit: e806d3c816f941c48ff646be11d6a4d6bb77ee10. Pre-merge astra revisions: application 34ff1af, content e93d52ff.

## Result

The graph retains neighborhood, subject and component views, topological placement, zoom, keyboard navigation and URL history from graph-experiments, together with astra's reviewed-links filter and compact-core expansion behavior. Filtering also recalculates component membership. The incoming semantic prerequisite lists were retained; nonconflicting mathematical corrections from both branches were preserved. The generated-ideal formula needed a manual semantic resolution because the textual merge combined two alternative formulas.

The graph audit and compiler now share redirect-aware registry construction. Compatibility redirects remain valid URLs without becoming duplicate canonical graph nodes. The dependency generator preserves both authored lists and semantic repair provenance. Tests from both branches remain enabled; the filter smoke test uses a small fixture because a fully reviewed real corpus no longer supplies an unreviewed edge on demand.

Research Advice Analysis retains its original develop body exactly, its original page title and kind, and continuous article presentation. Only incoming prerequisite-review metadata is retained in its header.

## Minimal openings

Read all 86 new/changed mathematical openings relative to develop, plus the GNS opening and the surrounding source needed for each change. Made 60 targeted edits. Examples, proofs, consequences, alternative constructions and convention commentary now unfold in later sections. Necessary hypotheses, quantifiers, operation signatures and conventions stay in the opening. The vector-space definition has eight named axioms, one list item per axiom. On narrow screens long items wrap naturally.

The Yang–Mills opening previously stopped at the setup: its defining energy formula was hidden by a heading. The formula is now in the core. Also corrected its Lie-algebra-bundle notation, the domain-openness hypothesis in the Fréchet derivative, and the overlapping generated-ideal formula. These changes are targeted editorial review, not new full-body certification.

## Validation

- 136 Python tests and the graph-model tests pass.
- Production canonical graph: 3,499 nodes, 10,911 prerequisite edges, zero cycles, missing targets or invalid sources.
- All 47 recorded learning-path and endpoint checks pass. These inspect authored lists; the graph audit separately resolves compatibility redirects.
- Production HTML scan passes with no rendered errors and the production-profile guard enabled.
- Section and external-link source audits pass for all 3,501 source files.
- Strict production build compiles 3,499 canonical entries. Development preview compiles 4,685 entries, including the existing local conjectures catalog.
- Browser suites pass for graph views, reviewed filtering/history, and reader pages at 320/390/1,440px. Visual inspection covers named axioms, mobile graph layout, and subject browsing.
- The composed development preview scan flags rendering errors in the separate local conjectures catalog. That source is outside these two merged repositories; the production build excludes it. The production rendering scan is the release check.
- The reader test checks eight named axiom items, initially collapsed details, the Yang–Mills formula in the core, uninterrupted prerequisite expansions, and the restored continuous research article.

## Review accounting

The incoming dependency reports are historical snapshots of graph-experiments, not newly recalculated full-body review results for this merge. Every current canonical prerequisite list has a recorded review. The full-review ledger carries forward 3,426 prior valid reviews only where a source comparison confirms identical body text and nondependency metadata. It records the 60 core edits as targeted reviews. It deliberately does not call these fresh full-body reviews: 65 starting entries have stale full-review hashes after substantive changes. Current counts are in refactor-progress.md. Eight foundations from graph-experiments bring cumulative additions to ten.

## Preview

- [Merged graph](http://100.69.17.72:8015/graph/)
- [This batch's body changes and additions](http://100.69.17.72:8015/review/merge-changes/)
- [Cumulative comparison with develop](http://100.69.17.72:8015/review/content-changes/)
- [Vector-space axioms](http://100.69.17.72:8015/linear-algebra/vector-space/)
- [Restored Research Advice Analysis](http://100.69.17.72:8015/posts/research-advice-analysis/)

The existing devserver-knowlpedia-astra-benchmark service serves public-imported on port 8015. Review artifacts must be regenerated after a full build, which replaces that output directory.

## Targeted opening edits

- algebra-category-theory/pretriangulated-category
- algebra-commutative/simple-artinian-matrix-ring
- algebra-homological/ext
- algebra-rings/field
- algebra-rings/ideal-generated
- algebra-rings/multivariable-formal-power-series-ring
- algebra-rings/product-of-ideals
- algebra-rings/ring-homomorphism
- algebra-rings/total-ring-of-fractions
- algebra-rings/unital-ring
- algebraic-geometry-foundations/geometric-fiber
- algebraic-geometry-foundations/regular-local-ring
- algebraic-geometry-foundations/regular-scheme
- algebraic-geometry-foundations/tilt-and-untilt
- analysis/quantitative-unique-continuation
- complex-analysis/cauchy-riemann-equations
- complex-analysis/isolated-singularity-classification
- complex-analysis/maximum-modulus-principle
- convex-analysis/convex-conjugate-fenchel
- convex-analysis/convexity-preserved-under-monotone-convex-composition
- convex-analysis/legendre-fenchel-transform
- differential-geometry/category-of-smooth-manifolds
- differential-geometry/differentiable-flow
- differential-geometry/geodesic
- differential-geometry/holomorphic-map
- fiber-bundles/atiyah-algebroid-of-a-principal-bundle
- fiber-bundles/connection-on-a-vector-bundle
- fiber-bundles/horizontal-lift-of-a-curve
- fiber-bundles/leibniz-rule-for-a-connection
- fiber-bundles/lie-bracket
- fiber-bundles/parallel-transport
- fiber-bundles/representation-variety
- fiber-bundles/unit-tangent-bundle
- fiber-bundles/yangmills-functional
- functional-analysis/banach-algebra
- functional-analysis/closed-quadratic-form
- harmonic-analysis/unitary-dual
- langlands/affine-springer-fiber
- langlands/irregular-singular-connection
- langlands/stable-distribution
- lie-groups/cartan-matrix
- lie-groups/general-linear-group
- lie-groups/generation-module-as-even-exterior-algebra
- lie-groups/lie-subgroup
- lie-groups/right-maurer-cartan-form
- lie-groups/stabilizer-lie-group
- linear-algebra/closed-linear-subspace
- linear-algebra/rank-nullity-theorem
- linear-algebra/vector-space
- mathematical-physics/existence-of-advanced-and-retarded-green-operators
- operator-algebras/gns-construction
- operator-algebras/involutive-algebra
- operator-algebras/strong-morita-equivalence
- real-analysis/frechet-derivative
- real-analysis/gradient
- real-analysis/one-sided-limit
- real-analysis/right-derivative-left-derivative
- shared-foundations/finite-permutation
- shared-foundations/p-adic-integers
- shared-foundations/permutation-sign
