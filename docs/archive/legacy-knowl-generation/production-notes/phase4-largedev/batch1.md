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

All cross-links must be woven naturally into the prose.

### 2. NO Knowl Shortcodes Inside Math
NEVER place `{{< knowl ... >}}` inside LaTeX math (`$...$` or `$$...$$`).

### 3. Cross-Section Links MUST Include `section`
When linking to a knowl in a DIFFERENT section, you MUST specify the section parameter.

Same section (large-deviations, no section param needed):
`{{< knowl id="rate-function" text="rate function" >}}`

Different section (section param REQUIRED):
`{{< knowl id="random-variable" section="probability" text="random variable" >}}`
`{{< knowl id="convex-conjugate-fenchel" section="convex-analysis" text="Fenchel conjugate" >}}`

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

**large-deviations (current section - no section param needed):**
large-deviation-principle, rate-function, good-rate-function, exponential-tightness, log-moment-generating-function, cramer-transform, laplace-principle, varadhans-lemma, cramers-theorem, sanovs-theorem, gartner-ellis-theorem, contraction-principle-ldp

**probability (use section="probability"):**
probability-space, random-variable, expectation, iid-sequence, moment-generating-function, distribution-law

**convex-analysis (use section="convex-analysis"):**
convex-conjugate-fenchel, legendre-fenchel-transform, convex-set, convex-function-via-epigraph

**measure-theory (use section="measure-theory"):**
measure-space, probability-measure, lebesgue-integral

---

## YOUR BATCH

Generate knowls for these slugs:

- large-deviation-principle
- rate-function
- good-rate-function
- exponential-tightness
- log-moment-generating-function
- cramer-transform
