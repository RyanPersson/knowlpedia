You are creating knowls (short definition/theorem cards) for a math blog on differential geometry of fiber bundles (500-level).

For each slug below, generate a markdown file with:
1. YAML front matter with `title` and `description` (plain text only, no LaTeX in description)
2. A clear, rigorous statement of the definition/theorem
3. Cross-links using Hugo shortcode `{{< knowl id="slug" text="display" >}}`
4. 2-3 concrete examples where applicable

**CROSS-LINK SYNTAX:**
- `{{< knowl id="slug" text="display text" >}}`
- Link first meaningful occurrence only
- DO NOT link terms inside LaTeX `$...$` or `$$...$$`
- DO NOT link the term being defined to itself

**CRITICAL RULES:**
- DO NOT include a "Related" or "Related knowls" section at the end
- All cross-links must be woven naturally into the prose
- YAML `description` must be plain text (no LaTeX)
- Use double braces: `{{<` not `{<`

**Available slugs for cross-linking:**
(See slug-manifest.txt - 324 total slugs available)

Key foundational slugs: smooth-manifold, smooth-map, diffeomorphism, tangent-bundle, cotangent-bundle, vector-field, differential-k-form, exterior-derivative, lie-group, lie-algebra, lie-bracket, principal-g-bundle, connection-on-a-vector-bundle, principal-connection, curvature, parallel-transport, holonomy-group

**Generate knowls for these items:**

- Definition: Principal homogeneous space (G-torsor) → `principal-homogeneous-space.md`
- Definition: Smooth (left) action of a Lie group on a manifold → `smooth-action-of-a-lie-group-on-a-manifold.md`
- Definition: Orbit of a group action → `orbit-of-a-group-action.md`
- Definition: Stabilizer (isotropy subgroup) → `stabilizer.md`
- Definition: Free action → `free-action.md`
- Definition: Proper action → `proper-action.md`
- Definition: Principal action (free and proper action) → `principal-action.md`
- Definition: Quotient space of an action → `quotient-space-of-an-action.md`
- Definition: Quotient manifold (for a free proper action) → `quotient-manifold.md`
- Definition: Orbit map → `orbit-map.md`
- Definition: Fundamental vector field (X^#) of X∈𝔤 for a right action → `fundamental-vector-field-of-x𝔤-for-a-right-action.md`
- Definition: Equivariant map (G-equivariant smooth map) → `equivariant-map.md`
- Definition: Invariant function (G-invariant function) → `invariant-function.md`
- Definition: Invariant differential form (G-invariant differential form) → `invariant-differential-form.md`
- Definition: Lie-algebra-valued k-form (𝔤-valued differential form) → `lie-algebra-valued-k-form.md`
- Definition: Ad-equivariant 𝔤-valued form (equivariance property) → `ad-equivariant-𝔤-valued-form.md`
- Definition: Horizontal (semi-basic) differential form on a principal bundle → `horizontal-differential-form-on-a-principal-bundle.md`
- Definition: Tensorial 𝔤-valued k-form on a principal bundle (horizontal + Ad-equivariant) → `tensorial-𝔤-valued-k-form-on-a-principal-bundle.md`
- Definition: Basic differential form on a principal bundle (horizontal + G-invariant) → `basic-differential-form-on-a-principal-bundle.md`
- Definition: Wedge–bracket on 𝔤-valued forms ([·∧·] operation) → `wedgebracket-on-𝔤-valued-forms.md`


**Output format for each:**

**`slug.md`**
```markdown
---
title: "Title"
description: "One-line plain-text description"
---

Content with natural cross-links woven into prose...

## Examples
1. ...
2. ...
```

Generate all 20 knowls now.
