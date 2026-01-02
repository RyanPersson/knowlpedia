# Claude Code Context

## Project Overview

A mathematics blog built with Hugo, featuring:
- **Build-time KaTeX rendering** - Math renders at build time, no client-side delay
- **Knowl system** - Clickable terms that expand inline to show definitions (inspired by nLab)
- **Submodule architecture** - Content (`knowlpedia-content`) separate from infrastructure (`mathblog`)
- **GitHub Pages deployment** - Automated via GitHub Actions

## Quick Start

```bash
# Clone with submodules
git clone --recurse-submodules git@github.com:RyanPersson/mathblog.git

# Start development server
hugo server

# Build for production
hugo --minify

# Validate knowl references
python3 scripts/validate-knowls.py
```

**Note for agents:** Before starting `hugo server`, check if port 1313 is already in use (`lsof -i :1313`). Another agent may have already started the server. If so, use the existing server rather than starting a new one.

## Repository Structure

```
mathblog/                          ← This repo (pipeline + infrastructure)
├── content/                       ← Git submodule → knowlpedia-content
├── layouts/                       ← Hugo templates (consolidated - works for all sections)
├── static/                        ← JS, CSS, fonts
├── scripts/                       ← Automation scripts
├── docs/                          ← Pipeline documentation
└── tmp/                           ← Local working files (gitignored)
```

## Key Files

- `layouts/_default/single.html` - Knowl entry template (handles all sections dynamically)
- `layouts/shortcodes/knowl.html` - `{{</* knowl id="term" section="section-name" text="display" */>}}`
- `static/js/knowls.js` - Client-side knowl behavior
- `scripts/validate-knowls.py` - Check for broken knowl references
- `scripts/feedback-api.py` - Local feedback voting API

## Knowl Usage

```markdown
{{</* knowl id="vector-space" text="vector space" */>}}
{{</* knowl id="ring" section="algebra-rings" text="ring" */>}}
```

## Detailed Documentation

See `IMPLEMENTATION.md` for:
- Full development workflows (infrastructure vs content changes)
- Submodule workflow for testing knowl regeneration
- Technical implementation details

See `docs/orchestration.md` for:
- Knowl generation pipeline
- Batch processing workflow

## Domain

**knowlpedia.com**
