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

- Definition: Fibered manifold (surjective submersion π:E→M) → `fibered-manifold.md`
- Definition: Vertical tangent space (V_eE = ker dπ_e) → `vertical-tangent-space.md`
- Definition: Vertical subbundle (VE ⊂ TE) → `vertical-subbundle.md`
- Definition: Vertical vector field → `vertical-vector-field.md`
- Definition: Fiber-preserving map (map over a base map) → `fiber-preserving-map.md`
- Definition: Bundle map (morphism of fibered manifolds) → `bundle-map.md`
- Definition: Section (global section) of π:E→M → `section-of-πem.md`
- Definition: Local section of π:E→M → `local-section-of-πem.md`
- Definition: Smooth fiber bundle (fiber bundle in the smooth category) → `smooth-fiber-bundle.md`
- Definition: Typical fiber (model fiber) → `typical-fiber.md`
- Definition: Local trivialization (bundle chart) → `local-trivialization.md`
- Definition: Bundle atlas (collection of compatible local trivializations) → `bundle-atlas.md`
- Definition: Transition function (change-of-trivialization map) → `transition-function.md`
- Definition: Cocycle condition for transition functions → `cocycle-condition-for-transition-functions.md`
- Definition: Equivalent bundle atlases (refinement / compatibility) → `equivalent-bundle-atlases.md`
- Definition: Trivial fiber bundle (globally trivial bundle) → `trivial-fiber-bundle.md`
- Definition: Bundle isomorphism (fiber bundle isomorphism) → `bundle-isomorphism.md`
- Definition: Bundle morphism (fiber bundle morphism covering a base map) → `bundle-morphism.md`
- Definition: Pullback bundle (pullback of a fiber bundle along a smooth map) → `pullback-bundle.md`
- Definition: Vector bundle (smooth real vector bundle) → `vector-bundle.md`


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
