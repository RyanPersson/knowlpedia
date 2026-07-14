You are creating knowls (short definition/theorem cards) for a mathematics reference site.

For each slug below, generate a markdown file following these rules exactly.

## OUTPUT FORMAT

For each knowl, output:

**`slug-name.md`**
```markdown
---
title: "Display Title"
description: "One-line plain-text description (NO LaTeX)"
---

[Content here]
```

## CRITICAL RULES

1. NO "Related" sections at the end
2. NO knowl shortcodes inside LaTeX math
3. Cross-section links MUST include `section` parameter
4. Plain-text description (no LaTeX)
5. Use exactly `{{<` and `>}}` for shortcodes

## AVAILABLE SLUGS BY SECTION

**quantum-foundations (current section - no section param needed):**
complex-hilbert-space-finite, bounded-operator-hilbert, self-adjoint-operator-observable, spectrum-self-adjoint-finite, trace-operator, density-operator, pure-state-quantum, mixed-state-quantum, partial-trace, von-neumann-entropy, quantum-relative-entropy, golden-thompson-inequality

**linear-algebra (use section="linear-algebra"):**
hilbert-space, linear-operator, eigenvalue, trace

**measure-theory (use section="measure-theory"):**
lebesgue-integral

## YOUR BATCH

Generate knowls for these slugs:

- complex-hilbert-space-finite
- bounded-operator-hilbert
- self-adjoint-operator-observable
- spectrum-self-adjoint-finite
- trace-operator
- density-operator
