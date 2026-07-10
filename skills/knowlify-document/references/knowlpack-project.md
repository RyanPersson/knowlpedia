# Knowlpack Project Contract

## Canonical locations

- Compiler/runtime: `knowl-system-refactor/`
- Canonical source package: sibling `knowlpedia-content/`
- Source knowls: `knowlpedia-content/content/**/*.knowl.md`
- Generated site: `knowl-system-refactor/public-imported/`
- Never author in `knowl-system-refactor/imports/` or `public-imported/`.

## Compact knowl format

Use TOML front matter beginning at byte zero:

```markdown
+++
id = "domain/stable-id"
title = "Display title"
kind = "knowl"
summary = "One-line definition."
aliases = ["term", "terms"]
domains = ["domain"]
+++

Definition-first Markdown body.
```

Semantic links use `[[domain/id|label]]`. Generated page and fragment routes are `/<id>/` and `/fragments/<id>/core.html`.

## Build and validation

Run from `knowl-system-refactor/`:

```bash
make preview-status
make build-content
make check-rendering
```

The full corpus has historical validation findings. Save the baseline report before edits and compare `public-imported/reports/validation.json` after the build; require no new failures attributable to the new content.

Check that every new ID appears once in `public-imported/indexes/registry.json`, transcript targets appear in `indexes/links.json`, and generated transcript/index HTML contains no `missing-knowl` class.

Record:

```bash
wc -c public-imported/<document-id>/index.html
rg -c '<template data-knowl-fragment' public-imported/<document-id>/index.html
```

## Preview

Use the tracked narrow server, which serves only `public-imported/`:

```bash
make preview-start
make preview-status
```

Default local URL is `http://127.0.0.1:8012/`. Do not serve a broad personal workspace directory.

## Browser QA

Open both the temporary index and the transcript. Verify:

1. ordinary clicks expand definitions inline;
2. nested links expand from inside a knowl;
3. close controls work;
4. math renders without raw delimiters or commands;
5. representative full-page navigation works;
6. wide formulas remain usable on a narrow viewport.
