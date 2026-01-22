# Anti-Patterns in Knowl Generation

This document catalogs patterns that MUST be avoided when generating knowls. These issues were identified from reviewing ~1,500 generated knowls.

## Critical Anti-Patterns

### 1. "Related knowls" Sections

**Pattern:** A dedicated section at the end listing related concepts.

**Bad:**
```markdown
---
title: "Normal Subgroup"
description: "A subgroup invariant under conjugation"
---

A **normal subgroup** is...

## Related knowls

- {{< knowl id="subgroup" text="Subgroup" >}}
- {{< knowl id="quotient-group" text="Quotient group" >}}
- {{< knowl id="kernel-group" text="Kernel" >}}
```

**Also bad:**
```markdown
**Related knowls.** See also {{< knowl id="subgroup" text="subgroup" >}},
{{< knowl id="quotient-group" text="quotient group" >}}.
```

**Why it's wrong:** Knowl links should be woven naturally into the prose, not segregated into a list. The reader discovers related concepts through the natural flow of the content.

**Good:**
```markdown
---
title: "Normal Subgroup"
description: "A subgroup invariant under conjugation"
---

A **normal subgroup** of a {{< knowl id="group" text="group" >}} $G$ is a
{{< knowl id="subgroup" text="subgroup" >}} $N$ such that $gNg^{-1} = N$ for all $g \in G$.

Normal subgroups are precisely the {{< knowl id="kernel-group" text="kernels" >}} of
group homomorphisms, and they allow the construction of
{{< knowl id="quotient-group" text="quotient groups" >}}.
```

**Detection:**
```bash
grep -r "Related knowls" content/
grep -r "## Related" content/
grep -r "^\*\*Related" content/
```

---

### 2. Knowl Shortcodes Inside LaTeX Math

**Pattern:** Placing `{{< knowl >}}` inside `$...$` or `$$...$$` math blocks.

**Bad:**
```markdown
The {{< knowl id="prime-spectrum" text="spectrum" >}} is defined as
$$\text{Spec}(R) = {{< knowl id="prime-ideal" text="\{\mathfrak{p}\}" >}}$$
```

**Bad:**
```markdown
Let $x \in {{< knowl id="open-ball" text="B(a,r)" >}}$ be arbitrary.
```

**Why it's wrong:** Hugo processes shortcodes before KaTeX processes math. This causes rendering failures, garbled output, or "HAHASHORTCODE" artifacts.

**Good:**
```markdown
The {{< knowl id="prime-spectrum" text="spectrum" >}} is defined as
$$\text{Spec}(R) = \{\mathfrak{p} : \mathfrak{p} \text{ is a prime ideal of } R\}$$

Let $x \in B(a,r)$ be an element of the {{< knowl id="open-ball" text="open ball" >}}.
```

**Detection:**
```bash
grep -r '\$.*{{< knowl' content/
grep -r '{{< knowl.*\$' content/
grep -r '\\\[.*{{< knowl' content/
```

---

### 3. Knowl Immediately After `=` in Math Context

**Pattern:** `foo={{< knowl ... >}}` or `={{< knowl` in equations.

**Bad:**
```markdown
The oscillation is defined as $\omega(f;I)={{< knowl id="supremum" text="sup" >}}|f(x)-f(y)|$.
```

**Why it's wrong:** The `=` suggests this is part of a mathematical equation, and the shortcode will not render correctly in this context.

**Good:**
```markdown
The oscillation is defined as $\omega(f;I) = \sup\{|f(x)-f(y)| : x,y \in I\}$,
where $\sup$ denotes the {{< knowl id="supremum" text="supremum" >}}.
```

**Detection:**
```bash
grep -r '={{< knowl' content/
grep -r '= {{< knowl' content/
```

---

### 4. Missing `section` Parameter for Cross-Section Links

**Pattern:** Linking to a knowl in a different section without specifying `section`.

**Bad (in algebra-homological/chain-complex.md):**
```markdown
A chain complex of {{< knowl id="module" text="modules" >}} is...
```

This will fail because `module.md` is in `algebra-modules/`, not `algebra-homological/`.

**Good:**
```markdown
A chain complex of {{< knowl id="module" section="algebra-modules" text="modules" >}} is...
```

**Detection:**
```bash
python3 scripts/validate-knowls.py
```

---

### 5. Categorized Sub-bullets in Related Sections

**Pattern:** Organizing related knowls by category with labeled sub-groups.

**Bad:**
```markdown
## Related knowls

**Ideals:**
- {{< knowl id="prime-ideal" text="Prime ideal" >}}
- {{< knowl id="maximal-ideal" text="Maximal ideal" >}}

**Topology:**
- {{< knowl id="zariski-topology" text="Zariski topology" >}}
```

**Why it's wrong:** This is an even more structured version of the "Related knowls" anti-pattern. It treats knowls as a reference list rather than integrated content.

**Good:** Integrate these concepts naturally into the prose.

---

### 6. Proof Sketches / Proof Idea Sections

**Pattern:** Sections with headers containing "proof" such as:
- `## Proof idea / significance`
- `## Proof idea / significance (sketch)`
- `## Proof idea (sketch)`
- `## Proof outline`
- `## Typical proof inputs (conceptual)`

**CRITICAL: DO NOT GENERATE THESE.** LLMs commonly add these as filler content under various rephrasings to appear thorough.

**Why it's wrong:** Knowls should be concise reference cards that define concepts and state results. They are NOT the place for proof sketches. A proof sketch is neither a rigorous proof (which belongs in a textbook) nor a definition (which belongs in a knowl).

**Bad:**
```markdown
## Proof idea / significance

The proof proceeds by applying Jensen's inequality to the convex function $-\log$...
```

**Bad (rephrasing to evade detection):**
```markdown
## Proof idea / significance (sketch)
## Typical proof inputs (conceptual)
## Key proof techniques
## Derivation outline
```

**Good:** If a key insight is essential to understanding, integrate it briefly into the prose:

```markdown
The inequality follows from applying Jensen's inequality to the convex function $-\log$, combined with the normalization of probability measures.
```

**Detection:**
```bash
grep -r "^##.*[Pp]roof" content/
python3 scripts/tests/knowl_tests.py --test anti_patterns
```

---

## Summary Checklist

Before committing generated knowls, verify:

- [ ] No "Related knowls" or "See also" sections
- [ ] No knowl shortcodes inside `$...$` or `$$...$$`
- [ ] No `={{< knowl` patterns
- [ ] All cross-section links include `section` parameter
- [ ] No categorized sub-bullet lists
- [ ] No proof sketches (or standardized "Key insight:" format)
- [ ] `description` field is plain text (no LaTeX)
- [ ] Shortcodes use exactly `{{<` and `>}}` (not `{<` or `{{{<`)

## Automated Detection

Run after each generation batch:

```bash
# Check for anti-patterns
grep -r "Related knowls" content/SECTION/
grep -r '\$.*{{< knowl' content/SECTION/
grep -r '={{< knowl' content/SECTION/

# Check for broken links
python3 scripts/validate-knowls.py
```
