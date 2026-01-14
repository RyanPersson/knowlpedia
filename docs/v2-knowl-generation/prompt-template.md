# Knowl Generation Prompt Template v2

Use this template as the base for all knowl generation prompts. It includes all anti-pattern rules and style guidelines.

## Base Prompt

```markdown
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

BAD: `$f(x) = {{< knowl id="supremum" text="sup" >}} g(y)$`
GOOD: `$f(x) = \sup_y g(y)$, where $\sup$ denotes the {{< knowl id="supremum" text="supremum" >}}`

### 3. Cross-Section Links MUST Include `section`
When linking to a knowl in a DIFFERENT section, you MUST specify the section parameter.

Same section (no section param needed):
`{{< knowl id="subgroup" text="subgroup" >}}`

Different section (section param REQUIRED):
`{{< knowl id="ring" section="algebra-rings" text="ring" >}}`
`{{< knowl id="vector-space" section="linear-algebra" text="vector space" >}}`

### 4. Plain-Text Description
The `description` field in YAML must be plain text only. NO LaTeX.

BAD: `description: "The map $f: X \to Y$ satisfying..."`
GOOD: `description: "A continuous map satisfying the universal property"`

### 5. Correct Shortcode Syntax
Use exactly double curly braces: `{{<` and `>}}`
- NOT `{<` (single brace - won't render)
- NOT `{{{<` (triple brace - causes errors)

### 6. NO Proof Sketches
Do not include "Proof sketch" sections. Knowls should be concise reference cards.

If a key insight is essential, use this format instead:
`**Key insight:** The proof uses [brief explanation].`

---

## CONTENT STRUCTURE

### For Definitions
```markdown
A **[term]** is [formal definition with LaTeX].

[1-2 sentences of context with cross-links to prerequisite concepts]

**Examples:**
- [Concrete example 1]
- [Concrete example 2]
- [Optional: edge case or counterexample]
```

### For Theorems/Lemmas/Propositions
```markdown
**[Name]:** [Precise statement with all hypotheses]

[1-2 sentences connecting to related concepts with cross-links]
```

### For Corollaries
```markdown
**[Name]:** [Statement of the corollary]

This follows from {{< knowl id="parent-theorem" text="[parent theorem]" >}}.
```


### Examples Guidelines

Include examples ONLY if they are:
- **Canonical**: The standard example everyone should know (e.g., $[0,1]$ for compact sets in $\mathbb{R}$)
- **Illuminating**: Clarifies a subtle point or common misconception
- **Contrasting**: A counterexample that sharpens the definition

Omit the **Examples:** section entirely for straightforward concepts where the definition speaks for itself. Not every knowl needs examples.

---

## LINKING GUIDELINES

**Link a term when:**
- First meaningful occurrence in prose
- Key concept that benefits from expansion
- Term in example descriptions

**Do NOT link:**
- Inside LaTeX math blocks
- The term being defined in its own definition
- Every occurrence (link only first)
- Common words that happen to match a term

**Plural/variant forms:**
- `{{< knowl id="group" text="groups" >}}` — plural uses same slug
- `{{< knowl id="abelian-group" text="abelian" >}}` — adjective form if context clear

---

## SECTION DIRECTORY REFERENCE

Use these exact section names for cross-links:

| Section | Content |
|---------|---------|
| `shared-foundations` | Set theory, logic, functions, relations |
| `linear-algebra` | Vector spaces, linear maps, matrices |
| `algebra-groups` | Groups, subgroups, actions |
| `algebra-rings` | Rings, ideals, fields |
| `algebra-modules` | Modules, exact sequences, tensor products |
| `algebra-fields-galois` | Field extensions, Galois theory |
| `algebra-commutative` | Localization, Noetherian, spectrum |
| `algebra-category-theory` | Categories, functors |
| `algebra-homological` | Chain complexes, Ext/Tor |
| `algebra-representation-theory` | Representations, characters |
| `analysis` | Real analysis, metric spaces |
| `convex-analysis` | Convex sets, functions |
| `fiber-bundles` | Fiber bundles, connections |
| `lie-groups` | Lie groups, Lie algebras |

---

## AVAILABLE SLUGS

**Current section ({SECTION_NAME}) - no section param needed:**
{CURRENT_SLUGS}

**Other sections - MUST use section param:**

**shared-foundations:** {SHARED_FOUNDATIONS_SLUGS}

**linear-algebra:** {SHARED_LINEAR_ALGEBRA_SLUGS}

**algebra-groups:** {ALGEBRA_GROUPS_SLUGS}

**algebra-rings:** {ALGEBRA_RINGS_SLUGS}

[... include all relevant prerequisite sections ...]

---

## YOUR BATCH

Generate knowls for these slugs:
{BATCH_SLUGS}

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
```

## Usage

1. Copy the base prompt
2. Fill in the placeholders:
   - `{SECTION_NAME}` - The section being generated (e.g., `algebra-modules`)
   - `{CURRENT_SLUGS}` - All slugs in the current section
   - `{SHARED_FOUNDATIONS_SLUGS}` - Slugs from shared-foundations
   - `{BATCH_SLUGS}` - The specific slugs for this batch (20-25 max)
3. Include only prerequisite sections that this section depends on
4. Run via Oracle or direct LLM API

## Batch Sizing

- **20-25 slugs per batch** for reliable generation
- **6 parallel batches max** when using Oracle
- Larger batches increase chance of format errors
