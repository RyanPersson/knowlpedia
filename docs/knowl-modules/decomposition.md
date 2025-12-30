# Modular Knowl Decomposition

This document decomposes the source lists into focused modules. Items appearing in multiple modules are marked with occurrence counts. Highly shared items form the **shared pools**; focused modules are **additions** to the relevant shared pools.

---

## Shared Pools

### `shared-foundations` (×2+)
Basic set theory, logic, and function concepts used across all mathematics.

**Definitions:**
- ✓ Set (×2) → `set.md`
- ✓ Subset (×2) → `subset.md`
- ✓ Proper subset (×1, but foundational) → `proper-subset.md`
- ✓ Empty set (×1, but foundational) → `empty-set.md`
- ✓ Union (×1, but foundational) → `union.md`
- ✓ Intersection (×1, but foundational) → `intersection.md`
- ✓ Set difference (×1) → `set-difference.md`
- ✓ Complement (×1) → `complement.md`
- ✓ Cartesian product (×2) → `cartesian-product.md`
- ✓ Ordered pair (×1) → `ordered-pair.md`
- ✓ Partition of a set (×2) → `partition.md`
- ✓ Function (map) (×2) → `function.md`
- ✓ Composition of functions (×2) → `composition.md`
- ✓ Identity function (×1, but foundational) → `identity-function.md`
- ✓ Domain (×1) → `domain.md`
- ✓ Codomain (×1) → `codomain.md`
- ✓ Image of a function (×2) → `image.md`
- ✓ Preimage of a function (×2) → `preimage.md`
- ✓ Injective function (×2) → `injective-function.md`
- ✓ Surjective function (×2) → `surjective-function.md`
- ✓ Bijective function (×2) → `bijective-function.md`
- ✓ Inverse function (×1) → `inverse-function.md`
- ✓ Relation (×2) → `relation.md`
- ✓ Equivalence relation (×2) → `equivalence-relation.md`
- ✓ Equivalence class (×2) → `equivalence-class.md`
- ✓ Quotient set (×1) → `quotient-set.md`
- ✓ Partial order (poset) (×2) → `partial-order.md`
- ✓ Total order (linear order) (×2) → `total-order.md`
- ✓ Upper bound (×2) → `upper-bound.md`
- ✓ Lower bound (×2) → `lower-bound.md`
- ✓ Well-ordered set (×1) → `well-ordered-set.md`
- ✓ Cardinality (×1) → `cardinality.md`
- ✓ Countable set (×1) → `countable-set.md`
- ✓ Binary operation (×2) → `binary-operation.md`

**Axioms:**
- ✓ Zermelo–Fraenkel axioms with Choice (ZFC) (×1, but foundational) → `zfc-axioms.md`
- ✓ Axiom of Choice (×1) → `axiom-of-choice.md`
- ✓ Principle of mathematical induction (×1) → `mathematical-induction.md`

**Theorems:**
- ✓ Well-ordering theorem (×1) → `well-ordering-theorem.md`
- ✓ Well-ordering principle for ℕ (×1) → `well-ordering-principle.md`

**Lemmas:**
- ✓ Zorn's lemma (×1, but foundational across algebra) → `zorns-lemma.md`

---

### `shared-linear-algebra` (×2)
Vector spaces, linear maps, and matrix theory used in both analysis and algebra.

**Definitions:**
- ✓ Vector space (×2) → `vector-space.md`
- ✓ Linear map (×2) → `linear-map.md`
- ✓ Linear operator (×1) → `linear-operator.md`
- ✓ Eigenvalue (×1) → `eigenvalue.md`
- ✓ Eigenvector (×1) → `eigenvector.md`
- ✓ Eigenspace (×1) → `eigenspace.md`
- ✓ Determinant (×1) → `determinant.md`
- ✓ Trace (linear algebra) (×1) → `trace.md`
- ✓ Characteristic polynomial (×1) → `characteristic-polynomial.md`
- ✓ Minimal polynomial (linear operator) (×1) → `minimal-polynomial.md`
- ✓ Euclidean space ℝ^k (×1) → `euclidean-space.md`
- ✓ Euclidean norm (×1) → `euclidean-norm.md`
- ✓ Inner product on ℝ^k (×1) → `inner-product.md`
- ✓ Orthogonality (×1) → `orthogonality.md`
- ✓ Operator norm (×1) → `operator-norm.md`

**Theorems:**
- ✓ Cayley–Hamilton theorem (×1) → `cayley-hamilton-theorem.md`
- ✓ Rank–nullity theorem (×1) → `rank-nullity-theorem.md`
- ✓ Existence of a basis for every vector space (×1) → `basis-existence-theorem.md`

---

## Algebra Modules

### `algebra-groups`
Group theory through Sylow theorems and structure.

*Depends on:* `shared-foundations`

**Definitions:**
- ✓ Semigroup → `semigroup.md`
- ✓ Monoid → `monoid.md`
- ✓ Group → `group.md`
- ✓ Abelian group → `abelian-group.md`
- ✓ Subgroup → `subgroup.md`
- ✓ Trivial subgroup → `trivial-subgroup.md`
- ✓ Proper subgroup → `proper-subgroup.md`
- ✓ Cyclic subgroup → `cyclic-subgroup.md`
- ✓ Generated subgroup → `generated-subgroup.md`
- ✓ Normal subgroup → `normal-subgroup.md`
- ✓ Characteristic subgroup → `characteristic-subgroup.md`
- ✓ Simple group → `simple-group.md`
- ✓ Solvable group → `solvable-group.md`
- ✓ Nilpotent group → `nilpotent-group.md`
- ✓ Perfect group → `perfect-group.md`
- ✓ Center of a group → `center-of-group.md`
- ✓ Centralizer → `centralizer.md`
- ✓ Normalizer → `normalizer.md`
- ✓ Conjugate element → `conjugate-element.md`
- ✓ Conjugacy class → `conjugacy-class.md`
- ✓ Class function → `class-function.md`
- ✓ Commutator of elements → `commutator.md`
- ✓ Commutator subgroup (derived subgroup) → `commutator-subgroup.md`
- ✓ Derived series → `derived-series.md`
- ✓ Lower central series → `lower-central-series.md`
- ✓ Upper central series → `upper-central-series.md`
- ✓ p-group → `p-group.md`
- ✓ Sylow p-subgroup → `sylow-subgroup.md`
- ✓ Hall subgroup → `hall-subgroup.md`
- ✓ Composition series (group) → `composition-series-group.md`
- ✓ Subnormal series → `subnormal-series.md`
- ✓ Chief series → `chief-series.md`
- ✓ Group homomorphism → `group-homomorphism.md`
- ✓ Group monomorphism → `group-monomorphism.md`
- ✓ Group epimorphism → `group-epimorphism.md`
- ✓ Group isomorphism → `group-isomorphism.md`
- ✓ Kernel (group homomorphism) → `kernel-group.md`
- ✓ Image (group homomorphism) → `image-group.md`
- ✓ Coset (left/right) → `coset.md`
- ✓ Index of a subgroup → `index-of-subgroup.md`
- ✓ Quotient group → `quotient-group.md`
- ✓ Direct product of groups → `direct-product-groups.md`
- ✓ Direct sum of groups → `direct-sum-groups.md`
- ✓ Internal direct product → `internal-direct-product.md`
- ✓ Semidirect product → `semidirect-product.md`
- ✓ Internal semidirect product → `internal-semidirect-product.md`
- ✓ Group action → `group-action.md`
- ✓ Orbit → `orbit.md`
- ✓ Stabilizer → `stabilizer.md`
- ✓ Fixed-point set → `fixed-point-set.md`
- ✓ Kernel of an action → `kernel-of-action.md`
- ✓ Faithful action → `faithful-action.md`
- ✓ Free action → `free-action.md`
- ✓ Transitive action → `transitive-action.md`
- ✓ Regular action → `regular-action.md`
- ✓ Permutation representation → `permutation-representation.md`
- ✓ Conjugation action → `conjugation-action.md`
- ✓ Automorphism group → `automorphism-group.md`
- ✓ Inner automorphism → `inner-automorphism.md`
- ✓ Outer automorphism group → `outer-automorphism-group.md`
- ✓ Group presentation → `group-presentation.md`
- ✓ Generating set → `generating-set.md`
- ✓ Free group → `free-group.md`
- ✓ Normal closure → `normal-closure.md`
- ✓ Group extension → `group-extension.md`
- ✓ Split extension → `split-extension.md`
- ✓ Central extension → `central-extension.md`
- ✓ Exact sequence of groups → `exact-sequence-groups.md`

**Theorems:**
- ✓ First isomorphism theorem (groups) → `first-isomorphism-theorem-groups.md`
- ✓ Second isomorphism theorem (groups) → `second-isomorphism-theorem-groups.md`
- ✓ Third isomorphism theorem (groups) → `third-isomorphism-theorem-groups.md`
- ✓ Correspondence theorem (groups) → `correspondence-theorem-groups.md`
- ✓ Cayley's theorem → `cayleys-theorem.md`
- ✓ Lagrange's theorem → `lagranges-theorem.md`
- ✓ Cauchy's theorem (finite groups) → `cauchys-theorem-groups.md`
- ✓ Orbit–stabilizer theorem → `orbit-stabilizer-theorem.md`
- ✓ Class equation → `class-equation.md`
- ✓ Burnside's lemma → `burnsides-lemma.md`
- ✓ Sylow's first theorem → `sylows-first-theorem.md`
- ✓ Sylow's second theorem → `sylows-second-theorem.md`
- ✓ Sylow's third theorem → `sylows-third-theorem.md`
- ✓ Jordan–Hölder theorem (groups) → `jordan-holder-theorem-groups.md`
- ✓ Schreier refinement theorem → `schreier-refinement-theorem.md`
- ✓ Fundamental theorem of finitely generated abelian groups → `fundamental-theorem-fg-abelian-groups.md`
- ✓ Nielsen–Schreier theorem → `nielsen-schreier-theorem.md`
- ✓ Schur–Zassenhaus theorem → `schur-zassenhaus-theorem.md`
- ✓ Burnside's p^a q^b theorem → `burnsides-pq-theorem.md`
- ✓ Krull–Remak–Schmidt theorem (groups) → `krull-remak-schmidt-theorem-groups.md`

**Lemmas:**
- ✓ Subgroup test (one-step) → `subgroup-test-one-step.md`
- ✓ Subgroup test (two-step) → `subgroup-test-two-step.md`
- ✓ Normal subgroup criterion → `normal-subgroup-criterion.md`
- ✓ Subgroup of index 2 is normal → `index-2-normal.md`
- ✓ p-group has nontrivial center → `p-group-nontrivial-center.md`
- ✓ Orbit decomposition lemma → `orbit-decomposition-lemma.md`
- ✓ Conjugacy class size lemma → `conjugacy-class-size-lemma.md`
- ✓ Sylow conjugacy lemma → `sylow-conjugacy-lemma.md`
- ✓ Frattini argument → `frattini-argument.md`
- ✓ Schreier's lemma → `schreiers-lemma.md`
- ✓ Cosets partition a group → `cosets-partition.md`
- ✓ Universal property of quotient groups → `quotient-group-universal-property.md`
- ✓ Kernels are normal subgroups → `kernels-are-normal.md`

**Propositions:**
- ✓ Uniqueness of identity → `uniqueness-of-identity-group.md`
- ✓ Uniqueness of inverses → `uniqueness-of-inverses-group.md`
- ✓ Cancellation laws → `cancellation-laws-group.md`
- ✓ Subgroups closed under inverses and products → `subgroups-closed.md`
- ✓ Intersection of subgroups is a subgroup → `intersection-of-subgroups.md`
- ✓ Product of normal subgroups is normal → `product-of-normal-subgroups.md`
- ✓ Center is characteristic → `center-is-characteristic.md`
- ✓ Kernel is normal → `kernel-is-normal.md`
- ✓ Image is a subgroup → `image-is-subgroup.md`
- ✓ G/ker(f) ≅ im(f) → `first-isomorphism-consequence-groups.md`
- ✓ Conjugation preserves order → `conjugation-preserves-order.md`
- ✓ Subgroups of cyclic groups are cyclic → `subgroups-of-cyclic-are-cyclic.md`
- ✓ Finite cyclic group ≅ ℤ/nℤ → `finite-cyclic-isomorphic-zn.md`
- ✓ Aut(cyclic of order n) ≅ (ℤ/nℤ)× → `automorphism-group-cyclic.md`
- ✓ Group acts on itself by left multiplication → `left-multiplication-action.md`
- ✓ Group acts on itself by conjugation → `conjugation-action-self.md`
- ✓ Class equation decomposition → `class-equation-decomposition.md`
- ✓ |G| prime implies G cyclic → `prime-order-cyclic.md`
- ✓ |G| = p² implies G abelian → `p-squared-abelian.md`
- ✓ Abelian implies all subgroups normal → `abelian-all-subgroups-normal.md`
- ✓ Finite p-group has subgroups of every order p^k → `p-group-subgroups-all-orders.md`
- ✓ n_p = 1 implies Sylow p-subgroup is normal → `sylow-normal-criterion.md`
- ✓ Semidirect product from splitting exact sequence → `semidirect-product-splitting.md`

**Corollaries:**
- ✓ Fermat's little theorem → `fermats-little-theorem.md`
- ✓ Euler's theorem → `eulers-theorem.md`
- ✓ Order of element divides order of group → `order-divides-group-order.md`
- ✓ Finite p-group has nontrivial center → `p-group-nontrivial-center-corollary.md`
- ✓ n_p ≡ 1 mod p → `sylow-congruence.md`
- ✓ Classification of finite abelian groups → `classification-finite-abelian-groups.md`
- ✓ Jordan–Hölder uniqueness → `jordan-holder-uniqueness.md`

---

### `algebra-rings`
Ring theory and ideal structure.

*Depends on:* `shared-foundations`, `algebra-groups` (abelian groups)

**Definitions:**
- ✓ Ring → `ring.md`
- ✓ Ring with identity (unital ring) → `unital-ring.md`
- ✓ Commutative ring → `commutative-ring.md`
- ✓ Subring → `subring.md`
- ✓ Ring homomorphism → `ring-homomorphism.md`
- ✓ Ring monomorphism → `ring-monomorphism.md`
- ✓ Ring epimorphism → `ring-epimorphism.md`
- ✓ Ring isomorphism → `ring-isomorphism.md`
- ✓ Kernel (ring homomorphism) → `kernel-ring.md`
- ✓ Image (ring homomorphism) → `image-ring.md`
- ✓ Ideal (left/right) → `ideal.md`
- ✓ Two-sided ideal → `two-sided-ideal.md`
- ✓ Principal ideal → `principal-ideal.md`
- ✓ Ideal generated by a subset → `ideal-generated.md`
- ✓ Sum of ideals → `sum-of-ideals.md`
- ✓ Product of ideals → `product-of-ideals.md`
- ✓ Intersection of ideals → `intersection-of-ideals.md`
- ✓ Quotient ring → `quotient-ring.md`
- ✓ Unit (invertible element) → `unit.md`
- ✓ Group of units → `group-of-units.md`
- ✓ Zero divisor → `zero-divisor.md`
- ✓ Regular element → `regular-element.md`
- ✓ Nilpotent element → `nilpotent-element.md`
- ✓ Idempotent element → `idempotent-element.md`
- ✓ Reduced ring → `reduced-ring.md`
- ✓ Nil ideal → `nil-ideal.md`
- ✓ Nilradical → `nilradical.md`
- ✓ Jacobson radical → `jacobson-radical.md`
- ✓ Annihilator ideal → `annihilator-ideal.md`
- ✓ Prime ideal → `prime-ideal.md`
- ✓ Maximal ideal → `maximal-ideal.md`
- ✓ Radical of an ideal → `radical-of-ideal.md`
- ✓ Primary ideal → `primary-ideal.md`
- ✓ Integral domain → `integral-domain.md`
- ✓ Field → `field.md`
- ✓ Division ring (skew field) → `division-ring.md`
- ✓ Prime ring → `prime-ring.md`
- ✓ Simple ring → `simple-ring.md`
- ✓ Semiprime ideal → `semiprime-ideal.md`
- ✓ Semisimple ring → `semisimple-ring.md`
- ✓ Artinian semisimple ring → `artinian-semisimple-ring.md`
- ✓ Center of a ring → `center-of-ring.md`
- ✓ Opposite ring → `opposite-ring.md`
- ✓ Matrix ring → `matrix-ring.md`
- ✓ Characteristic of a ring/field → `characteristic.md`
- ✓ Polynomial ring → `polynomial-ring.md`
- ✓ Laurent polynomial ring → `laurent-polynomial-ring.md`
- ✓ Formal power series ring → `formal-power-series-ring.md`
- ✓ Content of a polynomial → `content-polynomial.md`
- ✓ Primitive polynomial → `primitive-polynomial.md`
- ✓ Irreducible polynomial → `irreducible-polynomial.md`
- ✓ Minimal polynomial (over a field) → `minimal-polynomial-field.md`
- ✓ Euclidean domain → `euclidean-domain.md`
- ✓ Principal ideal domain (PID) → `pid.md`
- ✓ Unique factorization domain (UFD) → `ufd.md`
- ✓ Prime element → `prime-element.md`
- ✓ Irreducible element → `irreducible-element.md`
- ✓ Associated elements → `associated-elements.md`
- ✓ Greatest common divisor → `gcd.md`
- ✓ Least common multiple → `lcm.md`
- ✓ Fraction field → `fraction-field.md`
- ✓ Total ring of fractions → `total-ring-of-fractions.md`

**Axioms:**
- ✓ Ring axioms → `ring-axioms.md`
- ✓ Unital ring axiom → `unital-ring-axiom.md`
- ✓ Commutative ring axiom → `commutative-ring-axiom.md`
- ✓ Field axioms → `field-axioms-algebra.md`

**Theorems:**
- ✓ First isomorphism theorem (rings) → `first-isomorphism-theorem-rings.md`
- ✓ Second isomorphism theorem (rings) → `second-isomorphism-theorem-rings.md`
- ✓ Third isomorphism theorem (rings) → `third-isomorphism-theorem-rings.md`
- ✓ Correspondence theorem (rings) → `correspondence-theorem-rings.md`
- ✓ Chinese remainder theorem → `chinese-remainder-theorem.md`
- ✓ Existence of maximal ideals (Zorn) → `existence-of-maximal-ideals.md`
- ✓ Wedderburn's little theorem → `wedderburns-little-theorem.md`
- ✓ Artin–Wedderburn theorem → `artin-wedderburn-theorem.md`
- ✓ Hilbert basis theorem → `hilbert-basis-theorem.md`
- ✓ Hilbert's Nullstellensatz (weak) → `nullstellensatz-weak.md`
- ✓ Hilbert's Nullstellensatz (strong) → `nullstellensatz-strong.md`
- ✓ Gauss's lemma (content) → `gauss-lemma.md`
- ✓ Eisenstein's criterion → `eisensteins-criterion.md`
- ✓ Unique factorization theorem → `unique-factorization-theorem.md`
- ✓ Euclidean domain ⇒ PID → `euclidean-implies-pid.md`
- ✓ PID ⇒ UFD → `pid-implies-ufd.md`
- ✓ Gauss's theorem (UFD ⇒ polynomial ring is UFD) → `ufd-polynomial-ring.md`

**Lemmas:**
- ✓ Gauss lemma (content multiplicativity) → `gauss-content-lemma.md`
- ✓ Maximal ideals are prime → `maximal-ideals-are-prime.md`
- ✓ Fields are exactly commutative division rings → `fields-are-division-rings.md`
- ✓ Maximal ideal iff quotient is field → `maximal-iff-quotient-field.md`
- ✓ Prime ideal iff quotient is integral domain → `prime-iff-quotient-domain.md`
- ✓ Universal property of quotient rings → `quotient-ring-universal-property.md`
- ✓ Kernels are two-sided ideals → `kernels-are-ideals.md`

**Propositions:**
- ✓ Ring homomorphisms preserve 0, 1, +, × → `ring-homomorphism-properties.md`
- ✓ Kernel is an ideal → `kernel-is-ideal.md`
- ✓ Image is a subring → `image-is-subring.md`
- ✓ Ideal correspondence (ideals containing I ↔ ideals of R/I) → `ideal-correspondence.md`
- ✓ Units map to units → `units-map-to-units.md`
- ✓ Commutative ring is field iff only ideals are (0) and (1) → `field-iff-trivial-ideals.md`
- ✓ Cancellation in integral domains → `cancellation-integral-domain.md`
- ✓ Characteristic of integral domain is 0 or prime → `characteristic-zero-or-prime.md`
- ✓ UFD implies GCDs exist → `ufd-implies-gcd-exists.md`
- ✓ Euclidean algorithm yields gcd and Bézout identity → `euclidean-algorithm.md`
- ✓ Content formula → `content-formula.md`
- ✓ Nilradical = intersection of prime ideals → `nilradical-intersection-primes.md`
- ✓ Idempotents ↔ product decompositions → `idempotent-product-decomposition.md`
- ✓ Chinese remainder decomposition (comaximal ideals) → `chinese-remainder-decomposition.md`

**Corollaries:**
- ✓ Every nontrivial commutative ring with 1 has a maximal ideal → `maximal-ideal-existence-corollary.md`
- ✓ Every field has prime subfield ≅ ℚ or 𝔽_p → `prime-subfield.md`
- ✓ Every finite integral domain is a field → `finite-integral-domain-is-field.md`
- ✓ Every finite division ring is commutative (Wedderburn) → `finite-division-ring-commutative.md`

---

### `algebra-modules`
Module theory over rings.

*Depends on:* `algebra-rings`, `shared-linear-algebra`

**Definitions:**
✓ - Module (left/right) → `module.md`
✓ - Bimodule → `bimodule.md`
✓ - Submodule → `submodule.md`
✓ - Quotient module → `quotient-module.md`
✓ - Module homomorphism → `module-homomorphism.md`
✓ - Kernel (module homomorphism) → `kernel-module.md`
✓ - Image (module homomorphism) → `image-module.md`
✓ - Cokernel (module) → `cokernel-module.md`
✓ - Exact sequence of modules → `exact-sequence-modules.md`
✓ - Short exact sequence → `short-exact-sequence.md`
✓ - Split exact sequence → `split-exact-sequence.md`
✓ - Direct sum of modules → `direct-sum-modules.md`
✓ - Direct product of modules → `direct-product-modules.md`
✓ - Cyclic module → `cyclic-module.md`
✓ - Finitely generated module → `finitely-generated-module.md`
✓ - Free module → `free-module.md`
✓ - Basis (of a free module) → `basis-module.md`
✓ - Rank (of a free module) → `rank-module.md`
✓ - Torsion element → `torsion-element.md`
✓ - Torsion module → `torsion-module.md`
✓ - Torsion-free module → `torsion-free-module.md`
✓ - Annihilator of an element → `annihilator-element.md`
✓ - Annihilator of a module → `annihilator-module.md`
✓ - Simple module → `simple-module.md`
✓ - Semisimple module → `semisimple-module.md`
✓ - Composition series (module) → `composition-series-module.md`
✓ - Length (Jordan–Hölder length) → `length-module.md`
✓ - Noetherian module → `noetherian-module.md`
✓ - Artinian module → `artinian-module.md`
✓ - Projective module → `projective-module.md`
✓ - Injective module → `injective-module.md`
✓ - Flat module → `flat-module.md`
✓ - Tensor product of modules → `tensor-product.md`
✓ - Bilinear map → `bilinear-map.md`
✓ - Universal property of tensor product → `tensor-product-universal-property.md`
✓ - Hom module → `hom-module.md`
✓ - Dual module → `dual-module.md`
✓ - Tensor–Hom adjunction data → `tensor-hom-adjunction.md`
✓ - Algebra over a commutative ring → `algebra-over-ring.md`
✓ - Algebra homomorphism → `algebra-homomorphism.md`
✓ - Tensor product of algebras → `tensor-product-algebras.md`
✓ - Graded ring → `graded-ring.md`
✓ - Graded module → `graded-module.md`
✓ - Filtered ring → `filtered-ring.md`
✓ - Associated graded ring → `associated-graded-ring.md`

**Axioms:**
✓ - Module axioms → `module-axioms.md`
✓ - Vector space axioms → `vector-space-axioms.md`

**Theorems:**
✓ - First isomorphism theorem (modules) → `first-isomorphism-theorem-modules.md`
✓ - Second isomorphism theorem (modules) → `second-isomorphism-theorem-modules.md`
✓ - Third isomorphism theorem (modules) → `third-isomorphism-theorem-modules.md`
✓ - Correspondence theorem (modules) → `correspondence-theorem-modules.md`
✓ - Structure theorem for f.g. modules over PID → `structure-theorem-pid.md`
✓ - Elementary divisor theorem → `elementary-divisor-theorem.md`
✓ - Smith normal form theorem → `smith-normal-form-theorem.md`
✓ - Rational canonical form theorem → `rational-canonical-form-theorem.md`
✓ - Jordan canonical form theorem → `jordan-canonical-form-theorem.md`
✓ - Krull–Schmidt–Azumaya theorem → `krull-schmidt-azumaya-theorem.md`

**Lemmas:**
✓ - Splitting lemma → `splitting-lemma.md`
✓ - Projective iff every s.e.s. ending in it splits → `projective-ses-criterion.md`
✓ - Projective is direct summand of free → `projective-summand-of-free.md`
✓ - Baer's criterion (injectivity) → `baers-criterion.md`
✓ - Tensor product preserves direct sums → `tensor-preserves-direct-sums.md`
✓ - Tensor–Hom adjunction lemma → `tensor-hom-adjunction-lemma.md`
✓ - Universal property of quotient modules → `quotient-module-universal-property.md`
✓ - Kernels are submodules → `kernels-are-submodules.md`

**Propositions:**
✓ - Submodule criterion → `submodule-criterion.md`
✓ - Kernel and image are submodules → `kernel-image-submodules.md`
✓ - M/ker(f) ≅ im(f) → `first-isomorphism-consequence-modules.md`
✓ - Exactness via kernels and images → `exactness-via-kernels-images.md`
✓ - Direct sum universal property → `direct-sum-universal-property.md`
✓ - Free module universal property → `free-module-universal-property.md`
✓ - Tensor product universal property → `tensor-product-universal-property-prop.md`
✓ - Tensor commutes with direct limits/sums → `tensor-commutes-with-sums.md`
✓ - Hom turns sums into products → `hom-sums-to-products.md`
✓ - Projective ⇒ flat → `projective-implies-flat.md`
✓ - f.g. projective are locally free → `fg-projective-locally-free.md`
✓ - Semisimple ⇔ every submodule is direct summand → `semisimple-direct-summand.md`
✓ - Artinian + Noetherian ⇒ finite length → `artinian-noetherian-finite-length.md`

**Corollaries:**
✓ - f.g. torsion-free over PID is free → `fg-torsion-free-pid-free.md`
✓ - Classification of f.g. abelian groups → `classification-fg-abelian-groups.md`
✓ - Rational canonical form from structure theorem → `rcf-from-structure-theorem.md`
✓ - Jordan canonical form from RCF → `jcf-from-rcf.md`
✓ - Smith normal form invariants → `smith-normal-form-invariants.md`
✓ - Chinese remainder for modules → `chinese-remainder-modules.md`

---

### `algebra-fields-galois`
Field extensions and Galois theory.

*Depends on:* `algebra-rings`, `algebra-groups`

**Definitions:**
✓ - Field extension → `field-extension.md`
✓ - Intermediate field → `intermediate-field.md`
✓ - Degree of a field extension → `degree-of-extension.md`
✓ - Simple field extension → `simple-extension.md`
✓ - Tower of fields → `tower-of-fields.md`
✓ - Algebraic element → `algebraic-element.md`
✓ - Transcendental element → `transcendental-element.md`
✓ - Algebraic extension → `algebraic-extension.md`
✓ - Transcendental extension → `transcendental-extension.md`
✓ - Finitely generated field extension → `fg-field-extension.md`
✓ - Splitting field → `splitting-field.md`
✓ - Algebraic closure → `algebraic-closure.md`
✓ - Normal extension → `normal-extension.md`
✓ - Separable element → `separable-element.md`
✓ - Separable extension → `separable-extension.md`
✓ - Inseparable extension → `inseparable-extension.md`
✓ - Perfect field → `perfect-field.md`
✓ - Galois extension → `galois-extension.md`
✓ - Galois group → `galois-group.md`
✓ - Fixed field → `fixed-field.md`
✓ - Field embedding → `field-embedding.md`
✓ - Field automorphism → `field-automorphism.md`
✓ - Trace (field extension) → `trace-field.md`
✓ - Norm (field extension) → `norm-field.md`
✓ - Discriminant (field extension) → `discriminant-field.md`
✓ - Finite field → `finite-field.md`
✓ - Frobenius endomorphism → `frobenius-endomorphism.md`
✓ - Cyclotomic polynomial → `cyclotomic-polynomial.md`
✓ - Primitive root of unity → `primitive-root-of-unity.md`
✓ - Cyclotomic extension → `cyclotomic-extension.md`

**Theorems:**
✓ - Tower law (degree formula) → `tower-law.md`
✓ - Existence and uniqueness of splitting fields → `splitting-field-existence-uniqueness.md`
✓ - Existence of algebraic closures → `algebraic-closure-existence.md`
✓ - Primitive element theorem → `primitive-element-theorem.md`
✓ - Fundamental theorem of symmetric polynomials → `fundamental-theorem-symmetric-polynomials.md`
✓ - Fundamental theorem of Galois theory → `fundamental-theorem-galois-theory.md`
✓ - Artin's theorem on fixed fields → `artins-theorem-fixed-fields.md`
✓ - Existence and uniqueness of finite fields → `finite-field-existence-uniqueness.md`
✓ - Cyclicity of multiplicative group of finite field → `finite-field-multiplicative-group-cyclic.md`
✓ - Galois group of finite field is cyclic (Frobenius) → `finite-field-galois-group-cyclic.md`

**Lemmas:**
✓ - Dedekind's independence lemma → `dedekind-independence-lemma.md`
✓ - Separable polynomial has distinct roots → `separable-distinct-roots.md`
✓ - Separability preserved under towers → `separability-towers.md`
✓ - Normality = being a splitting field → `normality-splitting-field.md`

**Propositions:**
✓ - Finite extension over perfect field is separable → `finite-extension-perfect-separable.md`
✓ - Finite fields are perfect → `finite-fields-perfect.md`
✓ - Separable + normal ⇔ Galois → `separable-normal-galois.md`
✓ - Trace/norm in towers → `trace-norm-towers.md`
✓ - Splitting field degree bounds → `splitting-field-degree-bounds.md`

**Corollaries:**
✓ - Uniqueness of splitting fields up to K-isomorphism → `splitting-field-uniqueness.md`
✓ - Uniqueness of algebraic closures → `algebraic-closure-uniqueness.md`
✓ - Galois correspondence (subgroups ↔ intermediate fields) → `galois-correspondence.md`
✓ - |Gal(L/K)| = [L:K] for Galois extensions → `galois-degree-equals-group-order.md`
✓ - Finite field Galois groups are cyclic → `finite-field-galois-cyclic.md`
✓ - Existence and uniqueness of 𝔽_{p^n} → `finite-field-existence.md`
✓ - Multiplicative group of finite field is cyclic → `finite-field-multiplicative-cyclic.md`

---

### `algebra-commutative`
Commutative algebra: localization, Noetherian rings, primary decomposition.

*Depends on:* `algebra-rings`, `algebra-modules`

**Definitions:**
- Localization of a ring → `localization-ring.md`
- Multiplicative set → `multiplicative-set.md`
- Localization at a prime ideal → `localization-at-prime.md`
- Local ring → `local-ring.md`
- Maximal ideal of a local ring → `maximal-ideal-local-ring.md`
- Residue field → `residue-field.md`
- Localization of a module → `localization-module.md`
- Extension of scalars → `extension-of-scalars.md`
- Restriction of scalars → `restriction-of-scalars.md`
- Prime spectrum (Spec R) → `prime-spectrum.md`
- Maximal spectrum (MaxSpec R) → `maximal-spectrum.md`
- Zariski topology → `zariski-topology.md`
- Krull dimension → `krull-dimension.md`
- Height of a prime ideal → `height-of-prime.md`
- Integral element (over a subring) → `integral-element.md`
- Integral extension → `integral-extension.md`
- Integral closure → `integral-closure.md`
- Integrally closed domain → `integrally-closed-domain.md`
- Primary decomposition (ideal-theoretic) → `primary-decomposition.md`
- Noetherian ring (ACC on ideals) → `noetherian-ring.md`
- Artinian ring (DCC on ideals) → `artinian-ring.md`
- Dedekind domain → `dedekind-domain.md`
- Discrete valuation ring (DVR) → `dvr.md`

**Theorems:**
- Correspondence of primes under localization → `localization-prime-correspondence.md`
- Krull's principal ideal theorem → `krull-principal-ideal-theorem.md`
- Lasker–Noether primary decomposition theorem → `lasker-noether-theorem.md`
- Going-up theorem → `going-up-theorem.md`
- Lying-over theorem → `lying-over-theorem.md`
- Going-down theorem → `going-down-theorem.md`
- Nullstellensatz (ideal–variety correspondence) → `nullstellensatz-variety-correspondence.md`

**Lemmas:**
- Localization inverts precisely the multiplicative set → `localization-inverts-multiplicative-set.md`
- Nakayama lemma → `nakayama-lemma.md`
- Prime avoidance lemma → `prime-avoidance-lemma.md`
- Noether normalization lemma → `noether-normalization-lemma.md`
- Jacobson radical = intersection of maximal ideals → `jacobson-radical-intersection-maximals.md`

**Propositions:**
- Localization is exact (flatness) → `localization-exact.md`
- Localization of Noetherian is Noetherian → `localization-noetherian.md`
- Localization preserves primality/maximality → `localization-preserves-primality.md`
- Jacobson radical annihilates simple modules → `jacobson-annihilates-simples.md`
- Simple Artinian = matrix ring over division ring → `simple-artinian-matrix-ring.md`
- Semisimple Artinian = product of matrix rings → `semisimple-artinian-product.md`

**Corollaries:**
- Every ideal in Noetherian ring has primary decomposition → `noetherian-primary-decomposition.md`
- Hilbert basis theorem corollary (k[x₁,...,x_n] Noetherian) → `hilbert-basis-corollary.md`
- Nullstellensatz corollary (radical ideals ↔ affine algebraic sets) → `nullstellensatz-corollary.md`
- Localization corollary (localizations of Noetherian are Noetherian) → `localization-noetherian-corollary.md`
- Nakayama corollary (M f.g., IM = M, I ⊆ Jac(R) ⇒ M = 0) → `nakayama-corollary.md`

---

### `algebra-homological`
Homological algebra: chain complexes, derived functors.

*Depends on:* `algebra-modules`, `algebra-category-theory`

**Definitions:**
- Chain complex → `chain-complex.md`
- Cochain complex → `cochain-complex.md`
- Chain map → `chain-map.md`
- Homotopy of chain maps → `chain-homotopy.md`
- Exact complex → `exact-complex.md`
- Homology module → `homology-module.md`
- Cohomology module → `cohomology-module.md`
- Projective resolution → `projective-resolution.md`
- Injective resolution → `injective-resolution.md`
- Derived functor → `derived-functor.md`
- Ext^n → `ext.md`
- Tor_n → `tor.md`
- Long exact sequence (of derived functors) → `long-exact-sequence-derived.md`

**Theorems:**
- Tensor product is right exact → `tensor-right-exact.md`
- Hom functor is left exact → `hom-left-exact.md`
- Long exact sequence of Tor → `long-exact-sequence-tor.md`
- Long exact sequence of Ext → `long-exact-sequence-ext.md`

**Lemmas:**
- Snake lemma → `snake-lemma.md`
- Five lemma → `five-lemma.md`
- Four lemma → `four-lemma.md`
- Nine lemma (3×3 lemma) → `nine-lemma.md`
- Horseshoe lemma → `horseshoe-lemma.md`
- Connecting homomorphism yields long exact sequence → `connecting-homomorphism-lemma.md`
- Ext and Tor are derived functors of Hom and ⊗ → `ext-tor-derived-functors.md`

**Propositions:**
- Exactness of Hom and ⊗ in short exact sequences → `hom-tensor-exactness.md`
- Projective resolutions exist → `projective-resolutions-exist.md`
- Injective resolutions exist → `injective-resolutions-exist.md`

**Corollaries:**
- Snake lemma corollary (long exact sequence from s.e.s. of chain complexes) → `snake-lemma-corollary.md`
- Five lemma corollary (isomorphism criterion) → `five-lemma-corollary.md`
- Ext^1 classifies extensions → `ext1-classifies-extensions.md`

---

### `algebra-representation-theory`
Representation theory of finite groups.

*Depends on:* `algebra-groups`, `algebra-modules`, `shared-linear-algebra`

**Definitions:**
- (Linear) representation of a group → `group-representation.md`
- Subrepresentation → `subrepresentation.md`
- Irreducible representation → `irreducible-representation.md`
- Completely reducible representation → `completely-reducible-representation.md`
- Group algebra → `group-algebra.md`
- Character of a representation → `character.md`
- Irreducible character → `irreducible-character.md`
- Induced representation → `induced-representation.md`
- Restricted representation → `restricted-representation.md`
- Regular representation → `regular-representation.md`

**Theorems:**
- Maschke's theorem → `maschkes-theorem.md`
- Character orthogonality relations → `character-orthogonality.md`

**Lemmas:**
- Schur's lemma → `schurs-lemma.md`

**Propositions:**
- Character of direct sum = sum of characters → `character-direct-sum.md`
- Character of tensor product = product of characters → `character-tensor-product.md`
- Number of irreducibles = number of conjugacy classes → `number-irreducibles-conjugacy-classes.md`
- Sum of squares of degrees = |G| → `sum-squares-degrees.md`

**Corollaries:**
- Maschke corollary (group algebra semisimple when char ∤ |G|) → `maschke-corollary.md`
- Complete reducibility over ℂ → `complete-reducibility-complex.md`
- Schur corollary (End of irreducible over ℂ is ℂ) → `schur-corollary.md`
- Orthogonality corollary (irreducible characters are orthonormal basis) → `character-orthonormality.md`

---

### `algebra-category-theory`
Category theory foundations.

*Depends on:* `shared-foundations`

**Definitions:**
- Category → `category.md`
- Object (of a category) → `object.md`
- Morphism (arrow) → `morphism.md`
- Composition (in a category) → `composition-category.md`
- Identity morphism → `identity-morphism.md`
- Isomorphism (in a category) → `isomorphism-category.md`
- Monomorphism → `monomorphism-category.md`
- Epimorphism → `epimorphism-category.md`
- Endomorphism (categorical) → `endomorphism-category.md`
- Automorphism (categorical) → `automorphism-category.md`
- Subcategory → `subcategory.md`
- Full subcategory → `full-subcategory.md`
- Opposite category → `opposite-category.md`
- Functor (covariant) → `functor.md`
- Contravariant functor → `contravariant-functor.md`
- Natural transformation → `natural-transformation.md`
- Natural isomorphism → `natural-isomorphism.md`
- Equivalence of categories → `equivalence-of-categories.md`
- Product (categorical) → `categorical-product.md`
- Coproduct → `coproduct.md`
- Equalizer → `equalizer.md`
- Coequalizer → `coequalizer.md`
- Pullback (fiber product) → `pullback.md`
- Pushout → `pushout.md`
- Limit → `limit.md`
- Colimit → `colimit.md`
- Representable functor → `representable-functor.md`
- Yoneda embedding → `yoneda-embedding.md`
- Adjoint functors → `adjoint-functors.md`
- Unit of an adjunction → `unit-adjunction.md`
- Counit of an adjunction → `counit-adjunction.md`
- Additive category → `additive-category.md`
- Kernel (categorical) → `kernel-categorical.md`
- Cokernel (categorical) → `cokernel-categorical.md`
- Exact sequence (in an additive/abelian category) → `exact-sequence-categorical.md`
- Abelian category → `abelian-category.md`
- Left exact functor → `left-exact-functor.md`
- Right exact functor → `right-exact-functor.md`
- Exact functor → `exact-functor.md`

**Axioms:**
- Category axioms → `category-axioms.md`
- Axioms of an abelian category → `abelian-category-axioms.md`

**Lemmas:**
- Yoneda lemma → `yoneda-lemma.md`

---

## Module Dependency Graph

```
shared-foundations
    │
    ├── shared-linear-algebra
    │       │
    │       ├── analysis-multivariable
    │       ├── convex-analysis
    │       ├── algebra-modules
    │       └── algebra-representation-theory
    │
    ├── analysis-order-completeness
    │       │
    │       └── analysis-metric-topology
    │               │
    │               ├── analysis-sequences-series
    │               │       │
    │               │       └── analysis-continuity
    │               │               │
    │               │               └── analysis-compactness-connectedness
    │               │                       │
    │               │                       ├── analysis-differentiation-1d
    │               │                       │       │
    │               │                       │       └── analysis-riemann-integration
    │               │                       │               │
    │               │                       │               └── analysis-function-sequences
    │               │                       │
    │               │                       └── analysis-multivariable
    │               │
    │               ├── convex-analysis
    │               │
    │               └── (topology courses would branch here)
    │
    ├── algebra-groups
    │       │
    │       ├── algebra-fields-galois
    │       └── algebra-representation-theory
    │
    ├── algebra-rings
    │       │
    │       ├── algebra-modules
    │       │       │
    │       │       ├── algebra-commutative
    │       │       ├── algebra-homological
    │       │       └── algebra-representation-theory
    │       │
    │       └── algebra-fields-galois
    │
    └── algebra-category-theory
            │
            └── algebra-homological
```

---
