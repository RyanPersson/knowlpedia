# Step 2: Create Companion Knowls

## Your Task

Create knowls for the prerequisite concepts identified in Step 1. These form a "companion glossary" for reading the paper—quick references the reader can expand to recall definitions they've seen before but don't have memorized.

## Input

You will receive:
- **Prerequisite analysis from Step 1** — the prioritized concept list
- **Paper context** — field, notation conventions, how terms are used

## Output Format

For each concept, produce:

~~~markdown
**`[slug].md`**
```markdown
---
title: "[Name]"
description: "[One-line description]"
---

[Knowl content]
```
~~~

## Design Philosophy: Unknowling

These knowls serve a specific purpose: **helping readers recall concepts they've encountered before**. They are not comprehensive introductions; they are quick refreshers.

### Optimize for:
- **Fast recognition**: Reader should quickly confirm "ah yes, that's what I thought"
- **Paper context**: Emphasize aspects relevant to how the paper uses the concept
- **Minimal friction**: Short enough to read without losing place in the paper

### Structure

```markdown
---
title: "[Name]"
description: "[One-line description]"
---

A **[name]** is [concise definition].

[One sentence of context or intuition, if helpful]

**Key properties:**
- [Property relevant to the paper]
- [Another key property]

**Example:** [Single canonical example]
```

Keep knowls **short**—aim for 5-10 lines of content. The reader wants to glance, recall, and return to the paper.

## Content Guidelines

### Definition Style

**Compact and precise:**
```markdown
A **Banach space** is a complete normed vector space.
```

**Not tutorial-length:**
```markdown
A **Banach space** is a vector space $V$ over $\mathbb{R}$ or $\mathbb{C}$ equipped with
a norm $\|\cdot\|: V \to [0, \infty)$ satisfying [three axioms listed]... The key property
is completeness: every Cauchy sequence converges. This generalizes... [500 more words]
```

### Context Sensitivity

Tailor the knowl to the paper's usage. If the paper uses Banach spaces primarily for operator theory:

```markdown
A **Banach space** is a complete normed vector space.

The completeness ensures that bounded linear operators between Banach spaces have well-behaved spectra and that limits of operator sequences exist when expected.

**Examples:** $\ell^p$, $L^p(\mu)$, $C(K)$, spaces of bounded operators $\mathcal{B}(X,Y)$
```

### Key Properties Section

Include only properties the reader needs for *this paper*:

```markdown
**Key properties:**
- Closed subspaces are Banach spaces
- $\mathcal{B}(X,Y)$ is Banach when $Y$ is Banach
- The Open Mapping Theorem applies
```

### Single Example

One well-chosen example beats a list:

```markdown
**Example:** $L^2[0,1]$ with the norm $\|f\| = \left(\int_0^1 |f|^2\right)^{1/2}$
```

## Notation Knowls

For field-specific notation, create brief notation knowls:

```markdown
---
title: "Spectrum Notation"
description: "Standard notation for operator spectra"
---

For a bounded linear operator $T$ on a Banach space:

- $\sigma(T)$ — the **spectrum**: $\{\lambda \in \mathbb{C} : T - \lambda I \text{ not invertible}\}$
- $\sigma_p(T)$ — the **point spectrum**: eigenvalues of $T$
- $\sigma_c(T)$ — the **continuous spectrum**
- $\sigma_r(T)$ — the **residual spectrum**
- $\rho(T) = \mathbb{C} \setminus \sigma(T)$ — the **resolvent set**
```

## Dependency Ordering

Process knowls in rough dependency order:
1. Foundational structures (spaces, basic objects)
2. Properties and constructions on those structures
3. Theorems and named results
4. Specialized notation

Within each category, no strict ordering needed—these are all "prior knowledge."

## Example Knowls

**For a paper in operator theory:**

~~~markdown
**`banach-space.md`**
```markdown
---
title: "Banach Space"
description: "A complete normed vector space"
---

A **Banach space** is a normed vector space that is complete with respect to the metric induced by its norm.

**Key properties:**
- Bounded linear operators $T: X \to Y$ form a Banach space $\mathcal{B}(X,Y)$ when $Y$ is Banach
- The Open Mapping Theorem and Closed Graph Theorem apply

**Example:** $L^p(\mu)$ for $1 \leq p \leq \infty$
```
~~~

~~~markdown
**`compact-operator.md`**
```markdown
---
title: "Compact Operator"
description: "An operator that maps bounded sets to relatively compact sets"
---

A **compact operator** $T: X \to Y$ between Banach spaces maps bounded sets to relatively compact sets (sets with compact closure).

Equivalently, $T$ is compact iff the image of the unit ball has compact closure.

**Key properties:**
- Compact operators form a closed ideal in $\mathcal{B}(X)$
- $\sigma(T) \setminus \{0\}$ consists of eigenvalues with finite multiplicity
- Finite-rank operators are compact; limits of finite-rank operators are compact

**Example:** Integral operators $Tf(x) = \int K(x,y)f(y)\,dy$ with continuous kernel on $[0,1]^2$
```
~~~

~~~markdown
**`spectrum.md`**
```markdown
---
title: "Spectrum of an Operator"
description: "The set of λ where T - λI is not invertible"
---

The **spectrum** of a bounded linear operator $T: X \to X$ on a Banach space is
$$\sigma(T) = \{\lambda \in \mathbb{C} : T - \lambda I \text{ is not invertible in } \mathcal{B}(X)\}.$$

The spectrum is always nonempty, compact, and contained in $\{|\lambda| \leq \|T\|\}$.

**Decomposition:**
- $\sigma_p(T)$ — point spectrum (eigenvalues)
- $\sigma_c(T)$ — continuous spectrum
- $\sigma_r(T)$ — residual spectrum
```
~~~

## Cross-Linking

Add knowl links where one prerequisite concept references another:

```markdown
A **compact operator** $T: X \to Y$ between {{< knowl id="banach-space" text="Banach spaces" >}} maps bounded sets to relatively compact sets.
```

Link selectively—only when the reference genuinely helps the reader.

## Validation

Before submitting:
- [ ] Each knowl is ≤ 15 lines of content
- [ ] Definition is precise and self-contained
- [ ] Key properties are relevant to the paper's usage
- [ ] Example is concrete and canonical
- [ ] Cross-links reference actual knowls in the set

## After Completion

Output all knowls. They will be passed to Step 3 for a brief review, then ready for use as a paper companion.
