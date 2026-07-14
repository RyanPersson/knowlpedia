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

- Extension: Cartan's first structure equation (torsion equation) (frame bundle formulation) → `cartans-first-structure-equation.md`
- Extension: Cartan's second structure equation (curvature equation) (frame bundle formulation) → `cartans-second-structure-equation.md`
- Extension: Ambrose–Singer holonomy theorem → `ambrosesinger-holonomy-theorem.md`
- Extension: Holonomy reduction principle (holonomy contained in H ⇒ reduction to H) → `holonomy-reduction-principle.md`
- Extension: Integrality of Chern classes (relation to integral cohomology) (name-only, if covered) → `integrality-of-chern-classes.md`
- Extension: Chern–Simons gauge transformation behavior (secondary invariant behavior) (name-only, if covered) → `chernsimons-gauge-transformation-behavior.md`
- Extension: TFAE: Flat principal bundles — principal G-bundle P→M → `tfae-flat-principal-bundles-principal-g-bundle-pm.md`
- Extension: TFAE: Metric-compatible connections on a metric vector bundle (E,⟨·,·⟩) → `tfae-metric-compatible-connections-on-a-metric-vector-bundle.md`


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

Generate all 8 knowls now.
