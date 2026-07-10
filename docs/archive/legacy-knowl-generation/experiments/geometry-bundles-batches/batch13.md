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

- TFAE: TFAE: Tensorial forms vs ad(P)-valued forms — principal G-bundle P→M → `tfae-tensorial-forms-vs-ad-valued-forms-principal-g-bundle-pm.md`
- TFAE: TFAE: Vector bundle connections via frame bundles — rank-n vector bundle E→M → `tfae-vector-bundle-connections-via-frame-bundles-rank-n-vector-bundle-em.md`
- Example: Trivial principal bundle M×G→M → `trivial-principal-bundle-mgm.md`
- Example: Trivial vector bundle M×V→M → `trivial-vector-bundle-mvm.md`
- Example: Möbius line bundle over S^1 (nontrivial real line bundle) → `möbius-line-bundle-over-s1.md`
- Example: Hopf fibration S^3→S^2 as a principal U(1)-bundle → `hopf-fibration-s3s2-as-a-principal-u-bundle.md`
- Example: Principal bundle over S^1 defined by a clutching function (clutching construction example) → `principal-bundle-over-s1-defined-by-a-clutching-function.md`
- Example: Frame bundle Fr(TM) of a manifold M → `frame-bundle-fr-of-a-manifold-m.md`
- Example: Orthonormal frame bundle O(TM) of a Riemannian manifold → `orthonormal-frame-bundle-o-of-a-riemannian-manifold.md`
- Example: Tangent bundle TS^2 as a nontrivial rank-2 real vector bundle → `tangent-bundle-ts2-as-a-nontrivial-rank-2-real-vector-bundle.md`
- Example: Flat connection A=0 on a trivial bundle → `flat-connection-a0-on-a-trivial-bundle.md`
- Example: Pure gauge connection A=g^{-1}dg on a trivial bundle (flat) → `pure-gauge-connection-ag-1dg-on-a-trivial-bundle.md`
- Example: Dirac monopole connection on the Hopf bundle (nonzero curvature) → `dirac-monopole-connection-on-the-hopf-bundle.md`
- Example: Counterexample: nontrivial principal bundle admitting no global section (illustrates triviality criterion) → `counterexample-nontrivial-principal-bundle-admitting-no-global-section.md`
- Example: Example: reduction of GL(n)-structure to O(n) using a bundle metric → `example-reduction-of-gl-structure-to-o-using-a-bundle-metric.md`
- Extension: Paracompact topological space → `paracompact-topological-space.md`
- Extension: Paracompact manifold → `paracompact-manifold.md`
- Extension: Partition of unity subordinate to an open cover → `partition-of-unity-subordinate-to-an-open-cover.md`
- Extension: Good cover (contractible finite intersections) → `good-cover.md`
- Extension: Classifying space BG → `classifying-space-bg.md`


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
