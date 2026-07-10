# Analysis Modules

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

*Depends on:* `linear-algebra`, `analysis-differentiation-1d`, `analysis-riemann-integration`

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

*Depends on:* `shared-foundations`, `linear-algebra`, `analysis-metric-topology`

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
- ✓ Nonnegative real less than every ε > 0 must be zero → `nonnegative-real-less-than-every-0-must-be-zero.md`
- ✓ Subsequence index bound (n_k ≥ k) → `subsequence-index-bound-n_k-k.md`

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
- ✓ Set operations: sum, scalar multiple, difference → `set-operations-sum-scalar-multiple-difference.md`
- ✓ Closed sets characterized by sequences (version II) → `closed-sets-characterized-by-sequences-version-ii.md`

**Corollaries:**
- ✓ Young's inequality → `youngs-inequality.md`
- ✓ Weighted arithmetic–geometric mean inequality → `weighted-arithmeticgeometric-mean-inequality.md`
- ✓ Hölder inequality (finite sums) → `holder-inequality-finite-sums.md`
- ✓ Hölder inequality (integrals) → `holder-inequality-integrals.md`

---

## Additional Knowls (not yet categorized)

These knowls exist in the `content/analysis/` directory but are not listed in the module definitions above.

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

---
