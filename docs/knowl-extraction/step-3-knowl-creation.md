# Step 3: Create Knowl Content from Extracted Items

## Your Task

Transform the extracted items and prerequisites from Steps 1-2 into properly formatted knowl markdown files. For extracted items, preserve the author's formulation while standardizing format. For prerequisites, create appropriate definitions.

## Input

You will receive:
1. **Extraction report from Step 1** — containing original text for each extracted item
2. **Dependency-sorted sequence from Step 2** — the order to process items, with `[P]` and `[E:N]` markers

## Output Format

For each item in the sorted sequence, produce a markdown code block:

~~~markdown
**`[slug].md`** [P] or [E:N]
```markdown
---
title: "[Display Name]"
description: "[One-line plain-text description]"
---

[Content following the structure below]
```
~~~

For extracted items, you may optionally note the source in a comment or at the end of the description.

## Processing Rules by Item Type

### For Prerequisites (`[P]`)

Create standard knowl content from scratch:

```markdown
---
title: "[Name]"
description: "[Plain-text one-liner]"
---

A **[name]** is [standard mathematical definition in LaTeX].

[1-2 sentences of context]

**Examples:**
- [Example]
- [Example]
```

Use standard, widely-accepted definitions. Match the rigor level of the source notes.

### For Extracted Items (`[E:N]`)

Transform the extracted content while preserving the author's formulation:

#### Step A: Retrieve Original Text
Look up item N in the Step 1 extraction report.

#### Step B: Standardize Format

**Preserve:**
- The author's mathematical formulation
- Their notation choices
- Their phrasing (when rigorous)
- Any distinctive perspective or approach

**Standardize:**
- Convert to consistent LaTeX delimiters (`$...$` and `$$...$$`)
- Normalize whitespace and formatting
- Add front matter
- Add section structure (Examples, Proof sketch if appropriate)

#### Step C: Enhance (Minimally)

**Add only if missing:**
- Examples (if the source lacks them)
- Brief context sentence (if the statement is bare)
- Proof sketch for major theorems (if not implicit)

**Do NOT:**
- Rewrite mathematically correct definitions in different words
- Add extensive commentary not in the original
- Change the author's notation without reason
- Add formality beyond the source's level

## Content Structure Templates

### Definition (Extracted)

```markdown
---
title: "[Name]"
description: "[Plain-text description]"
---

A **[name]** is [author's definition, formatted consistently].

[Context from source, or minimal addition if source is bare]

**Examples:**
[From source if provided, or add 1-2 appropriate examples]
```

### Theorem/Lemma/Proposition (Extracted)

```markdown
---
title: "[Name]"
description: "[Plain-text description]"
---

**[Name]**: [Author's statement, formatted consistently]

[Context from source if any]

**Proof sketch** *(if included or summarizable)*:
[Author's proof outline, or brief description of approach]
```

### Corollary (Extracted)

```markdown
---
title: "[Name]"
description: "[Plain-text description]"
---

**[Name]**: [Author's statement]

[Connection to parent theorem]
```

## Notation Normalization

Apply consistent notation while respecting the source:

| Source Notation | Normalized | When to Change |
|-----------------|------------|----------------|
| `\mathbb R` | `\mathbb{R}` | Always (syntax) |
| `f: A→B` | `f: A \to B` | Always (LaTeX) |
| `x ε A` | `x \in A` | Always (wrong symbol) |
| `|G|` vs `\#G` vs `o(G)` | Keep source choice | Only if inconsistent within notes |
| `⊂` for non-strict | Note in conventions | Don't silently change |

### Notation Conventions Section

If the source uses non-standard notation, create a conventions knowl:

```markdown
**`notation-conventions.md`** [P]
```markdown
---
title: "Notation Conventions"
description: "Notation used throughout these notes"
---

The following **notation conventions** are used:

- $\subset$ denotes subset (not necessarily proper)
- $\mathbb{N}$ includes zero
- $\cong$ denotes isomorphism
- $\trianglelefteq$ denotes normal subgroup
```

## Handling Informal Source Content

### Informal Definitions

If the source is informal, formalize while preserving intent:

**Source:**
> "A group is basically a set with a multiplication that's nice — you can always undo things and there's an identity."

**Knowl:**
```markdown
A **group** is a set $G$ equipped with a binary operation $\cdot: G \times G \to G$ satisfying:

1. **Associativity**: $(a \cdot b) \cdot c = a \cdot (b \cdot c)$ for all $a, b, c \in G$
2. **Identity**: There exists $e \in G$ such that $e \cdot a = a \cdot e = a$ for all $a \in G$
3. **Inverses**: For each $a \in G$, there exists $a^{-1} \in G$ such that $a \cdot a^{-1} = a^{-1} \cdot a = e$

*Note: Formalized from informal description in source.*
```

### Missing Hypotheses

If the source omits hypotheses that are clear from context:

**Source:**
> "Theorem: A continuous function on [a,b] attains its maximum."

**Knowl:**
```markdown
**Extreme Value Theorem**: Let $f: [a,b] \to \mathbb{R}$ be continuous on the closed bounded interval $[a,b]$. Then $f$ attains its maximum and minimum values; that is, there exist $c, d \in [a,b]$ such that $f(c) \leq f(x) \leq f(d)$ for all $x \in [a,b]$.

*Note: Hypotheses (closed, bounded, real-valued) made explicit.*
```

## Example Transformation

**From Step 1 Extraction:**
```markdown
### 5. Definition: Coset
**Source location:** Lecture 3, page 12
**Original text:**
> If H ≤ G and g ∈ G, the left coset of H containing g is gH = {gh : h ∈ H}.
> Right cosets Hg defined similarly.

**Extracted name:** Coset
**Dependencies noted:** group, subgroup
```

**Knowl Output:**
~~~markdown
**`coset.md`** [E:5]
```markdown
---
title: "Coset"
description: "A translate of a subgroup by a group element"
---

A **left coset** of a subgroup $H$ in a group $G$ is a set of the form
$$gH = \{gh : h \in H\}$$
for some $g \in G$. The **right coset** is defined similarly as $Hg = \{hg : h \in H\}$.

Cosets are the equivalence classes of the relation $a \sim b \iff a^{-1}b \in H$. They partition $G$ into disjoint subsets of equal cardinality.

**Examples:**
- In $\mathbb{Z}$ with $H = n\mathbb{Z}$, the cosets are the residue classes $\{0, 1, \ldots, n-1\} + n\mathbb{Z}$
- In $S_3$ with $H = \langle (12) \rangle$, the left cosets are $H$, $(13)H$, and $(23)H$
```
~~~

## Batch Processing

For large note sets, process in batches:
- Batch 1: Prerequisites (`[P]` items)
- Batch 2: Extracted items 1-20
- Batch 3: Extracted items 21-40
- etc.

Each batch should produce all knowls in that range.

## Validation

Before submitting each knowl:

- [ ] Front matter is complete (title, description)
- [ ] LaTeX delimiters are consistent (`$...$` and `$$...$$`)
- [ ] Definition/theorem statement is complete and precise
- [ ] Examples are included (for definitions)
- [ ] Author's formulation is preserved where appropriate
- [ ] Slug follows naming convention (lowercase, hyphens)

## After Completion

Once all knowls are created, they will be passed to Step 4 for cross-linking. Do not add `{{</* knowl */>}}` shortcodes—output standalone knowl content only.
