## Knowls for mathematical writing

### Minimal terminology (so later choices are precise)

* **Static site**: a website whose served pages are precomputed files. Formally, if (U) is the set of URL paths for the site and (\mathcal{F}) is the set of files, a static site is (conceptually) a mapping (S:U\to\mathcal{F}) where the file (S(u)) is served “as-is”, with no per-request computation.

* **Static site generator (SSG)**: a program (G) that maps a **source tree** (Markdown + templates + assets) to a **build tree** (HTML/CSS/JS files). Formally, (G:T\to O) where (T) is a directory of source content and (O) is a directory of output files.

* **Transclusion**: inclusion of a document (or fragment) **by reference** into another document. Concretely, instead of following a link to a new page, you load the linked content and insert it into the current page. AIM’s knowl documentation explicitly uses this notion and emphasizes that the included content should be **self-contained** (“context independence / neutrality”).

* **Knowl**: an inline transclusion UI pattern: a trigger (typically a word/phrase) plus a hidden/loaded fragment that expands **in place** without navigating away. AIM’s reference implementation treats a knowl trigger like a hyperlink, but uses a `knowl="…"` attribute instead of `href="…"`, and loads ordinary HTML fragments.

* **Client-side rendering**: computation performed in the browser (JavaScript), e.g. fetching a knowl fragment and inserting it into the DOM.

* **Progressive enhancement**: a design constraint: without JavaScript, the site remains usable (e.g. a definition is a normal link to a glossary page); with JavaScript enabled, you upgrade that link into an inline knowl.

---

### What LMFDB does (the behavior you want)

LMFDB uses knowls as first-class “local expansions” for mathematical terms: the user stays on the same page; definitions, notes, etc. appear inline. Their contributor guidelines explicitly encourage defining key terms via knowls (e.g. “abelian variety”, “Hecke character”, etc.).

LMFDB also exposes a “knowledge base” of knowl pages (served under `/knowledge/...`), which reflects the architectural idea: knowls are addressable fragments that can be loaded into other pages.

A historical datapoint that matters for compatibility: a widely circulated knowl implementation (and documentation) states that knowls “made their first appearance on LMFDB.org in August, 2011.”

**Important caveat**: I could not reliably open all LMFDB pages due to anti-bot (reCAPTCHA) blocks in some paths, so the most detailed “view-source” level analysis of *their exact* JS wiring is incomplete here. The architectural pattern (trigger → fetch fragment → insert inline) is clear, but the exact selectors/classes used on current LMFDB pages could differ.

---

### nLab vs knowls (why nLab is the anti-pattern for your goal)

* **nLab pattern** (as you described): a *hyperlink graph* of concept pages. This is excellent for a reference wiki, but it induces the **rabbit-hole / combinatorial explosion** failure mode in linear reading: each definition becomes a new page, which itself links out, etc.

* **Knol pattern**: a *local expansion* that keeps the reader’s working context fixed (same scroll position), so you can add depth without breaking flow. AIM’s docs explicitly frame knowls as “like hyperlinks” except the target appears “at your original location.”

---

### “AMS knowls” vs what the evidence actually shows

Your prompt attributes knowls to AMS. The most direct primary documentation I found attributes the knowl concept/tooling to **AIM (American Institute of Mathematics)**, including explicit instructions and credit to the “Knowls creator Harald Schilly.”

I did **not** find (in the sources retrieved here) an AMS-maintained “official knowl.js” library distinct from the AIM/Schilly lineage. What *is* clearly documented is:

* an AIM-hosted “how to” page (includes JS/CSS includes and syntax),
* a small open repository describing knowls and their LMFDB origin story,
* Debian packaging of `knowl.js` (see next section),
  which together suggests the practical open implementation to start from is the AIM/Schilly codebase, not an AMS-branded one.

---

### Existing libraries / implementations

#### 1) The “classic” knowl.js (AIM / Schilly lineage)

AIM’s documentation describes a concrete implementation approach:

* include jQuery,
* include a `knowlstyle.css`,
* include `knowl.js`,
* write `<a knowl="target.html">trigger</a>`,
* store the knowl body as an HTML fragment (often without a full `<head>`).

This implementation is packaged in Debian as `libjs-knowl`, which is strong evidence that it exists as a reusable library rather than being purely site-specific.

**License constraint (very important)**: Debian’s copyright metadata lists the upstream as “knowl.js” and records the license as **GPL-3+** with copyright attributed to Harald Schilly (and Debian packaging by Doug Torrance). If you *embed or modify* GPL-licensed JS in your site and distribute it, you must comply with GPL obligations.

That license alone is often the decisive reason to **not** copy/fork knowl.js verbatim for a personal blog, unless you’re happy making your site’s JS source available under GPL-compatible terms.

#### 2) PreTeXt ecosystem (not a perfect fit for your constraints)

AIM’s knowl page notes knowls are used extensively in Beezer’s online linear algebra materials, which is historically tied to the PreTeXt/MathBook XML ecosystem.
PreTeXt has a rich knowl story, but it conflicts with your *Markdown-first* requirement (PreTeXt authoring is XML-ish, not Markdown).

---

## Recommendation for a static math blog

### The recommendation in one sentence

Implement a **custom, small, vanilla-JS knowl system** with **progressive enhancement**, storing knowl bodies as **build-generated HTML fragments** (one file per definition), and triggering **MathJax/KaTeX re-typesetting** when fragments are inserted.

This is essentially “Option A (custom)” but shaped to preserve the good parts of the LMFDB/AIM model while avoiding the two biggest problems:

1. GPL inheritance from classic knowl.js,
2. uncontrolled nesting / rabbit holes.

---

### Why “custom vanilla JS” beats “adapt existing knowl.js” for you

1. **License**: the classic knowl.js is GPL-3+. If you want a lightweight blog repo without GPL concerns, write your own.

2. **Accessibility**: classic implementations often start from `<a>` tags and click handlers. You can do better by emitting a `<button>`-like control with `aria-expanded`, explicit `aria-controls`, and keyboard behavior by construction.

3. **Control of depth**: you want “all layers collapsible down to axioms” *without* turning into nLab. That implies a **depth policy** (see below), which you’ll want to encode in the UI/JS.

---

## Content structure for definitions

### Strong default: one fragment per knowl, pre-rendered at build time

* Store each definition as a file with a stable **identifier** (ID).
  Example ID scheme: `def.vector_space`, `def.module`, `def.ring`.

* Build step produces:

  * a glossary page at `/glossary/def.vector_space/` (full page),
  * a fragment at `/knowls/def.vector_space.html` (the inline insertion payload).

**Reason**: this gives you:

* stable URLs (good for sharing),
* progressive enhancement fallback (no-JS users go to the glossary page),
* cacheability (fragments can be cached by browser/CDN),
* simple authoring (definitions are just Markdown content).

This matches the AIM model “file containing the knowl is just an ordinary html file … include the contents.”

### Alternative: a single JSON database (when you want cross-repo tooling)

You can store knowls as JSON objects `{id,title,html}` and ship one `knowls.json`. This makes linking easy but has downsides:

* initial payload can get large,
* harder to “view source” each knowl as a document,
* caching granularity is worse.

For a blog, per-fragment files are usually better.

---

## Authoring experience (syntax)

You want three simultaneous constraints:

1. easy to type,
2. readable in raw Markdown,
3. produces progressive-enhancement HTML.

### A good generic Markdown-level syntax

Use an inline attribute extension pattern (works in Pandoc/Quarto; can be emulated elsewhere):

```markdown
A **[vector space](/glossary/def.vector_space/){.knowl data-knowl="/knowls/def.vector_space.html"}**
```

Semantics:

* `href` points to the full-page glossary entry (fallback),
* `data-knowl` points to the fragment (JS enhancement),
* `.knowl` class marks triggers.

### Hugo-style (shortcode)

```markdown
A {{< knowl id="def.vector_space" text="vector space" >}} is …
```

Where the shortcode renders the progressive-enhancement anchor.

### Jekyll-style (Liquid include)

```liquid
A {% include knowl.html id="def.vector_space" text="vector space" %} is …
```

### Quarto-style (shortcode)

Quarto supports shortcodes; you can define:

```markdown
A {{< knowl def.vector_space "vector space" >}} is …
```

---

## Nested knowls (policy, not just capability)

AIM’s own example shows nested knowls are possible (a knowl contains another knowl link).

Your “anti-rabbit-hole” constraint means you should treat nesting as a *controlled resource*.

A practical policy:

* Define the **dependency depth** (d\in\mathbb{N}) of a knowl expansion as:

  * (d=0) for terms in the main article,
  * when a knowl expands inside another knowl, depth increases by 1.

* Enforce a hard cap (d\le 1) (or (d\le 2) if you’re confident).
  If a trigger is clicked at depth (>d_{\max}), replace it with a normal navigation to the glossary page.

This keeps “axioms available” while preventing runaway transclusion trees.

---

## Math inside knowls (MathJax/KaTeX timing)

### MathJax fact you rely on

MathJax works by scanning the page for math delimiters (e.g. `$$…$$`) and then converting to rendered output. Its docs explicitly describe a two-stage process: find math in the page, then convert and display it.

### Consequence for knowls

If you inject new HTML after page load, you must trigger *a re-typeset* on the injected container.

* **MathJax v3**: `MathJax.typesetPromise([container])`
* **MathJax v2**: queue a typeset on that container (`MathJax.Hub.Queue([...])`)

### KaTeX vs MathJax trade

* **KaTeX**: faster, but narrower TeX coverage (relevant when you want “down to axioms” but also want AMS environments and macros).
* **MathJax**: broader TeX/AMS coverage, better for research-level writing.

Quarto exposes this choice explicitly via `html-math-method` supporting `mathjax` or `katex` (and other methods).

---

## UX and accessibility recommendations

### Trigger behavior

* **Click/tap, not hover**. Hover fails on touch devices and creates accidental expansions.
* The trigger should be keyboard-activatable (Enter/Space).

### Placement

Insert the knowl body **after the nearest block container** that contains the trigger:

* if the trigger is in a `<p>`, insert after that `<p>`;
* if in a `<li>`, insert inside the `<li>` but after its main inline content.

AIM’s docs warn that poor HTML structure (e.g. not wrapping paragraphs) can cause placement issues.

### Multiple open knowls

Default: allow multiple open, but provide:

* a “close” control on each knowl,
* optionally “close siblings” behavior inside the same paragraph/list item to reduce clutter.

### Accessibility attributes (minimum viable)

* `aria-expanded="true|false"` on the trigger,
* `aria-controls="ID_OF_PANEL"` linking trigger ↔ panel,
* panel has `role="region"` and an `aria-label` or `aria-labelledby`.

---

## Prototype: progressive-enhancement knowls (vanilla JS + MathJax hook)

### HTML emitted by your shortcode/include

```html
<a class="knowl"
   href="/glossary/def.vector_space/"
   data-knowl="/knowls/def.vector_space.html"
   role="button"
   aria-expanded="false">
  vector space
</a>
```

### CSS sketch (minimal)

```css
.knowl-output {
  margin: 0.5rem 0 0.75rem 0;
  padding: 0.75rem 1rem;
  border-left: 3px solid #888;
  background: #f7f7f7;
}
.knowl-close {
  float: right;
  font-size: 0.9em;
}
```

### JavaScript (event delegation + caching + MathJax)

```html
<script>
(() => {
  const cache = new Map(); // url -> html string

  function nearestBlock(el) {
    // Find a reasonable insertion anchor for inline triggers.
    return el.closest('p, li, dd, dt, blockquote, div, section') || el;
  }

  async function fetchFragment(url) {
    if (cache.has(url)) return cache.get(url);
    const res = await fetch(url, { credentials: 'same-origin' });
    if (!res.ok) throw new Error(`knowl fetch failed: ${res.status} ${url}`);
    const html = await res.text();
    cache.set(url, html);
    return html;
  }

  async function typesetMath(container) {
    // MathJax v3
    if (window.MathJax && MathJax.typesetPromise) {
      await MathJax.typesetPromise([container]);
    }
    // KaTeX auto-render could be added here if you use it.
  }

  function makePanel(trigger) {
    const panel = document.createElement('div');
    panel.className = 'knowl-output';
    panel.hidden = true;

    const close = document.createElement('button');
    close.type = 'button';
    close.className = 'knowl-close';
    close.textContent = 'close';
    close.addEventListener('click', () => {
      panel.hidden = true;
      trigger.setAttribute('aria-expanded', 'false');
    });

    panel.appendChild(close);
    const body = document.createElement('div');
    body.className = 'knowl-body';
    panel.appendChild(body);

    return { panel, body };
  }

  document.addEventListener('click', async (e) => {
    const a = e.target.closest('a.knowl[data-knowl]');
    if (!a) return;

    // Progressive enhancement: still allow open-in-new-tab, etc.
    // But for normal click, intercept.
    if (e.defaultPrevented) return;
    if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;

    e.preventDefault();

    const url = a.getAttribute('data-knowl');
    if (!url) return;

    // Attach (or reuse) panel
    let panel = a._knowlPanel;
    let body  = a._knowlBody;
    if (!panel) {
      const obj = makePanel(a);
      panel = obj.panel;
      body  = obj.body;
      a._knowlPanel = panel;
      a._knowlBody  = body;

      const block = nearestBlock(a);
      block.insertAdjacentElement('afterend', panel);
    }

    const isOpen = !panel.hidden;
    if (isOpen) {
      panel.hidden = true;
      a.setAttribute('aria-expanded', 'false');
      return;
    }

    // Open it
    a.setAttribute('aria-expanded', 'true');
    panel.hidden = false;
    body.innerHTML = '<em>Loading…</em>';

    try {
      const html = await fetchFragment(url);
      body.innerHTML = html;
      await typesetMath(panel);
    } catch (err) {
      body.innerHTML = `<strong>Error loading knowl.</strong>`;
      // Fall back to navigation if desired:
      // window.location.href = a.href;
      console.error(err);
    }
  });
})();
</script>
```

This reproduces the core AIM/LMFDB behavioral contract (click → load fragment → insert locally).
It also bakes in your anti-pattern constraints: progressive enhancement, depth control (addable), and explicit insertion policy.

---

## Content management strategy for a definition library

### IDs and version control

* Choose an ID namespace you can live with for years, e.g.
  [
  \texttt{def.<topic>.<concept>}
  ]
  Example: `def.linear_algebra.vector_space`.

* Store each knowl source in a folder like:

  ```
  knowls/
    def.linear_algebra.vector_space.md
    def.linear_algebra.linear_map.md
    ...
  ```

* Put everything in git. Your “definition library” becomes a normal, reviewable text corpus.

### “Axioms all the way down” without explosion

Use a **two-tier structure inside each definition**:

1. **Surface definition**: the minimal axioms/bullets.
2. **Prerequisite unpacking**: a *bounded* list of prerequisite terms, each with its own knowl.

Then enforce (d_{\max}) nesting depth as described earlier.

### Cross-referencing

* Every knowl should be able to link to:

  * a full-page glossary entry,
  * related knowls (“See also” list),
  * references (book/theorem numbers).

But keep the knowl body **context-neutral** as AIM recommends: it should “make sense” without assuming the current article context.

---

# Commenting systems for a math blog (static site + LaTeX)

## The key constraint: where does math rendering happen?

* If comments are hosted on GitHub (giscus/utterances), **GitHub** does the Markdown + math rendering in their UI (and the widget embeds that). That gives you math support with no extra work in your site JS, but it forces a GitHub account.

* If comments are hosted by a self-hosted engine (Remark42/Isso/Commento/etc.), you control the DOM, so you can run MathJax on the comments container after comments load. MathJax is explicitly designed to scan a page for math delimiters and then typeset them.

---

## Comparison table (your candidates + one additional serious contender)

| System                         | Hosting model                          | Who can comment                                                                                  | Math in comments                                                                                     | Moderation / spam                                                               | Privacy notes                      |
| ------------------------------ | -------------------------------------- | ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ---------------------------------- |
| **giscus**                     | GitHub Discussions-backed widget       | Requires GitHub (it’s “powered by GitHub Discussions”)                                           | Works if GitHub supports math in Discussions (generally yes; some edge-case bugs exist historically) | GitHub moderation tools; plus repo-level controls                               | Tied to GitHub tracking model      |
| **utterances**                 | GitHub Issues-backed widget            | Requires GitHub OAuth authorization to post                                                      | Same idea: GitHub renders                                                                            | Issue moderation; repo workflow                                                 | Tied to GitHub                     |
| **Remark42**                   | Self-hosted comment engine             | Depends on configured auth; you host it                                                          | Not “native”, but you can run MathJax on rendered comments container                                 | Built-in moderation features (per project docs; verify in your deployment plan) | Marketed as “doesn’t spy on users” |
| **Isso**                       | Self-hosted (lightweight)              | Typically no global account needed (name/email style); depends on setup (not fully sourced here) | Usually needs MathJax injection                                                                      | Basic moderation                                                                | Good privacy if self-hosted        |
| **Commento / forks**           | Self-hosted or hosted service variants | Varies by fork/service                                                                           | Some forks add KaTeX/MathJax support (anecdotal)                                                     | Varies                                                                          | Varies                             |
| **Talkyard** (add’l contender) | Open-source + hosted option            | Account model depends on deployment; supports manual review policies                             | Would still require MathJax/KaTeX integration unless built-in                                        | Explicit anti-spam and moderation knobs described                               | Claims “no ads, no tracking”       |
| **Disqus**                     | Third-party SaaS                       | Easy for users                                                                                   | No official MathJax setting; people have asked for it                                                | Good moderation tools                                                           | Tracking/ads concerns              |

### Practical recommendation

**If “no GitHub account required” is truly a hard constraint**: the best match among your list is **Remark42** (self-hosted + privacy-oriented).
Then add MathJax on your page and, after the Remark42 widget renders or updates, call MathJax typesetting on the comment container. (Exact hook depends on Remark42 embed API; you’ll implement a “rerun typeset when new nodes appear” policy, e.g. with a `MutationObserver`.)

**If you can accept GitHub accounts**: **giscus** is the lowest-effort way to get math-capable comments on a static site, since it is explicitly “powered by GitHub Discussions” and widely embedded in static documentation themes.
But be explicit in your UX: “Commenting requires a GitHub account.”

**If you want a strong privacy story with a smoother non-GitHub login UX**: evaluate **Talkyard** as well; it is open source and emphasizes no tracking plus moderation controls.
(Math support still needs verification/integration planning in your specific theme.)

### Examples (math-adjacent evidence available in retrieved sources)

* A post about writing math notes with GitHub Discussions mentions switching between MathJax/KaTeX and between giscus and a Commento++ fork, and notes GitHub added math support in 2022.
* MkDocs Material documents a giscus-based setup (static site embedding pattern).
* Jupyter Book documents Utterances as GitHub-Issues-based and requiring a GitHub account.

---

# Static site generators for a math blog on GitHub Pages

## The math-rendering axis (what you’re actually choosing)

Let (M) be your math rendering method. For HTML output, many systems reduce to choosing (M\in{\text{MathJax},\text{KaTeX}}) and wiring it into templates.

Quarto makes this explicit as an HTML format option `html-math-method` supporting `mathjax` or `katex` (and other methods).

## Comparison (focused on your constraints)

Scores are relative (1=weak, 5=strong) for your particular use-case: Markdown authoring + math + custom JS (knowls) + GH Pages deploy.

| Generator                 |                                     Math support out of box |                                Extensibility for knowls |     Setup friction | GH Pages notes                                      |
| ------------------------- | ----------------------------------------------------------: | ------------------------------------------------------: | -----------------: | --------------------------------------------------- |
| **Quarto**                | 5 (explicit math method selection; MathJax/KaTeX supported) |             4 (shortcodes + template injection typical) |                3–4 | Deployable via Actions; (not directly sourced here) |
| **Jekyll**                |             3–4 (kramdown + typical MathJax/KaTeX patterns) | 3 (Liquid includes; plugins limited on native GH Pages) |                  3 | Native GH Pages support widely noted                |
| **Hugo**                  |                3 (usually manual MathJax/KaTeX integration) |                           5 (shortcodes + full control) |                  3 | Easy via Actions; fast builds                       |
| **Eleventy (11ty)**       |                      3 (Markdown-it plugins; manual wiring) |                                                       5 |                  3 | Actions deploy                                      |
| **Astro**                 |            3 (MDX/remark plugins; more frontend complexity) |                                                       5 | 2–3 (more tooling) | Actions deploy                                      |
| **MkDocs / Jupyter Book** |                       4 (math is common; doc-site oriented) |                                                     3–4 |                  4 | Actions deploy                                      |

### Recommendation

* **Best “math-first” default**: **Quarto**. It exposes math rendering as a first-class output option (`html-math-method: mathjax|katex`) and is designed for technical/scientific writing.
  This aligns with your “axioms-on-demand” idea because you’ll likely want consistent theorem environments, cross-references, and robust math rendering.

* **Best “maximal control + simple pipeline”**: **Hugo** with a custom knowl shortcode. Hugo doesn’t “natively” solve math, but integrating MathJax is straightforward in practice and well documented in community tutorials.

* **If you want to stay closest to GitHub Pages defaults**: **Jekyll**, but assume you’ll eventually move builds to GitHub Actions if you need non-whitelisted plugins. Jekyll’s popularity on GitHub Pages is widely noted.

### Example math-focused resources (within retrieved sources)

* Quarto documentation pages explicitly describe math rendering configuration (good proxy for capability).
* A math-focused Hugo tutorial page shows MathJax integration patterns.
* A Jekyll + KaTeX writeup shows a practical math blogging setup.

(I did not retrieve a clean “showcase list of math blogs per SSG” within the available sources; the items above are at least concrete, math-relevant deployments/documentation.)

---

## Summary deliverables (mapped to your requested outputs)

1. **Summary of nLab and AMS implement knowls**

* nLab: hyperlink-based definitions (as per your description; not independently sourced here).
* “AMS knowls”: the primary documentation retrieved attributes knowls to **AIM** (not AMS) and provides the concrete knowl.js + knowlstyle.css + `knowl="…"` syntax.
  I did not find a distinct AMS-maintained knowl library in the retrieved sources.

2. **Technical recommendation for knowls**

* Build a **custom vanilla-JS** knowl system with **progressive enhancement**.
* Store each definition as **one build-generated HTML fragment** + one full glossary page.
* Enforce a nesting-depth cap (d\le d_{\max}) to avoid rabbit holes.

3. **Proposed authoring syntax**

* Quarto/Pandoc: `[vector space](/glossary/def.vector_space/){.knowl data-knowl="/knowls/def.vector_space.html"}`
* Hugo: `{{< knowl id="def.vector_space" text="vector space" >}}`
* Jekyll: `{% include knowl.html id="def.vector_space" text="vector space" %}`

4. **Prototype code snippet**

* Provided above (HTML + CSS + vanilla JS + MathJax hook).

5. **Content management strategy**

* Definitions live as Markdown files with stable IDs; build produces fragment + glossary page.
* Enforce context-neutrality and bounded nesting.
* Keep everything in git; auto-generate an index/glossary page and optionally a dependency graph (IDs as nodes, “uses” edges) for maintenance.
