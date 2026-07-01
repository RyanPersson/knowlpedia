+++
id = "convex-analysis"
title = "Convex Analysis"
kind = "section"
summary = "Convex sets, convex functions, separation theorems, and the Hahn-Banach theorem"
aliases = ["convex-analysis", "Convex Analysis"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/_index.md"
+++

Click any term to expand its definition inline.

---

## Metric Spaces

### Definitions
- [[convex-analysis/metric-metric-space|Metric and metric space]]
- [[convex-analysis/open-and-closed-balls-in-a-metric-space|Open and closed balls]]
- [[convex-analysis/open-subset|Open set]]
- [[convex-analysis/closed-subset|Closed set]]
- [[convex-analysis/interior-of-a-set|Interior]]
- [[convex-analysis/closure-of-a-set|Closure]]
- [[convex-analysis/convergence-of-a-sequence|Convergence of a sequence]]
- [[convex-analysis/cauchy-sequence|Cauchy sequence]]
- [[convex-analysis/complete-metric-space-complete-subset|Complete metric space]]
- [[convex-analysis/distance-function-to-a-set|Distance function to a set]]
- [[convex-analysis/product-space-cartesian-product|Product space]]

### Properties
- [[convex-analysis/open-balls-are-open-sets|Open balls are open]]
- [[convex-analysis/closed-balls-are-closed-sets|Closed balls are closed]]
- [[convex-analysis/basic-properties-of-open-sets|Basic properties of open sets]]
- [[convex-analysis/basic-properties-of-closed-sets|Basic properties of closed sets]]
- [[convex-analysis/basic-properties-of-the-interior-operator|Basic properties of interior]]
- [[convex-analysis/basic-properties-of-the-closure-operator|Basic properties of closure]]
- [[convex-analysis/interior-characterized-by-existence-of-a-ball|Interior via balls]]
- [[convex-analysis/closure-characterized-by-ball-intersections|Closure via balls]]
- [[convex-analysis/closure-characterized-by-convergent-sequences|Closure via sequences]]
- [[convex-analysis/closed-sets-characterized-by-sequences-version-i|Closed sets via sequences (I)]]
- [[convex-analysis/closed-sets-characterized-by-sequences-version-ii|Closed sets via sequences (II)]]
- [[convex-analysis/uniqueness-of-limits-in-metric-spaces|Uniqueness of limits]]
- [[convex-analysis/convergent-sequences-are-bounded|Convergent sequences are bounded]]
- [[convex-analysis/convergent-sequences-are-cauchy|Convergent sequences are Cauchy]]
- [[convex-analysis/cauchy-sequences-are-bounded|Cauchy sequences are bounded]]
- [[convex-analysis/cauchy-sequence-with-a-convergent-subsequence-converges|Cauchy + convergent subsequence implies convergent]]
- [[convex-analysis/subsequences-of-convergent-sequences-converge-to-the-same-limit|Subsequences converge to the same limit]]
- [[convex-analysis/subsequence-index-bound-n_k-k|Subsequence index bound]]
- [[convex-analysis/completeness-implies-closedness-closed-subsets-of-complete-spaces-are-complete|Completeness and closedness]]
- [[convex-analysis/completeness-of-rk|Completeness of R^k]]
- [[convex-analysis/reverse-triangle-inequality|Reverse triangle inequality]]

---

## Normed Vector Spaces

### Definitions
- [[convex-analysis/norm-normed-vector-space|Norm and normed vector space]]
- [[convex-analysis/seminorm|Seminorm]]
- [[convex-analysis/bounded-set-and-bounded-sequence|Bounded sets and sequences]]
- [[convex-analysis/convergence-in-normed-spaces|Convergence in normed spaces]]
- [[convex-analysis/bounded-linear-functional-norm-of-a-functional|Bounded linear functional]]
- [[convex-analysis/dual-space-and-duality-pairing|Dual space and duality pairing]]

### Properties
- [[convex-analysis/norm-induces-a-metric-and-conversely|Norm induces a metric]]
- [[convex-analysis/convergence-implies-convergence-of-norms|Convergence implies convergence of norms]]
- [[convex-analysis/uniqueness-of-limits-and-boundedness-in-normed-spaces|Uniqueness of limits and boundedness]]
- [[convex-analysis/algebra-of-limits-in-normed-spaces|Algebra of limits]]
- [[convex-analysis/existence-of-a-functional-attaining-its-norm-at-a-point|Existence of a norming functional]]
- [[convex-analysis/continuity-of-linear-functionals-via-closed-level-sets|Continuity via closed level sets]]

---

## Vector Spaces and Linear Algebra

### Definitions
- [[convex-analysis/linear-subspace|Linear subspace]]
- [[convex-analysis/linear-combination|Linear combination]]
- [[convex-analysis/subspace-generated-by-a-set-span|Span]]
- [[convex-analysis/linearly-independent-and-linearly-dependent-sets|Linear independence and dependence]]
- [[convex-analysis/basis-hamel-basis-and-dimension|Basis and dimension]]
- [[convex-analysis/direct-sum-of-subspaces|Direct sum of subspaces]]
- [[convex-analysis/linear-operator-linear-transformation|Linear operator]]
- [[convex-analysis/image-and-kernel-linear-isomorphism|Image, kernel, and isomorphism]]
- [[convex-analysis/quotient-vector-space-codimension|Quotient vector space]]
- [[convex-analysis/codimension|Codimension]]
- [[convex-analysis/self-adjoint-linear-operator|Self-adjoint operator]]
- [[convex-analysis/nonnegative-positive-semidefinite-operator|Positive-semidefinite operator]]

### Properties
- [[convex-analysis/subspace-test-closure-under-addition-and-scalar-multiplication|Subspace test]]
- [[convex-analysis/intersection-of-subspaces-is-a-subspace|Intersection of subspaces]]
- [[convex-analysis/sum-of-subspaces-equals-span-of-the-union|Sum of subspaces equals span of union]]
- [[convex-analysis/span-equals-the-set-of-all-finite-linear-combinations|Span equals finite linear combinations]]
- [[convex-analysis/extension-of-a-linearly-independent-set-to-a-basis|Extension to a basis]]
- [[convex-analysis/existence-of-a-basis-hamel-basis|Existence of a basis]]
- [[convex-analysis/basis-characterized-by-maximal-linear-independence|Bases are maximal linearly independent]]
- [[convex-analysis/characterization-of-direct-sums|Characterization of direct sums]]
- [[convex-analysis/images-and-preimages-of-subspaces-under-linear-operators|Images and preimages of subspaces]]
- [[convex-analysis/isomorphism-theorem-and-dimension-formula-for-linear-operators|Isomorphism theorem]]
- [[convex-analysis/codimension-one-subspaces-yield-direct-sum-decompositions|Codimension-one subspaces]]
- [[convex-analysis/kernel-of-a-nonzero-linear-functional-has-codimension-one|Kernel has codimension one]]

---

## Convex Sets

### Definitions
- [[convex-analysis/convex-set|Convex set]]
- [[convex-analysis/convex-combination|Convex combination]]
- [[convex-analysis/convex-hull|Convex hull]]
- [[convex-analysis/line-segments-in-a-vector-space|Line segments]]
- [[convex-analysis/set-operations-sum-scalar-multiple-difference|Set operations (sum, scalar multiple)]]
- [[convex-analysis/set-valued-mapping-multifunction-domain-and-graph-convex-set-valued-mapping|Set-valued mapping]]
- [[convex-analysis/balanced-and-absorbing-sets|Balanced and absorbing sets]]

### Properties
- [[convex-analysis/convex-sets-characterized-by-closure-under-convex-combinations|Convexity via convex combinations]]
- [[convex-analysis/convex-hull-is-the-smallest-convex-set-containing|Convex hull is smallest]]
- [[convex-analysis/convex-hull-via-convex-combinations|Convex hull via combinations]]
- [[convex-analysis/intersections-of-convex-sets-are-convex|Intersections are convex]]
- [[convex-analysis/sums-and-scalar-multiples-of-convex-sets-are-convex|Sums and scalar multiples are convex]]
- [[convex-analysis/cartesian-product-of-convex-sets-is-convex|Cartesian products are convex]]
- [[convex-analysis/interior-and-closure-of-a-convex-set-are-convex|Interior and closure are convex]]
- [[convex-analysis/interior-and-closure-relations-for-convex-sets-with-nonempty-interior|Interior-closure relations]]
- [[convex-analysis/segments-from-interior-points-stay-in-the-interior|Segments from interior stay in interior]]
- [[convex-analysis/closure-of-intersections-under-interior-point-condition|Closure of intersections]]
- [[convex-analysis/basic-operations-preserving-convexity|Operations preserving convexity]]

---

## Affine Sets

### Definitions
- [[convex-analysis/affine-set|Affine set]]
- [[convex-analysis/affine-hull-affine-combination|Affine hull and affine combination]]
- [[convex-analysis/affine-mapping|Affine mapping]]
- [[convex-analysis/line-connecting-two-points|Line connecting two points]]
- [[convex-analysis/parallel-affine-set|Parallel affine set]]

### Properties
- [[convex-analysis/properties-of-affine-sets-and-affine-hulls|Properties of affine sets]]
- [[convex-analysis/affine-sets-are-translates-of-subspaces|Affine sets are translates of subspaces]]
- [[convex-analysis/parallel-subspace-to-an-affine-set-is|Parallel subspace]]
- [[convex-analysis/characterization-of-affine-mappings|Characterization of affine mappings]]
- [[convex-analysis/affine-images-and-preimages-of-convex-sets-are-convex|Affine images preserve convexity]]

---

## Algebraic Interior (Core)

### Definitions
- [[convex-analysis/algebraic-interior-core|Algebraic interior (core)]]
- [[convex-analysis/linear-closure|Linear closure]]

### Properties
- [[convex-analysis/core-characterized-by-absorbing-translations|Core via absorbing translations]]
- [[convex-analysis/core-of-a-convex-set-is-convex|Core is convex]]
- [[convex-analysis/core-equals-interior-for-convex-sets-in-normed-spaces|Core equals interior (normed spaces)]]
- [[convex-analysis/segments-from-core-points-stay-in-the-core|Segments from core stay in core]]
- [[convex-analysis/idempotence-of-the-core-operator|Idempotence of core]]
- [[convex-analysis/linear-closure-of-a-convex-set-is-convex|Linear closure is convex]]
- [[convex-analysis/linear-closure-equals-closure-for-solid-convex-sets|Linear closure equals topological closure]]

---

## Convex Functions

### Definitions
- [[convex-analysis/extended-real-number-system-and-conventions|Extended reals and conventions]]
- [[convex-analysis/domain-and-epigraph-proper-function|Domain, epigraph, proper function]]
- [[convex-analysis/convex-function-via-epigraph|Convex function via epigraph]]
- [[convex-analysis/strictly-convex-function|Strictly convex function]]
- [[convex-analysis/quasiconvex-function|Quasiconvex function]]
- [[convex-analysis/indicator-function-of-a-set|Indicator function]]
- [[convex-analysis/marginal-optimal-value-function|Marginal (optimal value) function]]

### Properties
- [[convex-analysis/equivalent-characterizations-of-convex-functions|Equivalent characterizations]]
- [[convex-analysis/domain-of-a-convex-function-is-convex|Domain is convex]]
- [[convex-analysis/convexity-on-a-convex-subset-via-extension|Convexity via extension]]
- [[convex-analysis/quasiconvexity-characterized-by-convex-sublevel-sets|Quasiconvexity via sublevel sets]]
- [[convex-analysis/slope-inequalities-for-convex-functions|Slope inequalities]]
- [[convex-analysis/convexity-characterized-by-monotonicity-of-derivative|Convexity via monotone derivative]]
- [[convex-analysis/convexity-via-nonnegative-second-derivative|Convexity via second derivative]]
- [[convex-analysis/convexity-characterized-by-positive-semidefinite-hessian|Convexity via Hessian]]
- [[convex-analysis/convexity-preserved-under-monotone-convex-composition|Monotone convex composition]]
- [[convex-analysis/convexity-preserved-under-affine-composition|Affine composition]]
- [[convex-analysis/supremum-of-convex-functions-is-convex|Supremum is convex]]
- [[convex-analysis/convexity-of-the-marginal-optimal-value-function|Marginal function is convex]]

---

## Minkowski Gauge and Sublinear Functions

### Definitions
- [[convex-analysis/subadditive-positively-homogeneous-and-sublinear-functions|Subadditive, positively homogeneous, sublinear]]
- [[convex-analysis/minkowski-function-gauge-of-a-set|Minkowski function (gauge)]]

### Properties
- [[convex-analysis/properties-of-the-minkowski-functional-of-a-convex-set|Properties of the Minkowski gauge]]
- [[convex-analysis/continuity-and-level-sets-of-the-minkowski-functional|Continuity and level sets]]

---

## Hyperplanes and Separation

### Definitions
- [[convex-analysis/hyperplane|Hyperplane]]
- [[convex-analysis/hyperplanes-are-level-sets-of-nonzero-linear-functionals|Hyperplanes as level sets]]

### Separation Theorems
- [[convex-analysis/separation-by-a-hyperplane|Separation by a hyperplane]]
- [[convex-analysis/separation-by-hyperplanes-via-supinf-inequality|Separation via sup/inf inequality]]
- [[convex-analysis/separation-of-a-point-and-a-subspace|Separation of point and subspace]]
- [[convex-analysis/separation-of-a-point-from-a-convex-set-via-the-core|Separation via core]]
- [[convex-analysis/auxiliary-separation-lemma-for-disjoint-convex-sets-with-nonempty-core|Auxiliary separation lemma]]
- [[convex-analysis/separation-of-two-convex-sets-via-the-core-condition|Separation of two convex sets]]
- [[convex-analysis/complex-separation-theorem-real-parts|Complex separation (real parts)]]
- [[convex-analysis/separation-by-a-closed-hyperplane|Separation by closed hyperplane]]
- [[convex-analysis/separation-by-closed-hyperplane-under-interior-condition|Closed hyperplane (interior condition)]]
- [[convex-analysis/strict-separation-with-an-open-convex-set|Strict separation (open set)]]
- [[convex-analysis/strict-separation-by-a-closed-hyperplane|Strict separation (closed hyperplane)]]
- [[convex-analysis/strict-separation-of-compact-and-closed-convex-sets|Strict separation (compact and closed)]]

---

## Hahn-Banach Theorems

- [[convex-analysis/hahn-banach-theorem-in-real-vector-spaces|Hahn-Banach (real vector spaces)]]
- [[convex-analysis/hahn-banach-extension-dominated-by-a-seminorm-real-case|Hahn-Banach (seminorm domination)]]
- [[convex-analysis/hahn-banach-theorem-in-complex-vector-spaces|Hahn-Banach (complex vector spaces)]]
- [[convex-analysis/hahn-banach-theorem-in-normed-spaces|Hahn-Banach (normed spaces)]]

---

## Inequalities

- [[convex-analysis/nonnegative-real-less-than-every-0-must-be-zero|Nonnegative real below every epsilon is zero]]
- [[convex-analysis/weighted-arithmeticgeometric-mean-inequality|Weighted AM-GM inequality]]
- [[convex-analysis/youngs-inequality|Young's inequality]]
- [[convex-analysis/holder-inequality-finite-sums|Hölder inequality (finite sums)]]
- [[convex-analysis/holder-inequality-integrals|Hölder inequality (integrals)]]
---

## Uncategorized

- [[convex-analysis/convex-lecture-notes|Modern Analysis: Lecture Notes and Further Reading Materials]]
