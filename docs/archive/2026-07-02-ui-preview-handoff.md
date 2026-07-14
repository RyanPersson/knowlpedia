# UI And Local Preview Handoff

Date: 2026-07-02

This note captures the light-mode knowl UI fix and the Mac desktop preview
server cleanup/manager work.

## UI Fixes

Light-mode knowl panel background cycling now starts with the alternate panel
shade relative to the parent page:

```text
page -> panel -> nested panel -> nested panel
white -> gray -> white -> gray
```

The dark-mode explicit overrides were left in place and still cycle:

```text
dark page -> panel -> nested panel -> nested panel
#1d1e20 -> #2e2e33 -> #1d1e20 -> #2e2e33
```

Other visible changes:

- Light-mode ordinary links now use standard blue `#0645ad` instead of green.
- Knowl fragments now render a second bottom-right close button after the body,
  symmetric with the top-right close button.

Touched files:

```text
packages/static-runtime/knowl.css
packages/compiler/knowl_compile.py
```

## Local Preview Manager

The Mac desktop repo now has a project-local preview manager:

```text
scripts/preview_server.py
```

Make targets:

```bash
make preview-status
make preview-start
make preview-stop
make preview-adopt
make preview-restart
make preview-scan
```

Default behavior:

- Serves `public-imported/`.
- Uses `http://127.0.0.1:8012/`.
- Stores state and logs under ignored `.preview-server/`.
- Reuses a running tracked preview instead of starting duplicates.
- Refuses to start if the target port is occupied by an untracked listener.
- Can adopt an already-running listener with `make preview-adopt`.

Current local state after cleanup:

```text
tracked preview: running
pid: 39977
url: http://127.0.0.1:8012/
directory: /Users/ryanpersson/anki/code/knowlpedia-root/knowl-system-refactor/public-imported
```

The old leftover Python preview servers on ports `8001` and `8011` were stopped.

## Verification

Commands run:

```bash
make build
make build-content
python3 -m py_compile scripts/preview_server.py packages/compiler/knowl_compile.py packages/importers/import_knowlpedia_content.py packages/compiler/preview_diagram.py
make preview-status
```

`make build-content` still reports the known imported-corpus validation errors
and warnings, but completes successfully.

Browser verification against `/convex-analysis/` confirmed:

- light panels: `rgb(247,247,247) -> rgb(255,255,255) -> rgb(247,247,247)`
- dark panels: `rgb(46,46,51) -> rgb(29,30,32) -> rgb(46,46,51)`
- each opened knowl fragment has two close buttons
- light full-page link color is `rgb(6,69,173)`

## Future Agent Guidance

Before starting any local preview in this repo:

```bash
make preview-status
```

If a preview is already tracked and running, use its URL. If a preview is
running but untracked on the default port, run:

```bash
make preview-adopt
```

Do not start raw `python3 -m http.server` processes for the imported preview
unless the manager is unsuitable for a specific one-off debugging reason.
