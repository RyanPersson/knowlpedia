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

Same section (convex-analysis, no section param needed):
`{{< knowl id="convex-set" text="convex set" >}}`

Different section (section param REQUIRED):
`{{< knowl id="function" section="shared-foundations" text="function" >}}`
`{{< knowl id="infimum" section="real-analysis" text="infimum" >}}`

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

**convex-analysis (current section - no section param needed):**
convex-set, convex-function-via-epigraph, convex-hull, convex-combination, hyperplane, separation-by-a-hyperplane, subadditive-positively-homogeneous-and-sublinear-functions, domain-and-epigraph-proper-function, strictly-convex-function, convex-conjugate-fenchel, legendre-transform, legendre-fenchel-transform, biconjugate, closed-convex-function, subdifferential, subgradient, supporting-hyperplane-convex-function, fenchel-young-inequality, fenchel-moreau-theorem, convex-duality-primal-dual

**shared-foundations (use section="shared-foundations"):**
function, set, subset, real-numbers, infimum, supremum

**real-analysis (use section="real-analysis"):**
infimum, supremum, derivative, differentiable-map, continuous-function

---

## YOUR BATCH

Generate knowls for these slugs:

- convex-conjugate-fenchel
- legendre-transform
- legendre-fenchel-transform
- biconjugate
- closed-convex-function
- subdifferential
