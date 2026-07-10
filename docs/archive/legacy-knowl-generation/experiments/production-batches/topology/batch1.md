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

**Current section (topology) - no section param needed:**
topological-space, topology, open-set, closed-set, interior, closure, neighborhood, limit-point, derived-set, dense-set, subspace-topology, continuous-map, homeomorphism, basis-of-topology, subbasis-of-topology, product-topology, quotient-topology, metric, metric-space, metric-induced-topology, open-ball, closed-ball, metric-sphere, diameter, bounded-set, separated-sets, convergent-sequence, cauchy-sequence, complete-metric-space, equivalent-metrics, isometry, uniformly-continuous-map, lipschitz-continuity, holder-continuity, cover, open-cover, refinement-of-open-cover, compact-set, sequentially-compact-set, totally-bounded-set, epsilon-net, relatively-compact-set, finite-intersection-property, connected-set, connected-component, path, curve, path-connected-set, t0-space, t1-space, hausdorff-space, baire-space, nowhere-dense-set, meager-set, residual-set, cauchy-sequence-is-bounded, convergent-sequence-is-cauchy, cantor-intersection-theorem, nested-interval-theorem, bolzano-weierstrass-theorem, finite-intersection-property-theorem, compactness-implies-boundedness, compactness-implies-closedness, closed-subset-of-compact-set-is-compact, continuous-image-of-compact-set-is-compact, continuous-attains-max-min-compact, sequential-compactness-equals-compactness, totally-bounded-cauchy-subsequence, compactness-implies-total-boundedness, compactness-implies-completeness, compact-iff-complete-totally-bounded, heine-borel-theorem, lebesgue-number-lemma, compactness-of-graphs-lemma, compact-to-hausdorff-homeomorphism-criterion, compact-subset-of-hausdorff-is-closed, continuous-image-of-connected-set-is-connected, connected-subsets-of-r-are-intervals, connectedness-criteria-r, image-compact-connected-is-interval, sequential-characterization-closed, sequential-characterization-closure, uniqueness-of-limits-hausdorff, baire-category-theorem, complete-metric-space-is-baire, intersection-of-dense-open-is-dense, category-argument-template


**shared-foundations:** set, empty-set, subset, proper-subset, union, intersection, complement, set-difference, symmetric-difference, power-set, ordered-pair, cartesian-product, indexed-family-of-sets, relation, equivalence-relation, equivalence-class, partition, quotient-set, function, domain, codomain, image, preimage, identity-function, restriction-of-a-function, composition, inverse-function, injective-function, surjective-function, bijective-function ... (50 total)

**linear-algebra:** vector-space, linear-map, linear-operator, bilinear-form, determinant, trace, eigenvalue, eigenvector, eigenspace, characteristic-polynomial, minimal-polynomial, inner-product, orthogonality, inner-product-space, norm, normed-vector-space, operator-norm, euclidean-space, euclidean-norm, banach-space, hilbert-space, compact-operator, rank-nullity-theorem, cauchy-schwarz-inequality, basis-existence-theorem, cayley-hamilton-theorem

**measure-theory:** set-algebra, sigma-algebra, measurable-space, measurable-set, borel-sigma-algebra, measurable-function, indicator-function, simple-function, premeasure, measure, measure-space, outer-measure, caratheodory-measurable-set, null-set, almost-everywhere, jordan-content, measurable-rectangle, lebesgue-measure, caratheodory-construction, continuity-from-above-measure, continuity-from-below-measure, lebesgue-criterion-for-riemann-integrability

**real-analysis:** field-axioms, order-axioms, absolute-value, interval, bounded-above, bounded-below, supremum, infimum, maximum, minimum, monotone-sequence, subsequence, limit-superior, limit-inferior, limit-at-a-point, limit-at-infinity, one-sided-limit, series, partial-sums, convergent-series, divergent-series, absolutely-convergent-series, conditionally-convergent-series, cauchy-product, rearrangement-of-series, power-series, derivative, differentiability-1d, higher-derivatives, class-ck-function ... (187 total)


---

## YOUR BATCH

Generate knowls for these slugs:
- topological-space
- topology
- open-set
- closed-set
- interior
- closure
- neighborhood
- limit-point
- derived-set
- dense-set
- subspace-topology
- continuous-map
- homeomorphism
- basis-of-topology
- subbasis-of-topology
- product-topology
- quotient-topology

---

## VERIFICATION BEFORE OUTPUT

For each knowl, verify:
- [ ] No "Related" section at the end
- [ ] No shortcodes inside `$...$` or `$$...$$`
- [ ] All cross-section links have `section` param
- [ ] `description` is plain text
- [ ] Shortcodes use `{{<` and `>}}`
- [ ] No proof sketch sections
