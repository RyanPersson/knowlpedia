You are creating knowls for a mathematics reference site.

A **knowl** is a compact reference card that answers exactly one question: "What is X?"

---

## What a Knowl Contains

Every knowl has exactly these parts:

### 1. Definition or Statement
The precise mathematical definition or theorem statement. This is the core content.

For a **definition**:
```
A **[term]** is [formal definition with LaTeX].
```

For a **theorem/proposition**:
```
**[Name]:** [Complete statement with all hypotheses and conclusions]
```

### 2. Context (1-2 sentences)
Brief prose connecting this concept to prerequisites. Weave in cross-links naturally:
```
This generalizes the notion of {{< knowl id="group" text="group" >}} by relaxing the invertibility requirement.
```

### 3. Examples (optional)
Include only if:
- **Canonical**: The standard example everyone learns (e.g., $\mathbb{R}^n$ for vector spaces)
- **Clarifying**: Illuminates a subtle point
- **Contrasting**: A counterexample that sharpens the definition

Omit examples entirely for straightforward concepts.

---

## Cross-Linking Syntax

Link to other knowls using this shortcode:
```
{{< knowl id="slug-name" text="display text" >}}
```

For knowls in a **different section**, add the section parameter:
```
{{< knowl id="ring" section="algebra-rings" text="ring" >}}
```

**Where to place links:**
- In the context sentence(s)
- In example descriptions
- First occurrence only (don't repeat)

**Where NOT to place links:**
- Inside LaTeX math (`$...$` or `$$...$$`) — the shortcode will break
- The term being defined in its own knowl

If you need to reference a concept inside an equation, put the link outside:
```
Let $x \in B(a,r)$ be a point in the {{< knowl id="open-ball" text="open ball" >}}.
```

---

## Output Format

For each slug, output:

**`slug-name.md`**
```markdown
---
title: "Display Title"
description: "One-line plain-text summary (no LaTeX)"
---

[Definition/Statement]

[Context with cross-links]

[Examples if warranted]
```

---

## Section Directory

Use these exact names for the `section` parameter:

| Section | Content |
|---------|---------|
| `shared-foundations` | Sets, logic, functions, relations |
| `linear-algebra` | Vector spaces, linear maps, matrices |
| `algebra-groups` | Groups, subgroups, actions |
| `algebra-rings` | Rings, ideals |
| `algebra-modules` | Modules, tensor products |
| `algebra-fields-galois` | Field extensions, Galois theory |
| `algebra-commutative` | Localization, spectrum |
| `algebra-category-theory` | Categories, functors |
| `algebra-homological` | Chain complexes, derived functors |
| `real-analysis` | Limits, continuity, differentiation |
| `measure-theory` | Measures, integration |
| `topology` | Topological spaces, continuity |
| `convex-analysis` | Convex sets and functions |
| `probability` | Probability spaces, random variables |
| `thermodynamics` | Thermodynamic potentials, equilibrium |
| `stat-mech` | Ensembles, partition functions |

---

## Available Slugs

**Current section (stat-mech-lattice):**
antiferromagnetic-ising, boundary-condition-lattice, configuration-space-lattice, dlr-equation, dlr-existence-theorem, external-field-coupling, extremal-gibbs-measure, ferromagnetic-ising, finite-range-interaction-lattice, finite-volume-gibbs-measure, gibbs-specification, heisenberg-model, infinite-volume-gibbs-measure, interaction-potential-phi, ising-1d-no-phase-transition, ising-2d-phase-transition, ising-model, lattice-gas, lattice-gas-ising-mapping, lattice-hamiltonian, mixture-gibbs-measures, onsager-2d-ising-solution, order-parameter, partition-function-lattice, phase-transition-gibbs, potts-model, pressure-lattice, prop-dlr-markov-property, prop-extremal-gibbs-ergodic, pure-phase, random-cluster-model, spin-configuration, spin-space, spontaneous-magnetization, spontaneous-symmetry-breaking, spontaneous-symmetry-breaking-group, tfae-phase-transition-indicators, thermodynamic-limit-pressure-lattice, translation-invariant-interaction, variational-principle-pressure-lattice, xy-model

**Cross-section references (use `section` parameter):**

`shared-foundations`: axiom-of-choice, bijective-function, binary-operation, bounded-infinite-set-has-limit-point, cardinality, cartesian-product, codomain, complement, complex-conjugate, complex-numbers-c, composition, composition-of-functions, contraction-mapping, countable-set, domain, empty-set, equivalence-class, equivalence-relation, function, graph-of-function, identity-function, image, indexed-family-of-sets, injective-function, integers, intersection, inverse-function, lower-bound, mathematical-induction, morphism, natural-numbers, ordered-pair, partial-order, partition, power-set, preimage, proper-subset, quotient-set, rational-numbers, real-numbers, relation, restriction-of-a-function, sequence, set, set-difference, subset, surjective-function, symmetric-difference, total-order, total-order-linear-order, union, upper-bound, well-ordered-set, well-ordering-principle, well-ordering-theorem, zfc-axioms, zorns-lemma

`linear-algebra`: banach-space, basis-existence-theorem, bilinear-form, cauchy-schwarz-inequality, cayley-hamilton-theorem, characteristic-polynomial, compact-operator, determinant, eigenspace, eigenvalue, eigenvector, euclidean-norm, euclidean-space, hilbert-space, inner-product, inner-product-space, linear-map, linear-operator, matrix, minimal-polynomial, norm, normed-vector-space, operator-norm, orthogonality, rank, rank-nullity-theorem, trace, vector-space

`shared-foundations`: axiom-of-choice, bijective-function, binary-operation, bounded-infinite-set-has-limit-point, cardinality, cartesian-product, codomain, complement, complex-conjugate, complex-numbers-c, composition, composition-of-functions, contraction-mapping, countable-set, domain, empty-set, equivalence-class, equivalence-relation, function, graph-of-function, identity-function, image, indexed-family-of-sets, injective-function, integers, intersection, inverse-function, lower-bound, mathematical-induction, morphism, natural-numbers, ordered-pair, partial-order, partition, power-set, preimage, proper-subset, quotient-set, rational-numbers, real-numbers, relation, restriction-of-a-function, sequence, set, set-difference, subset, surjective-function, symmetric-difference, total-order, total-order-linear-order, union, upper-bound, well-ordered-set, well-ordering-principle, well-ordering-theorem, zfc-axioms, zorns-lemma

`linear-algebra`: banach-space, basis-existence-theorem, bilinear-form, cauchy-schwarz-inequality, cayley-hamilton-theorem, characteristic-polynomial, compact-operator, determinant, eigenspace, eigenvalue, eigenvector, euclidean-norm, euclidean-space, hilbert-space, inner-product, inner-product-space, linear-map, linear-operator, matrix, minimal-polynomial, norm, normed-vector-space, operator-norm, orthogonality, rank, rank-nullity-theorem, trace, vector-space

`measure-theory`: ae-equality, almost-everywhere, borel-sigma-algebra, caratheodory-construction, caratheodory-measurable-set, change-of-variables-pushforward, characteristic-function-indicator-function, continuity-from-above-measure, continuity-from-below-measure, convergence-almost-everywhere, convergence-in-lp, convergence-in-measure, dominated-convergence-theorem, essential-supremum, fatous-lemma, fubinis-theorem, indicator-function, jensen-inequality-integral, jordan-content, l-infinity-function, l1-function, lebesgue-criterion-for-riemann-integrability, lebesgue-integrable-function, lebesgue-integral, lebesgue-integral-nonnegative, lebesgue-measure, lebesgue-number-lemma-auxiliary-refinement, lp-norm, lp-space, measurable-function, measurable-rectangle, measurable-set, measurable-space, measure, measure-space, minkowski-inequality-lp, monotone-convergence-theorem, null-set, outer-measure, premeasure, product-measure, pushforward-measure, set-algebra, set-of-measure-zero-in-rk, sigma-algebra, simple-function, tonellis-theorem, uniform-integrability

`probability`: central-limit-theorem, characteristic-function-probability, chebyshev-inequality, chernoff-bound, conditional-expectation, conditional-probability, correlation-coefficient, covariance, cumulant, cumulant-generating-function, differential-entropy, distribution-law, event-probability, expectation, expectation-function-of-rv, gibbs-inequality-kl, identically-distributed, iid-sequence, independence-events, independence-random-variables, independence-sigma-algebras, markov-inequality, maximum-entropy-principle, moment, moment-generating-function, pinsker-inequality, probability-measure, probability-space, radon-nikodym-theorem, random-variable, random-vector, relative-entropy-kl-divergence, shannon-entropy, strong-law-large-numbers, total-variation-distance, variance, weak-law-large-numbers

`topology`: baire-category-theorem, baire-space, basis-of-topology, bolzano-weierstrass-theorem, boundary, bounded-set, cantor-intersection-theorem, category-argument-template, cauchy-sequence, cauchy-sequence-is-bounded, closed-ball, closed-set, closed-sets-are-complements-of-open-sets, closed-subset-of-compact-set-is-compact, closure, compact-iff-complete-totally-bounded, compact-set, compact-subset-of-hausdorff-is-closed, compact-to-hausdorff-homeomorphism-criterion, compactness-implies-boundedness, compactness-implies-closedness, compactness-implies-completeness, compactness-implies-total-boundedness, compactness-of-graphs-lemma, complete-metric-space, complete-metric-space-is-baire, connected-component, connected-set, connected-subsets-of-r-are-intervals, connectedness-criteria-r, continuity-via-open-sets, continuous-attains-max-min-compact, continuous-bijection-from-compact-homeomorphism-criterion, continuous-image-of-compact-set-is-compact, continuous-image-of-connected-set-is-connected, continuous-map, continuous-on-compact-bounded-corollary, continuous-on-compact-is-bounded, convergence-in-product-metric-spaces, convergent-sequence, convergent-sequence-is-cauchy, cover, curve, dense-set, derived-set, diameter, epsilon-net, equivalent-metrics, extreme-value-theorem, finite-intersection-property, finite-intersection-property-theorem, hausdorff-space, heine-borel-theorem, heine-cantor-corollary, heine-cantor-theorem, holder-continuity, homeomorphism, image-compact-connected-is-interval, interior, intersection-of-dense-open-is-dense, isometry, lebesgue-number-lemma, limit-point, lipschitz-continuity, meager-set, metric, metric-induced-topology, metric-space, metric-sphere, neighborhood, nested-interval-theorem, nowhere-dense-set, open-ball, open-cover, open-set, open-sets-form-a-topology, path, path-connected-set, product-topology, quotient-topology... (99 total)

`real-analysis`: abel-test, abels-theorem, absolute-convergence-implies-cauchy, absolute-convergence-implies-convergence, absolute-value, absolute-value-preserves-integrability, absolutely-convergent-series, additivity-linearity-riemann-integral, algebraic-properties-sup-inf, alternating-series-test, antiderivative, archimedean-property, arzela-ascoli-theorem, banach-fixed-point-theorem, basic-properties-of-lim-sup-and-lim-inf, bounded-above, bounded-below, bounded-derivative-implies-uniform-continuity, bounded-sequence, bounded-sequence-has-convergent-subsequence, bounded-variation-function, c2-implies-equal-mixed-partials, cauchy-condensation-test, cauchy-criterion-in-rk, cauchy-hadamard-theorem, cauchy-mean-value-theorem, cauchy-product, chain-rule, chain-rule-multivariable, change-of-variables-formula, class-ck-function, class-ck-map, comparison-test, completeness-axiom, completeness-equivalences, composition-preserves-riemann-integrability, conditionally-convergent-series, constraint-set, continuity-at-a-point, continuity-on-a-set, continuity-via-sequences, convergent-series, convergent-series-terms-go-to-zero, critical-point, critical-value, darboux-theorem, density-of-irrationals, density-of-q, density-of-r-minus-q-in-r, derivative, derivative-sign-implies-monotonicity, derivative-zero-implies-constant, diffeomorphism, difference-quotient, differentiability-1d, differentiability-criterion, differentiability-implies-continuity, differentiability-one-variable, differentiable-map, differentiation-rules, dinis-theorem, directional-derivative, dirichlet-test, discontinuity-point, divergent-series, equicontinuity, equicontinuity-boundedness-criterion, equicontinuity-dense-set-lemma, equicontinuity-pointwise-bounded-uniform-bounded, equicontinuous-family, equivalent-definitions-continuity, existence-of-riemann-integral-for-continuous-functions, field-axioms, finite-subcover-lemma, fixed-point, frechet-derivative, fubini-theorem-riemann, fundamental-theorem-of-calculus-i, fundamental-theorem-of-calculus-ii, global-extrema... (243 total)

`convex-analysis`: affine-hull-affine-combination, affine-images-and-preimages-of-convex-sets-are-convex, affine-mapping, affine-set, affine-sets-are-translates-of-subspaces, algebra-of-limits-in-normed-spaces, algebraic-interior-core, auxiliary-separation-lemma-for-disjoint-convex-sets-with-nonempty-core, balanced-and-absorbing-sets, basic-operations-preserving-convexity, basic-properties-of-closed-sets, basic-properties-of-open-sets, basic-properties-of-the-closure-operator, basic-properties-of-the-interior-operator, basis-characterized-by-maximal-linear-independence, basis-hamel-basis-and-dimension, biconjugate, bounded-linear-functional-norm-of-a-functional, bounded-set-and-bounded-sequence, cartesian-product-of-convex-sets-is-convex, cauchy-sequence, cauchy-sequence-with-a-convergent-subsequence-converges, cauchy-sequences-are-bounded, characterization-of-affine-mappings, characterization-of-direct-sums, closed-balls-are-closed-sets, closed-convex-function, closed-sets-characterized-by-sequences-version-i, closed-sets-characterized-by-sequences-version-ii, closed-subset, closure-characterized-by-ball-intersections, closure-characterized-by-convergent-sequences, closure-of-a-set, closure-of-intersections-under-interior-point-condition, codimension, codimension-one-subspaces-yield-direct-sum-decompositions, complete-metric-space-complete-subset, completeness-implies-closedness-closed-subsets-of-complete-spaces-are-complete, completeness-of-rk, complex-separation-theorem-real-parts, continuity-and-level-sets-of-the-minkowski-functional, continuity-of-linear-functionals-via-closed-level-sets, convergence-implies-convergence-of-norms, convergence-in-normed-spaces, convergence-of-a-sequence, convergent-sequences-are-bounded, convergent-sequences-are-cauchy, convex-combination, convex-conjugate-fenchel, convex-duality-primal-dual, convex-function-via-epigraph, convex-hull, convex-hull-is-the-smallest-convex-set-containing, convex-hull-via-convex-combinations, convex-lecture-notes, convex-set, convex-sets-characterized-by-closure-under-convex-combinations, convexity-characterized-by-monotonicity-of-derivative, convexity-characterized-by-positive-semidefinite-hessian, convexity-of-the-marginal-optimal-value-function, convexity-on-a-convex-subset-via-extension, convexity-preserved-under-affine-composition, convexity-preserved-under-monotone-convex-composition, convexity-via-nonnegative-second-derivative, core-characterized-by-absorbing-translations, core-equals-interior-for-convex-sets-in-normed-spaces, core-of-a-convex-set-is-convex, direct-sum-of-subspaces, distance-function-to-a-set, domain-and-epigraph-proper-function, domain-of-a-convex-function-is-convex, dual-space-and-duality-pairing, equivalent-characterizations-of-convex-functions, existence-of-a-basis-hamel-basis, existence-of-a-functional-attaining-its-norm-at-a-point, extended-real-number-system-and-conventions, extension-of-a-linearly-independent-set-to-a-basis, fenchel-moreau-theorem, fenchel-young-inequality, hahn-banach-extension-dominated-by-a-seminorm-real-case... (163 total)

`thermodynamics`: absolute-temperature-scale, additivity-postulate, adiabatic-compressibility, adiabatic-wall, boltzmann-constant, boundary-condition-convention-lattice, canonical-ensemble-convention, chemical-equilibrium, chemical-potential-thermo, chemical-work-convention, clausius-inequality, clausius-statement-second-law, clausius-theorem-entropy, closed-system, construction-microcanonical-entropy-density-of-states, corollary-carnot-absolute-temperature, cyclic-process, diathermal-wall, energy-convexity-stability, energy-density, enthalpy, entropy-concavity-stability, entropy-density, entropy-normalization-convention, equation-of-state, euler-relation-thermodynamics, extensive-variable, extensivity-postulate, first-law-thermodynamics, fundamental-relation-energy, fundamental-relation-entropy, gibbs-duhem-relation, gibbs-duhem-theorem, gibbs-free-energy, grand-canonical-ensemble-convention, grand-potential, heat-capacity-constant-pressure, heat-capacity-constant-volume, heat-inexact-differential, helmholtz-free-energy, homogeneous-function-degree-one, intensive-variable, internal-energy-thermo, inverse-temperature-beta, irreversible-process, isolated-system, isothermal-compressibility, kelvin-planck-clausius-equivalence, kelvin-planck-statement, logarithm-convention-natural, maxwell-relation, maxwell-relations-theorem, mechanical-equilibrium, microcanonical-entropy-density, natural-units-convention, number-density, open-system, particle-number, path-function, pressure-thermo, pressure-volume-work-sign-convention, prop-entropy-concavity-energy, prop-free-energy-convexity-temperature, prop-grand-canonical-particle-number, quasistatic-process, response-function-thermo, reversible-process, second-law-thermodynamics, specific-quantity, state-function, state-variable, subadditivity-partition-function, superadditivity-entropy, surroundings-environment, system-boundary, temperature-thermo, tfae-thermodynamic-stability, thermal-equilibrium, thermal-expansion-coefficient, thermal-reservoir... (98 total)

`stat-mech`: boltzmann-entropy, boltzmann-entropy-microcanonical, boltzmann-equation-kinetic, boltzmann-h-theorem, bose-einstein-condensation, canonical-energy-fluctuation-identity, canonical-energy-identity, canonical-ensemble, carnot-efficiency-formula, carnot-theorem, chernoff-bounding-lemma, classical-harmonic-oscillator-example, clt-high-temperature-gibbs, cluster-expansion-convergence, cluster-expansion-theorem, cluster-integrals-mayer, connected-correlation-function, construction-bogoliubov-variational-bound, construction-canonical-from-microcanonical, construction-canonical-partition-function, construction-chemical-potential-from-entropy, construction-cluster-expansion, construction-connected-correlations-cumulants, construction-cumulant-generating-function, construction-dlr-specification, construction-entropy-maximization-thermal, construction-fluctuation-formulas-log-z, construction-free-energy-from-partition, construction-grand-canonical-partition-function, construction-infinite-volume-gibbs-weak-limit, construction-legendre-f-to-omega, construction-legendre-s-to-f, construction-legendre-u-to-g, construction-legendre-u-to-h, construction-mayer-expansion, construction-mean-field-variational, construction-observables-from-log-z, construction-pressure-from-entropy, construction-quantum-thermal-correlation, construction-reduced-density-matrix, construction-temperature-from-entropy, construction-transfer-matrix-1d, continuous-symmetry-on-spins, corollary-energy-fluctuations-cv, corollary-high-temp-exponential-decay, corollary-isentropic-adiabatic, corollary-kms-imaginary-time-periodicity, corollary-maxwell-standard-identities, corollary-multiple-gibbs-symmetry-breaking, corollary-relative-fluctuations-vanish, corollary-uniqueness-analyticity, correlation-function-two-point, correlation-length, covariance-observables-ensemble, critical-exponent, critical-point-phase-diagram, crooks-fluctuation-theorem, curie-weiss-model, debye-model, degenerate-fermi-gas, density-of-states, detailed-balance, dobrushin-uniqueness-theorem, donsker-varadhan-ldp, einstein-solid, ensemble-average, ensemble-equivalence-breakdown, ensemble-equivalence-theorem, ensemble-inequivalence-long-range, equipartition-theorem, euler-relation-theorem, exact-differential-criterion, example-ideal-gas-classical, exponential-decay-correlations-uniqueness, fekete-lemma, fkg-inequality, fluctuation-dissipation-theorem, fluctuation-observable, fluctuation-theorem-crooks, free-energy-difference-nonequilibrium... (183 total)

---

## Your Batch

Generate knowls for:
- dlr-existence-theorem
- prop-dlr-markov-property
- prop-extremal-gibbs-ergodic
- variational-principle-pressure-lattice