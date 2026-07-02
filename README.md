# Knowl System Refactor

This repo prototypes a goal-first architecture for a next-generation knowl
system.

The project is not defined by the current Knowlpedia implementation and not by
LMFDB. It is defined by the intended goal: a portable semantic hypertext format
for mathematical writing, with recursive knowls, structured proofs, TFAE views,
relations, static publishing, mobile-friendly disclosure, and optional local
automation tooling.

## Current Prototype

This repo now contains a first working compiler/runtime prototype:

```text
examples/basic/              semantic source package
packages/compiler/           Python compiler
packages/schema/             prototype schema notes
packages/static-runtime/     static browser runtime
public/                      generated output, ignored by git
```

Build it with:

```bash
make deps
make build
```

Serve it locally with:

```bash
make serve
```

`make deps` installs the Python fallback renderer from `requirements.txt` and
the local Node dependencies from `package-lock.json`, including KaTeX for
build-time math rendering. For Playwright browser checks on a fresh machine,
also run `npm run playwright:install`.

TikZ diagram SVG output also requires system TeX tools such as `latex` and
`dvisvgm`; on Debian/Ubuntu, install:

```bash
sudo apt install texlive-latex-base texlive-latex-extra texlive-pictures texlive-fonts-recommended dvisvgm
```

The generated site uses static HTML, static knowl fragments, JSON indexes, and an
optional SQLite artifact.

See `docs/prototype-status.md` for the current implementation status.
For the latest handoff summary, including imported corpus status, performance
notes, validation counts, and remaining work, see
`docs/current-refactor-handoff.md`.

## Mission

Design a richer knowl format and renderer where mathematical objects have a small
axiomatic core plus optional unfoldable layers:

- minimal definitions and axioms
- folded/structural definitions
- TFAE and equivalent characterizations
- exhaustive or curated examples
- category-theoretic definitions where applicable
- subset, superset, specialization, and generalization relations
- structured proofs and subproofs
- Lean statements/proofs and ordinary LaTeX proofs
- verification and confidence metadata

The long-term goal is an open source format for mathematicians to communicate in
LaTeX-rich, interlinked, recursively expandable mathematical writing.

## Core Constraint

The format should remain easy to publish on static hosting:

- GitHub Pages
- university static pages

That constraint argues against making a hosted database mandatory. A database may
still be very useful as a build artifact or local development accelerator.

## Working Hypothesis

Use structured source files as the canonical format, then compile them into fast
static artifacts.

In other words:

1. Authors and agents edit files.
2. A build step validates and indexes those files.
3. The build emits static HTML, knowl fragments, relation indexes, search indexes,
   and optionally a SQLite/JSON/NDJSON database artifact.
4. Runtime pages stay deployable on static hosting.

This gives database-like query performance without requiring every professor,
student, or static site owner to run a database server.

See `docs/architecture-recommendation.md` for the goal-first architecture
recommendation.

## Interaction Model

The user experience should support both reading styles:

- Inline mode: click a term to unfold the knowl in place; nested knowls unfold
  recursively.
- Page mode: open the knowl full page through a normal link affordance, modified
  click, context menu, or a visible "full page" action.
- Deep mode: progressively unfold further folded sections by clicking such as examples,
  TFAE, categorical definitions, relationship graph, proof details, and Lean data.

(Feedback)

Mobile should be a first-class target. Foldouts must avoid horizontal overflow,
unbounded nesting width, tiny controls, and panels that trap the reader.

## Data Model Sketch

A knowl should be more than one markdown blob. A possible logical model:

```yaml
id: group
slug: algebra-groups/group
title: Group
kind: definition
domains:
  - algebra
  - group-theory
aliases:
  - group
  - abstract group

core:
  statement: ./definition.md
  data:
    - carrier set
    - binary operation
    - identity element
    - inverse operation
  axioms:
    - associativity
    - identity laws
    - inverse laws

sections:
  equivalent_characterizations: ./tfae.md
  category_theoretic_definition: ./category.md
  relationships: ./relationships.yaml
  structured_proofs: ./proofs.yaml
  examples: ./examples.md
  literature: ./sources.yaml

verification:
  formal_sync: unknown
  human_review: unknown
  literature_alignment: unknown
```

The exact file syntax is open. The important part is separating semantic structure
from presentation so the same knowl can render as a full page, inline panel,
compact tooltip, export bundle, or database row.

## Relationship Types

The system should treat mathematical relationships as first-class edges:

- `prerequisite_of`
- `uses`
- `implies`
- `equivalent_to`
- `special_case_of`
- `generalization_of`
- `example_of`
- `counterexample_to`
- `subset_of`
- `superset_of`
- `object_in_category`
- `morphism_in_category`
- `same_as`

These edges can power navigation, validation, graph views, prerequisite maps,
TFAE rendering, and automatic linking.

## Proof Format Direction

Use a structured proof format inspired by Leslie Lamport's hierarchical proofs.
Each step should be an addressable object.

Example shape:

```yaml
id: proof-subgroup-one-step-test
proves: subgroup-test-one-step
style: structured
steps:
  - label: "1"
    assertion: "H is nonempty."
    justification:
      - uses: hypothesis
  - label: "2"
    assertion: "For all a,b in H, ab^{-1} is in H."
    justification:
      - uses: hypothesis
  - label: "3"
    assertion: "H is closed under multiplication."
    justification:
      - uses: step-2
      - uses: inverse-closed
  - label: "4"
    assertion: "H is a subgroup of G."
    justification:
      - uses: subgroup-definition
      - uses: step-1
      - uses: step-3
```

Rendered proof steps should have clickable justifications. Clicking an axiom,
lemma, previous step, or hidden subproof unfolds the relevant knowl or proof node.

## TFAE and Equivalent Definitions

Equivalent characterizations should probably be a standard optional section, not
a mandatory section on every knowl. When present, it should be structured enough
to distinguish:

- equivalent definitions
- theorem-level characterizations
- categorical reformulations
- finite-only or hypothesis-dependent equivalences
- historical or field-specific terminology

For the UI, two modes are worth prototyping:

- A list-style TFAE section on the full page.
- A compact "definition switcher" that lets a reader alternate between axiomatic,
  folded, categorical, or theorem-based definitions.

## Storage Options

### Option A: Markdown plus structured sidecars

Canonical files are ordinary markdown plus YAML/JSON files.

Pros:

- easy to edit
- friendly to static hosting and git diffs
- approachable for mathematicians
- compatible with the existing Hugo pipeline

Cons:

- cross-file validation is essential
- query performance requires build indexes

### Option B: Single structured `.knowl.md` files

Each knowl is one markdown file with front matter and named blocks.

Pros:

- easy to move around
- one-file authoring
- still static and git-native

Cons:

- block syntax must be designed carefully
- hard to store large proof graphs cleanly

### Option C: SQLite as source of truth

Knowls live directly in a database.

Pros:

- fast queries
- clear relational model
- good for local servers and dashboards

Cons:

- less friendly to static school webpages
- harder for casual contributors
- merge conflicts and review are worse than text files

### Option D: Files as source, database as build artifact

Source remains text files. The compiler emits SQLite, JSON, or NDJSON indexes.

Pros:

- static-site compatible
- fast local and browser queries
- good bridge to future hosted apps
- preserves git review and easy authoring

Cons:

- compiler and schema validation become central infrastructure

Current recommendation: start with Option D.

## Build Outputs

A mature compiler could emit:

- full static HTML pages
- inline knowl fragments
- section fragments for progressive unfold
- `registry.json` mapping ids, slugs, aliases, and sections
- `relations.json` or graph data
- search index
- proof graph index
- optional SQLite database
- validation report
- unresolved reference report
- Lean sync report

## MVP Proposal

1. Specify a tiny schema for three test knowls: `group`, `vector-space`, and
   `category`.
2. Write a compiler that emits current-Hugo-compatible markdown or HTML so the
   new model can piggyback on the existing site.
3. Add section-level fold/unfold rendering on full knowl pages.
4. Add modified-click behavior so inline knowl triggers preserve normal link
   affordances.
5. Build a relation registry and validate all knowl references against it.
6. Test the result on mobile widths before expanding the corpus.

## Open Questions

- What is the canonical granularity: every Mathlib class, every pedagogically
  important concept, or both with different visibility levels?
- Should axiomatic definitions always be the primary definition?
- How should additive/multiplicative duality be represented?
- Where should TFAE characterizations come from: manual curation, nLab,
  textbooks, Mathlib, Wikipedia, or a cited literature layer?
- How should source citations and confidence metadata be enforced?
- How much Lean should be visible to ordinary readers?
- Should the optional database artifact be SQLite, DuckDB, static JSON bundles,
  or multiple targets?
