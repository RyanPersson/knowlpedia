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

- Definition: Chern class (via Chern–Weil) → `chern-class.md`
- Definition: Pontryagin class (via Chern–Weil) → `pontryagin-class.md`
- Definition: Euler class (via Chern–Weil) → `euler-class.md`
- Definition: Chern character (via Chern–Weil) → `chern-character.md`
- Definition: Chern–Simons form (secondary characteristic form) → `chernsimons-form.md`
- Definition: Transgression form (difference form between two connections) → `transgression-form.md`
- Convention: Convention: manifolds are smooth (C^∞), Hausdorff, and second countable → `convention-manifolds-are-smooth-hausdorff-and-second-countable.md`
- Convention: Convention: principal bundles use a right G-action on P → `convention-principal-bundles-use-a-right-g-action-on-p.md`
- Convention: Convention: associated bundles use a left G-action on the fiber F → `convention-associated-bundles-use-a-left-g-action-on-the-fiber-f.md`
- Convention: Convention: fundamental vector field X^# is defined using the right action (R_{exp(tX)}) → `convention-fundamental-vector-field-x-is-defined-using-the-right-action.md`
- Convention: Convention: curvature convention Ω = dω + (1/2)[ω∧ω] → `convention-curvature-convention-ω-dω-ωω.md`
- Convention: Convention: local curvature convention F = dA + (1/2)[A∧A] → `convention-local-curvature-convention-f-da-aa.md`
- Convention: Convention: covariant exterior derivative d_ωα = dα + [ω∧α] on tensorial forms → `convention-covariant-exterior-derivative-d-ωα-dα-ωα-on-tensorial-forms.md`
- Convention: Convention: Ad(P)=P×_G G uses conjugation action g·h = ghg^{-1} → `convention-ad-p-g-g-uses-conjugation-action-gh-ghg-1.md`
- Convention: Convention: ad(P)=P×_G 𝔤 uses adjoint action Ad → `convention-ad-p-g-𝔤-uses-adjoint-action-ad.md`
- Construction: Construction: quotient manifold P/G for a free proper G-action → `construction-quotient-manifold-pg-for-a-free-proper-g-action.md`
- Construction: Construction: local trivialization from a local section (principal bundle) → `construction-local-trivialization-from-a-local-section.md`
- Construction: Construction: transition functions g_{ij}:U_i∩U_j→G from local sections → `construction-transition-functions-g-iju-iu-jg-from-local-sections.md`
- Construction: Construction: gluing a principal bundle from a Čech 1-cocycle (cocycle gluing) → `construction-gluing-a-principal-bundle-from-a-čech-1-cocycle.md`
- Construction: Construction: pullback principal bundle f^*P along f:N→M → `construction-pullback-principal-bundle-fp-along-fnm.md`


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
