You are creating knowls (short definition/theorem cards) for a mathematics reference site.

For each slug below, generate a markdown file following these rules exactly.

---

## OUTPUT FORMAT

For each knowl, output:

**`slug-name.md`**
```markdown
---
title: "Display Title"
description: "One-line plain-text description (NO LaTeX)"
---

[Content here]
```

---

## CRITICAL RULES (MUST FOLLOW)

### 1. NO "Related" Sections
DO NOT include any of these at the end of a knowl:
- `## Related knowls`
- `## See also`
- `**Related knowls.**`
- Any list of "related" concepts

All cross-links must be woven naturally into the prose.

### 2. NO Knowl Shortcodes Inside Math
NEVER place `{{< knowl ... >}}` inside LaTeX math (`$...$` or `$$...$$`).

BAD: `Let $x \in {{< knowl id="open-ball" text="B(a,r)" >}}$`
GOOD: `Let $x \in B(a,r)$ be in the {{< knowl id="open-ball" text="open ball" >}}`

### 3. Cross-Section Links MUST Include `section`
When linking to a knowl in a DIFFERENT section, you MUST specify the section parameter.

Same section (no section param needed):
`{{< knowl id="subset" text="subset" >}}`

Different section (section param REQUIRED):
`{{< knowl id="ring" section="algebra-rings" text="ring" >}}`

### 4. Plain-Text Description
The `description` field in YAML must be plain text only. NO LaTeX.

### 5. Correct Shortcode Syntax
Use exactly double curly braces: `{{<` and `>}}`
- NOT `{<` (single brace)
- NOT `{{{<` (triple brace)

### 6. NO Proof Sketches
Do not include "Proof sketch" sections.

---

## CONTENT STRUCTURE

### For Definitions
```markdown
A **[term]** is [formal definition with LaTeX].

[1-2 sentences of context with cross-links to prerequisite concepts]

**Examples:**
- [Concrete example 1]
- [Concrete example 2]
```

### For Theorems/Axioms/Principles
```markdown
**[Name]:** [Precise statement with all hypotheses]

[1-2 sentences connecting to related concepts with cross-links]
```

---

## SECTION DIRECTORY REFERENCE

| Section | Content |
|---------|---------|
| `shared-foundations` | Set theory, logic, functions, relations |
| `linear-algebra` | Vector spaces, linear maps, matrices |
| `topology` | Topological spaces, metric spaces, compactness |
| `measure-theory` | Sigma-algebras, measures, Lebesgue |
| `real-analysis` | Real numbers, sequences, series, calculus |
| `algebra-groups` | Groups, subgroups, actions |
| `algebra-rings` | Rings, ideals, fields |

---

## AVAILABLE SLUGS

**Current section (real-analysis) - no section param needed:**
field-axioms, order-axioms, absolute-value, interval, bounded-above, bounded-below, supremum, infimum, maximum, minimum, monotone-sequence, subsequence, limit-superior, limit-inferior, limit-at-a-point, limit-at-infinity, one-sided-limit, series, partial-sums, convergent-series, divergent-series, absolutely-convergent-series, conditionally-convergent-series, cauchy-product, rearrangement-of-series, power-series, derivative, differentiability-1d, higher-derivatives, class-ck-function, local-extremum, taylor-polynomial, monotone-function, class-ck-map, differentiable-map, frechet-derivative, partial-derivative, directional-derivative, mixed-partial-derivative, jacobian-matrix, jacobian-determinant, gradient, hessian-matrix, critical-point, constraint-set, regular-point, regular-value, critical-value, diffeomorphism, implicitly-defined-function, discontinuity-point, set-of-discontinuities, partition-of-an-interval, tagged-partition, mesh-of-a-partition, refinement-of-a-partition, step-function, riemann-sum, upper-sum, lower-sum, oscillation, riemann-integrable-function, riemann-integral, riemann-stieltjes-integral, integrator-function, bounded-variation-function, total-variation, iterated-integral, multiple-riemann-integral, pointwise-convergence, uniform-convergence, uniform-cauchy, series-of-functions, uniform-convergence-on-compact-sets, supremum-norm, uniform-metric, space-of-continuous-functions, pointwise-bounded-family, uniformly-bounded-family, equicontinuity, equicontinuous-family, monotone-sequence-of-functions, polynomial, subalgebra-of-continuous-functions, separates-points, archimedean-property, completeness-axiom, completeness-equivalences, sup-inf-algebra, uniqueness-of-sup-inf, supremum-approximation-lemma, density-of-q, density-of-irrationals, limit-algebra-for-sequences, squeeze-theorem, cauchy-criterion-in-rk, limsup-liminf-properties, monotone-sequence-convergence-theorem, monotone-subsequence-lemma, comparison-test, limit-comparison-test, ratio-test, root-test, integral-test, alternating-series-test, cauchy-condensation-test, dirichlet-test, abel-test, abels-theorem, cauchy-hadamard-theorem, terms-go-to-zero, absolute-convergence-implies-convergence, absolute-convergence-implies-cauchy, mertens-theorem, rearrangement-theorem-absolute, riemann-rearrangement-theorem, power-series-analytic-on-disk, term-by-term-operations, term-by-term-differentiation, term-by-term-integration, power-series-uniform-convergence-on-compacts, differentiability-implies-continuity, differentiation-rules, rolles-theorem, mean-value-theorem, cauchy-mean-value-theorem, mean-value-estimate-lemma, derivative-zero-implies-constant, derivative-sign-implies-monotonicity, positive-derivative-implies-increasing, darboux-theorem, intermediate-value-theorem, inverse-function-theorem-1d, lhopitals-rule, second-derivative-tests, sufficient-condition-for-differentiability, differentiability-criterion, taylors-theorem-with-remainder, bounded-derivative-implies-uniform-continuity, chain-rule, mean-value-inequality, schwarz-clairaut-theorem, implicit-function-theorem, local-implicit-function-parameterization, inverse-function-theorem-rk, local-diffeomorphism-corollary, lagrange-multiplier-condition, lagrange-multipliers-theorem, global-extrema, riemann-linearity, riemann-algebra, composition-preserves-riemann-integrability, absolute-value-preserves-integrability, riemann-integrability-implies-boundedness, riemann-integrability-finite-discontinuities, riemann-integrability-monotone, oscillation-criterion, refinement-lemma-upper-lower-sums, riemann-integral-continuous-exists, mean-value-theorem-for-integrals, fundamental-theorem-of-calculus-i, fundamental-theorem-of-calculus-ii, integration-by-parts, substitution-rule, riemann-stieltjes-integrability-theorem, jordan-decomposition-lemma, integration-by-parts-riemann-stieltjes, riemann-stieltjes-linearity, fubini-theorem-riemann, change-of-variables-formula, weierstrass-m-test, uniform-limit-of-continuous-is-continuous, uniform-limit-of-integrable-functions, interchange-limit-integral, uniform-convergence-integration, uniform-convergence-differentiation, uniform-cauchy-iff-uniform-convergence, uniform-convergence-implies-pointwise, uniform-convergence-preserves-boundedness, uniform-convergence-supnorm, m-test-corollary, dinis-theorem, arzela-ascoli-theorem, weierstrass-approximation-theorem, stone-weierstrass-theorem, equicontinuity-boundedness-criterion, equicontinuity-dense-set-lemma


**shared-foundations:** set, empty-set, subset, proper-subset, union, intersection, complement, set-difference, symmetric-difference, power-set, ordered-pair, cartesian-product, indexed-family-of-sets, relation, equivalence-relation, equivalence-class, partition, quotient-set, function, domain, codomain, image, preimage, identity-function, restriction-of-a-function, composition, inverse-function, injective-function, surjective-function, bijective-function ... (50 total)

**linear-algebra:** vector-space, linear-map, linear-operator, bilinear-form, determinant, trace, eigenvalue, eigenvector, eigenspace, characteristic-polynomial, minimal-polynomial, inner-product, orthogonality, inner-product-space, norm, normed-vector-space, operator-norm, euclidean-space, euclidean-norm, banach-space, hilbert-space, compact-operator, rank-nullity-theorem, cauchy-schwarz-inequality, basis-existence-theorem, cayley-hamilton-theorem

**topology:** topological-space, topology, open-set, closed-set, interior, closure, neighborhood, limit-point, derived-set, dense-set, subspace-topology, continuous-map, homeomorphism, basis-of-topology, subbasis-of-topology, product-topology, quotient-topology, metric, metric-space, metric-induced-topology, open-ball, closed-ball, metric-sphere, diameter, bounded-set, separated-sets, convergent-sequence, cauchy-sequence, complete-metric-space, equivalent-metrics ... (87 total)

**measure-theory:** set-algebra, sigma-algebra, measurable-space, measurable-set, borel-sigma-algebra, measurable-function, indicator-function, simple-function, premeasure, measure, measure-space, outer-measure, caratheodory-measurable-set, null-set, almost-everywhere, jordan-content, measurable-rectangle, lebesgue-measure, caratheodory-construction, continuity-from-above-measure, continuity-from-below-measure, lebesgue-criterion-for-riemann-integrability


---

## YOUR BATCH

Generate knowls for these slugs:
- multiple-riemann-integral
- pointwise-convergence
- uniform-convergence
- uniform-cauchy
- series-of-functions
- uniform-convergence-on-compact-sets
- supremum-norm
- uniform-metric
- space-of-continuous-functions
- pointwise-bounded-family
- uniformly-bounded-family
- equicontinuity
- equicontinuous-family
- monotone-sequence-of-functions
- polynomial
- subalgebra-of-continuous-functions
- separates-points

---

## VERIFICATION BEFORE OUTPUT

For each knowl, verify:
- [ ] No "Related" section at the end
- [ ] No shortcodes inside `$...$` or `$$...$$`
- [ ] All cross-section links have `section` param
- [ ] `description` is plain text
- [ ] Shortcodes use `{{<` and `>}}`
- [ ] No proof sketch sections
