# Step 4: Cross-Link Knowls

## Your Task

Take the knowl files from Step 3 and add cross-reference links wherever one knowl references a concept that has its own knowl. Output the updated versions of each knowl.

## Input

You will receive:
1. The complete set of knowl markdown files from Step 3
2. A list of all knowl slugs (filenames without `.md`)

## Linking Syntax

Use the Hugo knowl shortcode:
```
{{</* knowl id="[slug]" text="[display text]" */>}}
```

Where:
- `[slug]` is the filename without `.md` (e.g., `group`, `lagranges-theorem`)
- `[display text]` is the text shown to the reader (should match natural reading)

## Output Format

For each knowl that requires modifications, output the complete updated file:

~~~markdown
**`[slug].md`** *(updated)*
```markdown
[complete updated content]
```
~~~

For knowls with no changes needed, output:
```
**`[slug].md`** — no links added
```

At the end, provide a summary:
```
## Summary
- [N] knowls updated with cross-links
- [M] knowls unchanged
- [Total] total links added
```

## Linking Rules

### 1. What to Link

Link a term when:
- It appears in the prose/context sections
- It appears in example descriptions
- It is a key concept in the statement that benefits from expansion

Do **NOT** link:
- Terms inside LaTeX math environments (the shortcode won't render there)
- The term being defined in its own definition
- Every occurrence—link the **first meaningful occurrence** only
- Common English words that happen to match a mathematical term (use judgment)

### 2. Link Placement

**Link in prose, not in math:**

Good:
```markdown
Let $G$ be a {{</* knowl id="group" text="group" */>}} and $H$ a {{</* knowl id="subgroup" text="subgroup" */>}}.
```

Bad (inside math):
```markdown
Let ${{</* knowl id="group" text="G" */>}}$ be a group. <!-- Won't render correctly -->
```

### 3. First Occurrence Rule

Link only the first occurrence of each term within a knowl:

```markdown
A {{</* knowl id="subgroup" text="subgroup" */>}} is a subset that is itself a group.
If $H$ is a subgroup of $G$...  <!-- Don't link again -->
```

### 4. Display Text Variations

Match the grammatical form in the text:

- `{{</* knowl id="group" text="group" */>}}` — singular
- `{{</* knowl id="group" text="groups" */>}}` — plural (same slug)
- `{{</* knowl id="abelian-group" text="abelian" */>}}` — adjective form if context is clear
- `{{</* knowl id="continuous-function" text="continuous" */>}}` — when "function" is implied

### 5. Compound Terms

For compound terms where both parts have knowls:
- If the compound itself has a knowl, link to that: `{{</* knowl id="normal-subgroup" text="normal subgroup" */>}}`
- If not, link components separately: `{{</* knowl id="abelian-group" text="abelian" */>}} {{</* knowl id="group" text="group" */>}}`
- Use judgment—don't over-link: "abelian group" might just need the compound link

### 6. Context-Dependent Linking

Consider whether the reference adds value:
- In a definition of "ring," linking "group" is useful (reader may want to review)
- In the 50th knowl about rings, linking "group" may be unnecessary

Prefer linking when:
- The concept is genuinely a prerequisite for understanding
- The connection might not be obvious to the reader
- The referenced knowl contains useful examples

## Example Transformation

**Before** (`coset.md` from Step 3):
```markdown
---
title: "Coset"
type: "definition"
summary: "A translate of a subgroup by a group element"
build:
  list: local
---

**Coset**. Let $G$ be a group and $H \leq G$ a subgroup. For any $g \in G$, the *left coset* of $H$ containing $g$ is the set
$$gH = \{gh : h \in H\}.$$
Similarly, the *right coset* is $Hg = \{hg : h \in H\}$.

Cosets partition the group $G$ into disjoint subsets of equal size. The number of distinct left cosets of $H$ in $G$ is called the index of $H$ in $G$, denoted $[G:H]$.

**Examples:**
1. In $\mathbb{Z}$ with subgroup $3\mathbb{Z}$, the cosets are $3\mathbb{Z}$, $1 + 3\mathbb{Z}$, and $2 + 3\mathbb{Z}$ (the residue classes mod 3).
2. In $S_3$ with $H = \{e, (12)\}$, the left cosets are $H$, $(13)H = \{(13), (123)\}$, and $(23)H = \{(23), (132)\}$.
3. Left and right cosets can differ: in $S_3$, $(13)H = \{(13), (123)\}$ but $H(13) = \{(13), (132)\}$.
```

**After** (`coset.md` updated):
```markdown
---
title: "Coset"
type: "definition"
summary: "A translate of a subgroup by a group element"
build:
  list: local
---

**Coset**. Let $G$ be a {{</* knowl id="group" text="group" */>}} and $H \leq G$ a {{</* knowl id="subgroup" text="subgroup" */>}}. For any $g \in G$, the *left coset* of $H$ containing $g$ is the set
$$gH = \{gh : h \in H\}.$$
Similarly, the *right coset* is $Hg = \{hg : h \in H\}$.

Cosets partition the group $G$ into disjoint subsets of equal size. The number of distinct left cosets of $H$ in $G$ is called the {{</* knowl id="index-of-subgroup" text="index" */>}} of $H$ in $G$, denoted $[G:H]$.

**Examples:**
1. In $\mathbb{Z}$ with subgroup $3\mathbb{Z}$, the cosets are $3\mathbb{Z}$, $1 + 3\mathbb{Z}$, and $2 + 3\mathbb{Z}$ (the residue classes mod 3).
2. In $S_3$ with $H = \{e, (12)\}$, the left cosets are $H$, $(13)H = \{(13), (123)\}$, and $(23)H = \{(23), (132)\}$.
3. Left and right cosets can differ: in $S_3$, $(13)H = \{(13), (123)\}$ but $H(13) = \{(13), (132)\}$.
```

**Changes made:**
- Linked "group" (first occurrence, in prose)
- Linked "subgroup" (first occurrence, in prose)
- Linked "index" (references another concept)
- Did NOT link $S_3$ (it's a specific example, not a defined term)
- Did NOT re-link "subgroup" in examples

## Verification

Before submitting, verify:
- [ ] No shortcodes appear inside `$...$` or `$$...$$` math blocks
- [ ] No term is linked more than once per knowl
- [ ] The slug in each shortcode matches an actual knowl filename
- [ ] Display text reads naturally in context

## After Completion

Once all knowls are cross-linked, they will be passed to Step 5 for review. Output the complete set of updated knowls.
