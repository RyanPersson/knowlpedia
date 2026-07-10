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

- Theorem: Local curvature formula: F = dA + (1/2)[A∧A] → `local-curvature-formula-f-da-aa.md`
- Theorem: Gauge covariance of curvature: Ω ↦ Ad(g^{-1})Ω under gauge transformations → `gauge-covariance-of-curvature-ω-ad-ω-under-gauge-transformations.md`
- Theorem: Bianchi identity: d_ωΩ = 0 → `bianchi-identity-d-ωω-0.md`
- Theorem: Basic forms theorem: α is basic on P iff α = π^*β for a unique β on M → `basic-forms-theorem-α-is-basic-on-p-iff-α-πβ-for-a-unique-β-on-m.md`
- Theorem: Associated connection theorem: a principal connection induces connections on all associated bundles → `associated-connection-theorem-a-principal-connection-induces-connections-on-all-associated-bundles.md`
- Theorem: Chern–Weil theorem: P(Ω) is closed and its de Rham class is independent of connection → `chernweil-theorem-p-is-closed-and-its-de-rham-class-is-independent-of-connection.md`
- Theorem: Naturality of Chern–Weil classes under pullback → `naturality-of-chernweil-classes-under-pullback.md`
- Theorem: Transgression theorem: P(Ω_1)−P(Ω_0) is exact (Chern–Simons transgression) → `transgression-theorem-p-p-is-exact.md`
- Lemma: Lemma: vertical space at p∈P equals {X^#_p : X∈𝔤} → `lemma-vertical-space-at-pp-equals-x-p-x𝔤.md`
- Lemma: Lemma: ω determines horizontals by H_p = ker(ω_p) → `lemma-ω-determines-horizontals-by-h-p-ker.md`
- Lemma: Lemma: G-invariance of horizontals ⇔ equivariance of ω → `lemma-g-invariance-of-horizontals-equivariance-of-ω.md`
- Lemma: Lemma: ω(X^#)=X implies ω|_{V_pP} is an isomorphism V_pP≅𝔤 → `lemma-ω-x-implies-ω-v-pp-is-an-isomorphism-v-pp𝔤.md`
- Lemma: Lemma: difference of two principal connections is tensorial (horizontal + Ad-equivariant) → `lemma-difference-of-two-principal-connections-is-tensorial.md`
- Lemma: Lemma: tensorial 𝔤-valued k-forms on P correspond to ad(P)-valued k-forms on M → `lemma-tensorial-𝔤-valued-k-forms-on-p-correspond-to-ad-valued-k-forms-on-m.md`
- Lemma: Lemma: local gauge transformation law A^g = g^{-1}Ag + g^{-1}dg → `lemma-local-gauge-transformation-law-ag-g-1ag-g-1dg.md`
- Lemma: Lemma: local curvature transformation law F^g = g^{-1}Fg → `lemma-local-curvature-transformation-law-fg-g-1fg.md`
- Lemma: Lemma: curvature Ω measures failure of horizontals to be involutive (non-integrability lemma) → `lemma-curvature-ω-measures-failure-of-horizontals-to-be-involutive.md`
- Lemma: Lemma: covariant exterior derivative preserves tensoriality → `lemma-covariant-exterior-derivative-preserves-tensoriality.md`
- Lemma: Lemma: Maurer–Cartan equation for the left Maurer–Cartan form → `lemma-maurercartan-equation-for-the-left-maurercartan-form.md`
- Lemma: Lemma: Chern–Weil forms are basic (descend to the base) → `lemma-chernweil-forms-are-basic.md`


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
