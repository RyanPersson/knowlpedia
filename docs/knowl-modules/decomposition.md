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

## Analysis Modules

### `analysis-order-completeness`
The ordered field structure of ℝ and completeness properties.

*Depends on:* `shared-foundations`

**Definitions:**
- ✓ Supremum (least upper bound) → `supremum.md`
- ✓ Infimum (greatest lower bound) → `infimum.md`
- ✓ Maximum → `maximum.md`
- ✓ Minimum → `minimum.md`
- ✓ Bounded above → `bounded-above.md`
- ✓ Bounded below → `bounded-below.md`
- ✓ Bounded set (in an ordered set) → `bounded-set.md`
- ✓ Real numbers ℝ (as a complete ordered field) → `real-numbers-r.md`
- ✓ Complex numbers ℂ → `complex-numbers-c.md`
- ✓ Complex conjugate → `complex-conjugate.md`
- ✓ Absolute value on ℝ → `absolute-value-on-r.md`
- ✓ Modulus (absolute value) on ℂ → `modulus-on-c.md`

**Axioms:**
- ✓ Field axioms (for ℝ, ℂ) → `field-axioms.md`
- ✓ Order axioms (for ℝ as an ordered field) → `order-axioms.md`
- ✓ Completeness axiom of ℝ (least upper bound / supremum property) → `completeness-axiom-of-r.md`

**Theorems:**
- ✓ Least upper bound theorem → `least-upper-bound-theorem.md`
- ✓ Greatest lower bound theorem → `greatest-lower-bound-theorem.md`
- ✓ Archimedean property of ℝ → `archimedean-property-of-r.md`
- ✓ Density of ℚ in ℝ → `density-of-q-in-r.md`
- ✓ Density of ℝ \ ℚ in ℝ → `density-of-r-minus-q-in-r.md`
- ✓ Nested interval theorem → `nested-interval-theorem.md`

**Lemmas:**
- ✓ Supremum approximation lemma → `supremum-approximation-lemma.md`

**Propositions:**
- ✓ Uniqueness of supremum and infimum → `uniqueness-of-supremum-infimum.md`
- ✓ Basic algebraic properties of sup and inf → `algebraic-properties-sup-inf.md`
- ✓ Completeness equivalences → `completeness-equivalences.md`

---

### `analysis-metric-topology`
Metric spaces and point-set topology in the metric context.

*Depends on:* `shared-foundations`, `analysis-order-completeness`

**Definitions:**
- ✓ Distance (metric) → `metric.md`
- ✓ Metric space → `metric-space.md`
- ✓ Open ball → `open-ball.md`
- ✓ Closed ball → `closed-ball.md`
- ✓ Sphere (metric sphere) → `sphere-metric-sphere.md`
- ✓ Neighborhood → `neighborhood.md`
- ✓ Open set (in a metric space) → `open-set.md`
- ✓ Closed set (in a metric space) → `closed-set.md`
- ✓ Interior of a set → `interior.md`
- ✓ Closure of a set → `closure.md`
- ✓ Boundary of a set → `boundary.md`
- ✓ Limit point (accumulation point) → `limit-point-accumulation-point-cluster-point.md`
- ✓ Isolated point → `isolated-point.md`
- ✓ Derived set → `derived-set.md`
- ✓ Dense subset → `dense-subset.md`
- ✓ Diameter of a set → `diameter.md`
- Bounded set (in a metric space) → `bounded-set-metric.md`

**Theorems:**
- ✓ Open sets form a topology → `open-sets-form-a-topology.md`
- ✓ Closed sets are complements of open sets → `closed-sets-are-complements-of-open-sets.md`
- ✓ Sequential characterization of closure → `sequential-characterization-of-closure.md`
- ✓ Sequential characterization of closed sets → `sequential-characterization-of-closed-sets.md`

**Lemmas:**
- ✓ Triangle inequality → `triangle-inequality.md`
- ✓ Reverse triangle inequality → `reverse-triangle-inequality.md`

---

### `analysis-sequences-series`
Sequences, series, and convergence in ℝ and ℝ^k.

*Depends on:* `analysis-order-completeness`, `analysis-metric-topology`

**Definitions:**
- ✓ Convergent sequence → `convergent-sequence.md`
- ✓ Limit of a sequence → `limit-of-a-sequence.md`
- ✓ Bounded sequence → `bounded-sequence.md`
- ✓ Monotone sequence → `monotone-sequence.md`
- ✓ Subsequence → `subsequence.md`
- ✓ Limit superior (lim sup) → `limit-superior-lim-sup.md`
- ✓ Limit inferior (lim inf) → `limit-inferior-lim-inf.md`
- ✓ Cauchy sequence → `cauchy-sequence.md`
- ✓ Complete metric space → `complete-metric-space.md`
- ✓ Summable family / series → `series.md`
- ✓ Partial sums → `partial-sums.md`
- ✓ Convergent series → `convergent-series.md`
- ✓ Divergent series → `divergent-series.md`
- ✓ Absolutely convergent series → `absolutely-convergent-series.md`
- ✓ Conditionally convergent series → `conditionally-convergent-series.md`
- ✓ Rearrangement of a series → `rearrangement-of-a-series.md`
- ✓ Cauchy product → `cauchy-product.md`

**Theorems:**
- ✓ Monotone convergence theorem (sequences) → `monotone-convergence-theorem.md`
- ✓ Cauchy criterion for convergence → `cauchy-criterion-for-convergence-in-rk.md`
- ✓ Bolzano–Weierstrass theorem → `bolzano-weierstrass-theorem.md`
- ✓ Algebra of limits for sequences → `algebra-of-limits-for-sequences.md`
- ✓ Squeeze theorem → `squeeze-theorem.md`
- ✓ Absolute convergence implies convergence → `absolute-convergence-implies-convergence.md`
- ✓ Comparison test → `comparison-test.md`
- ✓ Limit comparison test → `limit-comparison-test.md`
- ✓ Ratio test → `ratio-test.md`
- ✓ Root test → `root-test.md`
- ✓ Integral test → `integral-test.md`
- ✓ Cauchy condensation test → `cauchy-condensation-test.md`
- ✓ Alternating series test → `alternating-series-test.md`
- ✓ Dirichlet test → `dirichlet-test.md`
- ✓ Abel test → `abel-test.md`
- ✓ Rearrangement theorem (absolutely convergent) → `rearrangement-theorem-for-absolutely-convergent-series.md`
- ✓ Riemann rearrangement theorem → `riemann-rearrangement-theorem.md`
- ✓ Mertens theorem → `mertens-theorem-on-cauchy-products.md`

**Lemmas:**
- ✓ Monotone subsequence lemma → `monotone-subsequence-lemma.md`
- ✓ Basic properties of lim sup and lim inf → `basic-properties-of-lim-sup-and-lim-inf.md`
- ✓ Uniqueness of limits → `uniqueness-of-limits.md`
- ✓ A convergent sequence is Cauchy → `convergent-sequence-is-cauchy.md`
- ✓ Every Cauchy sequence is bounded → `every-cauchy-sequence-is-bounded.md`

**Corollaries:**
- ✓ Every bounded sequence in ℝ^k has a convergent subsequence → `bounded-sequence-has-convergent-subsequence.md`
- ✓ A convergent series has terms tending to 0 → `convergent-series-terms-go-to-zero.md`

---

### `analysis-continuity`
Limits and continuity of functions.

*Depends on:* `analysis-metric-topology`, `analysis-sequences-series`

**Definitions:**
- ✓ Limit of a function at a point (ε–δ) → `limit-of-a-function-at-a-point.md`
- ✓ One-sided limit → `one-sided-limit.md`
- ✓ Limit at infinity → `limit-of-a-function-at-infinity.md`
- ✓ Continuity at a point → `continuity-at-a-point.md`
- ✓ Continuity on a set → `continuity-on-a-set.md`
- ✓ Uniform continuity → `uniform-continuity.md`
- ✓ Lipschitz continuity → `lipschitz-continuity.md`
- ✓ Hölder continuity → `holder-continuity.md`
- ✓ Isometry → `isometry.md`
- ✓ Homeomorphism → `homeomorphism.md`

**Theorems:**
- ✓ Continuity via sequences → `continuity-via-sequences.md`
- ✓ Continuity via open sets → `continuity-via-open-sets.md`

**Propositions:**
- ✓ Equivalent definitions of continuity → `equivalent-definitions-continuity.md`
- ✓ Uniform continuity implies continuity → `uniform-continuity-implies-continuity.md`
- ✓ Uniform continuity preserves Cauchy sequences → `uniform-continuity-preserves-cauchy.md`

---

### `analysis-compactness-connectedness`
Compactness and connectedness in metric spaces.

*Depends on:* `analysis-metric-topology`, `analysis-continuity`

**Definitions:**
- ✓ Compact set (open-cover) → `compact-set.md`
- ✓ Sequentially compact set → `sequentially-compact-set.md`
- ✓ Totally bounded set → `totally-bounded-set.md`
- ✓ Connected set → `connected-set.md`
- ✓ Separated sets → `separated-sets.md`
- ✓ Component (connected component) → `connected-component.md`
- ✓ Path → `path.md`
- ✓ Path-connected set → `path-connected-set.md`
- ✓ Interval (in ℝ) → `interval.md`
- ✓ Curve (parametrized curve) → `curve.md`
- ✓ Nowhere dense set → `nowhere-dense-set.md`
- ✓ Meager set → `meager-set.md`
- ✓ Residual set → `residual-set.md`

**Theorems:**
- ✓ Sequential compactness equals compactness (metric spaces) → `sequential-compactness-equals-compactness.md`
- ✓ Finite intersection property theorem → `finite-intersection-property-theorem.md`
- ✓ Lebesgue number lemma → `lebesgue-number-lemma.md`
- ✓ Compactness implies completeness → `compactness-implies-completeness.md`
- ✓ Compactness implies total boundedness → `compactness-implies-total-boundedness.md`
- ✓ Continuous image of compact set is compact → `continuous-image-of-compact-set-is-compact.md`
- ✓ Extreme value theorem → `extreme-value-theorem.md`
- ✓ Heine–Cantor theorem → `heine-cantor-theorem.md`
- ✓ Continuous bijection from compact to metric space is homeomorphism → `continuous-bijection-from-compact-homeomorphism-criterion.md`
- ✓ Heine–Borel theorem → `heine-borel-theorem.md`
- ✓ Continuous image of connected set is connected → `continuous-image-of-connected-set-is-connected.md`
- ✓ Connected subsets of ℝ are intervals → `connected-subsets-of-r-are-intervals.md`
- ✓ Intermediate value theorem → `intermediate-value-theorem.md`
- ✓ Cantor intersection theorem → `cantor-intersection-theorem.md`
- ✓ Baire category theorem → `baire-category-theorem.md`

**Lemmas:**
- ✓ Compactness implies boundedness → `compactness-implies-boundedness.md`
- ✓ Compactness implies closedness → `compactness-implies-closedness.md`
- ✓ Closed subset of compact is compact → `closed-subset-of-compact-set-is-compact.md`

**Corollaries:**
- ✓ Continuous function on compact is bounded → `continuous-on-compact-is-bounded.md`
- ✓ Continuous function on compact attains max and min → `continuous-attains-max-min-compact.md`
- ✓ Continuous function on compact is uniformly continuous → `heine-cantor-corollary.md`

---

### `analysis-differentiation-1d`
One-variable differentiation.

*Depends on:* `analysis-continuity`

**Definitions:**
- ✓ Differentiability at a point → `differentiability-one-variable.md`
- ✓ Difference quotient → `difference-quotient.md`
- ✓ Derivative → `derivative.md`
- ✓ Right/left derivative → `right-derivative-left-derivative.md`
- ✓ Higher derivatives → `higher-derivatives.md`
- ✓ Class C^k function → `class-ck-function-one-variable.md`
- ✓ Critical point → `critical-point.md`
- ✓ Local maximum / local minimum → `local-maximum-local-minimum.md`
- ✓ Global maximum / global minimum → `global-maximum-global-minimum.md`
- ✓ Taylor polynomial → `taylor-polynomial.md`
- ✓ Remainder term in Taylor's theorem → `remainder-term-in-taylors-theorem.md`

**Theorems:**
- ✓ Rolle's theorem → `rolles-theorem.md`
- ✓ Mean value theorem (Lagrange) → `mean-value-theorem.md`
- ✓ Cauchy mean value theorem → `cauchy-mean-value-theorem.md`
- ✓ Fixed sign of derivative implies monotonicity → `fixed-sign-of-derivative-implies-monotonicity.md`
- ✓ Taylor's theorem with remainder → `taylors-theorem-with-remainder.md`
- ✓ Darboux theorem → `darboux-theorem.md`
- ✓ Inverse function theorem (1D) → `inverse-function-theorem-one-variable.md`
- ✓ L'Hôpital's rule → `lhopitals-rule.md`

**Propositions:**
- ✓ Differentiability rules (linearity, product, quotient, chain) → `differentiation-rules-one-variable.md`
- ✓ Derivative zero implies constant → `derivative-zero-implies-constant.md`
- ✓ Bounded derivative implies uniformly continuous → `bounded-derivative-implies-uniform-continuity.md`

**Corollaries:**
- ✓ f′ > 0 implies strictly increasing → `positive-derivative-strictly-increasing.md`
- ✓ f′ = 0 implies constant → `zero-derivative-constant-corollary.md`

---

### `analysis-riemann-integration`
Riemann and Riemann–Stieltjes integration.

*Depends on:* `analysis-differentiation-1d`, `analysis-compactness-connectedness`

**Definitions:**
- ✓ Step function → `step-function.md`
- ✓ Partition of an interval → `partition-of-an-interval.md`
- ✓ Refinement → `refinement-of-a-partition.md`
- ✓ Mesh (norm) of partition → `mesh-of-a-partition.md`
- ✓ Upper sum / Lower sum → `upper-sum-riemann.md` and `lower-sum-riemann.md`
- ✓ Tagged partition → `tagged-partition.md`
- ✓ Riemann sum → `riemann-sum.md`
- ✓ Riemann integrable function → `riemann-integrable-function.md`
- ✓ Riemann integral → `riemann-integral.md`
- ✓ Oscillation of a function → `oscillation-of-a-function.md`
- ✓ Set of measure zero → `set-of-measure-zero-in-rk.md`
- ✓ Content (Jordan content) → `jordan-content.md`
- ✓ Riemann–Stieltjes integral → `riemann-stieltjes-integral.md`
- ✓ Integrator function → `integrator-function.md`

**Theorems:**
- ✓ Existence of Riemann integral for continuous functions → `existence-of-riemann-integral-for-continuous-functions.md`
- ✓ Riemann integrability of monotone functions → `riemann-integrability-of-monotone-functions.md`
- ✓ Riemann integrability with finitely many discontinuities → `riemann-integrability-of-functions-with-finitely-many-discontinuities.md`
- ✓ Lebesgue criterion for Riemann integrability → `lebesgue-criterion-for-riemann-integrability.md`
- ✓ Mean value theorem for integrals → `mean-value-theorem-for-integrals.md`
- ✓ Fundamental theorem of calculus (Part I) → `fundamental-theorem-of-calculus-part-i.md`
- ✓ Fundamental theorem of calculus (Part II) → `fundamental-theorem-of-calculus-part-ii.md`
- ✓ Substitution rule → `substitution-rule-for-one-variable-riemann-integrals.md`
- ✓ Riemann–Stieltjes integrability theorem → `riemann-stieltjes-integrability-theorem.md`
- ✓ Integration by parts (R-S) → `integration-by-parts-riemann-stieltjes.md`

**Lemmas:**
- ✓ Refinement lemma for upper/lower sums → `refinement-lemma-upper-lower-sums.md`
- ✓ Oscillation criterion lemma → `oscillation-criterion-lemma.md`
- ✓ Additivity and linearity lemmas → `additivity-linearity-riemann-integral.md`

**Propositions:**
- ✓ Riemann integrability implies boundedness → `riemann-integrability-implies-boundedness.md`
- ✓ |f| integrable if f integrable → `absolute-value-preserves-integrability.md`
- ✓ Closure properties (sums, products) → `algebra-of-riemann-integrable-functions.md`

**Corollaries:**
- ✓ FTC corollary: integration differentiates antiderivatives → `newton-leibniz-formula.md`

---

### `analysis-function-sequences`
Sequences and series of functions, uniform convergence, power series.

*Depends on:* `analysis-riemann-integration`, `analysis-compactness-connectedness`

**Definitions:**
- ✓ Pointwise convergence → `pointwise-convergence.md`
- ✓ Uniform convergence → `uniform-convergence-of-a-sequence-of-functions.md`
- ✓ Uniform Cauchy sequence of functions → `uniform-cauchy-sequence-of-functions.md`
- ✓ Uniform convergence on compact sets → `uniform-convergence-on-compact-sets.md`
- ✓ Series of functions → `series-of-functions.md`
- ✓ Equicontinuity (family of functions) → `equicontinuity.md`

**Theorems:**
- ✓ Uniform limit theorem for continuity → `uniform-limit-theorem-for-continuity.md`
- ✓ Weierstrass M-test → `weierstrass-m-test.md`
- ✓ Uniform convergence and integration theorem → `uniform-convergence-and-integration-theorem.md`
- ✓ Uniform convergence and differentiation theorem → `uniform-convergence-and-differentiation-theorem.md`
- ✓ Dini's theorem → `dinis-theorem.md`
- ✓ Weierstrass approximation theorem → `weierstrass-approximation-theorem.md`
- ✓ Stone–Weierstrass theorem → `stone-weierstrass-theorem.md`
- ✓ Cauchy–Hadamard theorem (radius of convergence) → `cauchy-hadamard-theorem.md`
- ✓ Uniform convergence of power series on compact subsets → `uniform-convergence-of-power-series-on-compact-subsets.md`
- ✓ Term-by-term differentiation of power series → `term-by-term-differentiation-of-power-series.md`
- ✓ Term-by-term integration of power series → `term-by-term-integration-of-power-series.md`
- ✓ Abel's theorem → `abels-theorem.md`

**Lemmas:**
- ✓ Uniform convergence implies uniform Cauchy → `uniform-convergence-implies-uniform-cauchy.md`
- ✓ Uniform Cauchy implies uniform convergence (complete codomain) → `uniform-cauchy-implies-uniform-convergence.md`
- ✓ Uniform convergence preserves boundedness → `uniform-convergence-preserves-boundedness.md`

**Corollaries:**
- ✓ Uniform convergence implies pointwise convergence → `uniform-convergence-implies-pointwise.md`
- ✓ Uniform limit of continuous functions is continuous → `uniform-limit-of-continuous-is-continuous.md`
- ✓ Power series are analytic on disk of convergence → `power-series-analytic-on-disk.md`

---

### `analysis-multivariable`
Multivariable differentiation and integration.

*Depends on:* `shared-linear-algebra`, `analysis-differentiation-1d`, `analysis-riemann-integration`

**Definitions:**
- ✓ Partial derivative → `partial-derivative.md`
- ✓ Mixed partial derivative → `mixed-partial-derivative.md`
- ✓ Directional derivative → `directional-derivative.md`
- ✓ Gradient → `gradient.md`
- ✓ Jacobian matrix → `jacobian-matrix.md`
- ✓ Jacobian determinant → `jacobian-determinant.md`
- ✓ Hessian matrix → `hessian-matrix.md`
- ✓ Total derivative (Fréchet derivative) → `total-derivative-frechet-derivative.md`
- ✓ Differentiable map (ℝ^k → ℝ^m) → `differentiable-map.md`
- ✓ Class C^k map → `class-ck-map.md`
- ✓ Diffeomorphism → `diffeomorphism.md`
- ✓ Implicitly defined function → `implicitly-defined-function.md`
- ✓ Regular point / critical point → `regular-point-critical-point-multivariable.md`
- ✓ Regular value / critical value → `regular-value-critical-value-multivariable.md`
- ✓ Multiple integral over a rectangle → `multiple-riemann-integral-over-a-rectangle.md`
- ✓ Iterated integral → `iterated-integral.md`
- ✓ Change of variables → `change-of-variables-for-multiple-integrals.md`
- ✓ Constraint set → `constraint-set.md`
- ✓ Lagrange multiplier condition → `lagrange-multiplier-condition.md`

**Theorems:**
- ✓ Differentiability implies continuity (multivariable) → `differentiability-implies-continuity.md`
- ✓ Chain rule (multivariable) → `chain-rule-multivariable.md`
- ✓ Mean value inequality → `mean-value-inequality-multivariable.md`
- ✓ C^1 implies differentiable → `sufficient-condition-for-differentiability.md`
- ✓ Schwarz (Clairaut) theorem → `schwarz-clairaut-theorem.md`
- ✓ Taylor's theorem (several variables) → `taylors-theorem-in-several-variables.md`
- ✓ Inverse function theorem (ℝ^k) → `inverse-function-theorem-rk.md`
- ✓ Implicit function theorem → `implicit-function-theorem.md`
- ✓ Fubini theorem (Riemann) → `fubini-theorem-for-riemann-integrals.md`
- ✓ Change of variables formula → `change-of-variables-formula-for-multiple-integrals.md`
- ✓ Lagrange multipliers theorem → `lagrange-multipliers-theorem.md`

**Lemmas:**
- ✓ Mean value estimate lemma → `mean-value-estimate-lemma.md`
- Determinant nonvanishing implies local invertibility → `determinant-local-invertibility.md`

**Corollaries:**
- ✓ Equality of mixed partials under C^2 → `c2-implies-equal-mixed-partials.md`
- ✓ Local diffeomorphism corollary → `local-diffeomorphism-corollary.md`
- ✓ Implicit function parameterization corollary → `local-implicit-function-parameterization.md`

---

### `convex-analysis`
Convex sets, convex functions, separation theorems, and Hahn–Banach theory in normed spaces.

*Depends on:* `shared-foundations`, `shared-linear-algebra`, `analysis-metric-topology`

**Definitions (Vector Spaces & Operators):**
- ✓ Vector space → `vector-space.md`
- ✓ Linear subspace → `linear-subspace.md`
- ✓ Linear combination → `linear-combination.md`
- ✓ Linearly independent/dependent sets → `linearly-independent-and-linearly-dependent-sets.md`
- ✓ Span (subspace generated by a set) → `subspace-generated-by-a-set-span.md`
- ✓ Basis (Hamel basis) → `basis-hamel-basis-and-dimension.md`
- ✓ Direct sum of subspaces → `direct-sum-of-subspaces.md`
- ✓ Linear operator (linear transformation) → `linear-operator-linear-transformation.md`
- ✓ Image and kernel of a linear map → `image-and-kernel-linear-isomorphism.md`
- ✓ Self-adjoint linear operator → `self-adjoint-linear-operator.md`
- ✓ Nonnegative (positive semidefinite) operator → `nonnegative-positive-semidefinite-operator.md`
- ✓ Codimension → `codimension.md`
- ✓ Quotient vector space → `quotient-vector-space-codimension.md`

**Definitions (Normed Spaces & Topology):**
- ✓ Norm, normed vector space → `norm-normed-vector-space.md`
- ✓ Metric, metric space → `metric-metric-space.md`
- ✓ Open and closed balls → `open-and-closed-balls-in-a-metric-space.md`
- ✓ Open subset → `open-subset.md`
- ✓ Closed subset → `closed-subset.md`
- ✓ Interior of a set → `interior-of-a-set.md`
- ✓ Closure of a set → `closure-of-a-set.md`
- ✓ Bounded set, bounded sequence → `bounded-set-and-bounded-sequence.md`
- ✓ Balanced and absorbing sets → `balanced-and-absorbing-sets.md`
- ✓ Distance function to a set → `distance-function-to-a-set.md`
- ✓ Product space (Cartesian product) → `product-space-cartesian-product.md`

**Definitions (Sequences & Completeness):**
- ✓ Convergence of a sequence → `convergence-of-a-sequence.md`
- ✓ Convergence in normed spaces → `convergence-in-normed-spaces.md`
- ✓ Cauchy sequence → `cauchy-sequence.md`
- ✓ Subsequence → `subsequence.md`
- ✓ Complete metric space, complete subset → `complete-metric-space-complete-subset.md`

**Definitions (Affine Sets & Hyperplanes):**
- ✓ Line segment in a vector space → `line-segments-in-a-vector-space.md`
- ✓ Line connecting two points → `line-connecting-two-points.md`
- ✓ Affine set → `affine-set.md`
- ✓ Affine hull, affine combination → `affine-hull-affine-combination.md`
- ✓ Parallel affine set → `parallel-affine-set.md`
- ✓ Affine mapping → `affine-mapping.md`
- ✓ Hyperplane → `hyperplane.md`

**Definitions (Convex Sets):**
- ✓ Convex set → `convex-set.md`
- ✓ Convex combination → `convex-combination.md`
- ✓ Convex hull → `convex-hull.md`
- ✓ Set-valued mapping (multifunction) → `set-valued-mapping-multifunction-domain-and-graph-convex-set-valued-mapping.md`

**Definitions (Algebraic Interior & Linear Closure):**
- ✓ Algebraic interior (core) → `algebraic-interior-core.md`
- ✓ Linear closure → `linear-closure.md`

**Definitions (Convex Functions):**
- ✓ Extended real number system → `extended-real-number-system-and-conventions.md`
- ✓ Domain and epigraph, proper function → `domain-and-epigraph-proper-function.md`
- ✓ Convex function (via epigraph) → `convex-function-via-epigraph.md`
- ✓ Strictly convex function → `strictly-convex-function.md`
- ✓ Quasiconvex function → `quasiconvex-function.md`
- ✓ Indicator function of a set → `indicator-function-of-a-set.md`
- ✓ Marginal (optimal value) function → `marginal-optimal-value-function.md`

**Definitions (Minkowski Functional & Seminorms):**
- ✓ Minkowski function (gauge) of a set → `minkowski-function-gauge-of-a-set.md`
- ✓ Subadditive, positively homogeneous, sublinear functions → `subadditive-positively-homogeneous-and-sublinear-functions.md`
- ✓ Seminorm → `seminorm.md`

**Definitions (Duality):**
- ✓ Bounded linear functional, norm of a functional → `bounded-linear-functional-norm-of-a-functional.md`
- ✓ Dual space and duality pairing → `dual-space-and-duality-pairing.md`

**Theorems:**
- ✓ Norm induces a metric (and conversely) → `norm-induces-a-metric-and-conversely.md`
- ✓ Existence of a basis (Hamel basis) → `existence-of-a-basis-hamel-basis.md`
- ✓ Extension of a linearly independent set to a basis → `extension-of-a-linearly-independent-set-to-a-basis.md`
- ✓ Isomorphism theorem and dimension formula → `isomorphism-theorem-and-dimension-formula-for-linear-operators.md`
- ✓ Completeness of ℝ^k → `completeness-of-rk.md`
- ✓ Affine sets are translates of subspaces → `affine-sets-are-translates-of-subspaces.md`
- ✓ Hyperplanes are level sets of nonzero linear functionals → `hyperplanes-are-level-sets-of-nonzero-linear-functionals.md`
- ✓ Convex hull is the smallest convex set containing → `convex-hull-is-the-smallest-convex-set-containing.md`
- ✓ Convex hull via convex combinations → `convex-hull-via-convex-combinations.md`
- ✓ Interior and closure of a convex set are convex → `interior-and-closure-of-a-convex-set-are-convex.md`
- ✓ Core equals interior for convex sets in normed spaces → `core-equals-interior-for-convex-sets-in-normed-spaces.md`
- ✓ Equivalent characterizations of convex functions → `equivalent-characterizations-of-convex-functions.md`
- ✓ Convexity characterized by monotonicity of derivative → `convexity-characterized-by-monotonicity-of-derivative.md`
- ✓ Convexity via nonnegative second derivative → `convexity-via-nonnegative-second-derivative.md`
- ✓ Convexity characterized by positive semidefinite Hessian → `convexity-characterized-by-positive-semidefinite-hessian.md`
- ✓ Convexity of the marginal optimal value function → `convexity-of-the-marginal-optimal-value-function.md`
- ✓ Hahn–Banach theorem (real vector spaces) → `hahn-banach-theorem-in-real-vector-spaces.md`
- ✓ Hahn–Banach extension dominated by a seminorm (real case) → `hahn-banach-extension-dominated-by-a-seminorm-real-case.md`
- ✓ Hahn–Banach theorem (complex vector spaces) → `hahn-banach-theorem-in-complex-vector-spaces.md`
- ✓ Hahn–Banach theorem (normed spaces) → `hahn-banach-theorem-in-normed-spaces.md`
- ✓ Separation of a point from a convex set via the core → `separation-of-a-point-from-a-convex-set-via-the-core.md`
- ✓ Separation of two convex sets via the core condition → `separation-of-two-convex-sets-via-the-core-condition.md`
- ✓ Separation by a closed hyperplane → `separation-by-a-closed-hyperplane.md`
- ✓ Strict separation with an open convex set → `strict-separation-with-an-open-convex-set.md`
- ✓ Strict separation by a closed hyperplane → `strict-separation-by-a-closed-hyperplane.md`
- ✓ Strict separation of compact and closed convex sets → `strict-separation-of-compact-and-closed-convex-sets.md`

**Lemmas:**
- ✓ Subspace test (closure under addition and scalar multiplication) → `subspace-test-closure-under-addition-and-scalar-multiplication.md`
- ✓ Basis characterized by maximal linear independence → `basis-characterized-by-maximal-linear-independence.md`
- ✓ Characterization of direct sums → `characterization-of-direct-sums.md`
- ✓ Reverse triangle inequality → `reverse-triangle-inequality.md`
- ✓ Convergent sequences are bounded → `convergent-sequences-are-bounded.md`
- ✓ Convergent sequences are Cauchy → `convergent-sequences-are-cauchy.md`
- ✓ Cauchy sequences are bounded → `cauchy-sequences-are-bounded.md`
- ✓ Cauchy sequence with a convergent subsequence converges → `cauchy-sequence-with-a-convergent-subsequence-converges.md`
- ✓ Subsequences of convergent sequences converge to the same limit → `subsequences-of-convergent-sequences-converge-to-the-same-limit.md`
- ✓ Characterization of affine mappings → `characterization-of-affine-mappings.md`
- ✓ Convex sets characterized by closure under convex combinations → `convex-sets-characterized-by-closure-under-convex-combinations.md`
- ✓ Segments from interior points stay in the interior → `segments-from-interior-points-stay-in-the-interior.md`
- ✓ Segments from core points stay in the core → `segments-from-core-points-stay-in-the-core.md`
- ✓ Core characterized by absorbing translations → `core-characterized-by-absorbing-translations.md`
- ✓ Core of a convex set is convex → `core-of-a-convex-set-is-convex.md`
- ✓ Idempotence of the core operator → `idempotence-of-the-core-operator.md`
- ✓ Linear closure of a convex set is convex → `linear-closure-of-a-convex-set-is-convex.md`
- ✓ Linear closure equals closure for solid convex sets → `linear-closure-equals-closure-for-solid-convex-sets.md`
- ✓ Slope inequalities for convex functions → `slope-inequalities-for-convex-functions.md`
- ✓ Properties of the Minkowski functional of a convex set → `properties-of-the-minkowski-functional-of-a-convex-set.md`
- ✓ Continuity and level sets of the Minkowski functional → `continuity-and-level-sets-of-the-minkowski-functional.md`
- ✓ Kernel of a nonzero linear functional has codimension one → `kernel-of-a-nonzero-linear-functional-has-codimension-one.md`
- ✓ Codimension one subspaces yield direct sum decompositions → `codimension-one-subspaces-yield-direct-sum-decompositions.md`
- ✓ Auxiliary separation lemma for disjoint convex sets with nonempty core → `auxiliary-separation-lemma-for-disjoint-convex-sets-with-nonempty-core.md`
- ✓ Continuity of linear functionals via closed level sets → `continuity-of-linear-functionals-via-closed-level-sets.md`

**Propositions:**
- ✓ Span equals the set of all finite linear combinations → `span-equals-the-set-of-all-finite-linear-combinations.md`
- ✓ Intersection of subspaces is a subspace → `intersection-of-subspaces-is-a-subspace.md`
- ✓ Sum of subspaces equals span of the union → `sum-of-subspaces-equals-span-of-the-union.md`
- ✓ Images and preimages of subspaces under linear operators → `images-and-preimages-of-subspaces-under-linear-operators.md`
- ✓ Basic properties of open sets → `basic-properties-of-open-sets.md`
- ✓ Basic properties of closed sets → `basic-properties-of-closed-sets.md`
- ✓ Basic properties of the interior operator → `basic-properties-of-the-interior-operator.md`
- ✓ Basic properties of the closure operator → `basic-properties-of-the-closure-operator.md`
- ✓ Open balls are open sets → `open-balls-are-open-sets.md`
- ✓ Closed balls are closed sets → `closed-balls-are-closed-sets.md`
- ✓ Interior characterized by existence of a ball → `interior-characterized-by-existence-of-a-ball.md`
- ✓ Closure characterized by ball intersections → `closure-characterized-by-ball-intersections.md`
- ✓ Closure characterized by convergent sequences → `closure-characterized-by-convergent-sequences.md`
- ✓ Closed sets characterized by sequences → `closed-sets-characterized-by-sequences-version-i.md`
- ✓ Uniqueness of limits in metric spaces → `uniqueness-of-limits-in-metric-spaces.md`
- ✓ Uniqueness of limits and boundedness in normed spaces → `uniqueness-of-limits-and-boundedness-in-normed-spaces.md`
- ✓ Convergence implies convergence of norms → `convergence-implies-convergence-of-norms.md`
- ✓ Algebra of limits in normed spaces → `algebra-of-limits-in-normed-spaces.md`
- ✓ Completeness implies closedness; closed subsets of complete spaces are complete → `completeness-implies-closedness-closed-subsets-of-complete-spaces-are-complete.md`
- ✓ Properties of affine sets and affine hulls → `properties-of-affine-sets-and-affine-hulls.md`
- ✓ Parallel subspace to an affine set → `parallel-subspace-to-an-affine-set-is.md`
- ✓ Affine images and preimages of convex sets are convex → `affine-images-and-preimages-of-convex-sets-are-convex.md`
- ✓ Intersections of convex sets are convex → `intersections-of-convex-sets-are-convex.md`
- ✓ Sums and scalar multiples of convex sets are convex → `sums-and-scalar-multiples-of-convex-sets-are-convex.md`
- ✓ Cartesian product of convex sets is convex → `cartesian-product-of-convex-sets-is-convex.md`
- ✓ Interior and closure relations for convex sets with nonempty interior → `interior-and-closure-relations-for-convex-sets-with-nonempty-interior.md`
- ✓ Closure of intersections under interior point condition → `closure-of-intersections-under-interior-point-condition.md`
- ✓ Convexity on a convex subset via extension → `convexity-on-a-convex-subset-via-extension.md`
- ✓ Domain of a convex function is convex → `domain-of-a-convex-function-is-convex.md`
- ✓ Quasiconvexity characterized by convex sublevel sets → `quasiconvexity-characterized-by-convex-sublevel-sets.md`
- ✓ Basic operations preserving convexity → `basic-operations-preserving-convexity.md`
- ✓ Convexity preserved under monotone convex composition → `convexity-preserved-under-monotone-convex-composition.md`
- ✓ Convexity preserved under affine composition → `convexity-preserved-under-affine-composition.md`
- ✓ Supremum of convex functions is convex → `supremum-of-convex-functions-is-convex.md`
- ✓ Separation by a hyperplane → `separation-by-a-hyperplane.md`
- ✓ Separation by hyperplanes via sup/inf inequality → `separation-by-hyperplanes-via-supinf-inequality.md`
- ✓ Separation of a point and a subspace → `separation-of-a-point-and-a-subspace.md`
- ✓ Complex separation theorem (real parts) → `complex-separation-theorem-real-parts.md`
- ✓ Separation by closed hyperplane under interior condition → `separation-by-closed-hyperplane-under-interior-condition.md`
- ✓ Existence of a functional attaining its norm at a point → `existence-of-a-functional-attaining-its-norm-at-a-point.md`

**Corollaries:**
- ✓ Young's inequality → `youngs-inequality.md`
- ✓ Weighted arithmetic–geometric mean inequality → `weighted-arithmeticgeometric-mean-inequality.md`
- ✓ Hölder inequality (finite sums) → `holder-inequality-finite-sums.md`
- ✓ Hölder inequality (integrals) → `holder-inequality-integrals.md`

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
- Ring → `ring.md`
- Ring with identity (unital ring) → `unital-ring.md`
- Commutative ring → `commutative-ring.md`
- Subring → `subring.md`
- Ring homomorphism → `ring-homomorphism.md`
- Ring monomorphism → `ring-monomorphism.md`
- Ring epimorphism → `ring-epimorphism.md`
- Ring isomorphism → `ring-isomorphism.md`
- Kernel (ring homomorphism) → `kernel-ring.md`
- Image (ring homomorphism) → `image-ring.md`
- Ideal (left/right) → `ideal.md`
- Two-sided ideal → `two-sided-ideal.md`
- Principal ideal → `principal-ideal.md`
- Ideal generated by a subset → `ideal-generated.md`
- Sum of ideals → `sum-of-ideals.md`
- Product of ideals → `product-of-ideals.md`
- Intersection of ideals → `intersection-of-ideals.md`
- Quotient ring → `quotient-ring.md`
- Unit (invertible element) → `unit.md`
- Group of units → `group-of-units.md`
- Zero divisor → `zero-divisor.md`
- Regular element → `regular-element.md`
- Nilpotent element → `nilpotent-element.md`
- Idempotent element → `idempotent-element.md`
- Reduced ring → `reduced-ring.md`
- Nil ideal → `nil-ideal.md`
- Nilradical → `nilradical.md`
- Jacobson radical → `jacobson-radical.md`
- Annihilator ideal → `annihilator-ideal.md`
- Prime ideal → `prime-ideal.md`
- Maximal ideal → `maximal-ideal.md`
- Radical of an ideal → `radical-of-ideal.md`
- Primary ideal → `primary-ideal.md`
- Integral domain → `integral-domain.md`
- Field → `field.md`
- Division ring (skew field) → `division-ring.md`
- Prime ring → `prime-ring.md`
- Simple ring → `simple-ring.md`
- Semiprime ideal → `semiprime-ideal.md`
- Semisimple ring → `semisimple-ring.md`
- Artinian semisimple ring → `artinian-semisimple-ring.md`
- Center of a ring → `center-of-ring.md`
- Opposite ring → `opposite-ring.md`
- Matrix ring → `matrix-ring.md`
- Characteristic of a ring/field → `characteristic.md`
- Polynomial ring → `polynomial-ring.md`
- Laurent polynomial ring → `laurent-polynomial-ring.md`
- Formal power series ring → `formal-power-series-ring.md`
- Content of a polynomial → `content-polynomial.md`
- Primitive polynomial → `primitive-polynomial.md`
- Irreducible polynomial → `irreducible-polynomial.md`
- Minimal polynomial (over a field) → `minimal-polynomial-field.md`
- Euclidean domain → `euclidean-domain.md`
- Principal ideal domain (PID) → `pid.md`
- Unique factorization domain (UFD) → `ufd.md`
- Prime element → `prime-element.md`
- Irreducible element → `irreducible-element.md`
- Associated elements → `associated-elements.md`
- Greatest common divisor → `gcd.md`
- Least common multiple → `lcm.md`
- Fraction field → `fraction-field.md`
- Total ring of fractions → `total-ring-of-fractions.md`

**Axioms:**
- Ring axioms → `ring-axioms.md`
- Unital ring axiom → `unital-ring-axiom.md`
- Commutative ring axiom → `commutative-ring-axiom.md`
- Field axioms → `field-axioms-algebra.md`

**Theorems:**
- First isomorphism theorem (rings) → `first-isomorphism-theorem-rings.md`
- Second isomorphism theorem (rings) → `second-isomorphism-theorem-rings.md`
- Third isomorphism theorem (rings) → `third-isomorphism-theorem-rings.md`
- Correspondence theorem (rings) → `correspondence-theorem-rings.md`
- Chinese remainder theorem → `chinese-remainder-theorem.md`
- Existence of maximal ideals (Zorn) → `existence-of-maximal-ideals.md`
- Wedderburn's little theorem → `wedderburns-little-theorem.md`
- Artin–Wedderburn theorem → `artin-wedderburn-theorem.md`
- Hilbert basis theorem → `hilbert-basis-theorem.md`
- Hilbert's Nullstellensatz (weak) → `nullstellensatz-weak.md`
- Hilbert's Nullstellensatz (strong) → `nullstellensatz-strong.md`
- Gauss's lemma (content) → `gauss-lemma.md`
- Eisenstein's criterion → `eisensteins-criterion.md`
- Unique factorization theorem → `unique-factorization-theorem.md`
- Euclidean domain ⇒ PID → `euclidean-implies-pid.md`
- PID ⇒ UFD → `pid-implies-ufd.md`
- Gauss's theorem (UFD ⇒ polynomial ring is UFD) → `ufd-polynomial-ring.md`

**Lemmas:**
- Gauss lemma (content multiplicativity) → `gauss-content-lemma.md`
- Maximal ideals are prime → `maximal-ideals-are-prime.md`
- Fields are exactly commutative division rings → `fields-are-division-rings.md`
- Maximal ideal iff quotient is field → `maximal-iff-quotient-field.md`
- Prime ideal iff quotient is integral domain → `prime-iff-quotient-domain.md`
- Universal property of quotient rings → `quotient-ring-universal-property.md`
- Kernels are two-sided ideals → `kernels-are-ideals.md`

**Propositions:**
- Ring homomorphisms preserve 0, 1, +, × → `ring-homomorphism-properties.md`
- Kernel is an ideal → `kernel-is-ideal.md`
- Image is a subring → `image-is-subring.md`
- Ideal correspondence (ideals containing I ↔ ideals of R/I) → `ideal-correspondence.md`
- Units map to units → `units-map-to-units.md`
- Commutative ring is field iff only ideals are (0) and (1) → `field-iff-trivial-ideals.md`
- Cancellation in integral domains → `cancellation-integral-domain.md`
- Characteristic of integral domain is 0 or prime → `characteristic-zero-or-prime.md`
- UFD implies GCDs exist → `ufd-implies-gcd-exists.md`
- Euclidean algorithm yields gcd and Bézout identity → `euclidean-algorithm.md`
- Content formula → `content-formula.md`
- Nilradical = intersection of prime ideals → `nilradical-intersection-primes.md`
- Idempotents ↔ product decompositions → `idempotent-product-decomposition.md`
- Chinese remainder decomposition (comaximal ideals) → `chinese-remainder-decomposition.md`

**Corollaries:**
- Every nontrivial commutative ring with 1 has a maximal ideal → `maximal-ideal-existence-corollary.md`
- Every field has prime subfield ≅ ℚ or 𝔽_p → `prime-subfield.md`
- Every finite integral domain is a field → `finite-integral-domain-is-field.md`
- Every finite division ring is commutative (Wedderburn) → `finite-division-ring-commutative.md`

---

### `algebra-modules`
Module theory over rings.

*Depends on:* `algebra-rings`, `shared-linear-algebra`

**Definitions:**
- Module (left/right) → `module.md`
- Bimodule → `bimodule.md`
- Submodule → `submodule.md`
- Quotient module → `quotient-module.md`
- Module homomorphism → `module-homomorphism.md`
- Kernel (module homomorphism) → `kernel-module.md`
- Image (module homomorphism) → `image-module.md`
- Cokernel (module) → `cokernel-module.md`
- Exact sequence of modules → `exact-sequence-modules.md`
- Short exact sequence → `short-exact-sequence.md`
- Split exact sequence → `split-exact-sequence.md`
- Direct sum of modules → `direct-sum-modules.md`
- Direct product of modules → `direct-product-modules.md`
- Cyclic module → `cyclic-module.md`
- Finitely generated module → `finitely-generated-module.md`
- Free module → `free-module.md`
- Basis (of a free module) → `basis-module.md`
- Rank (of a free module) → `rank-module.md`
- Torsion element → `torsion-element.md`
- Torsion module → `torsion-module.md`
- Torsion-free module → `torsion-free-module.md`
- Annihilator of an element → `annihilator-element.md`
- Annihilator of a module → `annihilator-module.md`
- Simple module → `simple-module.md`
- Semisimple module → `semisimple-module.md`
- Composition series (module) → `composition-series-module.md`
- Length (Jordan–Hölder length) → `length-module.md`
- Noetherian module → `noetherian-module.md`
- Artinian module → `artinian-module.md`
- Projective module → `projective-module.md`
- Injective module → `injective-module.md`
- Flat module → `flat-module.md`
- Tensor product of modules → `tensor-product.md`
- Bilinear map → `bilinear-map.md`
- Universal property of tensor product → `tensor-product-universal-property.md`
- Hom module → `hom-module.md`
- Dual module → `dual-module.md`
- Tensor–Hom adjunction data → `tensor-hom-adjunction.md`
- Algebra over a commutative ring → `algebra-over-ring.md`
- Algebra homomorphism → `algebra-homomorphism.md`
- Tensor product of algebras → `tensor-product-algebras.md`
- Graded ring → `graded-ring.md`
- Graded module → `graded-module.md`
- Filtered ring → `filtered-ring.md`
- Associated graded ring → `associated-graded-ring.md`

**Axioms:**
- Module axioms → `module-axioms.md`
- Vector space axioms → `vector-space-axioms.md`

**Theorems:**
- First isomorphism theorem (modules) → `first-isomorphism-theorem-modules.md`
- Second isomorphism theorem (modules) → `second-isomorphism-theorem-modules.md`
- Third isomorphism theorem (modules) → `third-isomorphism-theorem-modules.md`
- Correspondence theorem (modules) → `correspondence-theorem-modules.md`
- Structure theorem for f.g. modules over PID → `structure-theorem-pid.md`
- Elementary divisor theorem → `elementary-divisor-theorem.md`
- Smith normal form theorem → `smith-normal-form-theorem.md`
- Rational canonical form theorem → `rational-canonical-form-theorem.md`
- Jordan canonical form theorem → `jordan-canonical-form-theorem.md`
- Krull–Schmidt–Azumaya theorem → `krull-schmidt-azumaya-theorem.md`

**Lemmas:**
- Splitting lemma → `splitting-lemma.md`
- Projective iff every s.e.s. ending in it splits → `projective-ses-criterion.md`
- Projective is direct summand of free → `projective-summand-of-free.md`
- Baer's criterion (injectivity) → `baers-criterion.md`
- Tensor product preserves direct sums → `tensor-preserves-direct-sums.md`
- Tensor–Hom adjunction lemma → `tensor-hom-adjunction-lemma.md`
- Universal property of quotient modules → `quotient-module-universal-property.md`
- Kernels are submodules → `kernels-are-submodules.md`

**Propositions:**
- Submodule criterion → `submodule-criterion.md`
- Kernel and image are submodules → `kernel-image-submodules.md`
- M/ker(f) ≅ im(f) → `first-isomorphism-consequence-modules.md`
- Exactness via kernels and images → `exactness-via-kernels-images.md`
- Direct sum universal property → `direct-sum-universal-property.md`
- Free module universal property → `free-module-universal-property.md`
- Tensor product universal property → `tensor-product-universal-property-prop.md`
- Tensor commutes with direct limits/sums → `tensor-commutes-with-sums.md`
- Hom turns sums into products → `hom-sums-to-products.md`
- Projective ⇒ flat → `projective-implies-flat.md`
- f.g. projective are locally free → `fg-projective-locally-free.md`
- Semisimple ⇔ every submodule is direct summand → `semisimple-direct-summand.md`
- Artinian + Noetherian ⇒ finite length → `artinian-noetherian-finite-length.md`

**Corollaries:**
- f.g. torsion-free over PID is free → `fg-torsion-free-pid-free.md`
- Classification of f.g. abelian groups → `classification-fg-abelian-groups.md`
- Rational canonical form from structure theorem → `rcf-from-structure-theorem.md`
- Jordan canonical form from RCF → `jcf-from-rcf.md`
- Smith normal form invariants → `smith-normal-form-invariants.md`
- Chinese remainder for modules → `chinese-remainder-modules.md`

---

### `algebra-fields-galois`
Field extensions and Galois theory.

*Depends on:* `algebra-rings`, `algebra-groups`

**Definitions:**
- Field extension → `field-extension.md`
- Intermediate field → `intermediate-field.md`
- Degree of a field extension → `degree-of-extension.md`
- Simple field extension → `simple-extension.md`
- Tower of fields → `tower-of-fields.md`
- Algebraic element → `algebraic-element.md`
- Transcendental element → `transcendental-element.md`
- Algebraic extension → `algebraic-extension.md`
- Transcendental extension → `transcendental-extension.md`
- Finitely generated field extension → `fg-field-extension.md`
- Splitting field → `splitting-field.md`
- Algebraic closure → `algebraic-closure.md`
- Normal extension → `normal-extension.md`
- Separable element → `separable-element.md`
- Separable extension → `separable-extension.md`
- Inseparable extension → `inseparable-extension.md`
- Perfect field → `perfect-field.md`
- Galois extension → `galois-extension.md`
- Galois group → `galois-group.md`
- Fixed field → `fixed-field.md`
- Field embedding → `field-embedding.md`
- Field automorphism → `field-automorphism.md`
- Trace (field extension) → `trace-field.md`
- Norm (field extension) → `norm-field.md`
- Discriminant (field extension) → `discriminant-field.md`
- Finite field → `finite-field.md`
- Frobenius endomorphism → `frobenius-endomorphism.md`
- Cyclotomic polynomial → `cyclotomic-polynomial.md`
- Primitive root of unity → `primitive-root-of-unity.md`
- Cyclotomic extension → `cyclotomic-extension.md`

**Theorems:**
- Tower law (degree formula) → `tower-law.md`
- Existence and uniqueness of splitting fields → `splitting-field-existence-uniqueness.md`
- Existence of algebraic closures → `algebraic-closure-existence.md`
- Primitive element theorem → `primitive-element-theorem.md`
- Fundamental theorem of symmetric polynomials → `fundamental-theorem-symmetric-polynomials.md`
- Fundamental theorem of Galois theory → `fundamental-theorem-galois-theory.md`
- Artin's theorem on fixed fields → `artins-theorem-fixed-fields.md`
- Existence and uniqueness of finite fields → `finite-field-existence-uniqueness.md`
- Cyclicity of multiplicative group of finite field → `finite-field-multiplicative-group-cyclic.md`
- Galois group of finite field is cyclic (Frobenius) → `finite-field-galois-group-cyclic.md`

**Lemmas:**
- Dedekind's independence lemma → `dedekind-independence-lemma.md`
- Separable polynomial has distinct roots → `separable-distinct-roots.md`
- Separability preserved under towers → `separability-towers.md`
- Normality = being a splitting field → `normality-splitting-field.md`

**Propositions:**
- Finite extension over perfect field is separable → `finite-extension-perfect-separable.md`
- Finite fields are perfect → `finite-fields-perfect.md`
- Separable + normal ⇔ Galois → `separable-normal-galois.md`
- Trace/norm in towers → `trace-norm-towers.md`
- Splitting field degree bounds → `splitting-field-degree-bounds.md`

**Corollaries:**
- Uniqueness of splitting fields up to K-isomorphism → `splitting-field-uniqueness.md`
- Uniqueness of algebraic closures → `algebraic-closure-uniqueness.md`
- Galois correspondence (subgroups ↔ intermediate fields) → `galois-correspondence.md`
- |Gal(L/K)| = [L:K] for Galois extensions → `galois-degree-equals-group-order.md`
- Finite field Galois groups are cyclic → `finite-field-galois-cyclic.md`
- Existence and uniqueness of 𝔽_{p^n} → `finite-field-existence.md`
- Multiplicative group of finite field is cyclic → `finite-field-multiplicative-cyclic.md`

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

## Additional Knowls (not yet categorized)

These knowls exist in the content directories but are not listed in the module definitions above.

### `analysis` (additional)

**Definitions:**
- ✓ Baire space → `baire-space.md`
- ✓ Characteristic function (indicator function) → `characteristic-function-indicator-function.md`
- ✓ Contraction mapping → `contraction-mapping.md`
- ✓ Dense set → `dense-set.md`
- ✓ Equicontinuous family → `equicontinuous-family.md`
- ✓ Euclidean space ℝ^k → `euclidean-space-rk.md`
- ✓ Fixed point → `fixed-point.md`
- ✓ Indexed family of sets → `indexed-family-of-sets.md`
- ✓ Inner product on ℝ^k → `inner-product-on-rk.md`
- ✓ Pointwise bounded family → `pointwise-bounded-family.md`
- ✓ Power set → `power-set.md`
- ✓ Relatively compact set → `relatively-compact-set.md`
- ✓ Restriction of a function → `restriction-of-a-function.md`
- ✓ Symmetric difference → `symmetric-difference.md`
- ✓ Uniformly bounded family → `uniformly-bounded-family.md`

**Theorems:**
- ✓ Arzelà–Ascoli theorem → `arzela-ascoli-theorem.md`
- ✓ Banach fixed point theorem → `banach-fixed-point-theorem.md`
- ✓ Cauchy–Schwarz inequality → `cauchy-schwarz-inequality.md`
- ✓ Compactness criteria in ℝ^k → `compactness-criteria-rk.md`
- ✓ Completeness of C^k → `completeness-of-ck.md`
- ✓ Compact iff complete and totally bounded → `compact-iff-complete-totally-bounded.md`
- ✓ Connectedness criteria in ℝ → `connectedness-criteria-r.md`
- ✓ Convergence in product metric spaces → `convergence-in-product-metric-spaces.md`
- ✓ Second derivative tests → `second-derivative-tests.md`

**Lemmas:**
- ✓ Absolute convergence implies Cauchy criterion → `absolute-convergence-implies-cauchy-criterion.md`
- ✓ Bounded infinite set has limit point → `bounded-infinite-set-has-limit-point.md`
- ✓ Compactness of graphs lemma → `compactness-of-graphs-lemma.md`
- ✓ Equicontinuity: pointwise bounded implies uniformly bounded → `equicontinuity-pointwise-bounded-uniform-bounded.md`
- ✓ Equicontinuity: pointwise convergence on dense set lemma → `equicontinuity-pointwise-convergence-dense-set-lemma.md`
- ✓ Finite subcover lemma → `finite-subcover-lemma.md`
- ✓ Jordan decomposition lemma → `jordan-decomposition-lemma.md`
- ✓ Lebesgue number lemma (auxiliary refinement) → `lebesgue-number-lemma-auxiliary-refinement.md`
- ✓ Neumann series lemma → `neumann-series-lemma.md`
- ✓ Totally bounded implies Cauchy subsequence → `totally-bounded-cauchy-subsequence.md`

**Propositions:**
- ✓ Composition preserves Riemann integrability → `composition-preserves-riemann-integrability.md`
- ✓ Continuous on compact: bounded corollary → `continuous-on-compact-bounded-corollary.md`
- ✓ Continuous image: compact, closed, bounded → `continuous-image-compact-closed-bounded.md`
- ✓ Differentiability criterion via remainder → `differentiability-criterion-remainder.md`
- ✓ Differentiability on an interval → `differentiability-on-an-interval.md`
- ✓ Image of compact connected is interval → `image-compact-connected-is-interval.md`
- ✓ Integration by parts → `integration-by-parts.md`
- ✓ Interchange of limit and integral (uniform) → `interchange-limit-integral-uniform.md`
- ✓ Linearity in integrator (Riemann–Stieltjes) → `linearity-in-integrator-riemann-stieltjes.md`
- ✓ Total boundedness via ε-nets → `total-boundedness-epsilon-nets.md`
- ✓ Uniform convergence implies convergence of sup norms → `uniform-convergence-implies-convergence-of-sup-norms.md`
- ✓ Uniform limit of integrable functions → `uniform-limit-of-integrable-functions.md`
- ✓ Uniform convergence of series of functions → `uniform-convergence-of-a-series-of-functions.md`

**Corollaries:**
- ✓ IVT corollary → `ivt-corollary.md`
- ✓ M-test: continuity and integration corollary → `m-test-continuity-integration-corollary.md`
- ✓ Term-by-term operations on series → `term-by-term-operations-series.md`
- ✓ Change of variables (Jacobian corollary) → `change-of-variables-jacobian-corollary.md`

### `convex-analysis` (additional)

**Lemmas:**
- ✓ Nonnegative real less than every ε > 0 must be zero → `nonnegative-real-less-than-every-0-must-be-zero.md`
- ✓ Subsequence index bound (n_k ≥ k) → `subsequence-index-bound-n_k-k.md`

**Propositions:**
- ✓ Set operations: sum, scalar multiple, difference → `set-operations-sum-scalar-multiple-difference.md`
- ✓ Closed sets characterized by sequences (version II) → `closed-sets-characterized-by-sequences-version-ii.md`

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

## Usage

To generate knowls for a specific course:

**Baby Rudin Analysis:**
```
shared-foundations + shared-linear-algebra +
analysis-order-completeness + analysis-metric-topology +
analysis-sequences-series + analysis-continuity +
analysis-compactness-connectedness + analysis-differentiation-1d +
analysis-riemann-integration + analysis-function-sequences +
analysis-multivariable
```

**Undergraduate Group Theory (300-level):**
```
shared-foundations + algebra-groups (core only, exclude Schur–Zassenhaus, Burnside p^a q^b, etc.)
```

**Graduate Algebra I (Groups + Rings):**
```
shared-foundations + algebra-groups + algebra-rings
```

**Graduate Algebra II (Modules + Fields):**
```
shared-foundations + shared-linear-algebra + algebra-groups +
algebra-rings + algebra-modules + algebra-fields-galois
```

**Commutative Algebra:**
```
shared-foundations + algebra-rings + algebra-modules + algebra-commutative
```

**Homological Algebra:**
```
shared-foundations + algebra-category-theory + algebra-rings +
algebra-modules + algebra-homological
```

**Convex Analysis / Functional Analysis Foundations:**
```
shared-foundations + shared-linear-algebra + analysis-metric-topology +
convex-analysis
```
