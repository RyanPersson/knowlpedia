# Current Handoff

Date: 2026-07-02

This is the live operational handoff for the Mac checkout at:

```text
/Users/ryanpersson/anki/code/knowlpedia-root/knowl-system-refactor
```

Older narrative handoffs are archived under `docs/archive/`.

## Current State

- The refactor is a static-first compiler/runtime prototype.
- Source files are canonical; generated HTML, JSON, SQLite, and preview output
  are build artifacts.
- Normal full-corpus builds compile directly from the sibling source repo:

  ```text
  ../knowlpedia-content
  ```

- `imports/` is ignored scratch space for the legacy importer, not the current
  source of truth.
- The repo branch is `main`.
- The local preview manager is active and serves `public-imported/` at:

  ```text
  http://127.0.0.1:8012/
  ```

## Commands

Install dependencies:

```bash
make deps
```

Build the sibling content package:

```bash
make build
```

The explicit full-content target is equivalent:

```bash
make build-content
```

Build one page during iteration:

```bash
make build-page PAGE=algebra-category-theory/tikz-lab-whiskering-coherence
```

Preview one TikZ-like diagram:

```bash
make preview-diagram \
  DIAGRAM_SOURCE=../knowlpedia-content/content/algebra-category-theory/tikz-lab-whiskering-coherence.knowl.md \
  DIAGRAM_INDEX=1
```

Check the local preview before starting or changing servers:

```bash
make preview-status
```

Scan generated HTML for visible rendering errors:

```bash
make check-rendering
```

Rebuild the full content package and then scan generated HTML:

```bash
make check-rendering-content
```

Use the preview manager instead of raw `python3 -m http.server`:

```bash
make preview-start
make preview-stop
make preview-adopt
make preview-restart
make preview-scan
```

## Known Build Status

`make build-content` is expected to complete while reporting known imported
corpus validation issues. The last recorded status was:

- 2,089 knowls in `registry.json`
- 13,815 unique semantic links in `links.json`
- 31 validation errors
- 27 validation warnings

The validation report is emitted at:

```text
public-imported/reports/validation.json
```

`make check-rendering` scans generated HTML for visible rendering leaks. It
intentionally skips the generated `posts/semigroup-quasigroup-structure` page
and fragment because they contain the legacy interactive `{{< euler-diagram >}}`
shortcode. Keep that source content intact until the shortcode is deliberately
migrated.

## Recent Fixes To Preserve

- Light-mode knowl panels alternate `white -> gray -> white -> gray`.
- Dark-mode knowl panels alternate `#1d1e20 -> #2e2e33 -> #1d1e20`.
- Light-mode ordinary links use standard blue `#0645ad`.
- Knowl fragments render top-right and bottom-right close buttons.
- Nested knowl panels open at the clicked local phrase/context.
- Wikilink labels may contain `]`; the closing delimiter is `]]`.
- Build-time KaTeX is the preferred math renderer when local Node dependencies
  are installed.
- Diagram rendering uses the persistent cache at `.knowl-cache/diagrams`.
- The legacy `{{< euler-diagram >}}` shortcode is an explicit checker exception
  for now; do not remove it from content just to satisfy generated-output
  checks.

## Remaining Steps

### Immediate

- Add a second proof with a real nested subproof.
- Update proof rendering so subproofs fold and unfold recursively.
- Add regression tests for wikilink labels containing `]`.
- Triage the 31 validation errors and 27 warnings in the full corpus.

### Corpus

- Add semantic enrichment for examples, theorem statements, proof blocks, TFAE
  lists, category-theoretic sections, subset/superset relations, and
  prerequisites.
- Decide which enrichment should be automated and which should require manual
  review.

### Runtime And UI

- Add a production index/search strategy.
- Improve mobile behavior for deeply nested panels, long proof steps, and long
  display equations.
- Add keyboard traversal and focus management.
- Add better browser history behavior for opened panels.
- Add a repeatable browser performance harness for first-click and warmed-click
  latency.

### Schema And Artifacts

- Stabilize the schema for definitions, axioms, examples, TFAE entries,
  relationships, proof steps, and verification metadata.
- Decide whether single-file imported knowls are a compatibility format or only
  an import intermediate.
- Decide which generated database/search formats are official artifacts:
  SQLite, JSON, NDJSON, search index, or several targets.

### Math And Diagrams

- Compare KaTeX, `latex2mathml`, and MathJax-as-build-step on harder corpus
  examples.
- Evaluate output size, mobile overflow, accessibility, copy/paste behavior,
  and fidelity.
- Keep visual QA as part of TikZ/category-theory diagram work; compile success
  alone is not enough.

### Tests

- Add compiler tests for link conversion, math protection, validation, fragment
  generation, and SQLite emission.
- Add runtime tests for panel insertion, cache/preload behavior, modified-click
  navigation, and theme toggling.
- Add screenshot regression tests for tricky pages such as group, binary
  operation, abelian category, and algebra-commutative corollaries.

## Archived Handoffs

- `docs/archive/2026-07-01-refactor-handoff.md`
- `docs/archive/2026-07-02-ui-preview-handoff.md`
