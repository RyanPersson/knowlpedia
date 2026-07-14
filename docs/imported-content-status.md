# Imported Knowlpedia Content Status

Date: 2026-07-01

## Import Location

Original source:

```text
../knowlpedia-content/
```

Refactored semantic source:

```text
imports/knowlpedia-content/
```

Generated static comparison build:

```text
public-imported/
```

## Commands

Run the full import and build:

```bash
make build-imported
```

Serve the imported build:

```bash
make serve-imported
```

## Import Results

Latest import:

- 2,089 markdown files imported
- 32 section `_index.md` files imported as `kind = "section"`
- 3 root markdown pages imported as `kind = "page"`
- 14,251 Hugo knowl shortcodes converted to semantic wikilinks
- 0 malformed knowl shortcodes
- 1 unsupported non-knowl shortcode left visible: `euler-diagram`

Latest build:

- 2,089 knowls in `registry.json`
- 13,815 unique semantic links in `links.json`
- 2,089 knowls in `knowls.sqlite`
- 13,815 links in `knowls.sqlite`
- 4,187 generated files in `public-imported/`

## Comparison Examples

Old source:

```text
../knowlpedia-content/algebra-groups/group.md
```

Refactored source:

```text
imports/knowlpedia-content/content/algebra-groups/group.knowl.md
```

Generated page:

```text
public-imported/algebra-groups/group/index.html
```

Generated inline fragment:

```text
public-imported/fragments/algebra-groups/group/core.html
```

Old Hugo-style topics comparison page:

```text
public-imported/topics/index.html
```

This page mimics the old `../knowlpedia/layouts/index.html` topics list without
replacing the new exhaustive generated index at `public-imported/index.html`.

## Validation Report

The latest imported build has:

- 31 errors
- 27 warnings

These are recorded in:

```text
public-imported/reports/validation.json
```

The errors are mostly missing old knowl targets in section pages or corpus links.
The warnings are duplicate aliases where multiple knowls naturally share titles
or imported aliases.

The build still succeeds because imported legacy content should be comparable
even when it contains dangling references.

## Notes

- The imported source is intentionally conservative: it preserves the original
  markdown body and only changes the front matter plus knowl link syntax.
- The importer does not yet infer axioms, examples, proofs, or TFAE sections from
  prose. That should be a later semantic enrichment pass.
- The generated index page is large because it lists all 2,089 imported entries.
  A production reader should add section indexes, search, pagination, or grouped
  navigation.
- The compiler now protects TeX spans before Markdown inline formatting and
  renders math at build time with KaTeX when available, falling back to
  `latex2mathml` and then MathJax. See `docs/math-rendering.md` for details and
  remaining production choices.
- The compiler recognizes wikilink labels containing literal `]` characters by
  terminating labels on `]]`. This fixed the visible raw link in
  `/algebra-commutative/` for the Hilbert basis corollary label
  `k[x_1,...,x_n]`.
- The persistent comparison preview is served from `public-imported/` by the
  user systemd service `knowlpedia-refactor-preview.service`; see
  `docs/preview-server-service.md`.

## Latest Browser Checks

Playwright is installed for Node on the Optiplex and has been used for smoke
tests against the Tailscale preview.

Verified on 2026-07-01:

- `http://100.69.17.72:8002/topics/` loaded with title
  `Topics - Imported Knowlpedia Content`
- `http://100.69.17.72:8002/algebra-commutative/` no longer contains the raw
  `[[algebra-commutative/hilbert-basis-corollary|...]]` wikilink
- clicking the Hilbert basis corollary entry opened the corresponding knowl
  panel
