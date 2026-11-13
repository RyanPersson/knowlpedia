# Illuminated editions

Three working manuscript-inspired treatments for Knowlpedia, built on
`feat/illuminated-manuscript-themes` from `main` at
`46b29f27126d5c228424ff9a334fbcd9cc63648b`.

## Try them locally

In the application checkout, with `knowlpedia-content` in its usual sibling
directory:

```sh
git fetch origin
git switch --track origin/feat/illuminated-manuscript-themes
make build EXTRA_CONTENT_SOURCES=
make preview-status
```

Reuse the preview serving this checkout. If it is not running, start it with:

```sh
.venv/bin/python scripts/preview_server.py start --host 127.0.0.1 --port 8001 --directory public-imported
```

The build command uses the public content repository without requiring the
optional `conjectures-catalog` sibling. To include your usual local sources,
run your normal development build instead.

Open one of these addresses (adjust the port if your preview uses another):

- [Vellum](http://127.0.0.1:8001/illuminated/?palette=vellum&theme=light)
- [Lapis](http://127.0.0.1:8001/illuminated/?palette=lapis&theme=dark)
- [Black Hours](http://127.0.0.1:8001/illuminated/?palette=black-hours&theme=dark)

The comparison page contains the real **Group**, **Projective modules are direct
summands of free modules**, and **Inner product space** entries. Expand an underlined concept,
then expand another within it. Use “Read full entry” to see the style on a
normal page. The selected edition persists across navigation and reloads.

Every development page also exposes the three editions under **Testing →
Color palette**. Select **Current** there to return to the existing design.
The light/dark button works with every edition. Arrow keys move between the
edition cards; Escape closes expanded knowls.

## Design directions

| Edition | Visual language | Best use |
| --- | --- | --- |
| **Vellum** | Warm parchment, dark ink, red rubric initials, blue links, thin gold rules | The strongest starting point for everyday reading and long proofs |
| **Lapis** | Deep indigo, ivory lettering, geometric ornament, double gold borders | The most distinctive identity; especially suited to a rich dark mode |
| **Black Hours** | Charcoal, silver text, burnished gold, restrained borders | A quieter night-reading alternative |

All three have complete light and dark palettes. Selecting a card starts with
its signature mode: light for Vellum, dark for Lapis and Black Hours. Changing
the mode on the comparison page updates its URL, so reloading preserves that
choice.

The manuscript vocabulary is concentrated in initials, headings, rules,
corners, and margins. The body uses a readable system serif stack; navigation
and controls remain sans serif. KaTeX and MathJax retain their own fonts.
Expanded knowls keep alternating backgrounds to make recursive reading clear.
The homepage retains its compact layout.

There are no image textures, font downloads, or new runtime dependencies. The
corner ornament is a small original SVG, colored by CSS; the compass ornament
on the comparison page is inline SVG. Decorative shapes are hidden from
assistive technology. Mobile rules stack the edition choices and move the
margin notes below the text. Print rules remove the controls and return to
white paper.

## Where the changes live

- `packages/static-runtime/illuminated.css`: palettes, reading styles, specimen
  layout, mobile and print rules. Reader changes are guarded by
  `data-manuscript`.
- `packages/static-runtime/illumination.svg`: corner ornament.
- `packages/static-runtime/knowl-testing.js`: edition selection, persistence,
  keyboard controls, and comparison-page URLs.
- `packages/compiler/knowl_compile.py`: development-only asset inclusion and
  `/illuminated/`, reusing the existing content renderer.

The experiment follows the existing visual-lab boundary: it is available in
**development builds**. Production builds omit the comparison page, edition
controls, and illuminated assets. This makes the branch suitable for a local
design review; choosing a production default is a subsequent product decision.

## Checks

```sh
make test
make check-rendering
make build-production OUTPUT_DIR=tmp/production-check
npm run test:ui
npm run test:home-ui
npm run test:illuminated-ui
```

The UI tests expect a running development preview at `http://127.0.0.1:8001`.
Set `PREVIEW_URL` to use another address. Install Playwright Chromium with
`npm run playwright:install` if needed, or set `PLAYWRIGHT_CHROME_PATH` to an
installed Chrome/Chromium binary.

The illuminated smoke test covers all three editions in both modes, primary
text-token contrast of at least 4.5:1, recursive knowls, mobile overflow,
navigation and reload persistence, keyboard selection, print styling, and
blocked browser storage. To also save desktop previews:

```sh
SCREENSHOT_DIR=tmp/illuminated-previews npm run test:illuminated-ui
```

During implementation, all 293 Python tests passed and all six palette/mode
combinations passed direct text and nested-background contrast calculations.
Browser smoke tests could not launch in the implementation environment because
Chromium's required socket was denied. The connected browser was unavailable
and the remote browser could not access the local preview, so browser rendering
and interaction checks remain to be run in a local browser.
