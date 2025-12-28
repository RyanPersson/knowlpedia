# Step 1: Extract Definitions, Theorems, and Lemmas from Lecture Notes

## Your Task

Parse the provided lecture notes and extract all definitions, theorems, lemmas, propositions, corollaries, and axioms. Preserve the original mathematical content while cataloging each item.

## Input

You will receive:
- **Lecture notes**: One or more documents (markdown, LaTeX, PDF text, or plain text)
- **Source format**: The format of the input (to guide parsing)
- **Course context** (optional): Subject name, level, instructor conventions

## Output Format

Produce a markdown document cataloging all extracted items:

```markdown
# Extraction Report: [Course/Notes Title]

## Extraction Summary
- Total items extracted: [N]
- Definitions: [X]
- Axioms: [X]
- Theorems: [X]
- Lemmas: [X]
- Propositions: [X]
- Corollaries: [X]

## Extracted Items

### 1. [Type]: [Name or Description]
**Source location:** [Page/Section/Lecture reference]
**Original text:**
> [Exact quote from source, preserving formatting]

**Extracted name:** [Canonical name to use]
**Dependencies noted:** [Any terms referenced that need their own knowls]

---

### 2. [Type]: [Name or Description]
...
```

## Extraction Guidelines

### 1. Identifying Items

Look for explicit markers in the source:

| Marker Type | Examples |
|-------------|----------|
| Labeled blocks | "Definition 3.1", "Theorem (Lagrange)", "Lemma:" |
| Typography | Bold/italic terms being defined, boxed theorems |
| Language cues | "We define...", "We say that...", "Recall that..." |
| Structure | Numbered/labeled environments in LaTeX |

Also extract **implicit definitions**:
- "Let X be a [new term]..." when introducing terminology
- "A [term] is said to be [property] if..."
- "By [term] we mean..."

### 2. Classifying Item Types

**Definition**: Introduces a new term or concept
- "A group is a set G with..."
- "We say f is continuous if..."
- "The kernel of φ is defined as..."

**Axiom**: Foundational assumption stated without proof
- "We assume the completeness axiom..."
- "The field axioms are..."

**Theorem**: Major named result or significant claim with proof
- "Theorem (Bolzano-Weierstrass): Every bounded sequence..."
- "Theorem 4.2. If f is continuous on [a,b], then..."

**Lemma**: Helper result, often unnamed, used in proofs
- "Lemma: If H is a subgroup..."
- "We first establish the following lemma..."

**Proposition**: Result of moderate importance, between lemma and theorem
- "Proposition: Every cyclic group is abelian."

**Corollary**: Direct consequence of a preceding result
- "Corollary: It follows that..."
- "As an immediate consequence..."

### 3. Naming Extracted Items

Assign a canonical name to each item:

**Named results**: Use the standard name
- "Theorem (Heine-Borel)" → "Heine-Borel Theorem"
- "Lagrange's Theorem" → "Lagrange's Theorem"

**Numbered results**: Create a descriptive name
- "Theorem 3.7: Every finite integral domain is a field" → "Finite integral domains are fields"
- "Lemma 2.1" (about subgroup closure) → "Subgroup closure under operation"

**Implicit definitions**: Name the concept
- "Let G be a group. A subset H ⊆ G is called a subgroup if..." → "Subgroup"

### 4. Preserving Original Content

Quote the source exactly in the "Original text" field:
- Preserve LaTeX/math formatting
- Keep the author's notation
- Include any remarks or commentary that are part of the definition
- Note if the definition spans multiple paragraphs

### 5. Noting Dependencies

For each item, list concepts it references that should have their own knowls:

```markdown
**Dependencies noted:** group, subgroup, homomorphism
```

This helps with Step 2 (dependency sorting).

### 6. Handling Variations

**Multiple equivalent definitions**: Extract both, note they're equivalent
```markdown
### 7. Definition: Compact (sequential)
**Original text:**
> A set K is sequentially compact if every sequence in K has a convergent subsequence.

**Note:** Alternative definition; see also "Compact (open cover)" in item 8.
```

**Definitions with immediate properties**: Separate them
```markdown
### 12. Definition: Normal subgroup
**Original text:**
> A subgroup H of G is normal if gHg⁻¹ = H for all g ∈ G.

### 13. Proposition: Equivalent characterizations of normal subgroups
**Original text:**
> The following are equivalent: (i) H is normal, (ii) gH = Hg for all g, (iii) H is the kernel of some homomorphism.
```

### 7. Handling Incomplete or Informal Content

Lecture notes may contain:

**Informal definitions**: Flag for formalization
```markdown
**Note:** Informal definition; needs rigorous restatement in Step 3.
```

**Incomplete statements**: Note missing hypotheses
```markdown
**Note:** Missing hypothesis (probably requires continuity); verify in Step 3.
```

**References to external sources**: Note the reference
```markdown
**Note:** References "see Rudin, Theorem 3.2" — may need to consult source.
```

## Example Extraction

**Source text (LaTeX lecture notes):**
```latex
\begin{definition}
Let $(X, d)$ be a metric space. A sequence $(x_n)$ in $X$ is called a
\textbf{Cauchy sequence} if for every $\varepsilon > 0$, there exists
$N \in \mathbb{N}$ such that $d(x_m, x_n) < \varepsilon$ for all $m, n \geq N$.
\end{definition}

A metric space is \textbf{complete} if every Cauchy sequence converges.

\begin{theorem}[Banach Fixed Point]
Let $(X,d)$ be a complete metric space and $T: X \to X$ a contraction
(i.e., $d(T(x), T(y)) \leq c \cdot d(x,y)$ for some $c < 1$). Then $T$
has a unique fixed point.
\end{theorem}
```

**Extracted output:**

```markdown
### 1. Definition: Cauchy sequence
**Source location:** Lecture 5, Definition block
**Original text:**
> Let $(X, d)$ be a metric space. A sequence $(x_n)$ in $X$ is called a **Cauchy sequence** if for every $\varepsilon > 0$, there exists $N \in \mathbb{N}$ such that $d(x_m, x_n) < \varepsilon$ for all $m, n \geq N$.

**Extracted name:** Cauchy sequence
**Dependencies noted:** metric space, sequence, convergence (implicit)

---

### 2. Definition: Complete metric space
**Source location:** Lecture 5, inline after Definition
**Original text:**
> A metric space is **complete** if every Cauchy sequence converges.

**Extracted name:** Complete metric space
**Dependencies noted:** metric space, Cauchy sequence, convergence

---

### 3. Theorem: Banach Fixed Point Theorem
**Source location:** Lecture 5, Theorem block
**Original text:**
> Let $(X,d)$ be a complete metric space and $T: X \to X$ a contraction (i.e., $d(T(x), T(y)) \leq c \cdot d(x,y)$ for some $c < 1$). Then $T$ has a unique fixed point.

**Extracted name:** Banach Fixed Point Theorem
**Dependencies noted:** complete metric space, contraction, fixed point
**Note:** "Contraction" is defined inline; may need separate definition.
```

## Edge Cases

### Recursive/Inductive Definitions
Extract as a single item, note the recursive structure:
```markdown
**Note:** Inductive definition with base case and recursive case.
```

### Notational Conventions
If the notes establish notation (not definitions), catalog separately:
```markdown
## Notational Conventions
- $\mathbb{N}$ denotes positive integers (not including 0)
- $\subset$ means strict subset; $\subseteq$ means subset or equal
- $f: A \to B$ denotes a function with domain A and codomain B
```

### Assumed Prerequisites
List concepts used but not defined in the notes:
```markdown
## Prerequisites (referenced but not defined)
- Real numbers and their properties
- Basic set theory (union, intersection, complement)
- Function composition
```

## After Completion

Output the complete extraction report. This will be passed to Step 2 for dependency sorting. Do not proceed to Step 2—output only the extraction.
