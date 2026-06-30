# Prototype Status

Date: 2026-06-30

## What Exists

This repo now contains a first working prototype of the goal-first architecture:

```text
examples/basic/              semantic source package
packages/compiler/           Python compiler
packages/schema/             prototype schema notes
packages/static-runtime/     static browser runtime
public/                      generated output, ignored by git
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
python3 packages/compiler/knowl_compile.py examples/basic --out public
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
python3 packages/compiler/knowl_compile.py examples/basic --out public
python3 -m py_compile packages/compiler/knowl_compile.py
```

Results:

- 8 knowls compiled
- validation report was empty
- SQLite artifact contained 8 knowls and 7 relations
- local HTTP smoke test returned 200 for `/`
- local HTTP smoke test successfully fetched
  `/fragments/algebra-groups/group/core.html`

The `sqlite3` shell was not installed in this environment, so the SQLite artifact
was checked through Python's standard `sqlite3` module.

## Important Prototype Limits

- Markdown rendering is intentionally minimal.
- Math is loaded through MathJax from a CDN in the generated HTML. A mature static
  target should support local/build-time math rendering.
- TOML is used because it is available in the Python standard library. The
  architecture does not depend on TOML specifically.
- The static runtime is small and does not yet implement prefetching, service
  workers, keyboard traversal inside proofs, or advanced mobile history behavior.
- The compiler validates links, anchors, relations, TFAE references, and proof
  step references, but the schema is still early.

## Next Good Step

Add a second proof with an actual nested subproof, then update the proof renderer
so subproofs fold and unfold recursively.

