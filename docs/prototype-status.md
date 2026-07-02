# Prototype Status

Date: 2026-07-01

## What Exists

This repo now contains a first working prototype of the goal-first architecture:

```text
examples/basic/              semantic source package
imports/knowlpedia-content/  imported legacy corpus package
packages/compiler/           Python compiler
packages/importers/          legacy corpus importer
packages/schema/             prototype schema notes
packages/static-runtime/     static browser runtime
requirements.txt             build-time math fallback dependency
package.json                 build-time KaTeX and browser-check dependencies
public/                      generated output, ignored by git
public-imported/             generated full-corpus output, ignored by git
```

The compiler reads typed source files, normalizes them into a graph, validates
semantic links, and emits static artifacts.

## Example Source

The example package includes 8 knowls:

- `algebra-groups/group`
- `algebra-groups/monoid`
- `algebra-category-theory/category`
- `linear-algebra/vector-space`
- `shared-foundations/set`
- `shared-foundations/function`
- `shared-foundations/binary-operation`
- `shared-foundations/field`

The `group` knowl is the main stress test. It includes:

- a canonical core definition
- typed data
- typed axioms
- examples
- a TFAE/alternate-definition section
- a structured proof of identity uniqueness
- typed relations

## Build Command

```bash
make build
```

Equivalent direct command:

```bash
.venv/bin/python packages/compiler/knowl_compile.py examples/basic --out public
```

## Serve Command

```bash
make serve
```

The generated site expects to be served over HTTP because inline knowls fetch
fragment files.

## Generated Artifacts

The build emits:

```text
public/index.html
public/<knowl-id>/index.html
public/fragments/<knowl-id>/core.html
public/fragments/<knowl-id>/sections/<section-id>.html
public/indexes/registry.json
public/indexes/links.json
public/indexes/relations.json
public/indexes/proofs.json
public/indexes/knowls.sqlite
public/reports/validation.json
public/assets/knowl.css
public/assets/knowl.js
```

## Verification Run

Last verified:

```bash
make build
make build-imported
python3 -m py_compile packages/compiler/knowl_compile.py packages/importers/import_knowlpedia_content.py
```

Results:

- 8 knowls compiled
- validation report was empty
- SQLite artifact contained 8 knowls and 7 relations
- local HTTP smoke test returned 200 for `/`
- local HTTP smoke test successfully fetched
  `/fragments/algebra-groups/group/core.html`
- full legacy corpus imported and built into `public-imported/`
- imported build emitted 2,089 knowls and 13,815 links
- imported build had 31 validation errors and 27 warnings from legacy dangling
  links, missing targets, or duplicate aliases
- Playwright loaded the Tailscale `/topics/` page and clicked the fixed
  algebra-commutative Hilbert basis corollary knowl

The `sqlite3` shell was not installed in this environment, so the SQLite artifact
was checked through Python's standard `sqlite3` module.

## Important Prototype Limits

- Markdown rendering is intentionally minimal.
- Math is rendered at build time with repo-local npm KaTeX when available. The
  generated HTML falls back to `latex2mathml`, then client-side MathJax, when
  KaTeX is missing.
- TOML is used because it is available in the Python standard library. The
  architecture does not depend on TOML specifically.
- The static runtime has template caching, eager page preloading, index
  viewport preloading, hover/focus/touch preloading, nested preloading, instant
  open behavior, and a manual theme toggle.
- The static runtime does not yet implement service workers, keyboard traversal
  inside proofs, focus management, or advanced mobile history behavior.
- The compiler validates links, anchors, relations, TFAE references, and proof
  step references, but the schema is still early.
- Wikilink labels can contain literal `]`; the compiler treats `]]` as the
  label terminator.

## Next Good Step

Add a second proof with an actual nested subproof, then update the proof renderer
so subproofs fold and unfold recursively.

## Full Corpus Import

The legacy `../knowlpedia-content` corpus has also been imported into the new
format. See `docs/imported-content-status.md`.

## Current Handoff

For the latest implementation summary, commands, validation state, and remaining
work, see `docs/current-refactor-handoff.md`.
