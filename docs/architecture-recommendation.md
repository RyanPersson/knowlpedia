# Goal-First Architecture Recommendation

Date: 2026-06-30

This document intentionally derives the architecture from the intended goals of
the system, not from the current Knowlpedia implementation and not from LMFDB.

## Intended Goal

Build an open mathematical communication format and runtime for LaTeX-rich,
interlinked writing where:

- definitions can be minimal, axiomatic, and recursively expandable
- each mathematical object has a full page and inline knowl views
- optional sections such as examples, TFAE, categorical definitions, relations,
  proofs, Lean data, and citations can unfold progressively
- proof steps can cite the exact axiom, lemma, definition, or subproof they use
- lecture notes can be written in the same format
- mobile reading is excellent
- static publishing is first-class
- local dynamic tooling and AI-agent workflows are possible
- the format can be adopted by mathematicians without running a central service

## Architectural Consequence

The system should be a **portable semantic hypertext format** with a compiler and
multiple runtimes.

It should not be primarily a website, a database, or a pile of markdown files.

The best architecture is:

```text
human/agent-authored semantic source
        |
        v
validated mathematical object graph
        |
        v
compiled outputs
  - static HTML pages
  - inline fragments
  - relation indexes
  - proof indexes
  - search indexes
  - optional SQLite/database artifact
  - optional local live authoring server
```

The canonical layer is the semantic object graph. Files are the best default
storage format for that graph, but plain markdown alone is not expressive enough.

## Primary Recommendation

Use **structured source files as the canonical format**, and compile them into
fast static and database-like artifacts.

In short:

```text
files are source
graph is model
compiler is authority
static site is default runtime
database is optional cache/query artifact
```

## Why This Follows From The Goals

### The format should be adoptable

Mathematicians should be able to write, review, fork, diff, archive, and publish
the format without asking permission from a service.

That points toward canonical text files in git or ordinary folders.

### The system should be semantically rich

Definitions, examples, TFAE sections, proof steps, relations, citations, and Lean
metadata need typed structure.

That points away from ordinary markdown as the complete model.

### The system should be fast

Readers should not pay the cost of parsing the whole corpus at runtime.

That points toward compiled indexes, pre-rendered fragments, content hashes,
lazy-loaded sections, and client-side caches.

### The system should be static-publishable

Course notes and personal sites should work on static hosting.

That points away from requiring a server database in the publishing path.

### The system should support AI workflows

Agents need stable ids, schemas, validation errors, relation targets, and places
to write draft knowls, proofs, examples, and diagrams.

That points toward a compiler with strict validation and machine-readable
intermediate artifacts.

### The system should work well on mobile

Mobile performance depends on payload shape and interaction design:

- fetch only the sections being opened
- avoid runaway nested indentation
- keep math scrollable
- provide full-page reading mode
- make proof steps accordion-like
- make controls touch-sized

That points toward section-level fragments and a mobile-specific disclosure UI,
not toward a particular backend database.

## Recommended System Layers

### 1. Source Format

The source format should be human-editable, git-friendly, and schema-validated.

Support two authoring forms:

```text
single-file knowl
  compact concepts, lemmas, examples

bundle knowl
  larger objects with examples, proofs, TFAE, Lean data, citations, diagrams
```

Example single-file source:

```text
content/shared-foundations/injective-function.knowl.md
```

Example bundle source:

```text
content/algebra-groups/group/
  knowl.yaml
  core.md
  examples.md
  tfae.yaml
  relationships.yaml
  proofs/
    cayley-theorem.yaml
  lean.yaml
  sources.yaml
```

The author-facing files can contain markdown and LaTeX, but the metadata and
relationships should be typed.

### 2. Mathematical Object Graph

The compiler should normalize source files into a graph.

Node types:

- knowl
- section
- definition
- theorem
- lemma
- proof
- proof step
- example
- diagram
- citation
- Lean declaration

Edge types:

- uses
- proves
- assumes
- equivalent_to
- special_case_of
- generalizes
- example_of
- counterexample_to
- prerequisite_of
- cites
- formalizes
- alternate_definition_of

This graph is the real model of the system.

### 3. Validation

The compiler should be strict. Invalid semantic links should fail the build or at
least produce severity-ranked reports.

Validation targets:

- unique ids
- aliases and redirects
- valid knowl links
- valid section links
- valid relation endpoints
- valid proof-step justifications
- no links inside math unless explicitly supported
- citation requirements by confidence tier
- Lean declaration references
- diagram source validity
- mobile rendering hazards such as extremely long unbreakable labels

### 4. Render Targets

The same graph should compile into multiple render targets:

- static website
- local authoring preview
- printable notes
- single-course bundle
- machine-readable JSON
- optional SQLite
- future dynamic hosted app

This is important. The project is a format plus compiler, not merely one website.

### 5. Static Runtime

The default reader runtime should need only static files.

It should support:

- normal full pages
- inline recursive knowl expansion
- section-level lazy loading
- proof-step expansion
- TFAE panels or definition switchers
- relation graph widgets
- static search
- mobile-first disclosure behavior

The runtime should never need to query a server just to read an ordinary page.

### 6. Optional Local Dynamic Runtime

A local server is useful for authors and agents.

It can provide:

- file watching
- incremental compilation
- validation dashboards
- graph queries
- draft management
- TikZ compilation
- AI-agent write targets
- SQLite-backed local search

This should be optional tooling, not part of the minimum publishing requirement.

## Database Recommendation

Do not make a database canonical at the beginning.

Use databases as compiled artifacts.

### Best first database artifact: SQLite

SQLite fits the goals because it is:

- one file
- regenerable
- portable
- easy for local tools
- good for dashboards and relation queries
- compatible with static export as an optional artifact

### When a server database becomes appropriate

A server database becomes appropriate only for a central hosted version with:

- live editing
- user accounts
- review queues
- large dynamic search
- heavy object-table queries
- analytics
- collaborative moderation

That may eventually exist, but it should not define the open format.

## Recommended File Format Direction

Avoid inventing a syntax that is too clever.

Use:

- markdown for prose
- YAML or JSON for typed metadata
- explicit ids for addressable objects
- fenced blocks for structured proof fragments only if they remain readable
- separate sidecar files for large proof graphs, examples, relations, and Lean
  data

The format should be boring enough to survive.

## Recommended Package Shape

A portable mathematical text can be a "knowl package":

```text
knowlpack.yaml
content/
assets/
citations/
compiled/
```

`knowlpack.yaml` should define:

- package id
- title
- version
- authors
- license
- root notes/pages
- dependencies on other knowl packages
- compiler version constraints

This lets a course, paper companion, textbook chapter, or entire wiki share the
same packaging idea.

## Proof Architecture

Proofs should be structured objects, not just prose.

A proof should support:

- human-readable statement
- hierarchical steps
- local assumptions
- references to previous steps
- references to external knowls
- hidden subproofs
- exported prose proof
- exported LaTeX proof
- optional Lean link or Lean proof

Every proof step should have a stable address:

```text
group/cayley-theorem#proof.main.step.3.2
```

This is what makes clickable justifications possible.

## TFAE And Alternate Definitions

TFAE should be a standard optional object type.

It should not be forced into ordinary prose because equivalence claims often have
scope conditions.

A TFAE object should encode:

- hypotheses
- equivalent statements
- proof links between implications
- source citations
- whether each equivalence is definitional, theorem-level, classical, finite-only,
  category-specific, or dependent on additional assumptions

The UI can then render:

- a TFAE section
- a definition switcher
- an implication graph
- compact alternate-definition buttons

## Mobile Recommendation

Make the full page excellent on mobile and make inline expansion conservative.

For small screens:

- open inline knowls as full-width panels
- cap visual nesting
- provide "open full page" prominently
- use accordions for optional sections
- lazy-load examples/proofs/diagrams/Lean data
- keep formulas horizontally scrollable inside math blocks
- avoid placing controls only at the bottom of long panels
- use stable touch targets
- let the browser back button close deep panels where possible

Mobile quality should be tested as a core acceptance criterion, not a later CSS
polish pass.

## Performance Recommendation

Performance should come from compilation and loading strategy:

- pre-render math
- pre-render knowl fragments
- split large knowls into section fragments
- content-hash fragments for long-term caching
- static registry for ids and aliases
- static relation graph indexes
- static search index
- lazy-load proofs, examples, diagrams, and Lean details
- avoid loading the whole graph on first page load

The main corpus can be huge as long as each page loads a small, predictable
subset.

## Migration Recommendation

Do not migrate the whole existing corpus first.

Start by proving the model with a tiny canonical set:

- `group`
- `vector-space`
- `category`
- one theorem with a structured proof
- one TFAE object
- one relation graph
- one TikZ/category-theory diagram later, if needed

Then build importers from legacy markdown into draft knowl objects.

Manual migration of a large corpus before the schema is proven would waste
energy.

## Concrete Starting Plan

1. Define `knowlpack.yaml`.
2. Define the normalized graph schema.
3. Implement a compiler that reads single-file and bundle knowls.
4. Emit `registry.json`, `relations.json`, and static HTML fragments.
5. Render the three test concepts as full pages and inline fragments.
6. Add one structured proof and clickable justifications.
7. Add one TFAE object and render it two ways: section and switcher.
8. Add mobile acceptance checks before expanding scope.

## Recommendation In One Sentence

Build a git-native semantic math object format with a strict compiler, static
runtime, mobile-first disclosure UI, and optional database artifacts for local
tooling and future hosted services.

