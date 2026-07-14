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

- Definition: Complex vector bundle (smooth complex vector bundle) → `complex-vector-bundle.md`
- Definition: Rank of a vector bundle → `rank-of-a-vector-bundle.md`
- Definition: Vector bundle morphism (fiberwise linear bundle map) → `vector-bundle-morphism.md`
- Definition: Local frame of a vector bundle → `local-frame-of-a-vector-bundle.md`
- Definition: Transition matrix of a local frame → `transition-matrix-of-a-local-frame.md`
- Definition: Dual vector bundle → `dual-vector-bundle.md`
- Definition: Direct sum vector bundle (Whitney sum) → `direct-sum-vector-bundle.md`
- Definition: Tensor product vector bundle → `tensor-product-vector-bundle.md`
- Definition: Exterior power bundle (Λ^kE) → `exterior-power-bundle.md`
- Definition: Symmetric power bundle (S^kE) → `symmetric-power-bundle.md`
- Definition: Bundle metric (fiberwise inner product) → `bundle-metric.md`
- Definition: Hermitian metric (complex bundle metric) → `hermitian-metric.md`
- Definition: Orientation of a real vector bundle → `orientation-of-a-real-vector-bundle.md`
- Definition: Oriented frame → `oriented-frame.md`
- Definition: Frame bundle (GL(n)-frame bundle) of a rank-n vector bundle → `frame-bundle-frame-bundle-of-a-rank-n-vector-bundle.md`
- Definition: Orthonormal frame bundle (O(n)-reduction of the frame bundle) → `orthonormal-frame-bundle-reduction-of-the-frame-bundle.md`
- Definition: Special orthonormal frame bundle (SO(n)-reduction) → `special-orthonormal-frame-bundle-reduction.md`
- Definition: Unitary frame bundle (U(n)-reduction) → `unitary-frame-bundle-reduction.md`
- Definition: Special unitary frame bundle (SU(n)-reduction) → `special-unitary-frame-bundle-reduction.md`
- Definition: Principal G-bundle (smooth principal bundle) → `principal-g-bundle.md`


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
