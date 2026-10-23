# Source format

## What Knowlpack means here

Knowlpack is the local name for a collection of source knowls and its package metadata. Within this project it is the normal input format, not an experimental subset of the corpus. The package is described by `knowlpack.toml`; individual knowls are `.knowl.md` files.

A source inspection on 12 September 2026 found 3,641 `.knowl.md` entries in the main `knowlpedia-content/content/` tree and 10 in `testing/`. All parsed with the current compiler. The main count includes 62 compatibility redirects, so it is not a count of distinct definitions. There were no directory bundles with `knowl.toml` in that corpus; those appear in older prototype documentation.

TOML and Markdown are standard building blocks. The manifest fields, semantic link syntax, section behavior, and generated routes form this project's own contract.

## A collection

```toml
id = "org.example.notes"
title = "Example notes"
version = "0.1.0"
content_dir = "content"
development_content_dirs = ["testing"]
```

This file tells the compiler where to discover source entries. Development-only roots are excluded from production discovery. The private reading cache has a separate manifest with `private = true` and a dedicated compiler input; it is never composed into the public content package.

## An individual knowl

```markdown
+++
id = "example/sample-definition"
title = "Sample definition"
kind = "definition"
summary = "A short description used in search and indexes."
aliases = ["alternative name"]
domains = ["example"]
section_mode = "progressive"
prerequisites = []
+++

The precise definition goes here, with its hypotheses and conventions.

## Examples

Examples and motivation can unfold separately.
```

This is a structural template, not a new definition to add to the corpus. Empty prerequisites are appropriate only when justified by the mathematical content; they are not a shortcut around foundation work.

The stable `id` determines the page URL and link target. `title`, `summary`, and `aliases` help people find the entry. `kind` distinguishes definitions, theorems, examples, documents, and other content. `domains` supplies subject metadata.

With progressive sections, the text before the first level-two heading is the compact core; subsequent sections can open independently. The core must retain every qualification needed to interpret its statement. Documents use continuous reading by default; `section_mode = "continuous"` makes that intention explicit.

On a knowl's full page, level-two to level-four headings in the core get an `id` derived from their text, such as `1-modules` for `## 1. Modules`; repeated headings get `-2`, `-3`, and so on. A contents list links to them with ordinary links that include the page path, such as `[1. Modules](/posts/module-theory-learning-path/#1-modules)`. Headings inside inline knowl panels get no `id`.

A reading page made of inline knowls sets `knowls_open = true` so that its top-level knowl links start expanded. Adding `learning_path = true` also lists the page under “Learning paths” on the home page, above the subject directory. Only production pages are listed.

## Expandable links and prerequisites

```text
[[algebra-groups/group|group]]
```

This link displays the word “group” and opens the corresponding knowl. A link can also target a section. Ordinary Markdown links navigate to another page instead.

The `prerequisites` array has a different purpose: it records the concepts required to understand the definition. A prose link to an example, consequence, comparison, or historical remark is not automatically a prerequisite. Review the mathematical role of each edge. The compiler checks graph structure and rejects prerequisite cycles; it cannot prove that every edge is semantically correct or every missing edge has been found.

## Mathematics and document fidelity

The renderer handles LaTeX mathematics within the repository's supported delimiters. Preserve existing delimiter conventions when editing. A whole TeX document is not a drop-in input to this Markdown compiler, and `.knowl` alone is not currently a registered binary format or supported file extension. The concrete reading-source extension is `.knowl.md`, with LaTeX notation embedded in Markdown.

For a private reading copy, preserve an untouched extracted source and add only semantic-link wrappers to its body. Do not replace the author's wording with a paraphrase. PDF extraction needs its own visual and textual checks because line breaks, equations, footnotes, and reading order may be lost before linking even begins.
