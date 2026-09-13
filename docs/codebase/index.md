# Understanding Knowlpedia

Knowlpedia is a mathematical reference and an inline reading format. You can open an unfamiliar term, unfold its prerequisites, and return to the surrounding argument without leaving the page. The public corpus is the reusable knowledge produced by that reading process.

## Start here

- [Source format](/docs/source-format/) explains what a knowl file contains, what Knowlpack means, and how links differ from prerequisites.
- [Architecture](/docs/architecture/) follows a source file through the compiler to the browser.
- [Private reading](/docs/private-reading/) explains the document cache, the library, and the boundary between private reading copies and public definitions.
- [Development and checks](/docs/development/) explains how to build, inspect, and change the site.

## The intended reading experience

An illuminated reading copy preserves a document's wording and mathematical notation while adding expandable links. It is a conversion into a more readable format, rather than a rewritten explanation of the paper. A definition can unfold into simpler definitions until the reader understands it or reaches explicitly stated axioms and symbol-manipulation rules.

Try unfolding a [[algebra-groups/group|group]] here. Inside that knowl, links lead to further mathematical concepts. Closing an expansion returns you to this text.

The intended prerequisite structure is a shared directed acyclic graph: multiple concepts can reuse the same prerequisite. There is no preset depth cap. Its ultimate leaves are explicit primitive data, formation rules, axioms, and inference rules in the chosen foundation. This is the project's goal; the current corpus and review counters do not establish that every concept already has complete axiomatic closure.

## What exists today

The codebase compiles Markdown knowls with TOML metadata into static pages, reusable fragments, search data, and graph data. The browser supports recursive inline expansion, optional sections, mathematical notation, search, and a prerequisite graph. Development builds also contain these documentation pages, testing controls, and a private document library.

The library reads prepared `.knowl.md` documents from a separate private repository and resolves their links against the public corpus. Original PDFs are kept outside the served output. PDF upload, OCR or extraction, automatic terminology inventory, and automatic authoring of missing knowls are future reader features; adding a PDF to the cache alone does not yet convert it.

## The longer-term workflow

1. Import a PDF or TeX document into private storage.
2. Preserve the original and extract a faithful reading source.
3. Inventory mathematical terms and link suitable existing knowls.
4. Record missing concepts and expand their genuine prerequisites down to axiomatic data.
5. Research and author reusable definitions in our own words in the public corpus.
6. Link the private reading copy to those definitions and validate fidelity and rendering.

The public artifact is the reusable corpus. Source documents, their extracted wording, and illuminated reading copies remain private. Possible later work includes professor-oriented collections, portable static-site guides, and wider discovery of the project. Those are future directions rather than implemented features.

## About these pages

These pages describe the current compiler and runtime, rather than the architecture of an earlier refactor. Their source is `knowlpedia/docs/codebase/`. They are compiled only in development for now. The historical plans elsewhere in `docs/` remain useful background, but executable behavior and current tests are the authority when an old plan disagrees.
