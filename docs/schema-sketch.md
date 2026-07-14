# Schema Sketch

This is an intentionally early sketch. It is a target for discussion, not a
committed file format.

## Design Goals

- Knowls should be atomically addressable.
- Full pages and inline panels should use the same underlying content model.
- Sections should be independently unfoldable.
- Relations should be queryable.
- Proof steps should be linkable.
- Static export should remain straightforward.
- A database should be optional, not required for publishing.

## Entity Types

Potential first-class entities:

- `knowl`: a definition, theorem, construction, example, axiom, method, object,
  proof step, or named mathematical idea.
- `section`: an unfoldable unit attached to a knowl.
- `edge`: a typed relation between knowls or sections.
- `proof`: a structured proof graph or tree.
- `proof_step`: an addressable assertion with justifications.
- `source`: a citation, Mathlib declaration, textbook reference, or human review.
- `diagram`: a rendered TikZ, SVG, canvas, or image artifact.

## Minimal Knowl Fields

```yaml
id: string
title: string
kind: definition | theorem | lemma | example | construction | axiom | proof | note
slug: string
summary: string
domains: string[]
aliases: string[]
status: draft | reviewed | synced | deprecated
```

## Core Definition Fields

```yaml
core:
  statement_md: string
  assumptions:
    - id: string
      text: string
      refs: string[]
  data:
    - id: string
      text: string
      refs: string[]
  axioms:
    - id: string
      text: string
      refs: string[]
```

For a theorem or lemma, replace `data` and `axioms` with hypotheses and
conclusions. The same display machinery can still work.

## Section Model

```yaml
sections:
  - id: minimal-definition
    title: Minimal definition
    kind: definition
    default_open: true
    source: ./definition.md

  - id: examples
    title: Examples
    kind: examples
    default_open: false
    source: ./examples.md

  - id: tfae
    title: Equivalent characterizations
    kind: tfae
    default_open: false
    source: ./tfae.yaml

  - id: category-theoretic-definition
    title: Category-theoretic definition
    kind: alternate-definition
    default_open: false
    source: ./category.md
```

Sections should have stable ids so external links can target a subsection:

```text
/algebra-groups/group#section=tfae
/algebra-groups/group?open=tfae,examples
```

## Edge Model

```yaml
edges:
  - type: prerequisite_of
    from: monoid
    to: group
    scope: definition

  - type: equivalent_to
    from: group/minimal-definition
    to: group/folded-definition
    scope: classical-algebra

  - type: example_of
    from: symmetric-group
    to: group

  - type: object_in_category
    from: group
    to: category-of-groups
```

Edges should support optional metadata:

```yaml
confidence: reviewed | generated | conjectural | imported
source: mathlib | human | citation | generated
conditions: "finite groups only"
```

## TFAE Model

```yaml
tfae:
  title: Equivalent characterizations of compactness
  hypotheses:
    - "X is a metric space"
  items:
    - id: sequential-compactness
      statement: "Every sequence has a convergent subsequence."
      refs:
        - sequential-compactness
    - id: open-cover-compactness
      statement: "Every open cover has a finite subcover."
      refs:
        - open-cover
  proof:
    type: cycle
    steps:
      - from: open-cover-compactness
        to: sequential-compactness
        proof_ref: proof-compact-implies-sequential
```

The UI can render this as a TFAE list, a definition switcher, or a proof graph.

## Structured Proof Model

```yaml
proof:
  id: proof-example
  proves: theorem-id
  statement: "A concise theorem statement."
  steps:
    - id: "1"
      level: 1
      assertion_md: "First assertion."
      justifications:
        - type: uses
          target: definition-id

    - id: "2"
      level: 1
      assertion_md: "Second assertion."
      justifications:
        - type: uses
          target: "step:1"
        - type: uses
          target: lemma-id
      subproof:
        steps:
          - id: "2.1"
            level: 2
            assertion_md: "Hidden detail."
            justifications:
              - type: uses
                target: axiom-id
```

Rendering requirements:

- Every `target` should become clickable.
- A proof step can unfold its subproof.
- A justification can unfold the specific knowl it uses.
- A proof can export to ordinary LaTeX, readable markdown, and eventually Lean.

## Verification Metadata

```yaml
verification:
  formal_sync:
    status: pass | fail | unknown
    system: lean4
    source_decl: Mathlib.Algebra.Group.Defs.Group
    source_hash: string
    checked_at: date

  human_review:
    status: reviewed | unreviewed | needs_changes
    reviewer: string
    scope: "definition only"
    reviewed_at: date

  literature:
    status: cited | uncited | partial
    sources:
      - type: book
        citation_key: dummit-foote
        locator: "Section 1.1"

  overall_confidence: A | B | C | unknown
```

## Static Build Artifacts

The compiler should be able to emit:

```text
public/
  algebra-groups/group/index.html
  fragments/algebra-groups/group/core.html
  fragments/algebra-groups/group/examples.html
  indexes/registry.json
  indexes/relations.json
  indexes/search.json
  indexes/proofs.json
  indexes/knowls.sqlite
```

The SQLite file is useful for local search, dashboards, and maybe browser-side
querying through WebAssembly, but plain JSON should be enough for static readers.

