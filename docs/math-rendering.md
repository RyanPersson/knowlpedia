# Math Rendering Direction

Date: 2026-07-01

## Current Prototype State

The prototype now renders math during compilation with the repo-local npm KaTeX
module when available. The generated pages and knowl fragments contain static
KaTeX HTML plus MathML accessibility markup, and do not load MathJax in that
mode.

This matters for the imported corpus because TeX must be protected before
Markdown inline formatting runs. For example, `$*:S\times S\to S$` contains a
literal `*`; without math protection, a Markdown emphasis pass can corrupt the
formula before any renderer sees it.

If KaTeX is unavailable, the compiler falls back to `latex2mathml`. If both
build-time renderers are unavailable, the compiler leaves escaped TeX in the
HTML and the page shell loads MathJax as a compatibility fallback.

The imported corpus uses both:

- `$...$` inline math
- `\(...\)` inline math
- `$$...$$` display math
- `\[...\]` display math

The compiler recognizes all four forms before Markdown inline parsing.
Display forms are emitted as block-level HTML. If `\[...\]` or `$$...$$` appears
inside prose, the renderer splits the paragraph before and after the equation so
the output does not contain invalid `<p><div class="math-display">...` markup.

## TikZ And Diagram Rendering

The compiler now recognizes diagram source before ordinary Markdown code-fence
rendering. Supported source forms are:

- fenced `tikz` or `tikzpicture` blocks
- fenced `tikz-cd` or `tikzcd` blocks
- fenced `cd` or `amscd` blocks
- raw display math containing `\begin{tikzpicture}`, `\begin{tikzcd}`, or
  `\begin{CD}`
- raw `\begin{tikzpicture}` and `\begin{tikzcd}` block environments

When a local TeX engine and SVG converter are available, diagrams render during
compilation to inline SVG. The compiler currently looks for `tectonic` or
`pdflatex`, plus `pdftocairo` or `dvisvgm`.

When that toolchain is not available, diagrams degrade to a static source panel
instead of broken KaTeX/MathJax output. Failed compiles render the source plus a
truncated render log so an agent can repair the diagram.

## Recommended Production Direction

Prefer build-time math rendering for the production static runtime.

Reasons:

- faster page interaction on mobile
- less client JavaScript
- no CDN dependency
- better cache behavior
- consistent rendering for inline knowl fragments
- easier print/export behavior

The compiler now has the first version of this stage:

```text
source markdown with TeX
  -> protected math tokens
  -> Markdown/link rendering
  -> build-time KaTeX rendering
  -> static pages and fragments
```

The old Hugo site also used KaTeX at build time, so this path is the closest
match for old knowlpedia visual parity.

## Mobile Handling

Pre-rendered math can be mobile-friendly if display equations are contained.

Rules:

- Inline math should remain inline where possible.
- Display math should render in a block with `max-width: 100%`.
- Long display equations should scroll horizontally inside the equation block,
  not force the whole page to overflow.
- Knowl panels and proof panels should inherit the same math overflow behavior.
- Long equations should not be scaled with viewport width; scaling hurts
  readability and tap targets.

The current prototype CSS applies this to generated KaTeX, generated MathML, and
the MathJax fallback:

```css
.math-display,
mjx-container[display="true"] {
  display: block;
  max-width: 100%;
  overflow-x: auto;
}
```

## Open Implementation Choice

Candidate build-time renderers:

- current prototype primary path: Node KaTeX library as a compiler stage
- current prototype fallback: Python `latex2mathml`
- Hugo/KaTeX, similar to the existing static site path
- MathJax in Node as a compiler stage
- Python markdown extension plus a math renderer wrapper

The right final choice should be made after testing:

- full corpus build time
- output size
- mobile overflow behavior
- copy/paste TeX behavior
- inline fragment performance
- accessibility/MathML output

## Local Browser Validation

Ubuntu desktop on the Optiplex has Firefox available. The repo includes a
headless screenshot target:

```bash
make screenshot-imported PREVIEW_URL=http://127.0.0.1:8002
```

The screenshot is written to `tmp/screenshots/imported-group.png` by default.
Use `PREVIEW_PATH=/some/page/` and `SCREENSHOT=tmp/screenshots/name.png` to
capture another generated page.

The Makefile default still points at the older ad hoc `8001` preview. The
always-on systemd preview is on `8002`, so pass
`PREVIEW_URL=http://127.0.0.1:8002` when checking the current service.

Node Playwright is tracked in `package.json` and is the preferred way to check
interactive rendering and panel-opening behavior. The OptiPlex also has a
global install:

```text
node v22.22.1
npm 9.2.0
playwright 1.61.1
@playwright/test 1.61.1
```

For repo-local scripts after `make deps`, use `require("playwright")`. Because
Playwright is also installed globally on the OptiPlex, one-off direct Node
scripts can import it with the absolute module path:

```js
const { chromium } = require("/usr/local/lib/node_modules/playwright");
```

Recent Playwright checks confirmed:

- KaTeX-rendered pages load from the Tailscale preview
- display equations are centered block math
- a wikilink label containing `]` no longer renders as raw `[[...]]`
- clicking the fixed Hilbert basis corollary link opens its knowl panel
