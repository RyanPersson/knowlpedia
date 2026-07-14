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
`{{< knowl id="open-set" text="open set" >}}`

Different section (section param REQUIRED):
`{{< knowl id="function" section="shared-foundations" text="function" >}}`
`{{< knowl id="vector-space" section="linear-algebra" text="vector space" >}}`

### 4. Plain-Text Description
The `description` field in YAML must be plain text only. NO LaTeX.

### 5. Correct Shortcode Syntax
Use exactly double curly braces: `{{<` and `>}}`

### 6. NO Proof Sketches
Do not include "Proof sketch" sections.

---

## CONTENT STRUCTURE

### For Definitions
```markdown
A **[term]** is [formal definition with LaTeX].

[1-2 sentences of context with cross-links to prerequisite concepts]

**Examples:** (only if needed - see guidelines below)
- [Concrete example]
```

### For Theorems/Lemmas/Propositions
```markdown
**[Name]:** [Precise statement with all hypotheses]

[1-2 sentences connecting to related concepts with cross-links]
```

---

## EXAMPLES GUIDELINES (IMPORTANT)

Include examples ONLY if they are:
- **Canonical**: The standard example everyone should know (e.g., $[0,1]$ for compact sets)
- **Illuminating**: Clarifies a subtle point or common misconception
- **Contrasting**: A counterexample that sharpens the definition

**Omit the Examples section entirely** for straightforward concepts where the definition speaks for itself. Not every knowl needs examples.

---

## LINKING GUIDELINES

**Link a term when:**
- First meaningful occurrence in prose
- Key concept that benefits from expansion

**Do NOT link:**
- Inside LaTeX math blocks
- The term being defined in its own definition
- Every occurrence (link only first)

---

## AVAILABLE SLUGS

**Current section (topology-connectedness) - no section param needed:**
connected-set, connected-component, path, path-connected-set, continuous-image-of-connected-set-is-connected, connected-subsets-of-r-are-intervals, connectedness-criteria-r, image-compact-connected-is-interval, curve, intermediate-value-property-topological

**Other topology sections - MUST use section param:**

**topology-core:** topological-space, topology, topology-axioms, open-set, closed-set, interior, closure, neighborhood, limit-point-accumulation-point-cluster-point, derived-set, dense-set, dense-subset, subspace-topology, continuous-map, continuity-via-open-sets, homeomorphism, basis-of-a-topology, topology-generated-by-basis, subbasis-of-a-topology, product-topology, quotient-topology, cover

**topology-metric:** metric, metric-space, metric-induced-topology, open-ball, closed-ball, sphere-metric-sphere, diameter, bounded-set, separated-sets, convergent-sequence, limit-of-a-sequence, cauchy-sequence, every-cauchy-sequence-is-bounded, convergent-sequence-is-cauchy, complete-metric-space, equivalent-metrics, isometry, uniformly-continuous-map, lipschitz-continuity, holder-continuity, cantor-intersection-theorem, nested-interval-theorem, bolzano-weierstrass-theorem

**topology-compactness:** open-cover, refinement-of-an-open-cover, finite-subcover-lemma, compact-set, compactness-implies-boundedness, compactness-implies-closedness, closed-subset-of-compact-set-is-compact, continuous-image-of-compact-set-is-compact, continuous-attains-max-min-compact, finite-intersection-property-theorem, sequentially-compact-set, sequential-compactness-equals-compactness, total-boundedness-epsilon-nets, totally-bounded-set, totally-bounded-cauchy-subsequence, compactness-implies-total-boundedness, compactness-implies-completeness, compact-iff-complete-totally-bounded, heine-borel-theorem, lebesgue-number-lemma, lebesgue-number-lemma-auxiliary-refinement, compactness-of-graphs-lemma, continuous-bijection-from-compact-homeomorphism-criterion, continuous-image-compact-closed-bounded, compact-subset-of-hausdorff-is-closed, compactness-criteria-rk

**topology-separation:** t0-space, t1-space, hausdorff-space, sequential-characterization-of-closed-sets, sequential-characterization-of-closure, uniqueness-of-limits-hausdorff

**topology-baire:** baire-space, baire-category-theorem, nowhere-dense-set, meager-set, residual-set, complete-metric-space-is-baire, intersection-of-dense-open-is-dense, category-argument-template

**shared-foundations - MUST use section param:**
axiom-of-choice, bijective-function, binary-operation, cardinality, cartesian-product, codomain, complement, composition, countable-set, domain, empty-set, equivalence-class, equivalence-relation, function, identity-function, image, injective-function, intersection, inverse-function, lower-bound, mathematical-induction, morphism, ordered-pair, partial-order, partition, preimage, proper-subset, quotient-set, relation, set, set-difference, subset, surjective-function, total-order, union, upper-bound, well-ordered-set, well-ordering-principle, well-ordering-theorem, zfc-axioms, zorns-lemma

**linear-algebra - MUST use section param:**
banach-space, basis-existence-theorem, bilinear-form, cayley-hamilton-theorem, characteristic-polynomial, compact-operator, determinant, eigenspace, eigenvalue, eigenvector, euclidean-norm, euclidean-space, hilbert-space, inner-product, inner-product-space, linear-map, linear-operator, minimal-polynomial, norm, operator-norm, orthogonality, rank-nullity-theorem, trace, vector-space

---

## YOUR BATCH

Generate knowls for these slugs:
- connected-set
- connected-component
- path
- path-connected-set
- continuous-image-of-connected-set-is-connected
- connected-subsets-of-r-are-intervals
- connectedness-criteria-r
- image-compact-connected-is-interval
- curve
- intermediate-value-property-topological

---

## VERIFICATION BEFORE OUTPUT

For each knowl, verify:
- [ ] No "Related" section at the end
- [ ] No shortcodes inside `$...$` or `$$...$$`
- [ ] All cross-section links have `section` param
- [ ] `description` is plain text
- [ ] Shortcodes use `{{<` and `>}}`
- [ ] No proof sketch sections
- [ ] Examples are canonical/illuminating (or omitted if unnecessary)
