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

- Extension: Universal principal bundle EG→BG → `universal-principal-bundle-egbg.md`
- Extension: Classifying map of a principal bundle → `classifying-map-of-a-principal-bundle.md`
- Extension: Homotopy class [M,BG] → `homotopy-class-mbg.md`
- Extension: Clutching function (for bundles over spheres) → `clutching-function.md`
- Extension: Solder form (tautological 1-form) on the frame bundle → `solder-form-on-the-frame-bundle.md`
- Extension: Cartan connection (Cartan geometry) → `cartan-connection.md`
- Extension: Levi–Civita connection (as principal O(n)-connection) → `levicivita-connection-connection.md`
- Extension: Torsion 2-form (torsion of a connection on a frame bundle) → `torsion-2-form.md`
- Extension: Holonomy algebra (Lie algebra of holonomy group) → `holonomy-algebra.md`
- Extension: Ambrose–Singer curvature span (curvature generates holonomy algebra notion) → `ambrosesinger-curvature-span.md`
- Extension: Bundle of connections (affine bundle over M with fibers connections) → `bundle-of-connections.md`
- Extension: Jet bundle (1-jet bundle of sections) (if included) → `jet-bundle.md`
- Extension: Equivariant cohomology (Cartan model) → `equivariant-cohomology.md`
- Extension: Moment map (Hamiltonian G-space) (if symplectic extension) → `moment-map.md`
- Extension: Yang–Mills functional → `yangmills-functional.md`
- Extension: Yang–Mills equation (critical point condition) → `yangmills-equation.md`
- Extension: Yang–Mills connection → `yangmills-connection.md`
- Extension: Existence of partitions of unity on paracompact manifolds → `existence-of-partitions-of-unity-on-paracompact-manifolds.md`
- Extension: Classification theorem: principal G-bundles over M are classified by homotopy classes [M,BG] → `classification-theorem-principal-g-bundles-over-m-are-classified-by-homotopy-classes-mbg.md`
- Extension: Clutching classification of principal G-bundles over S^n by π_{n-1}(G) → `clutching-classification-of-principal-g-bundles-over-sn-by-π-n-1.md`


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
