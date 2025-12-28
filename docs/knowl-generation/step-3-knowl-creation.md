# Step 3: Create Knowl Content

## Your Task

For each item in the dependency-sorted list from Step 2, create a complete knowl markdown file. Process items **in order**, producing one markdown code block per knowl.

## Input

You will receive the dependency-sorted sequence from Step 2:
```
1. [Type]: [Name]
2. [Type]: [Name]
...
```

## Output Format

For each item, produce a markdown code block labeled with the filename:

~~~markdown
**`[slug].md`**
```markdown
---
title: "[Display Name]"
description: "[One-line plain-text description]"
---

[Content following the structure below]
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

## Content Structure by Type

### For Definitions

```markdown
---
title: "[Name]"
description: "[Plain-text one-liner]"
---

A **[name]** is [formal definition using LaTeX notation].

[1-3 sentences of context: What is this object? Where does it arise? Why is it important?]

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

[1-2 sentences on the role of this axiom in the theory]
```

### For Theorems, Lemmas, Propositions

```markdown
---
title: "[Name]"
description: "[Plain-text one-liner]"
---

**[Name]**: [Precise statement of the result using LaTeX notation]

[1-3 sentences of context: Why is this result important? What does it tell us?]

**Proof sketch** *(optional, include for major theorems)*:
[2-4 sentences outlining the key idea of the proof, not a full proof]
```

### For Corollaries

```markdown
---
title: "[Name]"
description: "[Plain-text one-liner]"
---

**[Name]**: [Statement of the corollary]

[1-2 sentences connecting this to its parent theorem]
```

## Writing Guidelines

### 1. Mathematical Notation

Use LaTeX with these delimiters:
- Inline math: `$...$`
- Display math: `$$...$$`

Standard conventions:
- Sets: uppercase letters ($A$, $B$, $G$, $V$)
- Elements: lowercase letters ($a$, $b$, $g$, $v$)
- Functions/maps: $f$, $g$, $\varphi$, $\psi$
- Fields: $\mathbb{F}$, $\mathbb{R}$, $\mathbb{C}$, $\mathbb{Q}$
- Common structures: $\mathbb{Z}$, $\mathbb{N}$, $\mathbb{R}^n$

### 2. Precision and Rigor

- State definitions with complete logical precision
- Include all hypotheses in theorem statements
- Specify domains and codomains for functions
- Distinguish between "for all" and "there exists"
- Be explicit about what structure is being assumed

**Good**: "A **left coset** of $H$ in $G$ is a set of the form $gH = \{gh : h \in H\}$ for some $g \in G$."

**Bad**: "A coset is when you multiply a subgroup by an element."

### 3. Brevity

- The formal definition/statement should be complete and self-contained
- Context paragraphs should be concise (aim for 2-3 sentences)
- Examples should be specific and illuminating, not exhaustive
- Do not include full proofs (only optional proof sketches)

### 4. Level Appropriateness

Match the rigor to the course level:
- 300-level: Definitions can be slightly informal, focus on intuition
- 400-level: Full rigor, standard undergraduate analysis/algebra style
- 500-level: Graduate-level precision, measure-theoretic care, categorical language where appropriate

### 5. Examples

Include 2-4 examples for definitions. Good examples:
- Start with the simplest non-trivial case
- Include a "standard" example that will recur
- Include an edge case or clarifying counterexample if helpful

## Example Output

For item "7. Definition: Coset":

~~~markdown
**`coset.md`**
```markdown
---
title: "Coset"
description: "A translate of a subgroup by a group element"
---

A **left coset** of a subgroup $H$ in a group $G$ is a set of the form
$$gH = \{gh : h \in H\}$$
for some $g \in G$. Similarly, a **right coset** is $Hg = \{hg : h \in H\}$.

Cosets partition the group $G$ into disjoint subsets of equal size. The number of distinct left cosets of $H$ in $G$ is called the index of $H$ in $G$, denoted $[G:H]$.

**Examples:**
- In $\mathbb{Z}$ with subgroup $3\mathbb{Z}$, the cosets are $3\mathbb{Z}$, $1 + 3\mathbb{Z}$, and $2 + 3\mathbb{Z}$ (the residue classes mod 3)
- In $S_3$ with $H = \{e, (12)\}$, the left cosets are $H$, $(13)H = \{(13), (123)\}$, and $(23)H = \{(23), (132)\}$
- Left and right cosets can differ: in $S_3$, $(13)H = \{(13), (123)\}$ but $H(13) = \{(13), (132)\}$
```
~~~

For item "15. Theorem: Lagrange's Theorem":

~~~markdown
**`lagranges-theorem.md`**
```markdown
---
title: "Lagrange's Theorem"
description: "The order of a subgroup divides the order of the group"
---

**Lagrange's Theorem**: Let $G$ be a finite group and $H \leq G$ a subgroup. Then $|H|$ divides $|G|$, and
$$|G| = |H| \cdot [G:H].$$

This fundamental result constrains what subgroups can exist in a finite group. It implies that the order of any element must divide the order of the group.

**Proof sketch**: The left cosets of $H$ partition $G$ into disjoint subsets, each of size $|H|$. Therefore $|G| = (\text{number of cosets}) \cdot |H|$.
```
~~~

## Processing Instructions

1. Process items **in the order given** (this respects dependencies)
2. Produce **one .md code block per knowl**
3. After producing all knowls, output a summary line: `Generated [N] knowls.`
4. **Do not add cross-references yet**—that happens in Step 4

## Batch Processing

If the list is long, you may be asked to process items in batches (e.g., items 1-20, then 21-40). Process whatever range you are given and stop at the end of that range.

## After Completion

Once all knowls are created, they will be passed to Step 4 for cross-linking. 
