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

- Definition: Right principal action (right G-action on the total space) → `right-principal-action.md`
- Definition: Equivariant local trivialization (principal bundle trivialization) → `equivariant-local-trivialization.md`
- Definition: Principal bundle transition function → `principal-bundle-transition-function.md`
- Definition: Principal bundle morphism (G-equivariant bundle map) → `principal-bundle-morphism.md`
- Definition: Principal bundle isomorphism → `principal-bundle-isomorphism.md`
- Definition: Principal bundle automorphism → `principal-bundle-automorphism.md`
- Definition: Gauge transformation (principal automorphism over id_M) → `gauge-transformation.md`
- Definition: Gauge group (group of gauge transformations) → `gauge-group.md`
- Definition: Local gauge transformation (map g:U→G acting on local data) → `local-gauge-transformation.md`
- Definition: Associated bundle (P×_G F for a left G-space F) → `associated-bundle.md`
- Definition: Associated vector bundle (associated bundle via a representation) → `associated-vector-bundle.md`
- Definition: Bundle of orbits (quotient definition of P×_G F) → `bundle-of-orbits.md`
- Definition: Equivariant map P→F (left G-space) associated to a section of P×_G F → `equivariant-map-pf-associated-to-a-section-of-p-g-f.md`
- Definition: Adjoint bundle (Ad(P)=P×_G G with conjugation action) → `adjoint-bundle-p-g-g-with-conjugation-action.md`
- Definition: Adjoint Lie algebra bundle (ad(P)=P×_G 𝔤 with adjoint action) → `adjoint-lie-algebra-bundle-p-g-𝔤-with-adjoint-action.md`
- Definition: Section of Ad(P) (gauge function viewpoint) → `section-of-ad.md`
- Definition: Reduction of structure group (reduction property) → `reduction-of-structure-group.md`
- Definition: Principal H-subbundle (reduction to H⊂G) → `principal-h-subbundle.md`
- Definition: Extension of structure group (pushforward along φ:G→H) → `extension-of-structure-group.md`
- Definition: Open cover (of a manifold) → `open-cover.md`


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
