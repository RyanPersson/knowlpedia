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

- Proposition: Proposition: gauge group acts on Conn(P) by pullback (connection action) → `proposition-gauge-group-acts-on-conn-by-pullback.md`
- Proposition: Proposition: gauge group action on Conn(P) is affine over Ω^1(M;ad(P)) → `proposition-gauge-group-action-on-conn-is-affine-over-ω1.md`
- Proposition: Proposition: induced connection on an associated vector bundle satisfies the Leibniz rule → `proposition-induced-connection-on-an-associated-vector-bundle-satisfies-the-leibniz-rule.md`
- Proposition: Proposition: curvature of an induced associated connection is ρ_*(Ω) → `proposition-curvature-of-an-induced-associated-connection-is-ρ.md`
- Proposition: Proposition: parallel transport respects concatenation of paths → `proposition-parallel-transport-respects-concatenation-of-paths.md`
- Proposition: Proposition: flatness implies path-independence on simply connected domains → `proposition-flatness-implies-path-independence-on-simply-connected-domains.md`
- Proposition: Proposition: flatness implies holonomy depends only on homotopy class of loops → `proposition-flatness-implies-holonomy-depends-only-on-homotopy-class-of-loops.md`
- Proposition: Proposition: reduction to H yields an H-connection iff the connection form takes values in 𝔥 on the reduction (reduction compatibility) → `proposition-reduction-to-h-yields-an-h-connection-iff-the-connection-form-takes-values-in-𝔥-on-the-reduction.md`
- Definition: Corollary: every principal G-bundle over a smooth manifold admits a connection → `corollary-every-principal-g-bundle-over-a-smooth-manifold-admits-a-connection.md`
- Definition: Corollary: every vector bundle over a smooth manifold admits a connection → `corollary-every-vector-bundle-over-a-smooth-manifold-admits-a-connection.md`
- Definition: Corollary: Conn(P)/Gauge(P) (moduli of connections) is a well-defined orbit space → `corollary-conn-gauge-is-a-well-defined-orbit-space.md`
- Definition: Corollary: a flat connection determines a conjugacy class of representations π_1(M)→G (monodromy) → `corollary-a-flat-connection-determines-a-conjugacy-class-of-representations-π-1-g.md`
- Definition: Corollary: Chern–Weil characteristic classes are invariants of the principal bundle (independent of connection) → `corollary-chernweil-characteristic-classes-are-invariants-of-the-principal-bundle.md`
- Definition: Corollary: isomorphic principal bundles have identical Chern–Weil characteristic classes → `corollary-isomorphic-principal-bundles-have-identical-chernweil-characteristic-classes.md`
- TFAE: TFAE: Triviality of a principal G-bundle — principal G-bundle P→M → `tfae-triviality-of-a-principal-g-bundle-principal-g-bundle-pm.md`
- TFAE: TFAE: Čech description of principal bundles — principal G-bundle P→M with cover {U_i} → `tfae-čech-description-of-principal-bundles-principal-g-bundle-pm-with-cover-u-i.md`
- TFAE: TFAE: Reduction of structure group to H⊂G — principal G-bundle P→M → `tfae-reduction-of-structure-group-to-hg-principal-g-bundle-pm.md`
- TFAE: TFAE: Principal connection data — principal G-bundle P→M → `tfae-principal-connection-data-principal-g-bundle-pm.md`
- TFAE: TFAE: Flatness of a principal connection — principal connection ω on P→M → `tfae-flatness-of-a-principal-connection-principal-connection-ω-on-pm.md`
- TFAE: TFAE: Basic forms on a principal bundle — principal G-bundle π:P→M → `tfae-basic-forms-on-a-principal-bundle-principal-g-bundle-πpm.md`


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
