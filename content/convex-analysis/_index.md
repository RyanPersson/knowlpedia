---
title: "Convex Analysis"
description: "Convex sets, convex functions, separation theorems, and the Hahn-Banach theorem"
---

Click any term to expand its definition inline.

---

## Metric Spaces

### Definitions
- {{< knowl id="metric-metric-space" text="Metric and metric space" >}}
- {{< knowl id="open-and-closed-balls-in-a-metric-space" text="Open and closed balls" >}}
- {{< knowl id="open-subset" text="Open set" >}}
- {{< knowl id="closed-subset" text="Closed set" >}}
- {{< knowl id="interior-of-a-set" text="Interior" >}}
- {{< knowl id="closure-of-a-set" text="Closure" >}}
- {{< knowl id="convergence-of-a-sequence" text="Convergence of a sequence" >}}
- {{< knowl id="cauchy-sequence" text="Cauchy sequence" >}}
- {{< knowl id="complete-metric-space-complete-subset" text="Complete metric space" >}}
- {{< knowl id="distance-function-to-a-set" text="Distance function to a set" >}}
- {{< knowl id="product-space-cartesian-product" text="Product space" >}}

### Properties
- {{< knowl id="open-balls-are-open-sets" text="Open balls are open" >}}
- {{< knowl id="closed-balls-are-closed-sets" text="Closed balls are closed" >}}
- {{< knowl id="basic-properties-of-open-sets" text="Basic properties of open sets" >}}
- {{< knowl id="basic-properties-of-closed-sets" text="Basic properties of closed sets" >}}
- {{< knowl id="basic-properties-of-the-interior-operator" text="Basic properties of interior" >}}
- {{< knowl id="basic-properties-of-the-closure-operator" text="Basic properties of closure" >}}
- {{< knowl id="interior-characterized-by-existence-of-a-ball" text="Interior via balls" >}}
- {{< knowl id="closure-characterized-by-ball-intersections" text="Closure via balls" >}}
- {{< knowl id="closure-characterized-by-convergent-sequences" text="Closure via sequences" >}}
- {{< knowl id="closed-sets-characterized-by-sequences-version-i" text="Closed sets via sequences (I)" >}}
- {{< knowl id="closed-sets-characterized-by-sequences-version-ii" text="Closed sets via sequences (II)" >}}
- {{< knowl id="uniqueness-of-limits-in-metric-spaces" text="Uniqueness of limits" >}}
- {{< knowl id="convergent-sequences-are-bounded" text="Convergent sequences are bounded" >}}
- {{< knowl id="convergent-sequences-are-cauchy" text="Convergent sequences are Cauchy" >}}
- {{< knowl id="cauchy-sequences-are-bounded" text="Cauchy sequences are bounded" >}}
- {{< knowl id="cauchy-sequence-with-a-convergent-subsequence-converges" text="Cauchy + convergent subsequence implies convergent" >}}
- {{< knowl id="subsequences-of-convergent-sequences-converge-to-the-same-limit" text="Subsequences converge to the same limit" >}}
- {{< knowl id="subsequence-index-bound-n_k-k" text="Subsequence index bound" >}}
- {{< knowl id="completeness-implies-closedness-closed-subsets-of-complete-spaces-are-complete" text="Completeness and closedness" >}}
- {{< knowl id="completeness-of-rk" text="Completeness of R^k" >}}
- {{< knowl id="reverse-triangle-inequality" text="Reverse triangle inequality" >}}

---

## Normed Vector Spaces

### Definitions
- {{< knowl id="norm-normed-vector-space" text="Norm and normed vector space" >}}
- {{< knowl id="seminorm" text="Seminorm" >}}
- {{< knowl id="bounded-set-and-bounded-sequence" text="Bounded sets and sequences" >}}
- {{< knowl id="convergence-in-normed-spaces" text="Convergence in normed spaces" >}}
- {{< knowl id="bounded-linear-functional-norm-of-a-functional" text="Bounded linear functional" >}}
- {{< knowl id="dual-space-and-duality-pairing" text="Dual space and duality pairing" >}}

### Properties
- {{< knowl id="norm-induces-a-metric-and-conversely" text="Norm induces a metric" >}}
- {{< knowl id="convergence-implies-convergence-of-norms" text="Convergence implies convergence of norms" >}}
- {{< knowl id="uniqueness-of-limits-and-boundedness-in-normed-spaces" text="Uniqueness of limits and boundedness" >}}
- {{< knowl id="algebra-of-limits-in-normed-spaces" text="Algebra of limits" >}}
- {{< knowl id="existence-of-a-functional-attaining-its-norm-at-a-point" text="Existence of a norming functional" >}}
- {{< knowl id="continuity-of-linear-functionals-via-closed-level-sets" text="Continuity via closed level sets" >}}

---

## Vector Spaces and Linear Algebra

### Definitions
- {{< knowl id="linear-subspace" text="Linear subspace" >}}
- {{< knowl id="linear-combination" text="Linear combination" >}}
- {{< knowl id="subspace-generated-by-a-set-span" text="Span" >}}
- {{< knowl id="linearly-independent-and-linearly-dependent-sets" text="Linear independence and dependence" >}}
- {{< knowl id="basis-hamel-basis-and-dimension" text="Basis and dimension" >}}
- {{< knowl id="direct-sum-of-subspaces" text="Direct sum of subspaces" >}}
- {{< knowl id="linear-operator-linear-transformation" text="Linear operator" >}}
- {{< knowl id="image-and-kernel-linear-isomorphism" text="Image, kernel, and isomorphism" >}}
- {{< knowl id="quotient-vector-space-codimension" text="Quotient vector space" >}}
- {{< knowl id="codimension" text="Codimension" >}}
- {{< knowl id="self-adjoint-linear-operator" text="Self-adjoint operator" >}}
- {{< knowl id="nonnegative-positive-semidefinite-operator" text="Positive-semidefinite operator" >}}

### Properties
- {{< knowl id="subspace-test-closure-under-addition-and-scalar-multiplication" text="Subspace test" >}}
- {{< knowl id="intersection-of-subspaces-is-a-subspace" text="Intersection of subspaces" >}}
- {{< knowl id="sum-of-subspaces-equals-span-of-the-union" text="Sum of subspaces equals span of union" >}}
- {{< knowl id="span-equals-the-set-of-all-finite-linear-combinations" text="Span equals finite linear combinations" >}}
- {{< knowl id="extension-of-a-linearly-independent-set-to-a-basis" text="Extension to a basis" >}}
- {{< knowl id="existence-of-a-basis-hamel-basis" text="Existence of a basis" >}}
- {{< knowl id="basis-characterized-by-maximal-linear-independence" text="Bases are maximal linearly independent" >}}
- {{< knowl id="characterization-of-direct-sums" text="Characterization of direct sums" >}}
- {{< knowl id="images-and-preimages-of-subspaces-under-linear-operators" text="Images and preimages of subspaces" >}}
- {{< knowl id="isomorphism-theorem-and-dimension-formula-for-linear-operators" text="Isomorphism theorem" >}}
- {{< knowl id="codimension-one-subspaces-yield-direct-sum-decompositions" text="Codimension-one subspaces" >}}
- {{< knowl id="kernel-of-a-nonzero-linear-functional-has-codimension-one" text="Kernel has codimension one" >}}

---

## Convex Sets

### Definitions
- {{< knowl id="convex-set" text="Convex set" >}}
- {{< knowl id="convex-combination" text="Convex combination" >}}
- {{< knowl id="convex-hull" text="Convex hull" >}}
- {{< knowl id="line-segments-in-a-vector-space" text="Line segments" >}}
- {{< knowl id="set-operations-sum-scalar-multiple-difference" text="Set operations (sum, scalar multiple)" >}}
- {{< knowl id="set-valued-mapping-multifunction-domain-and-graph-convex-set-valued-mapping" text="Set-valued mapping" >}}
- {{< knowl id="balanced-and-absorbing-sets" text="Balanced and absorbing sets" >}}

### Properties
- {{< knowl id="convex-sets-characterized-by-closure-under-convex-combinations" text="Convexity via convex combinations" >}}
- {{< knowl id="convex-hull-is-the-smallest-convex-set-containing" text="Convex hull is smallest" >}}
- {{< knowl id="convex-hull-via-convex-combinations" text="Convex hull via combinations" >}}
- {{< knowl id="intersections-of-convex-sets-are-convex" text="Intersections are convex" >}}
- {{< knowl id="sums-and-scalar-multiples-of-convex-sets-are-convex" text="Sums and scalar multiples are convex" >}}
- {{< knowl id="cartesian-product-of-convex-sets-is-convex" text="Cartesian products are convex" >}}
- {{< knowl id="interior-and-closure-of-a-convex-set-are-convex" text="Interior and closure are convex" >}}
- {{< knowl id="interior-and-closure-relations-for-convex-sets-with-nonempty-interior" text="Interior-closure relations" >}}
- {{< knowl id="segments-from-interior-points-stay-in-the-interior" text="Segments from interior stay in interior" >}}
- {{< knowl id="closure-of-intersections-under-interior-point-condition" text="Closure of intersections" >}}
- {{< knowl id="basic-operations-preserving-convexity" text="Operations preserving convexity" >}}

---

## Affine Sets

### Definitions
- {{< knowl id="affine-set" text="Affine set" >}}
- {{< knowl id="affine-hull-affine-combination" text="Affine hull and affine combination" >}}
- {{< knowl id="affine-mapping" text="Affine mapping" >}}
- {{< knowl id="line-connecting-two-points" text="Line connecting two points" >}}
- {{< knowl id="parallel-affine-set" text="Parallel affine set" >}}

### Properties
- {{< knowl id="properties-of-affine-sets-and-affine-hulls" text="Properties of affine sets" >}}
- {{< knowl id="affine-sets-are-translates-of-subspaces" text="Affine sets are translates of subspaces" >}}
- {{< knowl id="parallel-subspace-to-an-affine-set-is" text="Parallel subspace" >}}
- {{< knowl id="characterization-of-affine-mappings" text="Characterization of affine mappings" >}}
- {{< knowl id="affine-images-and-preimages-of-convex-sets-are-convex" text="Affine images preserve convexity" >}}

---

## Algebraic Interior (Core)

### Definitions
- {{< knowl id="algebraic-interior-core" text="Algebraic interior (core)" >}}
- {{< knowl id="linear-closure" text="Linear closure" >}}

### Properties
- {{< knowl id="core-characterized-by-absorbing-translations" text="Core via absorbing translations" >}}
- {{< knowl id="core-of-a-convex-set-is-convex" text="Core is convex" >}}
- {{< knowl id="core-equals-interior-for-convex-sets-in-normed-spaces" text="Core equals interior (normed spaces)" >}}
- {{< knowl id="segments-from-core-points-stay-in-the-core" text="Segments from core stay in core" >}}
- {{< knowl id="idempotence-of-the-core-operator" text="Idempotence of core" >}}
- {{< knowl id="linear-closure-of-a-convex-set-is-convex" text="Linear closure is convex" >}}
- {{< knowl id="linear-closure-equals-closure-for-solid-convex-sets" text="Linear closure equals topological closure" >}}

---

## Convex Functions

### Definitions
- {{< knowl id="extended-real-number-system-and-conventions" text="Extended reals and conventions" >}}
- {{< knowl id="domain-and-epigraph-proper-function" text="Domain, epigraph, proper function" >}}
- {{< knowl id="convex-function-via-epigraph" text="Convex function via epigraph" >}}
- {{< knowl id="strictly-convex-function" text="Strictly convex function" >}}
- {{< knowl id="quasiconvex-function" text="Quasiconvex function" >}}
- {{< knowl id="indicator-function-of-a-set" text="Indicator function" >}}
- {{< knowl id="marginal-optimal-value-function" text="Marginal (optimal value) function" >}}

### Properties
- {{< knowl id="equivalent-characterizations-of-convex-functions" text="Equivalent characterizations" >}}
- {{< knowl id="domain-of-a-convex-function-is-convex" text="Domain is convex" >}}
- {{< knowl id="convexity-on-a-convex-subset-via-extension" text="Convexity via extension" >}}
- {{< knowl id="quasiconvexity-characterized-by-convex-sublevel-sets" text="Quasiconvexity via sublevel sets" >}}
- {{< knowl id="slope-inequalities-for-convex-functions" text="Slope inequalities" >}}
- {{< knowl id="convexity-characterized-by-monotonicity-of-derivative" text="Convexity via monotone derivative" >}}
- {{< knowl id="convexity-via-nonnegative-second-derivative" text="Convexity via second derivative" >}}
- {{< knowl id="convexity-characterized-by-positive-semidefinite-hessian" text="Convexity via Hessian" >}}
- {{< knowl id="convexity-preserved-under-monotone-convex-composition" text="Monotone convex composition" >}}
- {{< knowl id="convexity-preserved-under-affine-composition" text="Affine composition" >}}
- {{< knowl id="supremum-of-convex-functions-is-convex" text="Supremum is convex" >}}
- {{< knowl id="convexity-of-the-marginal-optimal-value-function" text="Marginal function is convex" >}}

---

## Minkowski Gauge and Sublinear Functions

### Definitions
- {{< knowl id="subadditive-positively-homogeneous-and-sublinear-functions" text="Subadditive, positively homogeneous, sublinear" >}}
- {{< knowl id="minkowski-function-gauge-of-a-set" text="Minkowski function (gauge)" >}}

### Properties
- {{< knowl id="properties-of-the-minkowski-functional-of-a-convex-set" text="Properties of the Minkowski gauge" >}}
- {{< knowl id="continuity-and-level-sets-of-the-minkowski-functional" text="Continuity and level sets" >}}

---

## Hyperplanes and Separation

### Definitions
- {{< knowl id="hyperplane" text="Hyperplane" >}}
- {{< knowl id="hyperplanes-are-level-sets-of-nonzero-linear-functionals" text="Hyperplanes as level sets" >}}

### Separation Theorems
- {{< knowl id="separation-by-a-hyperplane" text="Separation by a hyperplane" >}}
- {{< knowl id="separation-by-hyperplanes-via-supinf-inequality" text="Separation via sup/inf inequality" >}}
- {{< knowl id="separation-of-a-point-and-a-subspace" text="Separation of point and subspace" >}}
- {{< knowl id="separation-of-a-point-from-a-convex-set-via-the-core" text="Separation via core" >}}
- {{< knowl id="auxiliary-separation-lemma-for-disjoint-convex-sets-with-nonempty-core" text="Auxiliary separation lemma" >}}
- {{< knowl id="separation-of-two-convex-sets-via-the-core-condition" text="Separation of two convex sets" >}}
- {{< knowl id="complex-separation-theorem-real-parts" text="Complex separation (real parts)" >}}
- {{< knowl id="separation-by-a-closed-hyperplane" text="Separation by closed hyperplane" >}}
- {{< knowl id="separation-by-closed-hyperplane-under-interior-condition" text="Closed hyperplane (interior condition)" >}}
- {{< knowl id="strict-separation-with-an-open-convex-set" text="Strict separation (open set)" >}}
- {{< knowl id="strict-separation-by-a-closed-hyperplane" text="Strict separation (closed hyperplane)" >}}
- {{< knowl id="strict-separation-of-compact-and-closed-convex-sets" text="Strict separation (compact and closed)" >}}

---

## Hahn-Banach Theorems

- {{< knowl id="hahn-banach-theorem-in-real-vector-spaces" text="Hahn-Banach (real vector spaces)" >}}
- {{< knowl id="hahn-banach-extension-dominated-by-a-seminorm-real-case" text="Hahn-Banach (seminorm domination)" >}}
- {{< knowl id="hahn-banach-theorem-in-complex-vector-spaces" text="Hahn-Banach (complex vector spaces)" >}}
- {{< knowl id="hahn-banach-theorem-in-normed-spaces" text="Hahn-Banach (normed spaces)" >}}

---

## Inequalities

- {{< knowl id="nonnegative-real-less-than-every-0-must-be-zero" text="Nonnegative real below every epsilon is zero" >}}
- {{< knowl id="weighted-arithmeticgeometric-mean-inequality" text="Weighted AM-GM inequality" >}}
- {{< knowl id="youngs-inequality" text="Young's inequality" >}}
- {{< knowl id="holder-inequality-finite-sums" text="Hölder inequality (finite sums)" >}}
- {{< knowl id="holder-inequality-integrals" text="Hölder inequality (integrals)" >}}
---

## Uncategorized

- {{< knowl id="convex-lecture-notes" text="Modern Analysis: Lecture Notes and Further Reading Materials" >}}
