# Step 3: Create and Link Knowls (Parallelizable)

## Your Task

Create knowl markdown files **with cross-links already included**. You will receive:
1. The **full slug manifest** — all knowl slugs that will exist
2. Your **assigned batch** — the specific knowls you must create

Create each knowl in your batch with complete content and all relevant cross-links to other knowls in the manifest.

## Input

You will receive two sections:

### Slug Manifest

The complete list of all knowl slugs (provided for linking):
```
group.md
subgroup.md
normal-subgroup.md
coset.md
lagranges-theorem.md
...
```

### Your Batch

The specific items you must create (from the dependency-sorted list):
```
15. Definition: Coset
16. Theorem: Lagrange's Theorem
17. Definition: Normal Subgroup
...
```

## Output Format

For each item in your batch, produce a complete knowl with links:

~~~markdown
**`[slug].md`**
```markdown
---
title: "[Display Name]"
description: "[One-line plain-text description]"
---

[Content with {{</* knowl */>}} links already included]
```
~~~

### Filename Convention

Convert the name to a URL-friendly slug:
- Lowercase
- Replace spaces with hyphens
- Remove apostrophes, parentheses, and special characters
- Examples:
  - "Lagrange's Theorem" → `lagranges-theorem.md`
  - "Group" → `group.md`
  - "L^p spaces" → `lp-spaces.md`
  - "First Isomorphism Theorem" → `first-isomorphism-theorem.md`

## Linking Syntax

Use the Hugo knowl shortcode:
```
{{</* knowl id="[slug]" text="[display text]" */>}}
```

**CRITICAL:** The shortcode uses **double curly braces**: `{{<` not `{<`. Single braces will not render correctly.

Where:
- `[slug]` is the filename without `.md` (e.g., `group`, `lagranges-theorem`)
- `[display text]` is the text shown to the reader

### Linking Rules

**Link a term when:**
- It appears in prose/context sections
- It appears in example descriptions
- It is a key concept in the statement that benefits from expansion

**Do NOT link:**
- Terms inside LaTeX math environments (`$...$` or `$$...$$`)
- The term being defined in its own definition
- Every occurrence—link only the **first meaningful occurrence**
- Common English words that happen to match a mathematical term

**Display text variations:**
- `{{</* knowl id="group" text="group" */>}}` — singular
- `{{</* knowl id="group" text="groups" */>}}` — plural (same slug)
- `{{</* knowl id="abelian-group" text="abelian" */>}}` — adjective form if context clear

**Compound terms:**
- If the compound has its own knowl, link to that: `{{</* knowl id="normal-subgroup" text="normal subgroup" */>}}`
- If not, link the most specific available term

## Content Structure by Type

### For Definitions

```markdown
---
title: "[Name]"
description: "[Plain-text one-liner]"
---

A **[name]** is [formal definition using LaTeX notation].

[1-3 sentences of context with {{</* knowl */>}} links to prerequisite concepts]

**Examples:**
- [Concrete example with values/specifics]
- [Another example, possibly from a different context]
- [Optional: counterexample or edge case]
```

### For Axioms

```markdown
---
title: "[Name]"
description: "[Plain-text one-liner]"
---

The **[name]** [state the axiom(s) using LaTeX notation].

[1-2 sentences on the role of this axiom, with links to related concepts]
```

### For Theorems, Lemmas, Propositions

```markdown
---
title: "[Name]"
description: "[Plain-text one-liner]"
---

**[Name]**: [Precise statement of the result using LaTeX notation]

[1-3 sentences of context with {{</* knowl */>}} links to key concepts]

**Proof sketch** *(optional, include for major theorems)*:
[2-4 sentences outlining the key idea of the proof]
```

### For Corollaries

```markdown
---
title: "[Name]"
description: "[Plain-text one-liner]"
---

**[Name]**: [Statement of the corollary]

[1-2 sentences connecting this to its {{</* knowl */>}} linked parent theorem]
```

## Complete Example

Given slug manifest including: `group.md`, `subgroup.md`, `index-of-subgroup.md`, `lagranges-theorem.md`, `coset.md`

For batch item "15. Definition: Coset":

~~~markdown
**`coset.md`**
```markdown
---
title: "Coset"
description: "A translate of a subgroup by a group element"
---

A **left coset** of a {{</* knowl id="subgroup" text="subgroup" */>}} $H$ in a {{</* knowl id="group" text="group" */>}} $G$ is a set of the form
$$gH = \{gh : h \in H\}$$
for some $g \in G$. Similarly, a **right coset** is $Hg = \{hg : h \in H\}$.

Cosets partition the group $G$ into disjoint subsets of equal size. The number of distinct left cosets of $H$ in $G$ is called the {{</* knowl id="index-of-subgroup" text="index" */>}} of $H$ in $G$, denoted $[G:H]$.

**Examples:**
- In $\mathbb{Z}$ with subgroup $3\mathbb{Z}$, the cosets are $3\mathbb{Z}$, $1 + 3\mathbb{Z}$, and $2 + 3\mathbb{Z}$ (the residue classes mod 3)
- In $S_3$ with $H = \{e, (12)\}$, the left cosets are $H$, $(13)H = \{(13), (123)\}$, and $(23)H = \{(23), (132)\}$
- Left and right cosets can differ: in $S_3$, $(13)H = \{(13), (123)\}$ but $H(13) = \{(13), (132)\}$
```
~~~

**Links added:**
- `subgroup` — first occurrence, in prose
- `group` — first occurrence, in prose
- `index-of-subgroup` — references another concept

**Not linked:**
- $S_3$ — specific example, not a defined term
- "subgroup" in examples — already linked above

## Writing Guidelines

### Mathematical Notation

Use LaTeX with these delimiters:
- Inline math: `$...$`
- Display math: `$$...$$`

Standard conventions:
- Sets: uppercase letters ($A$, $B$, $G$, $V$)
- Elements: lowercase letters ($a$, $b$, $g$, $v$)
- Functions/maps: $f$, $g$, $\varphi$, $\psi$
- Fields: $\mathbb{F}$, $\mathbb{R}$, $\mathbb{C}$, $\mathbb{Q}$
- Common structures: $\mathbb{Z}$, $\mathbb{N}$, $\mathbb{R}^n$

### Precision and Rigor

- State definitions with complete logical precision
- Include all hypotheses in theorem statements
- Specify domains and codomains for functions
- Distinguish between "for all" and "there exists"
- Be explicit about what structure is being assumed

**Good**: "A **left coset** of $H$ in $G$ is a set of the form $gH = \{gh : h \in H\}$ for some $g \in G$."

**Bad**: "A coset is when you multiply a subgroup by an element."

### Brevity

- The formal definition/statement should be complete and self-contained
- Context paragraphs should be concise (aim for 2-3 sentences)
- Examples should be specific and illuminating, not exhaustive
- Do not include full proofs (only optional proof sketches)

### Level Appropriateness

Match the rigor to the course level:
- 300-level: Definitions can be slightly informal, focus on intuition
- 400-level: Full rigor, standard undergraduate analysis/algebra style
- 500-level: Graduate-level precision, measure-theoretic care, categorical language where appropriate

### Examples

Include 2-4 examples for definitions. Good examples:
- Start with the simplest non-trivial case
- Include a "standard" example that will recur
- Include an edge case or clarifying counterexample if helpful

## Processing Instructions

1. You have the **full slug manifest** — you can link to any slug in it
2. Process only the items in **your assigned batch**
3. For each item, create the knowl with all cross-links included
4. Only link to slugs that appear in the manifest
5. After producing all knowls, output: `Generated [N] knowls with links.`

## Parallelization

This step is designed for parallel execution:
- Multiple agents can process different batches simultaneously
- Each agent receives the same full slug manifest
- Each agent creates its assigned batch independently
- No inter-batch dependencies (linking uses the manifest, not other agents' output)

## Critical Formatting Rules

**YAML Front Matter:**
- `description` must be **plain text only** — no LaTeX, no math symbols
- Bad: `description: "The map $f: X \to Y$ satisfying..."`
- Good: `description: "A continuous map satisfying the universal property"`

**Shortcode Braces:**
- Use **exactly two** curly braces: `{{<` and `>}}`
- Triple braces `{{{<` will cause Hugo errors
- Single braces `{<` will not render

**LaTeX Escaping:**
- Do NOT escape asterisks in LaTeX: use `F^*` not `F^\*`
- Do NOT escape underscores in LaTeX: use `x_1` not `x\_1`

**No "Related" Sections:**
- Do NOT include a "Related" or "Related knowls" section at the end
- All cross-links must be woven naturally into the prose

## Verification

Before submitting, verify:
- [ ] No shortcodes appear inside `$...$` or `$$...$$` math blocks
- [ ] No LaTeX or math symbols in YAML `description` field
- [ ] Shortcodes use exactly double braces `{{<` and `>}}`
- [ ] No term is linked more than once per knowl
- [ ] Every slug in your shortcodes appears in the manifest
- [ ] Display text reads naturally in context
- [ ] The term being defined is NOT linked to itself
- [ ] No "Related" section at the end

## After Completion

All batches will be collected and passed to Step 4 for review.
