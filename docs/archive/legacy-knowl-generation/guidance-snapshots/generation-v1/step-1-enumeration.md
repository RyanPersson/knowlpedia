# Step 1: Enumerate Knowl Candidates (Atomic Definitions + Results)

## Your Task

Produce an **over-complete, high-granularity** enumeration of all items that should become separate knowls for a standard course on the given subject/level. The output is meant to seed a dependency graph and then a linked knowlset. Therefore:

- Prefer **more** items at **finer** granularity.
- Use **atomic** units: one definition/result per knowl-candidate.
- Explicitly include **equivalence packages** (TFAE lists) as their own knowl objects.


## Inputs

You will be given:

- **Subject**: e.g. "Real Analysis", "Abstract Algebra", "Principal Bundles and Connections"
- **Level**: one of 200-level | 300-level | 400-level | 500-level | 600-level
- **Scope constraints** (optional): inclusions/exclusions, emphasis (e.g. "geometry-heavy", "physics-gauge-theory flavor"), and any forbidden topics


## Atomicity / Granularity Rules (strict)

A. **Atomic definition** = a definition that introduces exactly one new predicate/structure/property on top of already-listed data.

   Examples (each should be separate items):
   - "bundle" vs "vector bundle" vs "principal G-bundle" vs "associated bundle"
   - "connection" vs "principal connection" vs "connection 1-form" vs "covariant derivative" vs "curvature" vs "holonomy"
   - "compact" vs "sequentially compact" vs "totally bounded" vs "complete"

B. If a notion has **standard variants**, list each variant as its own knowl:
   - left/right versions, local/global versions, smooth/topological versions, based/pointed versions, equivariant versions, etc.

C. If a concept is usually taught as a **cluster** (e.g., connections), do *not* collapse it into one bullet. List all standard components separately.

D. Avoid "mega-items" like "Gauge theory" unless you also decompose them into the concrete definitions/results that actually appear.


## Equivalences (TFAE) Rule

Whenever a course proves multiple conditions equivalent:

1. Create a separate item in a dedicated section:
   - TFAE: [Concept] — [Setting]

2. Also list each individual condition as its own knowl-candidate in the appropriate section (Definitions / Theorems / Propositions), using short canonical names.

3. The TFAE item should be written so it can link out to each condition-item.


## Scope Discipline (but biased toward inclusion)

- Include everything that is **commonly** encountered in a standard course at that level.
- If you are uncertain whether something belongs in the "core", include it anyway but place it under **Common Extensions** (see below).
- Do not include highly specialized research-only material unless explicitly requested.


## Output Format

Return a single markdown code block. Use bullet points only (no numbering). You may use nested bullets to express families, but every *leaf bullet* must be a valid standalone knowl-candidate name.

```markdown
# [Subject] — [Level] Knowl Enumeration (High Granularity)

## Core Definitions (atomic)

- ...
- ... (optional nested family)
  - ...

## Core Axioms / Conventions

- ...

## Core Constructions / Objects

(standard constructions that are not best phrased as "definitions", but will be referenced as objects)

- ...

## Core Theorems

- ...

## Core Lemmas

- ...

## Core Propositions

- ...

## Core Corollaries

- ...

## Core Equivalences (TFAE packages)

- TFAE: ...
  - Condition: ...
  - Condition: ...
- ...

## Standard Examples / Counterexamples

(if typically used in the course)

- ...

## Common Extensions

(often taught, instructor-dependent; include aggressively)

### Definitions

- ...

### Theorems / Results

- ...

### TFAE packages

- ...
```


## Naming Requirements

Use the most canonical/common names. If multiple names are genuinely standard, choose one canonical name and include aliases in parentheses:

```
Arzelà–Ascoli Theorem (Arzela–Ascoli)
```

For unnamed-but-standard results, use stable descriptive names:

```
Uniqueness of lift for covering maps (example style)
```


## Completeness Sanity Checks (required)

Before outputting, ensure:

1. No category is silently omitted; if empty, write `(none)`.
2. Every theorem/lemma/proposition you list uses only concepts that appear somewhere in the enumeration.
3. Equivalent formulations are handled via both individual items and a TFAE package item.
