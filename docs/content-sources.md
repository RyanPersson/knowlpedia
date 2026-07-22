# Content sources

Knowlpedia uses separate source sets for local exploration and GitHub Pages.

## Local development and preview

`make build-content`, `make build-page`, and the preview targets compose:

1. `../knowlpedia-content`, the primary content package; and
2. every repository named in `EXTRA_CONTENT_SOURCES`, which defaults to the
   local-only `../conjectures-catalog`.

The sources are copied into the ignored
`.knowl-cache/content-package/` directory. `scripts/compose_content.py` rejects
relative-path collisions and writes `.knowl-source-manifest.json` so every
compiled file can be traced to its canonical repository.

## GitHub Pages production

`make build-production` does not use `EXTRA_CONTENT_SOURCES`. It creates a
separate ignored package at `.knowl-cache/production-content-package/` from
`../knowlpedia-content` alone. The composer receives an exact-source assertion;
the build fails if any additional repository appears in its manifest.

The Pages workflow checks out only `knowlpedia` and the `main` branch of
`knowlpedia-content`, then invokes `make build-production`. It never checks out
`conjectures-catalog`. Consequently, the local conjecture corpus can be viewed
through the same UI on the OptiPlex without becoming part of the deployed site.

## Adding another local source

A contributor normally exposes a `content/` directory. It may instead include a
`knowlpack.toml` with a custom `content_dir`.

```bash
make build-content \
  EXTRA_CONTENT_SOURCES="../conjectures-catalog ../another-local-source"
```

Adding a source to local builds does not authorize adding it to production.
