# Knowl Generation Prompt Template v3

This version focuses entirely on **what knowls are** rather than what to avoid. The goal is to give the model a clear, positive mental model without priming undesired patterns.

## Base Prompt

```markdown
You are creating knowls for a mathematics reference site.

A **knowl** is a compact reference card that answers exactly one question: "What is X?"

---

## What a Knowl Contains

Every knowl has exactly these parts:

### 1. Definition or Statement
The precise mathematical definition or theorem statement. This is the core content.

For a **definition**:
```
A **[term]** is [formal definition with LaTeX].
```

For a **theorem/proposition**:
```
**[Name]:** [Complete statement with all hypotheses and conclusions]
```

### 2. Context (1-2 sentences)
Brief prose connecting this concept to prerequisites. Weave in cross-links naturally:
```
This generalizes the notion of {{< knowl id="group" text="group" >}} by relaxing the invertibility requirement.
```

### 3. Examples (optional)
Include only if:
- **Canonical**: The standard example everyone learns (e.g., $\mathbb{R}^n$ for vector spaces)
- **Clarifying**: Illuminates a subtle point
- **Contrasting**: A counterexample that sharpens the definition

Omit examples entirely for straightforward concepts.

---

## Cross-Linking Syntax

Link to other knowls using this shortcode:
```
{{< knowl id="slug-name" text="display text" >}}
```

For knowls in a **different section**, add the section parameter:
```
{{< knowl id="ring" section="algebra-rings" text="ring" >}}
```

**Where to place links:**
- In the context sentence(s)
- In example descriptions
- First occurrence only (don't repeat)

**Where NOT to place links:**
- Inside LaTeX math (`$...$` or `$$...$$`) — the shortcode will break
- The term being defined in its own knowl

If you need to reference a concept inside an equation, put the link outside:
```
Let $x \in B(a,r)$ be a point in the {{< knowl id="open-ball" text="open ball" >}}.
```

---

## Output Format

For each slug, output:

**`slug-name.md`**
```markdown
---
title: "Display Title"
description: "One-line plain-text summary (no LaTeX)"
---

[Definition/Statement]

[Context with cross-links]

[Examples if warranted]
```

---

## Section Directory

Use these exact names for the `section` parameter:

| Section | Content |
|---------|---------|
| `shared-foundations` | Sets, logic, functions, relations |
| `linear-algebra` | Vector spaces, linear maps, matrices |
| `algebra-groups` | Groups, subgroups, actions |
| `algebra-rings` | Rings, ideals |
| `algebra-modules` | Modules, tensor products |
| `algebra-fields-galois` | Field extensions, Galois theory |
| `algebra-commutative` | Localization, spectrum |
| `algebra-category-theory` | Categories, functors |
| `algebra-homological` | Chain complexes, derived functors |
| `real-analysis` | Limits, continuity, differentiation |
| `measure-theory` | Measures, integration |
| `topology` | Topological spaces, continuity |
| `convex-analysis` | Convex sets and functions |
| `probability` | Probability spaces, random variables |
| `thermodynamics` | Thermodynamic potentials, equilibrium |
| `stat-mech` | Ensembles, partition functions |

---

## Available Slugs

**Current section ({SECTION_NAME}):**
{CURRENT_SLUGS}

**Cross-section references (use `section` parameter):**

`shared-foundations`: {SHARED_FOUNDATIONS_SLUGS}

`linear-algebra`: {LINEAR_ALGEBRA_SLUGS}

[Include other relevant prerequisite sections...]

---

## Your Batch

Generate knowls for:
{BATCH_SLUGS}
```

---

## Design Philosophy

This prompt works by:

1. **Positive framing**: Defines what a knowl IS, not what it isn't
2. **Structural clarity**: Three components (definition, context, examples) with clear purposes
3. **Constraints as affordances**: "Examples only if canonical/clarifying" guides quality without forbidding
4. **No negative examples**: Avoids priming undesired patterns

The model should produce focused reference cards because that's the only structure we've given it.
