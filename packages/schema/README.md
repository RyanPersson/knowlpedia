# Prototype Schema

This prototype uses TOML metadata and markdown prose so it can compile with only
the Python standard library.

The intended model is not "TOML forever"; the intended model is:

```text
typed source files -> validated graph -> static/runtime artifacts
```

## Package

`knowlpack.toml` identifies a package:

```toml
id = "org.example.course"
title = "Example Course"
version = "0.1.0"
content_dir = "content"
```

## Single-File Knowl

Use a `.knowl.md` file for compact concepts:

```markdown
+++
id = "shared-foundations/set"
title = "Set"
kind = "definition"
summary = "A collection of objects."
aliases = ["set", "sets"]
+++

A **set** is ...
```

## Bundle Knowl

Use a directory with `knowl.toml` for richer concepts:

```text
group/
  knowl.toml
  core.md
  examples.md
  tfae.toml
  proofs/
    identity-uniqueness.toml
```

Important fields:

- `id`: stable graph id, such as `algebra-groups/group`
- `title`: display title
- `kind`: `definition`, `theorem`, `lemma`, `example`, etc.
- `summary`: one-line description
- `aliases`: terms for future search/autolinking
- `core`: canonical section
- `sections`: optional unfoldable layers
- `relations`: typed graph edges

## Wikilinks

Markdown uses explicit semantic links:

```markdown
[[algebra-groups/group|group]]
[[algebra-groups/group#axiom.identity|identity axiom]]
```

The compiler validates the target id and anchor.

