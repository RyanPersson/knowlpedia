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

- Definition: Čech 0-cochain with values in G (local gauge data) → `čech-0-cochain-with-values-in-g.md`
- Definition: Čech 1-cochain with values in G (transition data) → `čech-1-cochain-with-values-in-g.md`
- Definition: Čech 1-cocycle condition (g_{ij}g_{jk}g_{ki}=e) → `čech-1-cocycle-condition.md`
- Definition: Čech coboundary (change of cocycle by a 0-cochain) → `čech-coboundary.md`
- Definition: Equivalence of cocycles (cohomologous cocycles) → `equivalence-of-cocycles.md`
- Definition: Ehresmann connection (on a fibered manifold π:E→M) → `ehresmann-connection.md`
- Definition: Horizontal subbundle (HE ⊂ TE) → `horizontal-subbundle.md`
- Definition: Horizontal distribution (choice of horizontals) → `horizontal-distribution.md`
- Definition: Horizontal lift of a tangent vector → `horizontal-lift-of-a-tangent-vector.md`
- Definition: Horizontal lift of a vector field → `horizontal-lift-of-a-vector-field.md`
- Definition: Horizontal lift of a curve → `horizontal-lift-of-a-curve.md`
- Definition: Parallel transport (Ehresmann connection notion) → `parallel-transport.md`
- Definition: Integrable horizontal distribution (involutive horizontals) → `integrable-horizontal-distribution.md`
- Definition: Connection on a vector bundle (Koszul connection ∇) → `connection-on-a-vector-bundle.md`
- Definition: Covariant derivative of a section (∇_X s) → `covariant-derivative-of-a-section.md`
- Definition: Leibniz rule for a connection → `leibniz-rule-for-a-connection.md`
- Definition: Local connection 1-form (matrix of 1-forms in a frame) → `local-connection-1-form.md`
- Definition: Curvature of a vector bundle connection (R^∇) → `curvature-of-a-vector-bundle-connection.md`
- Definition: Curvature 2-form (endomorphism-valued 2-form) in a frame → `curvature-2-form-in-a-frame.md`
- Definition: Flat vector bundle connection (R^∇=0) → `flat-vector-bundle-connection.md`


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
