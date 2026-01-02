# Implementation Roadmap

## Final Architecture

```
Hugo (v0.132+) + Build-time KaTeX (htmlAndMathml) + Custom Knowls + Giscus + Form Submission
```

---

## Phase 1: Hugo Setup with Math Rendering

### 1.1 Initialize Hugo Site
- Install Hugo (v0.132.0 or later required for `transform.ToMath`)
- Create new site: `hugo new site blog`
- Choose/create a minimal theme

### 1.2 Configure Build-time Math Rendering

**`hugo.toml`:**
```toml
[markup]
  [markup.goldmark]
    [markup.goldmark.extensions]
      [markup.goldmark.extensions.passthrough]
        enable = true
        [markup.goldmark.extensions.passthrough.delimiters]
          block = [['\\[', '\\]'], ['$$', '$$']]
          inline = [['\\(', '\\)'], ['$', '$']]
```

**`layouts/_default/_markup/render-passthrough.html`:**
```go-html-template
{{- $opts := dict "output" "htmlAndMathml" "displayMode" (eq .Type "block") -}}
{{- with try (transform.ToMath .Inner $opts) -}}
  {{- with .Err -}}
    {{- errorf "KaTeX error: %s (%s)" . $.Position -}}
  {{- else -}}
    {{- .Value -}}
    {{- $.Page.Store.Set "hasMath" true -}}
  {{- end -}}
{{- end -}}
```

### 1.3 Add KaTeX CSS (self-hosted)

**In `layouts/partials/extend_head.html`:**
```html
<link rel="stylesheet" href="{{ "css/katex.min.css" | relURL }}">
```

KaTeX CSS and fonts are self-hosted in `static/css/` for reliability and performance.

---

## Phase 2: Knowl System

### 2.1 Content Structure
```
content/
  posts/
    example-post.md
    group-axioms.md
  glossary/
    _index.md
    vector-space.md
    linear-map.md
    group.md
    ...

layouts/
  knowls/
    single.html          # Fragment output (no <html> wrapper)
  glossary/
    single.html          # Full page output
```

### 2.2 Knowl Shortcode

**`layouts/shortcodes/knowl.html`:**
```go-html-template
{{- $id := .Get "id" -}}
{{- $text := .Get "text" -}}
<a class="knowl"
   href="/glossary/{{ $id }}/"
   data-knowl="/knowls/{{ $id }}.html"
   role="button"
   aria-expanded="false">{{ $text }}</a>
```

**Usage in posts:**
```markdown
A {{< knowl id="def.vector_space" text="vector space" >}} is a set V with...
```

### 2.3 Knowl JavaScript

**`static/js/knowls.js`:** (~80 lines)
- Event delegation for `.knowl` clicks
- Fetch fragment from `data-knowl` URL
- Insert after nearest block element
- Cache fetched fragments
- No MathJax re-render needed (already pre-rendered)

### 2.4 Knowl CSS (inlined in extend_head.html)
- Dotted underline trigger style
- Expandable panel with border-left accent
- Close button
- Alternating depth shading for nested knowls
- Print styles
- CSS is inlined to eliminate render-blocking request

---

## Phase 3: Giscus Integration

### 3.1 Setup
1. Enable GitHub Discussions on your blog repo
2. Install Giscus app: https://github.com/apps/giscus
3. Configure at https://giscus.app/

### 3.2 Embed in Post Template

**`layouts/posts/single.html`:**
```html
<script src="https://giscus.app/client.js"
        data-repo="YOUR_USERNAME/YOUR_REPO"
        data-repo-id="YOUR_REPO_ID"
        data-category="Comments"
        data-category-id="YOUR_CATEGORY_ID"
        data-mapping="pathname"
        data-strict="0"
        data-reactions-enabled="1"
        data-emit-metadata="0"
        data-input-position="top"
        data-theme="preferred_color_scheme"
        data-lang="en"
        crossorigin="anonymous"
        async>
</script>
```

---

## Phase 4: Non-GitHub Comment Form

### 4.1 Choose Form Backend
Recommended: **Formspree** (simple) or **Formspark** (more submissions)

### 4.2 Add Form to Post Template

```html
<details class="comment-form-fallback">
  <summary>No GitHub account? Submit a comment here</summary>
  <form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
    <label>
      Name (or pseudonym):
      <input type="text" name="name" required>
    </label>
    <label>
      Comment:
      <textarea name="comment" rows="4" required></textarea>
    </label>
    <input type="hidden" name="_subject" value="Blog comment submission">
    <input type="hidden" name="post" value="{{ .Permalink }}">
    <button type="submit">Submit for Review</button>
  </form>
  <p><small>Your comment will be reviewed and posted to the discussion.</small></p>
</details>
```

### 4.3 Workflow
1. Formspree emails you submissions
2. You review, then post to GitHub Discussion with attribution:
   > **From: [Name]**
   >
   > [Their comment]

---

## Phase 5: RSS Feed

### 5.1 Hugo Default RSS
Hugo generates RSS automatically at `/index.xml`

### 5.2 Customize (optional)
- Add disclaimer about math not rendering in readers
- Ensure full content in feed (not excerpts)

### 5.3 Submit to mathblogging.org
After launch, submit your feed URL

---

## Phase 6: GitHub Pages Deployment

### 6.1 GitHub Actions Workflow

**`.github/workflows/hugo.yml`:**
```yaml
name: Deploy Hugo site to Pages

on:
  push:
    branches: ["main"]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

defaults:
  run:
    shell: bash

jobs:
  build:
    runs-on: ubuntu-latest
    env:
      HUGO_VERSION: 0.139.0
    steps:
      - name: Install Hugo CLI
        run: |
          wget -O ${{ runner.temp }}/hugo.deb https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.deb \
          && sudo dpkg -i ${{ runner.temp }}/hugo.deb
      - name: Checkout
        uses: actions/checkout@v4
        with:
          submodules: recursive
      - name: Setup Pages
        id: pages
        uses: actions/configure-pages@v4
      - name: Build with Hugo
        env:
          HUGO_ENVIRONMENT: production
        run: |
          hugo \
            --minify \
            --baseURL "${{ steps.pages.outputs.base_url }}/"
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./public

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

### 6.2 Enable GitHub Pages
- Repo Settings → Pages → Source: "GitHub Actions"

---

## Implementation Order

1. **Phase 1** - Get Hugo + math rendering working locally
2. **Phase 6** - Deploy bare site to GitHub Pages (validates pipeline)
3. **Phase 3** - Add Giscus (core comment functionality)
4. **Phase 2** - Build knowl system (your unique feature)
5. **Phase 4** - Add submission form (accessibility)
6. **Phase 5** - Polish RSS, submit to aggregators

---

## Current Status

### Completed
- [x] Hugo + PaperMod theme setup
- [x] Build-time KaTeX math rendering (self-hosted CSS/fonts)
- [x] Knowl system (unlimited depth, alternating shading, close buttons, inlined CSS)
- [x] GitHub Actions deployment workflow
- [x] Glossary with mathematical definitions (linear algebra + algebraic structures)
- [x] Custom RSS feed template
- [x] Euler diagram shortcode for algebraic structure visualization

### TODO
- [ ] **Comments (Giscus + Formspree)** - Template exists in `layouts/partials/comments.html` but is commented out. To enable:
  1. Enable GitHub Discussions on the repo
  2. Install Giscus app: https://github.com/apps/giscus
  3. Configure at https://giscus.app/ to get repo ID and category ID
  4. Sign up at https://formspree.io for the fallback form
  5. Uncomment the template and fill in the placeholders


## Open Items to Decide

- [ ] Form service: Formspree vs Formspark vs other?

---

## Repository Structure (Post-Refactor)

This project uses a **submodule architecture** to separate content from infrastructure:

```
mathblog/                          ← This repo (pipeline + infrastructure)
├── content/                       ← Git submodule → knowlpedia-content
├── layouts/                       ← Hugo templates
├── static/                        ← JS, CSS, fonts
├── scripts/                       ← Automation scripts
├── docs/                          ← Pipeline documentation
└── tmp/                           ← Local working files (gitignored)

knowlpedia-content/                ← Separate repo (generated knowls)
├── algebra-groups/
├── algebra-modules/
├── analysis/
├── geometry-bundles/
└── ... (~1,500 knowl files)
```

**Why submodules?**
- Iterate on the generation pipeline without affecting production content
- Test regenerating knowls on a branch without losing good content
- Clean separation of concerns

---

## Development Workflows

### Fresh Clone (new machine or collaborator)

```bash
git clone --recurse-submodules git@github.com:RyanPersson/mathblog.git

# Or if already cloned without submodules:
git submodule update --init --recursive
```

### Working on Infrastructure (layouts, scripts, docs)

Changes to pipeline code stay in the main mathblog repo:

```bash
# Edit layouts, static files, scripts, docs...
git add .
git commit -m "Update layouts"
git push origin main
```

### Working on Content (generating/editing knowls)

Content lives in the submodule. Work inside it:

```bash
cd content/
git checkout -b test-regeneration    # Branch inside the content repo

# Generate or edit knowls...
# Delete and regenerate a section if needed:
rm -rf algebra-groups/*
# Run generation pipeline...

# Test locally (from parent dir)
cd ..
hugo server

# If results are good:
cd content/
git add . && git commit -m "Regenerated algebra-groups"
git checkout main
git merge test-regeneration
git push

# Update submodule reference in parent
cd ..
git add content
git commit -m "Update content submodule"
git push origin main

# If results are bad - discard:
cd content/
git checkout main
git branch -D test-regeneration
```

### Validating Knowl References

Check for broken knowl links:

```bash
python3 scripts/validate-knowls.py
```

This scans all `{{< knowl id="..." section="..." >}}` references and reports any that point to non-existent files.

### Local Development with Feedback System

```bash
# Terminal 1: Hugo server
hugo server

# Terminal 2: Feedback API (for upvote/downvote functionality)
python3 scripts/feedback-api.py
```

---

## Scripts Reference

| Script | Purpose |
|--------|---------|
| `scripts/validate-knowls.py` | Check for broken knowl references |
| `scripts/feedback-api.py` | Local feedback voting API (localhost only) |

---

## Reference Docs

| Document | Purpose |
|----------|---------|
| `docs/orchestration.md` | Full knowl generation pipeline |
| `docs/knowl-generation/` | Step-by-step generation workflow |
| `docs/knowl-modules/decomposition.md` | Module specs and progress tracking |
| `CLAUDE.md` | Quick reference for Claude agents |

