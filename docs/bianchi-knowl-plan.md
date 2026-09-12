# Bianchi groups: knowl plan and implementation

## Scope and baseline

Prepared 2026-09-12 from the [Wikipedia Bianchi group article](https://en.wikipedia.org/w/index.php?title=Bianchi_group&oldid=1372725401), particularly its definition, Geometry, and Arithmetic properties sections.

Both working repositories are on `bianchi`, created from their local `develop` branches:

- `knowlpedia`: `3efcb734d6`.
- `knowlpedia-content`: `5fa3fa0dcb`.

The original inventory and proposed writing order are retained below. The batch is now implemented as described in the implementation section. In the original inventory, absence means no dedicated owner was found in the audited content tree, not that a term never occurs in prose.

## Implemented batch

The content commit is `cce5c343` on `bianchi`: **39 new concept/theorem knowls, one new index, and six navigation updates**. The original 28 candidates are covered, both matrix-group decisions became ring-valued companions, and nine further prerequisite knowls were added: horoball, parabolic hyperbolic isometry, quaternion algebra, standard quaternion conjugation, reduced norm, split quaternion algebra, quaternion order, its norm-one group, and real-place ramification.

- [New-knowl collection](http://100.69.17.72:8015/knowlification/bianchi-index/)
- [Live develop-to-bianchi comparison](http://100.69.17.72:8015/review/bianchi/)
- [Bianchi group entry](http://100.69.17.72:8015/algebra-groups/bianchi-group/)

The existing `devserver-knowlpedia-astra-benchmark` service on port 8015 serves the branch build from `public-imported`. The persistent develop service remains on port 8003.

The content repository's `reviews/bianchi-batch.json` records the complete new-ID manifest and checks. `reviews/refactor-ledger.json` has a `bianchi-2026-09-12` batch with source hashes and **targeted** review evidence. These entries do not claim completed full mathematical reviews.

### Validation

- Full composed build: 4,765 knowls compiled, no compiler errors and no warnings on new knowls. Ten existing alias warnings remain elsewhere.
- Every new internal target resolves; the new prerequisite closure contains 274 knowls and is acyclic.
- No rendering-scan findings in the new batch. The broad fragment scan found 128 issues entirely in imported conjectures.
- Browser checks: all 40 new routes returned HTTP 200; all 39 concept/theorem targets are linked from the index; inline expansion works; desktop and mobile Bianchi layouts inspected.
- Diff: 46 comparisons (40 added, six modified), with additions visible by default. The page compares the committed content branch against develop.

### Refreshing the preview and comparison

From the application repository, run `make build-content`, then:

```bash
.venv/bin/python scripts/generate_content_review.py \
  --content-repo ../knowlpedia-content \
  --left-ref develop --right-ref bianchi \
  --left-label develop --right-label bianchi \
  --include-added --heading 'Bianchi knowls: develop vs bianchi' \
  --output public-imported/review/bianchi
```

The comparison uses Git revisions, so commit new content before regenerating it. The generator initially hides additions when modifications also exist. For this additions-focused batch, check “Include newly created knowls”; the currently hosted artifact has that checkbox checked by default. A full rebuild may replace review output, so generate the comparison after the build.

## Coverage audit

Searched filenames and full text, and inspected IDs, titles, and aliases across 3,601 `.knowl.md` source records under `knowlpedia-content/content`, including the legacy Langlands-letter material. Read the relevant near-matches to distinguish actual coverage from mentions and different meanings.

| Existing canonical ID | Reuse or limitation |
| --- | --- |
| `algebra-fields-galois/number-field` | Reuse the definition of a finite extension of the rationals. |
| `algebra-fields-galois/field-extension` | Reuse for quadratic extensions. |
| `algebra-commutative/integral-element` | Reuse general integrality; an algebraic-integer specialization would give that named concept its own target. |
| `algebra-commutative/integral-closure` | Reuse for the construction of the ring of integers. |
| `algebra-commutative/dedekind-domain` | Already mentions rings of integers as examples, but does not own their definition. |
| `algebra-rings/ideal`, `algebra-rings/principal-ideal` | Reuse for ideal classes and norms. |
| `algebra-fields-galois/trace-field`, `algebra-fields-galois/norm-field` | Reuse; field norm and ideal norm need distinct targets. |
| `algebra-fields-galois/discriminant-field` | Owns the discriminant of a field basis. The integral discriminant of a number field is a separate missing target. |
| `lie-groups/special-linear-group` | Core currently restricts scalars to the real or complex numbers. Needs a ring-valued definition for this batch. |
| `algebra-groups/projective-special-linear-group` | Core currently assumes a field. Cannot silently use it as the definition over a ring of integers. |
| `lie-groups/psl2-complex` | Reuse the ambient complex Lie group. |
| `lie-groups/discrete-subgroup` | Reuse; already covers Lie groups. |
| `differential-geometry/hyperbolic-three-space` | Reuse; mentions Kleinian groups but does not give them a dedicated target. |
| `lie-groups/psl2c-action-on-hyperbolic-three-space` | Reuse the isometry-group identification and action; mentions orbifolds without defining them. |
| `complex-analysis/mobius-transformation` | Reuse for boundary actions when needed. |
| `algebra-groups/group-action`, `algebra-groups/orbit`, `algebra-groups/stabilizer` | Reuse the action vocabulary. |
| `fiber-bundles/quotient-space-of-an-action` | Reuse the orbit-space topology; a quotient space alone does not define an orbifold structure. |
| `lie-groups/proper-action-lie`, `fiber-bundles/quotient-manifold` | Reuse where applicable; do not apply the free-action manifold theorem to a quotient with torsion stabilizers. |
| `algebra-groups/index-of-subgroup`, `algebra-groups/torsion-free-group` | Reuse for commensurability and the manifold distinction. |
| `harmonic-analysis/haar-measure`, `differential-geometry/volume-form` | Reuse measure and volume foundations. |
| `differential-geometry/orientation-of-a-smooth-manifold`, `topology/isometry` | Reuse orientation and isometry foundations. |

False matches excluded: `fiber-bundles/bianchi-identity` is unrelated; `shared-foundations/lattice` is an order-theoretic lattice; weight/root lattices do not define Lie-group lattices; cuspidal representations do not define geometric cusps. Bianchi classification is the article's disambiguation link, not part of this batch.

## Article-centered additions (8 candidates)

These are proposed independently linkable owners extracted from the article's topics. Definitions should not depend on the later theorems about them.

| Candidate ID | Kind | Intended scope and direct dependencies |
| --- | --- | --- |
| `algebra-groups/bianchi-group` | definition | Define the group using an imaginary quadratic ring of integers and an explicit projective matrix convention. Depends on the number-theory entry layer and ring-valued SL/PSL definitions. |
| `differential-geometry/bianchi-orbifold` | definition | The quotient with its hyperbolic orbifold structure. Depends on Bianchi group, the existing hyperbolic action, and hyperbolic orbifold. |
| `lie-groups/bianchi-group-nonuniform-lattice` | theorem | Discreteness, finite covolume, and noncompact quotient. Depends on Bianchi group and a Lie-group lattice definition. |
| `differential-geometry/bianchi-cusp-ideal-class-correspondence` | theorem | Relate cusp orbits to ideal classes; state the cusp-count consequence here. Depends on cusp, Bianchi orbifold, ideal class group, and class number. |
| `differential-geometry/bianchi-orbifold-volume-formula` | theorem | State the volume result with the discriminant, zeta function, and metric/group normalization explicit. Depends on Bianchi orbifold, number-field discriminant, and Dedekind zeta. |
| `lie-groups/arithmetic-kleinian-group` | definition | Give an independent standard definition; do not define the term by the classification theorem that follows. Deeper prerequisite audit required before authorship. |
| `lie-groups/bianchi-group-arithmeticity` | theorem | Explain why these groups satisfy that definition. Depends on Bianchi group and arithmetic Kleinian group. |
| `lie-groups/noncocompact-arithmetic-kleinian-classification` | theorem | The article's commensurability-up-to-conjugacy statement. Verify the exact finite-covolume hypotheses against the cited monograph before writing. |

## Missing prerequisite targets (20 candidates)

These are proposed prerequisite additions based on the local coverage audit. Specializations earn separate knowls when they are useful named link targets; they should link to the existing general construction.

| Candidate ID | Purpose / dependencies |
| --- | --- |
| `shared-foundations/square-free-integer` | Clarify the parameter convention; use existing integer/divisibility foundations. |
| `algebra-fields-galois/imaginary-quadratic-field` | Define the particular number fields used here; link number field and square-free integer. A separate general quadratic-field knowl is optional. |
| `algebra-fields-galois/algebraic-integer` | Specialize integral element to the integers. |
| `algebra-fields-galois/ring-of-integers` | Own the ring construction; link number field, algebraic integer, and integral closure. |
| `algebra-fields-galois/imaginary-quadratic-ring-of-integers` | A theorem/computation giving the explicit ring by congruence class, with small examples. Supports concrete Bianchi examples. |
| `algebra-fields-galois/integral-basis` | Distinguish an integral basis from an arbitrary rational field basis. |
| `algebra-fields-galois/number-field-discriminant` | Apply the existing trace-pairing discriminant to an integral basis; distinguish the two meanings explicitly. |
| `algebra-commutative/fractional-ideal` | Own fractional ideals in a domain's fraction field; reuse ideal/module foundations. |
| `algebra-fields-galois/ideal-class-group` | Use nonzero fractional ideals modulo principal fractional ideals in a number field; include the class notation in this owner. |
| `algebra-fields-galois/class-number` | Own the cardinality invariant; link the ideal class group. |
| `algebra-fields-galois/ideal-norm` | Own the absolute norm of a nonzero integral ideal; do not redirect to field norm. |
| `algebra-fields-galois/dedekind-zeta-function` | Define the ideal Dirichlet series in its convergence half-plane. Analytic continuation is not needed for the initial volume statement. |
| `lie-groups/kleinian-group` | Extract the named discrete-subgroup concept already mentioned in the hyperbolic-space knowl. |
| `differential-geometry/orbifold` | A genuine local finite-quotient definition with compatibility, not merely “a singular manifold.” |
| `differential-geometry/hyperbolic-three-orbifold` | Own the geometric specialization; distinguish the orbifold structure from the underlying topological space. |
| `differential-geometry/horosphere` | Prepare the geometric cusp description; reuse the upper-half-space model. |
| `differential-geometry/hyperbolic-orbifold-cusp` | Define a cusp end with its quotient geometry; include the relation with boundary-point orbits. |
| `algebra-groups/commensurable-subgroups` | Define intersection of finite index in each subgroup and explain the additional conjugacy qualification. |
| `lie-groups/lattice-in-lie-group` | Finite invariant covolume for a discrete subgroup; reuse Haar measure and quotient vocabulary. |
| `lie-groups/uniform-lattice` | Own cocompactness, with nonuniform as its negation among lattices; avoid a duplicate nonuniform-lattice definition. |

## Two existing owners needing extension or a companion

1. **Special linear group:** introduce determinant-one matrices over a commutative ring. Decide whether to generalize the existing core and retain its Lie-group discussion as a specialization, or add `algebra-groups/special-linear-group-over-ring` with explicit cross-links. The current real/complex owner should remain a valid Lie-group prerequisite.
2. **Projective special linear group:** support the ring-of-integers case without conflating an abstract central quotient, a projective image, and points of an algebraic-group quotient. Prefer the concrete image inside the existing complex projective group for the initial Bianchi definition; decide whether that needs `algebra-groups/projective-special-linear-group-over-ring` or a carefully scoped extension of the existing owner.

Thus the working estimate is **28 new targets plus two existing-owner decisions**; companion knowls could bring it to 30. It is not a final batch size.

## Suggested writing order

1. **Definition and examples first:** square-free integer, imaginary quadratic field, algebraic integer, ring of integers, its explicit imaginary-quadratic computation, the two matrix-group decisions, and Bianchi group. Reuse the existing hyperbolic space and action immediately.
2. **Geometric quotient:** Kleinian group, orbifold, hyperbolic three-orbifold, Bianchi orbifold, lattice, uniform lattice, and the nonuniform-lattice theorem.
3. **Cusps and volume:** horosphere, cusp, fractional ideal, ideal class group, class number, integral basis, number-field discriminant, ideal norm, Dedekind zeta, and the two Bianchi-specific geometric theorems.
4. **Arithmetic classification last:** commensurability, arithmetic Kleinian group, arithmeticity, and classification. Audit the exact definition and its prerequisites before fixing this stage's size.

The first stage is a useful small initial batch on its own. Later results can be ordinary further-reading links without becoming prerequisites of the definition.

## Open editorial and verification questions

- The arithmetic stage may require quaternion algebras over number fields, orders, reduced norm/norm-one groups, embeddings, and ramification. The existing real quaternion division algebra is not sufficient coverage. Those are possible second-wave additions, not silently included in the 28-target estimate. Check the monograph's formulation first.
- A detailed cusp construction may justify a dedicated parabolic hyperbolic-isometry knowl. For an initial cusp definition via horoball quotients, define the required stabilizer condition explicitly and audit whether another owner is needed.
- Do not assume all torsion-bearing hyperbolic quotients are manifolds. Keep the orbifold structure visible even when its underlying space has a familiar topology.
- Match all eventual volume formulas and examples to one convention. Hatcher's linked illustration page explicitly uses **PGL**, whereas the Wikipedia article uses **PSL**. Those pictures cannot be transferred without checking the change of group and covolume.
- Do not use the article or this plan as evidence of a completed full mathematical review. Check exact theorem statements, hypotheses, and source locators when drafting. Run the ordinary content/dependency checks only after knowls are authored.

## Sources and follow-up verification

- [Wikipedia, Bianchi group, revision 1372725401](https://en.wikipedia.org/w/index.php?title=Bianchi_group&oldid=1372725401): read as the requested topic inventory, not as the sole final authority.
- [Allen Hatcher, Bianchi Orbifolds](https://pi.math.cornell.edu/~hatcher/bianchi.html): inspected the author's landing page; its PGL convention is explicit. Its linked report remains to be checked before importing examples.
- Maclachlan and Reid, *The Arithmetic of Hyperbolic 3-Manifolds* (2003), p. 58 as cited by the article: verification target for classification; not yet inspected for this plan.
- Use an authoritative algebraic-number-theory text for the new arithmetic prerequisites, and the hyperbolic-geometry references already cited by the existing geometry knowls. Record exact checked locators during authorship.
