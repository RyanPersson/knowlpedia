# Legacy knowl quality audit — July 30

This audit follows the two-speed editorial contract in
`knowlpedia-content/EDITORIAL.md`: an ordinary knowl should have one exact
definition, theorem, construction, or example in its core, with qualifications
and slower exposition in progressive sections.

The review excluded every production file already added or modified by the
July 30 mathematical expansion. It inspected the remaining 2,678 pre-existing
production knowls through registry/link scans, short-core and generic-kind
inventories, semantic duplicate searches, targeted mathematical sampling, and
rendered-output checks.

## Completed improvement batch

This batch preserves every existing knowl ID. It changes 37 pre-existing
production knowls.

### Correct definitions and theorem hypotheses

- `algebra-modules/bilinear-map`: separates bilinear maps over a commutative
  ring from balanced maps for a right-left module pair.
- `topology/bounded-set`: handles the empty set and restores the finite-diameter
  equivalence.
- `topology/extreme-value-theorem`: requires a nonempty compact domain.
- `topology/nested-interval-theorem`: requires bounded closed intervals and
  records the unbounded counterexample.
- `differential-geometry/riemann-surface`: states the automatic
  biholomorphic-inverse theorem and respects the connectedness convention.
- `real-analysis/global-maximum-global-minimum`: distinguishes maximizing
  points from maximum values.
- `fiber-bundles/special-unitary-frame-bundle-reduction`: makes the determinant
  trivialization part of the data and removes false rank-one canonicity.
- `quantum-foundations/positive-operator-valued-measure`: replaces the
  finite-outcome special case with the measurable-space definition and weak
  countable additivity.
- `probability/differential-entropy`: states when the extended integral is
  defined and records its dependence on reference measure and coordinates.
- `operator-algebras/weight-on-von-neumann-algebra`: gives the standard span
  description of the finite ideal.

### Lie theory, Galois descent, and automorphic foundations

- `langlands-letter/knowls/adeles-restricted-product`
- `langlands-letter/knowls/chevalley-basis`
- `langlands-letter/knowls/euler-product-and-local-factor`
- `langlands-letter/knowls/galois-descent-forms`
- `langlands-letter/knowls/langlands-functoriality-l-homomorphism`
- `langlands-letter/knowls/maximal-compact-hyperspecial`
- `langlands-letter/knowls/nonabelian-h1-galois-cohomology`
- `lie-groups/cartan-subalgebra-self-normalizing-lemma`

These revisions add the missing topology, continuity, normalization,
coefficient groups, integral models, local parameters, and convention
boundaries. In particular, torsors, forms, inner forms, and pure inner forms
are no longer conflated.

### Infinite-dimensional Gaussian and CCR conventions

- `shale-paper/gaussian-measure-hilbert-space`
- `shale-paper/symplectic-hilbert-space`
- `shale-paper/weyl-ccr-quantization`

The Gaussian record now uses an isonormal process on an auxiliary probability
space and explicitly rules out identity covariance as a Borel Gaussian measure
on an infinite-dimensional Hilbert space. The symplectic record distinguishes
weak from strong nondegeneracy. The CCR record defines a regular Weyl
representation before introducing its unbounded Stone generators.

### Broken or misleading links and visible source artifacts

- `algebra-representation-theory/completely-reducible-representation`
- `algebra-representation-theory/maschkes-theorem`
- `algebra-representation-theory/sum-squares-degrees`
- `convex-analysis/youngs-inequality`
- `differential-geometry/coisotropic-submanifold`
- `differential-geometry/kahler-form`
- `differential-geometry/maslov-class-lagrangian-grassmannian`
- `differential-geometry/maslov-cycle`
- `differential-geometry/maslov-index`
- `differential-geometry/relative-maslov-index`
- `fiber-bundles/jet-bundle`
- `lie-groups/global-cartan-decomposition`
- `lie-groups/maurer-cartan-equation`
- `linear-algebra/vector-space`
- `operator-algebras/normal-positive-map`
- `real-analysis/implicit-function-theorem`

The four Maslov records percent-encode parentheses in a DOI that the current
Markdown-link parser otherwise truncates. The remaining edits remove one
recursive self-link, correct semantic targets and labels, and replace literal
JSON-style Unicode escapes.

## Corpus-wide findings

The internal registry is in good structural condition:

- no missing knowl IDs were found among the untouched production files;
- no unresolved structured relations or fragment references were found;
- no unrecognized raw knowl markers were found outside protected math/code;
- the sampled modern functional-analysis, PDE, operator-algebra, Kähler, and
  hyperkähler records were generally precise and appropriately progressive.

The highest remaining quality debt is concentrated in older migrated
real-analysis, elementary topology, and duplicated foundation records.

## Follow-up queue

These items require a separate migration rather than opportunistic edits.

1. **Canonical-ID and redirect support.** Exact or near duplicates include:
   composition of functions; fibers of a map; orthonormal frame bundles;
   continuous functions being Riemann integrable; the uniform-limit theorem;
   convergent-series terms tending to zero; one-variable differentiability;
   limits at a point; and several supremum/infimum collections. Deleting one
   member today would break incoming IDs because the content model has no
   redirect mechanism.
2. **Atomic real-analysis cleanup.**
   `additivity-linearity-riemann-integral` and
   `m-test-continuity-integration-corollary` bundle several independently
   named results already represented elsewhere. The limsup/liminf and
   supremum/infimum property collections need a manifest of atomic theorem
   IDs before they are split.
3. **Ring-convention boundary.** The foundational `ring` record permits
   nonunital rings and `ring-homomorphism` does not require preservation of
   one, while commutative algebra and algebraic geometry tacitly use unital
   rings and unital maps. This should be resolved as one documented convention
   migration across local rings, spectra, affine schemes, and related maps.
4. **Renderer support for balanced URL parentheses.** Encoding repaired the
   known Maslov DOI, but the Markdown parser should eventually accept balanced
   parentheses in arbitrary link destinations and gain a regression test.
5. **Further targeted enrichments.** Good next candidates include the
   automorphic-form regularity conditions, based root data and highest-weight
   hypotheses, the precise locally compact Følner equivalence, and additional
   generic-kind normalization for correct but thin elementary theorem records.

Each follow-up should get its own bounded manifest, comparison page, and
validation run rather than being folded silently into an unrelated expansion.

## External-link placement follow-up

A later presentation audit found 950 genuine clickable source citations
outside reference sections in 759 production knowls. The audit parser was also
corrected after an initial count of 954: unmatched mathematical interval
notation could make a later bibliography link look like part of a multiline
body link. In nearly every genuine case, the source was already represented in
the same knowl's bibliography.

Git history shows that this was a recent batch-generation convention rather
than established corpus style. Of the 950 citations, 834 came from `3b9a0a2`
on July 26, 101 from `d456ea2` on July 27, 9 from `316d4e7` on July 30, and 6
from `9d63894` on July 30.

The corpus now removes both hyperlinks and plain-text source pointers from
non-reference sections while retaining bibliographic entries in final
`## References` sections. Forty singular `## Reference` headings were
normalized to `## References`. The policy is recorded in
`knowlpedia-content/EDITORIAL.md` and enforced by
`scripts/audit_external_links.py` through the `make audit-external-links`
target.
