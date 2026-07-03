# Current Refactor Handoff

Date: 2026-07-01

Repo:

```text
/home/codex/code/knowlpedia-root/knowl-system-refactor
```

This document summarizes the current state of the knowl-system refactor so a new
session can continue without reconstructing the work from chat history.

## Architecture Direction

The refactor is currently a static-first compiler/runtime system.

The recommended direction is:

1. Keep authoring and agent edits in portable source files.
2. Compile those files into a validated semantic graph.
3. Emit fast static artifacts for GitHub Pages, university pages, and local
   previews.
4. Also emit database-like artifacts, currently SQLite and JSON, for local
   querying, validation, search, and automation.

The important decision is that a database is useful as a generated artifact, but
it should not be mandatory for ordinary public hosting. That keeps the format
friendly to professors, students, GitHub Pages, and simple static school sites.

## What Was Added

### Compiler

Main file:

```text
packages/compiler/knowl_compile.py
```

The compiler now:

- reads semantic knowl source packages
- supports both bundled knowls with `knowl.toml` and imported
  single-file `*.knowl.md` knowls
- validates knowl links, anchors, relations, proof references, and TFAE
  references
- emits full HTML pages
- emits inline knowl fragments
- emits an old Hugo-style `/topics/` comparison page with the former hardcoded
  topic list
- emits `registry.json`, `links.json`, `relations.json`, `proofs.json`, and
  `knowls.sqlite`
- supports `--allow-validation-errors` for legacy corpus comparison builds
- builds full pages with one-click-deep knowl fragments embedded as hidden
  templates
- caches rendered fragments during compilation so the full imported build stays
  reasonably fast
- protects TeX spans before Markdown inline formatting
- parses semantic wikilink labels until the closing `]]`, so labels may contain
  literal `]` characters such as `k[x_1,...,x_n]`
- renders math at build time with KaTeX when the local KaTeX module is
  available, producing static KaTeX HTML plus MathML accessibility markup
- falls back to `latex2mathml`, then MathJax, when KaTeX is unavailable
- emits display math as real block HTML, including when `\[...\]` or `$$...$$`
  appears inside prose
- strips imported Codex/browser status footer lines such as
  `14m45s ... gpt-...` during rendering

The visible generated `Core` heading was removed. The internal `section.core`
anchor remains available for validation and linking.

### Static Runtime

Main files:

```text
packages/static-runtime/knowl.js
packages/static-runtime/knowl.css
```

The runtime now:

- opens knowls instantly when their fragment is already embedded or cached
- has no intentional opening animation or delay
- preserves normal browser behavior for modified clicks, context menus, and
  opening full pages in new tabs
- loads hidden template fragments into an in-memory cache on page initialization
- eagerly preloads one-click knowls on normal full pages
- uses visible/nearby preloading for the large imported index
- preloads on hover, focus, and touch start
- preloads nested knowls after a panel opens
- limits concurrent preload requests
- renders the generated index as unfoldable knowl triggers instead of plain
  links
- includes a manual light/dark theme toggle backed by `localStorage`
- fixes nested insertion so a knowl opened from inside an expanded panel inserts
  at the clicked phrase instead of escaping below the parent panel
- appends index-opened panels inside their owning topic list item
- uses old-Hugo-style alternating nested panel backgrounds and thinner knowl
  headers

The nested-panel bug was caused by insertion logic using too broad an ancestor
as the insertion point. The runtime now respects the nearest `.knowl-panel`
boundary and chooses the local phrase/list/block context.

### Importer

Main files:

```text
packages/importers/import_knowlpedia_content.py
packages/importers/README.md
```

The importer converts the legacy corpus from:

```text
../knowlpedia-content/
```

into:

```text
imports/knowlpedia-content/
```

It is intentionally conservative. It preserves the old prose and converts Hugo
knowl shortcodes into the new semantic wikilink syntax, but it does not infer
proof structure, examples, axioms, TFAE sections, or relationship metadata from
the prose.

### Math Rendering

Dependency:

```text
requirements.txt
package.json
package-lock.json
```

The prototype uses the repo-local npm KaTeX install as the preferred build-time renderer
through:

```text
packages/compiler/katex_worker.cjs
```

Run `make deps` after cloning to create `.venv/` and install `node_modules/`.
The compiler now checks `node_modules/katex/dist/katex.js` first, then falls
back to older machine-local discovery paths, and copies KaTeX CSS/fonts into
`public*/assets/`. If KaTeX is not available, it falls back to
`latex2mathml==3.81.0`, then to escaped TeX plus client-side MathJax.

This fixed the observed rendering failures where Markdown emphasis touched TeX
characters before math rendering, such as formulas containing `*`.

The latest visual parity pass also fixed:

- clipped-looking inline math by using KaTeX fonts/CSS instead of raw MathML
- left-aligned single-line display equations by emitting display math as block
  KaTeX
- invalid paragraph/display equation nesting
- the stray imported agent status line in Uniform Continuity
- a raw wikilink rendering bug when the display label contained a closing
  bracket, e.g. `Hilbert basis theorem corollary (k[x_1,...,x_n] Noetherian)`

Details are in:

```text
docs/math-rendering.md
```

### Browser Validation

The Optiplex can validate generated pages with headless Firefox. The Makefile
target is still available:

```bash
make screenshot-imported PREVIEW_URL=http://127.0.0.1:8002
```

Useful options:

```bash
make screenshot-imported \
  PREVIEW_URL=http://127.0.0.1:8002 \
  PREVIEW_PATH=/algebra-category-theory/abelian-category/ \
  SCREENSHOT=tmp/screenshots/abelian-category.png
```

Firefox is installed as a snap, so screenshot commands may need unsandboxed
execution from Codex.

The Makefile default `PREVIEW_URL` still points at the old ad hoc `8001`
workflow, so pass `PREVIEW_URL=http://127.0.0.1:8002` when validating the
always-on service.

Node, npm, and Playwright are also installed on the Optiplex:

```text
node v22.22.1
npm 9.2.0
global playwright 1.61.1
global @playwright/test 1.61.1
```

The global Playwright module lives under:

```text
/usr/local/lib/node_modules
```

A known-good smoke-test shape is:

```bash
node -e "const { chromium } = require('/usr/local/lib/node_modules/playwright'); /* ... */"
```

Latest Playwright checks:

- `/topics/` loaded with title `Topics - Imported Knowlpedia Content`
- `/algebra-commutative/` no longer contains the raw
  `[[algebra-commutative/hilbert-basis-corollary|...]]` text
- clicking the Hilbert basis corollary link opened a `HILBERT BASIS COROLLARY`
  knowl panel

## Current Commands

Install dependencies:

```bash
make deps
```

Build the small semantic example package:

```bash
make build
```

Serve the small package:

```bash
make serve
```

Import and build the full legacy corpus:

```bash
make build-imported
```

Serve the imported corpus:

```bash
make serve-imported
```

## TikZ Diagram Lab And Fast Iteration Handoff

Date: 2026-07-02

Local repos in the desktop environment:

```text
/Users/ryanpersson/anki/code/knowlpedia-root/knowl-system-refactor
/Users/ryanpersson/anki/code/knowlpedia-root/knowlpedia-content
```

Current content branch:

```text
knowlpedia-content: tikz-diagram-lab
```

The refactor repo is on `main`. Before the source migration, the generated
imported corpus under `imports/knowlpedia-content/` was tracked and became dirty
after running imports from the content branch. The migration commit untracks and
ignores `imports/` so it is scratch space rather than source.

### Current TikZ Work

New TikZ-heavy test content was added in `knowlpedia-content`:

```text
algebra-category-theory/tikz-diagram-lab.md
algebra-category-theory/tikz-lab-pullback-pasting.md
algebra-category-theory/tikz-lab-adjunction-naturality.md
algebra-category-theory/tikz-lab-whiskering-coherence.md
```

The whiskering diagram in `tikz-lab-whiskering-coherence.md` was corrected after
visual QA. The key fix was to stop placing `F`, `G`, and `\eta` with separate
`node[pos=...]` labels on the curved paths. Instead, the diagram defines the
midpoint axis explicitly:

```tex
\coordinate (CDmid) at ($(C)!0.5!(D)$);
```

Then `F`, `G`, and the 2-cell arrow are placed from offsets on that same axis.
This aligns the natural transformation with the upper curve hump and lower curve
trough, which was the intended visual semantics.

The custom Codex skill was updated:

```text
/Users/ryanpersson/.codex/skills/knowlpedia-tikz/SKILL.md
/Users/ryanpersson/.codex/skills/knowlpedia-tikz/references/tikz-official-docs.md
```

Important skill lessons:

- Do not declare a TikZ diagram done from compile success alone.
- Visually inspect each diagram against the intended mathematical picture.
- For symmetric curved functor arrows, use explicit midpoint coordinates from
  the TikZ `calc` library instead of tuning separate `pos` labels.
- On this macOS path, `pdflatex` plus Ghostscript PNG output has been the most
  reliable browser-facing TikZ rendering mode.

### Current Build Loop

Normal refactor builds now compile directly from the sibling Knowlpack-format
content repo:

```bash
make build-content
```

That target runs the compiler against:

```text
../knowlpedia-content -> public-imported
```

The legacy importer remains available as an explicit one-off migration tool:

```bash
make import-legacy-content
```

Do not run the importer as part of ordinary editing. `imports/` is ignored and is
scratch space.

### Fast Iteration Commands

1. Diagram-only preview.

   ```bash
   make preview-diagram \
     DIAGRAM_SOURCE=../knowlpedia-content/content/algebra-category-theory/tikz-lab-whiskering-coherence.knowl.md \
     DIAGRAM_INDEX=2
   ```

   This extracts one TikZ-like block from a source file and renders a tiny HTML
   preview using the same `DiagramRenderer` as the compiler. It validates the
   diagram render, not full page layout, knowl links, or page integration.

2. Single-page compile.

   ```bash
   make build-page PAGE=algebra-category-theory/tikz-lab-whiskering-coherence
   ```

   The compiler still loads the full registry for link resolution and
   validation, but it only rewrites the selected page, its core fragment, its
   section fragments, and immediate preload fragments. Indexes and unrelated
   preloaded fragments can be stale until a full build, so use this for local
   iteration, not final verification.

3. Persistent rendered-diagram cache.

   `DiagramRenderer` caches rendered diagram HTML by a hash of the source, kind,
   renderer backend, TeX wrapper, and toolchain paths. The default cache path is:

   ```text
   .knowl-cache/diagrams
   ```

   Override it with `DIAGRAM_CACHE_DIR=...` or compiler
   `--diagram-cache-dir ...`. Use `--no-diagram-cache` to disable it for timing
   or debugging.

Measured locally on 2026-07-02:

```text
baseline full build before these changes:                 15.34s
diagram-only preview, no persistent cache:                 0.61s
single-page compile, no persistent cache:                  1.84s
full build, cold persistent diagram cache:                14.08s
full build, warm persistent diagram cache:                 3.17s
single-page compile + warm persistent diagram cache:       0.27s
diagram-only preview + warm persistent diagram cache:      0.10s
make build-content, warm cache and dependency stamp:       3.11s
make build-page, warm cache and dependency stamp:          0.24s
make preview-diagram, warm cache and dependency stamp:     0.10s
```

Run full `make build-content` before commits or deployment checks. Use
`make preview-diagram` and `make build-page` during diagram/page iteration.
Do not run full and single-page builds concurrently into the same output
directory; both write `public-imported`.

### Import Folder Source-Of-Truth Question

`imports/knowlpedia-content` is generated by
`packages/importers/import_knowlpedia_content.py`, but it is no longer tracked in
the refactor repo. The sibling `knowlpedia-content` repo is the normal source of
truth for refactor content on the `tikz-diagram-lab` branch.

Current import transformation:

- Hugo YAML front matter becomes Knowlpack TOML front matter.
- Each file gets `id`, `title`, `kind`, `summary`, `aliases`, `domains`, and
  `legacy_source_path`.
- Hugo knowl shortcodes such as
  `{{< knowl id="natural-transformation" text="natural transformation" >}}`
  become semantic wikilinks such as
  `[[algebra-category-theory/natural-transformation|natural transformation]]`.
- `_index.md` files become section knowls.
- Root-level pages and some special paths become page knowls.
- Ordinary domain files become `kind = "knowl"`.
- Markdown bodies are otherwise preserved conservatively.
- The importer does not infer structured axioms, examples, proofs, TFAE data, or
  relation metadata from prose.

Migration decision on 2026-07-02:

The `tikz-diagram-lab` branch of the sibling `knowlpedia-content` repo was
migrated to the generated Knowlpack format and is treated as the canonical local
source for refactor work. Normal refactor builds compile directly from
`../knowlpedia-content` into `public-imported`, without regenerating
`imports/knowlpedia-content`.

The legacy importer remains useful as a one-off migration tool, but it should no
longer run as part of the normal edit/build loop. Generated import output under
`imports/` is ignored by the refactor repo so it can be used as scratch space
without producing tracked churn.

For any new long-running dev server on this Optiplex, first check whether an
existing persistent service already serves the changed artifact. For
Knowlpedia imported/static preview changes, reuse the existing `8002` service
instead of starting a second server. For unrelated new previews, prefer the host
helper:

```bash
devserver start <name> -- <command...>
devserver status <name>
devserver logs -f <name>
devserver stop <name>
```

Global guidance for this is in:

```text
/home/codex/.codex/AGENTS.md
```

On the Mac desktop repo, use the project-local preview manager instead of
starting raw `python3 -m http.server` processes:

```bash
make preview-status
make preview-start
make preview-stop
make preview-adopt
make preview-restart
make preview-scan
```

The manager records the tracked local preview under `.preview-server/`, serves
`public-imported/` on `http://127.0.0.1:8012/` by default, and refuses to start a
second tracked preview if the tracked server or port is already active. Use
`make preview-adopt` to track an already-running listener on the default port.
Use `make preview-scan` before creating any ad hoc local server; it lists Python
TCP listeners so stale servers from earlier Codex threads are visible.

The latest preview server was exposed on the Tailscale network at:

```text
http://100.69.17.72:8002/
```

That link is now backed by a user systemd service rather than an ad hoc Codex
shell process. See:

```text
docs/preview-server-service.md
```

When a future agent changes rendered pages or examples, its final Codex chat
response should include a direct URL to the page that demonstrates the change,
preferably the Tailscale URL when the user may open it from another machine. For
changes visible in `public-imported/`, use the existing
`http://100.69.17.72:8002/` preview rather than creating a new server.

## Current Full-Corpus Status

Latest import:

- 2,089 markdown files imported
- 32 section `_index.md` files imported as `kind = "section"`
- 3 root markdown pages imported as `kind = "page"`
- 14,251 Hugo knowl shortcodes converted
- 0 malformed knowl shortcodes
- 1 unsupported non-knowl shortcode left visible: `euler-diagram`

Latest imported build:

- 2,089 knowls in `registry.json`
- 13,815 unique semantic links in `links.json`
- 2,089 knowls in `knowls.sqlite`
- 13,815 links in `knowls.sqlite`
- 4,187 generated files in `public-imported/`

Validation currently reports:

- 31 errors
- 27 warnings

Those are in:

```text
public-imported/reports/validation.json
```

They are mostly legacy dangling links, missing targets, or duplicate aliases.
The imported build intentionally uses `--allow-validation-errors` so comparison
artifacts are still produced.

More details:

```text
docs/imported-content-status.md
```

## Recent Fixes To Preserve

- Server persistence: the preview is a user systemd service,
  `knowlpedia-refactor-preview.service`, with user lingering enabled. Do not
  replace it with a foreground shell server.
- Math rendering: server-side KaTeX is active and KaTeX fonts/CSS are copied to
  generated assets. This is the current visual match to old knowlpedia.
- Display math: `\[...\]` and `$$...$$` are emitted as block-level HTML, even
  when they appear inside prose.
- Nested panels: knowls clicked inside expanded knowls should open at the local
  clicked phrase/context, not below the whole parent panel.
- Wikilinks: labels can include `]`; the closing delimiter is `]]`.

## Current Performance State

Recovered from the old pre-refactor runtime:

```text
../knowlpedia/static/js/knowls.js
```

The old runtime used in-memory fragment caching, hover preload,
`IntersectionObserver` preload, and nested preload after opening a panel. The
new runtime uses the same basic strategy plus embedded one-click-deep templates
on full knowl pages.

One local measurement run:

```text
current group page, localhost: 0.000653s, 28,168 bytes
current index, localhost: 0.001057s, 740,590 bytes
current binary-operation fragment, localhost: 0.000635s, 3,821 bytes
live knowlpedia.com group page: 0.324015s, 39,259 bytes
live knowlpedia.com binary-operation page: 0.152686s, 28,886 bytes
live knowlpedia.com root: 0.147141s, 16,669 bytes
```

These are useful for payload and serving-shape comparisons. They are not a
substitute for real phone-over-Tailscale latency testing.

More details:

```text
docs/performance-notes.md
```

## Generated And Untracked Files

Ignored generated output:

```text
public/
public-imported/
imports/
.knowl-cache/
.venv/
tmp/
```

`imports/` is generated scratch space for the legacy importer. The canonical
refactor-format corpus for current work is the sibling `../knowlpedia-content`
repo, not anything under `imports/`.

The diagram cache under `.knowl-cache/` is intentionally local. It is keyed by
diagram source, kind, TeX wrapper, renderer backend, and local toolchain paths,
so it should not be committed.

## Work Remaining

### Architecture And Schema

- Decide the long-term canonical source format.
- Stabilize the schema for definitions, axioms, examples, TFAE entries,
  relationships, proof steps, and verification metadata.
- Decide whether single-file imported knowls stay as a compatibility format or
  become only an import intermediate.
- Decide which generated database formats should be official artifacts:
  SQLite, JSON, NDJSON, search index, or all of them.

### Corpus Import

- Triage the 31 validation errors and 27 warnings in the imported corpus.
- Add importer support for the unsupported `euler-diagram` shortcode.
- Add semantic enrichment passes for examples, theorem statements, proof blocks,
  TFAE lists, category-theoretic sections, subset/superset relations, and
  prerequisites.
- Decide how much of that enrichment should be automated versus manually
  reviewed.

### Runtime And UI

- Add a production index strategy: grouped index pages, search, pagination, or a
  compact browser-side search index.
- Add mobile polish for deeply nested panels, long proof steps, and long
  display equations.
- Add keyboard traversal and focus management for accessibility.
- Add better browser history behavior for opened panels.
- Add a service worker or cache manifest if the static reader should feel
  offline-fast.
- Add a repeatable browser performance harness for first-click and warmed-click
  latency.

### Math Rendering

- Compare `latex2mathml`, KaTeX, and MathJax-as-build-step on the full corpus.
- Evaluate output size, mobile overflow, accessibility, copy/paste behavior, and
  fidelity on harder TeX examples.
- Decide whether KaTeX HTML+MathML is the production default and whether MathML
  alone remains only a compatibility target.

### Proofs And Lecture Notes

- Implement recursively foldable proof/subproof rendering.
- Make each proof step addressable and able to unfold axioms, lemmas, previous
  steps, and hidden subproofs.
- Add a structured proof authoring format inspired by Lamport-style hierarchical
  proofs.
- Add lecture-note pages that can mix prose, diagrams, proof blocks, and knowl
  panels.

### TFAE And Alternate Definitions

- Add a standard optional TFAE section.
- Add a compact definition switcher for equivalent definitions when appropriate.
- Track hypotheses on equivalent characterizations so finite-only or
  context-specific equivalences do not look unconditional.

### Local AI Workbench

The live conversation/workbench idea belongs in the separate repo:

```text
/home/codex/code/knowlpedia-root/knowl-live-workbench
```

That project is still mostly design notes. It should eventually support:

- live markdown/knowl rendering from files written by agents
- programmatic interlinking to the knowl graph
- TikZ diagram compilation and preview
- access from Mac and phone over Tailscale

### Tests

- Add compiler unit tests for link conversion, math protection, validation,
  fragment generation, and SQLite emission.
- Add a regression test for wikilink labels containing `]`, such as
  `[[target/path|label with k[x]]]`.
- Add runtime tests for panel insertion, cache/preload behavior, modified-click
  navigation, and theme toggling.
- Add screenshot regression tests for known tricky pages such as group, binary
  operation, abelian category, and algebra-commutative corollaries.
