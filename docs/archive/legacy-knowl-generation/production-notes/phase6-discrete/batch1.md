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

**discrete-structures (current section - no section param needed):**
graph-vertex-edge, finite-graph, lattice-zd, finite-box-lattice, boundary-finite-region, nearest-neighbor-zd, finite-range-interaction-lattice, translation-invariant-interaction

**shared-foundations (use section="shared-foundations"):**
set, function, integers, natural-numbers

## YOUR BATCH

Generate knowls for these slugs:

- graph-vertex-edge
- finite-graph
- lattice-zd
- finite-box-lattice
- boundary-finite-region
- nearest-neighbor-zd
- finite-range-interaction-lattice
- translation-invariant-interaction
