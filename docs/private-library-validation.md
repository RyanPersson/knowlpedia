# Docs and private library validation

Validated on 12 September 2026 in the main sibling checkouts under
`knowlpedia-root`, with the application and public content on `bianchi`.

The development header now links to five codebase documentation pages and a
private reading library. Prepared documents come from the separate
`knowlification-cache` package and open public knowls recursively. The cache
uses only its local bare Git remote; original inputs in `docs/` are ignored.
PDF extraction and automatic linking are future work.

## Passing checks

- Source inventory: all 3,641 main content entries and 10 testing entries parse
  with the current compiler. The main count includes 62 redirects.
- `make test`: 177 Python tests pass, including nine private-library cases.
- Development build: 4,766 entries, including the original private reading demo.
- Production build: 3,579 entries; strict rendered-HTML and diagram checks pass.
- Production exclusion checks pass for private pages, fragments, JSON indexes,
  metadata and development navigation. Tests also verify that a production
  rebuild removes private artifacts left by a development build.
- All eight new generated documentation/library/document HTML files and private
  fragments pass the rendering checker.
- Browser checks pass: `test:private-library`, `test:home-ui`, and `test:ui`.
  These cover navigation, nested expansion, Escape, search, five palettes,
  mobile layout and Testing-panel placement. The private-library check includes
  320px, 390px and 720px viewport widths.
- External-link source audit passes. Public mathematical source files are
  unchanged.

The existing runtime test now opens the Real numbers page's Remarks section
before clicking the rational-numbers link inside it. Its assertions are intact.

## Remaining audit findings

`make audit-sections` reports one content-order mismatch in unchanged source:
`content/fiber-bundles/construction-splitting-of-atiyah-sequence-from-a-principal-connection.knowl.md`.

The full development rendering audit reports 726 issues: 56 KaTeX errors,
558 raw-backslash findings, 46 raw display-math delimiters and 66 raw LaTeX
commands. The displayed failures concern imported conjecture content, including
source bibliography syntax and equations. The production artifact and new
reading/docs pages pass their rendering checks. No corpus-wide delimiter or
content rewrite was performed as part of this feature.

The scope audit reports 168 findings for later mathematical review. No audit
gate was disabled or weakened.

## Local review

The existing `knowlpedia-astra-benchmark` devserver serves `public-imported/` on
port 8015. Review `/docs/`, `/library/`, and `/documents/reading-demo/` there.
Separate validation outputs were built under `tmp/docs-library-development`
and `tmp/docs-library-production`. The development artifact was copied into
the existing served directory while preserving its prior comparison pages.
The public site was not deployed.
