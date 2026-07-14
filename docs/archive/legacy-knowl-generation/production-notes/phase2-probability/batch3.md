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
NEVER place `{< knowl ... >}` inside LaTeX math (`$...$` or `$$...$$`).

### 3. Cross-Section Links MUST Include `section`
When linking to a knowl in a DIFFERENT section, you MUST specify the section parameter.

Same section (probability, no section param needed):
`{< knowl id="random-variable" text="random variable" >}`

Different section (section param REQUIRED):
`{< knowl id="measure-space" section="measure-theory" text="measure space" >}`
`{< knowl id="function" section="shared-foundations" text="function" >}`

### 4. Plain-Text Description
The `description` field in YAML must be plain text only. NO LaTeX.

### 5. Correct Shortcode Syntax
Use exactly double curly braces: `{<` and `>}`

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

**probability (current section - no section param needed):**
probability-measure, probability-space, event-probability, random-variable, random-vector, distribution-law, expectation, expectation-function-of-rv, conditional-expectation, conditional-probability, independence-events, independence-sigma-algebras, independence-random-variables, identically-distributed, iid-sequence, variance, covariance, correlation-coefficient, moment, moment-generating-function, characteristic-function-probability, cumulant-generating-function, cumulant, markov-inequality, chebyshev-inequality, chernoff-bound, weak-law-large-numbers, strong-law-large-numbers, central-limit-theorem, shannon-entropy, differential-entropy, relative-entropy-kl-divergence, gibbs-inequality-kl, total-variation-distance, pinsker-inequality, maximum-entropy-principle, radon-nikodym-theorem

**measure-theory (use section="measure-theory"):**
measure, measure-space, sigma-algebra, measurable-function, measurable-set, lebesgue-measure, lebesgue-integral, l1-function, lp-space, convergence-almost-everywhere, convergence-in-measure, dominated-convergence-theorem, fubinis-theorem

**shared-foundations (use section="shared-foundations"):**
function, set, subset, sequence, countable-set, bijective-function, real-numbers, natural-numbers

**real-analysis (use section="real-analysis"):**
supremum, infimum, limit-of-a-sequence, convergent-series, absolute-value, limit-superior, limit-inferior

---

## YOUR BATCH

Generate knowls for these slugs:

- conditional-expectation
- conditional-probability
- independence-events
- independence-sigma-algebras
