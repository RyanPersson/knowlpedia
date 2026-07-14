# Knowl Generation Workflow v2

This is the improved knowl generation workflow, incorporating lessons learned from generating ~1,500 knowls.

## Key Improvements Over v1

1. **Anti-pattern prevention** - Explicit rules baked into prompts
2. **Cross-section linking** - Mandatory `section` parameter for external references
3. **Single-repo workflow** - Content and infrastructure versioned together
4. **Consolidated layouts** - No per-section layout creation needed
5. **Validation integration** - Automated broken link detection
6. **Consistency standards** - Uniform style across all sections

## Quick Reference

| Document | Purpose |
|----------|---------|
| `anti-patterns.md` | What NOT to generate (critical reading) |
| `prompt-template.md` | Base prompt with all rules embedded |
| `workflow.md` | Step-by-step generation process |
| `validation.md` | Post-generation quality checks |
| `../knowl-generation/orchestration.md` | Oracle/GPT automation (v1, still applicable) |

## Anti-Patterns Summary

These MUST be avoided in all generated knowls:

| Anti-Pattern | Description | Count in v1 |
|--------------|-------------|-------------|
| Related knowls section | Separate section listing related concepts | 41 files |
| Knowl in LaTeX | `{{< knowl >}}` inside `$...$` or `$$...$$` | 14 instances |
| `={{<` pattern | Knowl shortcode in equation context | 10 instances |
| Missing section param | Cross-section links without `section="..."` | 97+ references |
| Proof sketch inconsistency | Some sections have them, others don't | 283 files |

## Workflow Overview

```
1. Enumerate      → List all knowls needed for a section
2. Dependency     → Topological sort + slug manifest
3. Generate       → Create knowls with cross-links (parallel batches)
4. Validate       → Check for anti-patterns and broken links
5. Review         → Manual quality check
6. Commit         → Commit section changes in-repo
```

## Repository Structure

```
mathblog/                          ← Pipeline repo
├── docs/v2-knowl-generation/      ← This workflow
├── scripts/validate-knowls.py     ← Validation script
└── content/                       ← Tracked knowl corpus
```

## Getting Started

1. Read `anti-patterns.md` thoroughly
2. Set up your generation environment (see `workflow.md`)
3. Use `prompt-template.md` as the base for all generation prompts
4. Run validation after each batch

## Style Standards

### Always Include
- YAML front matter with `title` and `description`
- Clear, formal definition/theorem statement
- 2-3 concrete examples for definitions
- Cross-links woven naturally into prose

### Never Include
- "Related knowls" or "See also" sections
- Knowl shortcodes inside math blocks
- Proof sketches (removed for consistency)
- Categorized sub-bullets

### Cross-Section Links

**Same section** (section parameter optional):
```markdown
{{< knowl id="subgroup" text="subgroup" >}}
```

**Different section** (section parameter REQUIRED):
```markdown
{{< knowl id="vector-space" section="linear-algebra" text="vector space" >}}
{{< knowl id="ring" section="algebra-rings" text="ring" >}}
```

## Section Directory Mapping

| Section | Content |
|---------|---------|
| `shared-foundations` | Set theory, logic, functions, relations |
| `linear-algebra` | Vector spaces, linear maps, matrices, eigenvalues |
| `algebra-groups` | Groups, subgroups, homomorphisms, actions |
| `algebra-rings` | Rings, ideals, fields, polynomials |
| `algebra-modules` | Modules, exact sequences, tensor products |
| `algebra-fields-galois` | Field extensions, Galois theory |
| `algebra-commutative` | Commutative algebra, localization, Noetherian |
| `algebra-category-theory` | Categories, functors, natural transformations |
| `algebra-homological` | Chain complexes, derived functors, Ext/Tor |
| `algebra-representation-theory` | Group representations, characters |
| `analysis` | Real analysis, metric spaces, convergence |
| `convex-analysis` | Convex sets, functions, optimization |
| `fiber-bundles` | Fiber bundles, connections, curvature |
| `lie-groups` | Lie groups, Lie algebras |
