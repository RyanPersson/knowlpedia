# Static Runtime

This directory contains the tiny browser runtime copied into generated static
sites.

It supports:

- click-to-expand inline knowls
- normal full-page navigation for modified clicks and context menus
- a full-page fallback when an inline fragment cannot be loaded
- recursive nested knowls
- progressively disclosed, lazily loaded inline sections
- close controls, focus restoration, and deepest-first Escape-to-close
- TFAE/alternate-definition switchers
- on-demand static search with `/` and Command/Ctrl+K shortcuts
- a responsive index grouped by mathematical area
- mobile full-width inline panels with bounded nested indentation
- light/dark themes with WCAG AA text contrast

The runtime is intentionally static-only. It does not require a server database.
