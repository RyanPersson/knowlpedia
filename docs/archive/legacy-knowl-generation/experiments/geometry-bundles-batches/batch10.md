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

- Construction: Construction: splitting of Atiyah sequence from a principal connection → `construction-splitting-of-atiyah-sequence-from-a-principal-connection.md`
- Construction: Construction: Chern–Weil form P(Ω) from invariant polynomial P and curvature Ω → `construction-chernweil-form-p-from-invariant-polynomial-p-and-curvature-ω.md`
- Construction: Construction: transgression / Chern–Simons form between two connections ω_0, ω_1 → `construction-transgression-chernsimons-form-between-two-connections-ω-0-ω-1.md`
- Construction: Construction: change-of-connection formula for characteristic forms (P(Ω_1)−P(Ω_0)) → `construction-change-of-connection-formula-for-characteristic-forms-p.md`
- Construction: Construction: reduction of structure group to H via transition functions valued in H → `construction-reduction-of-structure-group-to-h-via-transition-functions-valued-in-h.md`
- Construction: Construction: extension of structure group via a homomorphism φ:G→H → `construction-extension-of-structure-group-via-a-homomorphism-φgh.md`
- Construction: Construction: frame bundle Fr(E) of a vector bundle E → `construction-frame-bundle-fr-of-a-vector-bundle-e.md`
- Construction: Construction: connection on Fr(E) induced by a vector bundle connection (and conversely) → `construction-connection-on-fr-induced-by-a-vector-bundle-connection.md`
- Theorem: Trivial principal bundle criterion: global section ⇒ principal bundle is trivial → `trivial-principal-bundle-criterion-global-section-principal-bundle-is-trivial.md`
- Theorem: Converse triviality criterion: trivial principal bundle ⇒ admits a global section → `converse-triviality-criterion-trivial-principal-bundle-admits-a-global-section.md`
- Theorem: Pullback functoriality: pullback of a principal bundle is a principal bundle → `pullback-functoriality-pullback-of-a-principal-bundle-is-a-principal-bundle.md`
- Theorem: Pullback functoriality: pullback of a principal connection is a principal connection → `pullback-functoriality-pullback-of-a-principal-connection-is-a-principal-connection.md`
- Theorem: Čech cocycle classification (smooth): principal G-bundles correspond to transition cocycles up to coboundary → `čech-cocycle-classification-principal-g-bundles-correspond-to-transition-cocycles-up-to-coboundary.md`
- Theorem: Reduction by cocycle: structure group reduces to H iff transition functions can be chosen H-valued → `reduction-by-cocycle-structure-group-reduces-to-h-iff-transition-functions-can-be-chosen-h-valued.md`
- Theorem: Existence of principal connections on smooth manifolds (existence via partitions of unity / manifold paracompactness) → `existence-of-principal-connections-on-smooth-manifolds.md`
- Theorem: Affine space of connections: Conn(P) is an affine space modeled on Ω^1(M;ad(P)) → `affine-space-of-connections-conn-is-an-affine-space-modeled-on-ω1.md`
- Theorem: Equivalence: principal connections ↔ splittings of the Atiyah sequence → `equivalence-principal-connections-splittings-of-the-atiyah-sequence.md`
- Theorem: Existence/uniqueness of horizontal lift of a curve (given initial point) → `existenceuniqueness-of-horizontal-lift-of-a-curve.md`
- Theorem: Parallel transport defines a G-equivariant map between fibers → `parallel-transport-defines-a-g-equivariant-map-between-fibers.md`
- Theorem: Curvature tensoriality: Ω is horizontal and Ad-equivariant → `curvature-tensoriality-ω-is-horizontal-and-ad-equivariant.md`


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
