# Private reading

## A faithful, expandable reading copy

The [Library](/library/) lists prepared documents in `knowlification-cache`. Opening one uses the same reader as the public corpus, so its linked concepts can unfold recursively. The source document's prose remains the author's text; reusable definitions live in the shared corpus.

The included reading demonstration is original project text, not a converted paper. It provides a small way to check that private documents can open public knowls and their nested links.

## Where each artifact belongs

| Artifact | Location | Git and serving behavior |
| --- | --- | --- |
| Original PDFs, scans or TeX inputs | `knowlification-cache/docs/` | Gitignored; not served by the site |
| Untouched extracted Markdown or text | `knowlification-cache/sources/` | Versioned only in the private repository; not served |
| Linked reading documents | `knowlification-cache/documents/*.knowl.md` | Versioned privately; rendered only in development |
| Term dictionaries, missing-knowl candidates and link decisions | `knowlification-cache/metadata/` | Versioned privately; not served |
| Independently authored reusable knowls | `knowlpedia-content/content/` | Intended for public review and publication |
| Application code and these documentation pages | `knowlpedia/` | Public code repository; docs currently visible only in development |

Original papers and their linked or extracted wording never belong in either public repository. Author public knowls in our own words after checking the mathematical sources; do not copy a paper's prose or figures into the corpus. Keep source-dependent quotations and extraction artifacts private.

## Add a prepared document

1. Put the original input in the cache's ignored `docs/` directory.
2. Preserve a faithful extracted version in `sources/` before inserting links.
3. Save the linked version under `documents/` as a `.knowl.md` file. Give it a unique `documents/<slug>` ID and `kind = "document"`.
4. Add `[[target/id|original visible text]]` wrappers where a mathematically suitable public knowl exists. Preserve the wording, ordering, headings and notation.
5. Keep a term inventory and unresolved candidates in `metadata/`. Research and author missing reusable knowls, including their missing prerequisites, in the public corpus.
6. Check source fidelity after stripping link wrappers, run the project's required validation, and rebuild development with `make build` from the application checkout.

```markdown
+++
id = "documents/my-reading-copy"
title = "My reading copy"
kind = "document"
summary = "A private reading copy."
domains = ["documents"]
section_mode = "continuous"
+++

The faithfully extracted document body goes here.
```

The compiler discovers the sibling cache when its manifest exists. To choose another private cache, set `PRIVATE_CONTENT_PACKAGE` when building. A full build refreshes the library index; a single-page build updates only that document and its fragments.

## Preserve PDF page layouts

A prepared PDF document can use a facsimile manifest. Its reader displays the original page images with expandable term overlays, a selectable linked transcript, source cross-references, and optional local notation notes. Page controls, contents, zoom, direct page URLs, and browser history retain the reading position. Concepts open in a drawer; their prerequisite links continue to unfold recursively.

Add `facsimile_manifest = "metadata/my-document/pages.json"` to a private document's frontmatter and keep `section_mode = "continuous"`. The body contains the linked extraction with form-feed characters separating pages. After removing link wrappers, each page must match its manifest's text hash. Independently compare the complete unwrapped body with the untouched extraction to verify whitespace and page boundaries as well.

The version-one manifest contains consecutive `pages` with dimensions, relative image paths, image and text SHA-256 hashes, term `links` with source-coordinate rectangles, and optional page `concepts`. It may also contain `bookmarks`, `notes`, and an HTTPS `source_url`. Original PDF references retain their rectangles and either a destination `page` with vertical position `y` or an HTTPS `url`. The compiler validates the manifest and all concept targets before writing output.

Page images belong in the private package, usually an ignored reproducible `build/` directory. Only the explicitly listed, hash-checked image files are copied under that document's development route. Paths must stay inside the private package, and SVGs cannot contain scripts or external references. The original PDF is never copied. Production builds reject private facsimile input and remove prior private document assets when rebuilding an output directory.

This is a prepared-document format. Extracting page geometry, selecting mathematically suitable phrases, distinguishing local notation, and recording link decisions remain explicit authoring steps.

## What is and is not automated

Prepared documents are discovered and compiled automatically during development builds. Suitable existing wikilinks resolve against the combined development registry, including the public corpus. The private library index is generated from the discovered documents.

Adding a PDF does not yet perform extraction, OCR, terminology discovery, automatic linking, or prerequisite authoring. Those are intended additions to an AI-assisted import workflow. The source format, private repository boundary, and reader integration provide the foundation for them.

## Private Git remote

The cache has only a local bare remote at `/home/ryan/git/knowlification-cache.git`. Its pre-push check restricts pushes to that destination. There is no GitHub remote. `docs/` is ignored, so the private Git remote does not preserve the original PDFs; keep those source inputs according to your own storage needs.

The source, converted document, and private metadata can be committed in this repository. Public knowls are committed in `knowlpedia-content` separately, after the relevant research and validation. Production builds contain neither the private library nor its document pages, fragments or index entries.
