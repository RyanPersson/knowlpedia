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

- Definition: Parallel section along a curve (vector bundle) → `parallel-section-along-a-curve.md`
- Definition: Principal connection (G-invariant Ehresmann connection on P→M) → `principal-connection.md`
- Definition: Connection 1-form on a principal bundle (principal connection form ω∈Ω^1(P;𝔤)) → `connection-1-form-on-a-principal-bundle.md`
- Definition: Reproduction property (ω(X^#)=X) → `reproduction-property-x.md`
- Definition: Equivariance property (R_g^*ω = Ad(g^{-1})ω) → `equivariance-property-ω.md`
- Definition: Gauge transform of a local connection form (A ↦ A^g) → `gauge-transform-of-a-local-connection-form.md`
- Definition: Curvature 2-form of a principal connection (Ω∈Ω^2(P;𝔤)) → `curvature-2-form-of-a-principal-connection.md`
- Definition: Local curvature 2-form (F = s^*Ω) → `local-curvature-2-form.md`
- Definition: Exterior covariant derivative (d_ω on tensorial forms) → `exterior-covariant-derivative.md`
- Definition: Covariant exterior derivative on ad(P)-valued forms (d_∇) → `covariant-exterior-derivative-on-ad-valued-forms.md`
- Definition: Flat principal connection (Ω=0) → `flat-principal-connection.md`
- Definition: Holonomy group (principal connection holonomy) → `holonomy-group.md`
- Definition: Restricted holonomy group (identity component holonomy) → `restricted-holonomy-group.md`
- Definition: Holonomy representation (flat case / π_1-representation data) → `holonomy-representation.md`
- Definition: Atiyah algebroid of a principal bundle (TP/G) → `atiyah-algebroid-of-a-principal-bundle.md`
- Definition: Atiyah sequence (0→ad(P)→TP/G→TM→0) → `atiyah-sequence-tpgtm0.md`
- Definition: Splitting of the Atiyah sequence (as connection data) → `splitting-of-the-atiyah-sequence.md`
- Definition: Ad-invariant polynomial on 𝔤 (invariant symmetric multilinear form) → `ad-invariant-polynomial-on-𝔤.md`
- Definition: Chern–Weil form (characteristic form P(Ω)) → `chernweil-form.md`
- Definition: Characteristic class (de Rham class [P(Ω)]) → `characteristic-class.md`


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
