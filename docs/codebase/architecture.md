# Architecture

## Three repositories, three responsibilities

| Repository | Responsibility | Publication boundary |
| --- | --- | --- |
| `knowlpedia` | Compiler, browser runtime, scripts, tests, codebase docs | Public application code |
| `knowlpedia-content` | Reusable mathematical definitions, theorems, relations, review evidence | Publicly intended authored content |
| `knowlification-cache` | Original inputs, faithful extracted sources, linked reading copies, term inventories | Private; local Git remote only |

These repositories normally sit beside each other under `knowlpedia-root`. Separate worktrees under `persistant/` and experimental directories are different checkouts; inspect the working directory and branch before changing or building anything. The private cache is not a submodule of either public repository.

## From source to reader

```text
knowlpedia-content
        |
        v
compose_content.py --> selected public/local reference sources
        |
        v
knowl_compile.py <---- private documents (development only)
        |
        +--> HTML pages and expandable fragments
        +--> search, link and prerequisite indexes
        +--> validation and build reports
        |
        v
static server --> knowl.js + knowl.css --> inline reading
```

The diagram describes data flow. It does not imply that private documents are copied into the public content repository.

## Where to look in the code

| File or directory | What it owns |
| --- | --- |
| `Makefile` | Dependencies, source composition, build profiles, audits and preview commands |
| `scripts/compose_content.py` | Copies selected sources into an ignored build package and records provenance; rejects private packages |
| `packages/compiler/knowl_compile.py` | Parses source entries, resolves IDs and redirects, validates links and prerequisites, renders pages and indexes |
| `packages/compiler/graph_algorithms.py` | Graph algorithms shared by the compiler |
| `packages/static-runtime/knowl.js` | Search and recursive inline expansion in the browser |
| `packages/static-runtime/graph.js` | Prerequisite graph interaction |
| `packages/static-runtime/knowl.css` | Typography, page layout, expansion panels, themes and responsive behavior |
| `packages/static-runtime/knowl-testing.js` | Development-only visual testing and feedback controls |
| `scripts/check_rendering_errors.py` | Detects broken rendered output and production-profile contamination |
| `tests/` | Python behavior tests and browser smoke checks |
| `workflows/create-knowl-batch.md` | Required process for researched, linked and validated content batches |

The current implementation deliberately keeps most compilation in one Python module. These docs explain that structure; they do not require another refactor to make the architecture look more elaborate.

## What a build produces

The usual output directory is `public-imported/`. A knowl has a standalone page at its ID path, a reusable `fragments/<id>/core.html` fragment, and optional section fragments. The output also contains `assets/`, `indexes/`, and `reports/`.

Small pages can embed the fragments they directly reference. Larger pages load fragments as needed. The browser inserts an expansion near the clicked link; links inside the expansion can open additional knowls. The original page remains in place.

Generated files are disposable output, not canonical authoring locations. A full compiler build replaces its output directory, including generated comparison pages stored there. Recreate any comparison artifacts needed after rebuilding.

## Development and production

Development includes testing content, documentation, and the private library. Local-only reference collections can also be composed for exploration. Private documents are loaded separately with `--private-package`; their entries are marked private and do not enter the public subject index.

Production composes only the primary public package. It does not pass the private input to the compiler. The compiler refuses private packages as primary input, and the composer refuses them as public contributors. The production checker rejects documentation, library and private-document routes, private fragments, private build metadata, and development navigation.

These are build-time boundaries. A development server is not an authenticated private portal: access depends on the machine and network serving it. Use local or Tailscale access for a build containing reading copies. Never upload a development output directory to public hosting.
