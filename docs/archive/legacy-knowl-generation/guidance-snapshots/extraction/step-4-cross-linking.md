# Step 4: Cross-Link Knowls

## Your Task

Add cross-reference links between knowls wherever one knowl references a concept that has its own knowl. This includes links between extracted items and prerequisite items.

## Input

You will receive:
1. The complete set of knowl markdown files from Step 3
2. A manifest of all knowl slugs (filenames without `.md`)

## Linking Syntax

Use the Hugo knowl shortcode:
```
{{</* knowl id="[slug]" text="[display text]" */>}}
```

Where:
- `[slug]` is the filename without `.md` (e.g., `group`, `lagranges-theorem`)
- `[display text]` is the text shown to the reader

## Output Format

For each knowl requiring modifications, output the complete updated file:

~~~markdown
**`[slug].md`** *(updated)*
```markdown
[complete updated content]
```
~~~

For knowls with no changes:
```
**`[slug].md`** — no links added
```

End with a summary:
```markdown
## Summary
- Prerequisite knowls updated: [N]
- Extracted knowls updated: [M]
- Knowls unchanged: [K]
- Total links added: [L]
```

## Linking Rules

### 1. What to Link

**Link:**
- Terms in prose/context sections that have knowls
- Prerequisite concepts referenced in extracted content
- Cross-references between related theorems/definitions
- First meaningful occurrence of each term per knowl

**Do NOT link:**
- Terms inside `$...$` or `$$...$$` math blocks (shortcode won't render)
- The term being defined in its own definition (the title term)
- Every occurrence—only the **first** meaningful one
- Assumed-external concepts (integers, real numbers, etc.)

### 2. Prerequisite → Extracted Linking

When a prerequisite knowl is referenced by extracted content, this creates valuable connections:

```markdown
<!-- In an extracted theorem knowl -->
Let $G$ be a {{</* knowl id="group" text="group" */>}} and $H$ a {{</* knowl id="subgroup" text="subgroup" */>}}.
```

### 3. Extracted → Extracted Linking

Link between extracted items when one references another:

```markdown
<!-- In First Isomorphism Theorem knowl -->
...the {{</* knowl id="kernel" text="kernel" */>}} of a {{</* knowl id="group-homomorphism" text="homomorphism" */>}}...
```

### 4. Link Placement

**Link in prose, not in math:**

✓ Correct:
```markdown
Let $G$ be a {{</* knowl id="group" text="group" */>}} with operation $\cdot$.
```

✗ Incorrect:
```markdown
Let ${{</* knowl id="group" text="G" */>}}$ be a group.  <!-- Inside math -->
```

### 5. First Occurrence Rule

Link only the first meaningful occurrence:

```markdown
A {{</* knowl id="subgroup" text="subgroup" */>}} is a subset forming a group.
If $H$ is a subgroup of $G$...  <!-- Don't link again -->
Every subgroup satisfies...      <!-- Don't link again -->
```

### 6. Display Text Variations

Match grammatical context:

```markdown
{{</* knowl id="group" text="group" */>}}           <!-- singular -->
{{</* knowl id="group" text="groups" */>}}          <!-- plural, same knowl -->
{{</* knowl id="continuous-function" text="continuous" */>}}  <!-- when "function" is implied -->
{{</* knowl id="cyclic-group" text="cyclic" */>}}   <!-- adjective form -->
```

### 7. Compound Terms

For compound terms:
- If the compound has its own knowl, link to that: `{{</* knowl id="normal-subgroup" text="normal subgroup" */>}}`
- If not, link components if it helps: `{{</* knowl id="abelian-group" text="abelian" */>}} group`
- Don't over-link: sometimes just linking the compound suffices

### 8. Context Sensitivity

Consider the reader's journey:
- **Early knowls** (prerequisites, basic definitions): Link more liberally—reader may need grounding
- **Later knowls** (advanced theorems): Link selectively—don't distract from the main content
- **Proof sketches**: Link if it clarifies the argument
- **Examples**: Link if the example uses a defined concept in a non-obvious way

## Example Transformation

**Before** (`first-isomorphism-theorem.md` from Step 3):
```markdown
---
title: "First Isomorphism Theorem"
type: "theorem"
summary: "A homomorphism induces an isomorphism between quotient and image"
source: "Lecture 8, Theorem 2"
build:
  list: local
---

**First Isomorphism Theorem**. Let $\varphi: G \to H$ be a group homomorphism. Then the kernel $\ker(\varphi)$ is a normal subgroup of $G$, and there is a natural isomorphism
$$G / \ker(\varphi) \cong \operatorname{im}(\varphi).$$

This theorem reveals the deep connection between homomorphisms and quotient structures. Every homomorphism factors through the quotient by its kernel.

**Proof sketch**: Define $\bar{\varphi}: G/\ker(\varphi) \to \operatorname{im}(\varphi)$ by $\bar{\varphi}(g\ker\varphi) = \varphi(g)$. Well-definedness follows from the definition of kernel. Injectivity follows because $\bar{\varphi}(g\ker\varphi) = e$ implies $g \in \ker\varphi$. Surjectivity is immediate.
```

**After** (updated):
```markdown
---
title: "First Isomorphism Theorem"
type: "theorem"
summary: "A homomorphism induces an isomorphism between quotient and image"
source: "Lecture 8, Theorem 2"
build:
  list: local
---

**First Isomorphism Theorem**. Let $\varphi: G \to H$ be a {{</* knowl id="group-homomorphism" text="group homomorphism" */>}}. Then the {{</* knowl id="kernel" text="kernel" */>}} $\ker(\varphi)$ is a {{</* knowl id="normal-subgroup" text="normal subgroup" */>}} of $G$, and there is a natural {{</* knowl id="group-isomorphism" text="isomorphism" */>}}
$$G / \ker(\varphi) \cong \operatorname{im}(\varphi).$$

This theorem reveals the deep connection between homomorphisms and {{</* knowl id="quotient-group" text="quotient" */>}} structures. Every homomorphism factors through the quotient by its kernel.

**Proof sketch**: Define $\bar{\varphi}: G/\ker(\varphi) \to \operatorname{im}(\varphi)$ by $\bar{\varphi}(g\ker\varphi) = \varphi(g)$. Well-definedness follows from the definition of kernel. Injectivity follows because $\bar{\varphi}(g\ker\varphi) = e$ implies $g \in \ker\varphi$. Surjectivity is immediate.
```

**Links added:**
- `group-homomorphism` (defines what φ is)
- `kernel` (key concept in statement)
- `normal-subgroup` (part of the conclusion)
- `group-isomorphism` (the main result type)
- `quotient-group` (in context paragraph)

**Not linked:**
- $G$, $H$ (inside math)
- "kernel" in proof sketch (already linked above)
- "homomorphism" in context (already linked as "group homomorphism")

## Verification Checklist

Before submitting:

- [ ] No shortcodes inside math delimiters
- [ ] No term linked more than once per knowl
- [ ] All slugs reference actual knowl files
- [ ] Display text reads naturally
- [ ] Self-references are not linked (don't link "Group" in group.md)

## After Completion

Output all updated knowls and the summary. These will be passed to Step 5 for review.
