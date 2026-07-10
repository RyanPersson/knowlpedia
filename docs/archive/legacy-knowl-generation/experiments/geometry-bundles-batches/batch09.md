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

- Construction: Construction: pullback connection f^*ω on f^*P → `construction-pullback-connection-fω-on-fp.md`
- Construction: Construction: product principal bundle (P×_M Q) when defined → `construction-product-principal-bundle-when-defined.md`
- Construction: Construction: associated bundle P×_G F from a left G-space F → `construction-associated-bundle-p-g-f-from-a-left-g-space-f.md`
- Construction: Construction: associated vector bundle P×_G V from a representation ρ:G→GL(V) → `construction-associated-vector-bundle-p-g-v-from-a-representation-ρggl.md`
- Construction: Construction: induced map on associated bundles from a principal bundle morphism → `construction-induced-map-on-associated-bundles-from-a-principal-bundle-morphism.md`
- Construction: Construction: adjoint bundle Ad(P) → `construction-adjoint-bundle-ad.md`
- Construction: Construction: adjoint Lie algebra bundle ad(P) → `construction-adjoint-lie-algebra-bundle-ad.md`
- Construction: Construction: gauge group identified with Γ(Ad(P)) (sections of Ad(P)) → `construction-gauge-group-identified-with-γ.md`
- Construction: Construction: affine difference of connections (ω_1−ω_0) as a tensorial 𝔤-valued 1-form → `construction-affine-difference-of-connections-as-a-tensorial-𝔤-valued-1-form.md`
- Construction: Construction: identification of tensorial 𝔤-valued 1-forms on P with Ω^1(M;ad(P)) → `construction-identification-of-tensorial-𝔤-valued-1-forms-on-p-with-ω1.md`
- Construction: Construction: horizontal lift of curves and uniqueness of horizontal lift → `construction-horizontal-lift-of-curves-and-uniqueness-of-horizontal-lift.md`
- Construction: Construction: parallel transport map along a curve (principal/associated) → `construction-parallel-transport-map-along-a-curve.md`
- Construction: Construction: holonomy element from parallel transport around a loop → `construction-holonomy-element-from-parallel-transport-around-a-loop.md`
- Construction: Construction: local gauge potential A = s^*ω → `construction-local-gauge-potential-a-sω.md`
- Construction: Construction: local curvature F = s^*Ω → `construction-local-curvature-f-sω.md`
- Construction: Construction: gauge transformation of local data (A,F) via g:U→G → `construction-gauge-transformation-of-local-data-via-gug.md`
- Construction: Construction: induced connection on an associated bundle using horizontals → `construction-induced-connection-on-an-associated-bundle-using-horizontals.md`
- Construction: Construction: induced covariant derivative on associated vector bundle sections → `construction-induced-covariant-derivative-on-associated-vector-bundle-sections.md`
- Construction: Construction: curvature of an induced associated connection via representation → `construction-curvature-of-an-induced-associated-connection-via-representation.md`
- Construction: Construction: Atiyah algebroid TP/G and its anchor map to TM → `construction-atiyah-algebroid-tpg-and-its-anchor-map-to-tm.md`


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
