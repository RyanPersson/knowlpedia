# Knowl Runtime Performance Notes

Date: 2026-07-01

## Recovered Pre-Refactor Optimization

The old Hugo runtime in `../knowlpedia/static/js/knowls.js` used:

- an in-memory fragment cache
- preloading on hover
- `IntersectionObserver` preloading as knowl links approached the viewport
- nested knowl preloading after a panel opened

That made most common knowl openings feel instant once the page had settled.

## Current Refactor Runtime

The refactor now uses the same idea plus a static-site optimization:

- full knowl pages embed one-click-deep knowl fragments in hidden
  `<template data-knowl-fragment="...">` nodes
- the runtime loads those templates into its cache on page initialization
- direct knowls on a full page can open without a network request
- nested knowls are preloaded after a panel opens
- the generated index uses unfoldable knowl triggers, but does not embed all
  2,089 fragments; it preloads visible/nearby entries with an
  `IntersectionObserver`
- fragment preloading has a small concurrency cap
- CSS explicitly disables transitions and animations

This keeps individual knowl pages fast without making the global index enormous.

## Latest Runtime Fix

The generated index now uses unfoldable knowl triggers, which exposed a nested
insertion bug. If a knowl link inside an index-opened panel was not inside an
inner list item, the old insertion logic could find the outer index `<li>` and
open the nested panel below the parent panel instead of inline inside it.

The runtime now respects the nearest `.knowl-panel` boundary when choosing an
insertion target. This keeps nested knowls inside their parent panel while still
allowing ordinary list-item insertion for inner lists.

This was checked with browser validation of the imported abelian category page:

```text
tmp/screenshots/nested-index-fixed.png
```

Playwright is now installed for Node on the Optiplex, so future interaction
checks should prefer Playwright over static screenshots when possible.

The 2026-07-01 Playwright smoke checks also verified that:

- `/topics/` loads over the Tailscale preview
- the algebra-commutative Hilbert basis corollary entry no longer renders as raw
  `[[...]]`
- clicking that entry opens the corresponding knowl panel

## Measurements

Local build-loop timings on the Mac desktop after the Knowlpack content
migration and TikZ fast-path work:

```text
baseline full build before fast paths:            15.34s
diagram preview, no persistent cache:             0.61s
single-page compile, no persistent cache:         1.84s
full build, cold persistent diagram cache:        14.08s
full build, warm persistent diagram cache:         3.17s
make build-content, warm cache:                    3.11s
make build-page, warm cache:                       0.24s
make preview-diagram, warm cache:                  0.10s
```

Use `make preview-diagram` while correcting one TikZ block, `make build-page
PAGE=<knowl-id>` while checking page integration, and `make build-content` for
commit/deploy verification. The persistent diagram cache lives under
`.knowl-cache/diagrams` and is ignored by git.

One local run on the Optiplex:

```text
current group page, localhost: 0.000653s, 28,168 bytes
current index, localhost: 0.001057s, 740,590 bytes
current binary-operation fragment, localhost: 0.000635s, 3,821 bytes
live knowlpedia.com group page: 0.324015s, 39,259 bytes
live knowlpedia.com binary-operation page: 0.152686s, 28,886 bytes
live knowlpedia.com root: 0.147141s, 16,669 bytes
```

The Tailscale checks from the Optiplex to its own Tailscale IP were also
sub-millisecond, so they confirm serving and payload shape more than real
phone-to-Optiplex latency.

## Open Performance Follow-Ups

- Add gzip or brotli compression for the local preview server if it becomes more
  than a development server.
- Split the huge generated index into grouped pages or add client search.
- Add a Playwright timing harness for repeatable first-click and warmed-click
  latency numbers.
- Add phone-over-Tailscale measurements, since localhost numbers mostly measure
  serving overhead and payload shape.
