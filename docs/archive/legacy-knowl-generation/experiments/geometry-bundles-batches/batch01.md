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

- Definition: Smooth chart (coordinate chart) → `smooth-chart.md`
- Definition: Fiber of a map (preimage fiber) → `fiber-of-a-map.md`
- Definition: Differential (pushforward) of a smooth map → `differential-of-a-smooth-map.md`
- Definition: Pullback (of covectors) → `pullback.md`
- Definition: Lie derivative (of a differential form) → `lie-derivative.md`
- Definition: Interior product (contraction) (ι_X) → `interior-product.md`
- Definition: Lie algebra (of a Lie group) → `lie-algebra.md`
- Definition: Differential of a Lie group homomorphism (Lie algebra homomorphism) → `differential-of-a-lie-group-homomorphism.md`
- Definition: Exponential map (Lie group exponential) → `exponential-map.md`
- Definition: Left translation (L_g) → `left-translation.md`
- Definition: Right translation (R_g) → `right-translation.md`
- Definition: Left Maurer–Cartan form → `left-maurercartan-form.md`
- Definition: Right Maurer–Cartan form → `right-maurercartan-form.md`
- Definition: Maurer–Cartan equation → `maurercartan-equation.md`
- Definition: Adjoint action of a Lie group (Ad) → `adjoint-action-of-a-lie-group.md`
- Definition: Coadjoint action of a Lie group (Ad*) → `coadjoint-action-of-a-lie-group.md`
- Definition: Adjoint representation of a Lie algebra (ad) → `adjoint-representation-of-a-lie-algebra.md`
- Definition: Representation of a Lie group → `representation-of-a-lie-group.md`
- Definition: Representation of a Lie algebra → `representation-of-a-lie-algebra.md`
- Definition: Conjugation action of a Lie group on itself → `conjugation-action-of-a-lie-group-on-itself.md`


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
