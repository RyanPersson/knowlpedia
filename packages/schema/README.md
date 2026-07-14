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

## Knowl Source

Each knowl is one `.knowl.md` file with TOML front matter and Markdown body:

```markdown
+++
id = "shared-foundations/set"
title = "Set"
kind = "definition"
summary = "A collection of objects."
aliases = ["set", "sets"]
+++

A **set** is ...

## Examples

A basic example belongs here.
```

Examples and other secondary material can follow the core body as level-two
sections. The compiler turns those sections into addressable, unfoldable
fragments without splitting one knowl across multiple source files.

Important fields:

- `id`: stable graph id, such as `algebra-groups/group`
- `title`: display title
- `kind`: `definition`, `theorem`, `lemma`, `example`, etc.
- `summary`: one-line description
- `aliases`: terms for future search/autolinking
- `relations`: typed graph edges

## Wikilinks

Markdown uses explicit semantic links:

```markdown
[[algebra-groups/group|group]]
[[algebra-groups/group#axiom.identity|identity axiom]]
```

The compiler validates the target id and anchor.
