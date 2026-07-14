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
`{{< knowl id="lebesgue-measure" text="Lebesgue measure" >}}`

Different section (section param REQUIRED):
`{{< knowl id="function" section="shared-foundations" text="function" >}}`
`{{< knowl id="supremum" section="real-analysis" text="supremum" >}}`

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

**Examples:**
- [Concrete example 1]
- [Concrete example 2]
```

### For Theorems
```markdown
**[Name]:** [Precise statement with all hypotheses]

[1-2 sentences connecting to related concepts with cross-links]
```

---

## AVAILABLE SLUGS BY SECTION

**measure-theory (current section - no section param needed):**
almost-everywhere, borel-sigma-algebra, caratheodory-construction, caratheodory-measurable-set, characteristic-function-indicator-function, indicator-function, lebesgue-measure, measurable-function, measurable-rectangle, measurable-set, measurable-space, measure, measure-space, null-set, outer-measure, premeasure, sigma-algebra, simple-function

**shared-foundations (use section="shared-foundations"):**
function, set, subset, union, intersection, cartesian-product, sequence, countable-set, bijective-function, injective-function, surjective-function, equivalence-relation, equivalence-class, upper-bound, lower-bound

**real-analysis (use section="real-analysis"):**
supremum, infimum, limit-of-a-sequence, convergent-series, absolute-value, interval, bounded-above, bounded-below, continuity-via-sequences, uniform-convergence, pointwise-convergence

**All slugs being generated in this batch (measure-theory, no section param):**
ae-equality, lebesgue-integrable-function, lebesgue-integral-nonnegative, lebesgue-integral, l1-function, l-infinity-function, essential-supremum, lp-norm, lp-space, convergence-almost-everywhere, convergence-in-measure, convergence-in-lp, uniform-integrability, product-measure, pushforward-measure, change-of-variables-pushforward, monotone-convergence-theorem, fatous-lemma, dominated-convergence-theorem, tonellis-theorem, fubinis-theorem, jensen-inequality-integral, minkowski-inequality-lp

---

## YOUR BATCH

Generate knowls for these slugs:

- ae-equality
- lebesgue-integrable-function
- lebesgue-integral-nonnegative
- lebesgue-integral
- l1-function
