# Modular Knowl System

This directory contains a modular decomposition of mathematical knowls into focused, composable units.

## Philosophy

Rather than generating monolithic knowl sets for entire subjects, we decompose mathematics into:

1. **Shared Pools** — Foundational concepts used across multiple fields
2. **Focused Modules** — Topic-specific additions to the shared pools

A course's knowl set is constructed by combining the relevant shared pools with the appropriate focused modules.

## Structure

```
knowl-modules/
├── README.md                         # This file
├── decomposition.md                  # Shared pools + algebra modules
├── analysis-decomp.md                # Analysis modules + convex analysis
├── source-real-analysis-400.md       # Original enumeration (Baby Rudin)
└── source-abstract-algebra-500.md    # Original enumeration (graduate algebra)
```

## Current Content Structure

```
content/
├── shared-foundations/    # 58 knowls - Sets, functions, relations, orders
├── linear-algebra/        # 27 knowls - Vector spaces, linear maps, eigenvalues
├── real-analysis/         # 234 knowls - Sequences, continuity, differentiation, integration
├── topology/              # 97 knowls - Metric spaces, compactness, connectedness
├── measure-theory/        # 26 knowls - Lebesgue measure, integration
├── convex-analysis/       # Convex sets/functions, separation theorems
├── algebra-groups/        # Group theory through Sylow
├── algebra-rings/         # Rings, ideals, PIDs, UFDs
├── algebra-modules/       # Modules, tensor products
├── algebra-fields-galois/ # Field extensions, Galois theory
├── algebra-commutative/   # Localization, Noetherian rings
├── algebra-homological/   # Chain complexes, Ext, Tor
├── algebra-representation-theory/  # Representations, characters
├── algebra-category-theory/        # Categories, functors, Yoneda
├── lie-groups/            # Lie groups and algebras
└── fiber-bundles/         # Fiber bundles, connections
```

## Shared Pools

| Pool | Knowls | Description | Used By |
|------|--------|-------------|---------|
| `shared-foundations` | 58 | Sets, functions, relations, orders | Everything |
| `linear-algebra` | 27 | Vector spaces, linear maps, eigenvalues | Analysis, Algebra, many others |

## Analysis Modules

| Module | Knowls | Content |
|--------|--------|---------|
| `real-analysis` | 234 | Sequences, series, continuity, differentiation, Riemann integration, multivariable |
| `topology` | 97 | Metric spaces, open/closed sets, compactness, connectedness |
| `measure-theory` | 26 | Lebesgue measure, measurable functions, integration |
| `convex-analysis` | — | Convex sets/functions, separation, Hahn–Banach |

## Algebra Modules

| Module | Content |
|--------|---------|
| `algebra-groups` | Group theory through Sylow |
| `algebra-rings` | Rings, ideals, PIDs, UFDs |
| `algebra-modules` | Modules, tensor products, projective/injective |
| `algebra-fields-galois` | Field extensions, Galois theory |
| `algebra-commutative` | Localization, Noetherian, primary decomposition |
| `algebra-homological` | Chain complexes, Ext, Tor |
| `algebra-representation-theory` | Representations, characters |
| `algebra-category-theory` | Categories, functors, Yoneda |

## Occurrence Counts

Items in the decomposition files are marked with occurrence counts like `(×2)`. This indicates how many modules use that concept:

- **×1**: Appears in one module only (topic-specific)
- **×2+**: Appears in multiple modules (candidate for shared pool)

Items with high counts should live in shared pools; items with ×1 are specific to their module.

## Composing a Course

Each section is self-contained. Cross-references use the knowl shortcode with explicit section:

```hugo
{{</* knowl id="vector-space" section="linear-algebra" text="vector space" */>}}
```

**Example: Real Analysis Course**
- `shared-foundations` — prerequisite definitions
- `linear-algebra` — for multivariable topics
- `real-analysis` — main content
- `topology` — metric space foundations

**Example: Graduate Algebra Course**
- `shared-foundations` — prerequisite definitions
- `linear-algebra` — for module theory
- `algebra-groups`
- `algebra-rings`
- `algebra-modules`
- `algebra-fields-galois`

## Avoiding Duplication

When a knowl appears in multiple modules:
1. It lives in the **shared pool** (`shared-foundations` or `linear-algebra`) if high-occurrence
2. It lives in the **first module in dependency order** if lower-occurrence
3. Later modules reference it via knowl shortcodes but don't recreate it

Knowl files are organized in flat section directories:
```
content/
  shared-foundations/
    set.md
    function.md
    ...
  real-analysis/
    metric-space.md
    cauchy-sequence.md
    ...
  algebra-groups/
    group.md
    normal-subgroup.md
    ...
```

## Extending the System

To add a new subject (e.g., Topology, Number Theory):

1. Generate the full enumeration using `knowl-generation/step-1-enumeration.md`
2. Add it as `source-[subject]-[level].md`
3. Decompose it in the appropriate decomposition file, marking overlaps with existing modules
4. Create new focused modules as needed
5. Identify new shared pool candidates (items with ×3+ occurrences)
