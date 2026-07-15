## 0. Provenance and terminology (to fix a likely false premise)

A **knowl** (pronounced “knoll”) is a hyperlink-like reference whose target content is **transcluded** (inserted by reference) *into the current page* instead of navigating away. ([American Institute of Mathematics][1])

The earliest sources I found attribute knowls to Harald Schilly and first deployment on **LMFDB** (Aug 2011), with dissemination and a reference implementation published by **AIM** (American Institute of Mathematics), not AMS. ([American Institute of Mathematics][1])
(AMS may use/host content that uses knowls in some contexts, but “AMS created knowls” is not supported by the sources above.)

---

## 1. LMFDB’s model (the “gold standard” you pointed at)

### 1.1 UX contract: inline expansion, dismissible, no page change

LMFDB frames knowls as “hidden knowledge”: a term is visually marked (dotted underline), and clicking expands a box of explanatory text without leaving the page. ([LMFDB][2])

### 1.2 Content contract: glossary-like, consistent definitions, minimal clutter

LMFDB explicitly positions its “knowledge/knowl” layer as a **glossary of technical terms used across pages** so that (i) object pages don’t get cluttered and (ii) definitions remain consistent. ([Springer Link][3])

### 1.3 Information architecture: globally addressable knowls with stable identifiers

LMFDB exposes an entire “Knowledge database” whose entries have identifiers like `mf.slash_action`, `group.pseudo_random_elements`, etc. ([LMFDB][4])

It also maintains documentation about **naming conventions for knowl identifiers and description fields**, with review metadata (status, last editor, history). ([LMFDB][5])

**Takeaway for a static blog:** the key idea is not merely “inline expand/collapse”, but “a separate, addressable definition layer” with stable IDs and editorial discipline (review state, history, cross-references).

---

## 2. nLab’s model (the anti-pattern you want to avoid)

nLab’s navigation model is intentionally “wiki-like”: dense **hyperlinking between pages** is treated as a central feature of the system. ([NCAT Lab][6])

So the contrast is structural:

* **nLab:** definitions are primarily *page destinations* (graph navigation).
* **LMFDB/knowl model:** definitions are primarily *inline transclusions* (local deepening without context switching). ([Springer Link][3])

---

## 3. Existing reusable implementations (what you can actually build on)

### 3.1 AIM’s “Knowlepedia” reference implementation (static-friendly)

AIM provides a “how to put knowls on your own website” guide with the core mechanics:

* include jQuery + `knowl.js` + `knowlstyle.css`
* author a knowl link by writing `knowl="target_file"` instead of `href="…"`
* store the knowl target as a small HTML fragment file (often body-only) ([American Institute of Mathematics][1])

It also states the core design principle as **context independence / context neutrality**: a knowl should be self-contained and not require its embedding context to make sense. ([American Institute of Mathematics][1])

### 3.2 BooksHTML/knowls (packaged knowl assets)

A GitHub-distributed bundle describes knowls exactly as “hyperlinks whose targets open within the current page” and documents the same authoring syntax `<a knowl="target_file">…</a>`, explicitly attributing creation to Harald Schilly and first appearance on LMFDB. ([GitHub][7])

### 3.3 PreTeXt: industrial-scale knowlization (especially relevant for math)

PreTeXt’s documentation treats knowls as a first-class output feature:

* defines “knowl” in the glossary (dotted underline; appears inside current page) ([PreTeXt][8])
* supports “knowlization” switches to “born” many element types as knowls in HTML output ([PreTeXt][9])
* cross-references in HTML are implemented as knowls with an “in-context” link back to the original location ([PreTeXt][10])

**Implication:** if you want the *LMFDB-style discipline at scale* (automatic knowlization, consistent IDs, cross-reference knowls, math-aware behavior), PreTeXt is the closest “already-solved” ecosystem, even if you don’t adopt its XML authoring.

---

## 4. Technical recommendation for a static math blog

### Recommendation: “LMFDB-style IDs + AIM/PreTeXt-style transclusion,” implemented statically

Concretely:

1. **Definitions live in their own namespace** (a folder like `/knowls/`), each with a stable **identifier**.
2. A knowl link in a post is a small inline marker that references that identifier.
3. Clicking the marker **fetches a static HTML fragment** (or pre-rendered Markdown → HTML) and inserts it inline, below the term.
4. After insertion, call MathJax/KaTeX to render any LaTeX inside the inserted fragment.

This matches all your constraints:

* static hosting / GitHub Pages friendly (no server required),
* keeps readers on-page (no rabbit hole),
* definitions can be made axiomatic and layered.

### What to avoid (to satisfy your “anti-pattern” constraints)

* **Unbounded nesting:** allow nesting technically, but impose a policy:

  * depth cap (e.g. 2),
  * or “nested knowls open in-place but collapse siblings,”
  * or “nested knowls redirect to the glossary page for that ID.”
* **Hover-only UI:** use click/tap for mobile + accessibility.
* **Popover tooltips for long math definitions:** they do not scale to axioms/proofs (scrolling, selection, MathJax reflow).

---

## 5. Proposed authoring syntax (practical, generator-agnostic)

You want something that is:

* readable in Markdown source,
* compiles to a simple HTML marker.

Two workable patterns:

### Pattern A (shortcode style; Hugo-like)

Source:

* `{{< knowl id="lin_alg.vector_space" text="vector space" >}}`

Expands to:

* `<button class="knowl" data-knowl="lin_alg.vector_space">vector space</button>`

### Pattern B (wiki-link style; Obsidian-like)

Source:

* `[[knowl:lin_alg.vector_space|vector space]]`

Expands to the same HTML as above.

**Definition storage rule:** `lin_alg.vector_space` resolves to `/knowls/lin_alg.vector_space.html` (or `/knowls/lin_alg/vector_space.html`), mirroring LMFDB’s dot-scoped IDs. ([LMFDB][4])

---

## 6. Prototype (vanilla JS, static fragments, MathJax-aware)

### HTML (in your post)

```html
<p>
A <button class="knowl" data-knowl="lin_alg.vector_space" aria-expanded="false">
  vector space
</button> is …
</p>
```

### Definition file (static): `/knowls/lin_alg.vector_space.html`

```html
<div class="knowl-fragment">
  <div class="knowl-title">Vector space (axioms)</div>
  <ol>
    <li>Underlying set: a set V with an addition + : V×V → V.</li>
    <li>Field: a field 𝔽 with scalar multiplication · : 𝔽×V → V.</li>
    <li>… (axioms) …</li>
  </ol>
  <p>Example: …</p>
  <p>Formula: \( (\lambda+\mu)v = \lambda v + \mu v \).</p>
</div>
```

### JS (load once site-wide)

```html
<script>
(() => {
  const cache = new Map(); // id -> html string

  function knowlPath(id) {
    return `/knowls/${id}.html`;
  }

  function nextKnolBoxId(id) {
    // stable enough for DOM uniqueness; avoids collisions when the same knowl appears many times
    return `knowl-box:${id}:${Math.random().toString(16).slice(2)}`;
  }

  async function fetchKnowl(id) {
    if (cache.has(id)) return cache.get(id);
    const res = await fetch(knowlPath(id), { credentials: "omit" });
    if (!res.ok) throw new Error(`Failed to load knowl ${id}: ${res.status}`);
    const html = await res.text();
    cache.set(id, html);
    return html;
  }

  async function typesetMath(container) {
    // MathJax v3
    if (window.MathJax?.typesetPromise) {
      await window.MathJax.typesetPromise([container]);
      return;
    }
    // KaTeX auto-render (optional)
    if (window.renderMathInElement) {
      window.renderMathInElement(container, {
        delimiters: [
          { left: "$$", right: "$$", display: true },
          { left: "\\(", right: "\\)", display: false },
          { left: "$", right: "$", display: false }
        ]
      });
    }
  }

  function closeBox(button, box) {
    box.remove();
    button.setAttribute("aria-expanded", "false");
    const controls = button.getAttribute("aria-controls");
    if (controls) button.removeAttribute("aria-controls");
  }

  async function toggleKnowl(button) {
    const id = button.dataset.knowl;
    if (!id) return;

    // If next sibling is the box for this button, close it.
    const next = button.parentNode?.querySelector?.(`.knowl-box[data-owner="${button.__knowlOwnerId}"]`);
    if (next) {
      closeBox(button, next);
      return;
    }

    // Create new box
    const ownerId = nextKnolBoxId(id);
    button.__knowlOwnerId = ownerId;

    const box = document.createElement("div");
    box.className = "knowl-box";
    box.dataset.owner = ownerId;

    const header = document.createElement("div");
    header.className = "knowl-box-header";

    const close = document.createElement("button");
    close.className = "knowl-close";
    close.type = "button";
    close.textContent = "×";
    close.addEventListener("click", () => closeBox(button, box));

    header.appendChild(close);
    box.appendChild(header);

    const body = document.createElement("div");
    body.className = "knowl-box-body";
    body.textContent = "Loading…";
    box.appendChild(body);

    // Insert *immediately after* the button
    button.insertAdjacentElement("afterend", box);

    button.setAttribute("aria-expanded", "true");
    button.setAttribute("aria-controls", ownerId);
    box.id = ownerId;

    try {
      const html = await fetchKnowl(id);
      body.innerHTML = html;
      await typesetMath(body);
    } catch (e) {
      body.textContent = String(e);
    }
  }

  // Event delegation so knowls inserted inside knowls also work.
  document.addEventListener("click", (evt) => {
    const button = evt.target.closest?.(".knowl");
    if (!button) return;
    evt.preventDefault();
    toggleKnowl(button);
  });
})();
</script>
```

### Minimal CSS

```html
<style>
.knowl { text-decoration: underline dotted; cursor: pointer; background: none; border: none; padding: 0; font: inherit; }
.knowl-box { margin: 0.6rem 0 0.8rem 0; padding: 0.6rem 0.8rem; border: 1px solid #666; border-radius: 8px; }
.knowl-box-header { display: flex; justify-content: flex-end; }
.knowl-close { background: none; border: none; cursor: pointer; font-size: 1.2rem; line-height: 1; }
.knowl-title { font-weight: 600; margin-bottom: 0.4rem; }
</style>
```

This is the core “static transclusion” mechanism described by AIM (link-like marker + separate fragment file), but implemented without jQuery. ([American Institute of Mathematics][1])

---

## 7. Content management strategy for an axiomatic definition library

### 7.1 Storage format

* Put each knowl in `knowls/<id>.md` (author-friendly), compile to `knowls/<id>.html` (browser-friendly).
* Use front matter:

  * `id: lin_alg.vector_space`
  * `title: Vector space`
  * `depends_on: [set, field, abelian_group, scalar_multiplication]`
  * `status: draft|reviewed`
  * `aliases: [linear space]`

This recreates (statically) the separation LMFDB uses: pages stay clean; the definition layer is centralized and addressable. ([Springer Link][3])

### 7.2 Naming convention (steal the part that works)

Use dot-scoped IDs by subject area (`lin_alg.*`, `top.*`, `cat.*`), matching LMFDB’s practice. ([LMFDB][4])

### 7.3 Editorial workflow (replace “LMFDB review UI” with git)

LMFDB exposes review status, authorship, and edit history per knowl. ([LMFDB][5])
In a static blog you can replicate this with:

* git history as the ground-truth “who/when changed what,”
* front matter `status:` to gate what gets shown,
* CI checks:

  * no missing `depends_on`,
  * no cycles in `depends_on`,
  * max dependency depth (to prevent rabbit holes),
  * lints enforcing “axioms-first” formatting.

### 7.4 Cross-references and “escape hatches”

PreTeXt’s cross-reference knowls include an “in-context” link to jump to the full surrounding material. ([PreTeXt][10])
You can add the same idea statically:

* At the bottom of each knowl, include:

  * “Full discussion: /posts/…#vector-space”
  * “All definitions: /glossary/#lin_alg.vector_space”

That preserves flow *and* gives readers a controlled way to go deeper.

---

## 8. Bottom line decision

If you want the **LMFDB feel** on a static blog with minimal machinery:

* Adopt **LMFDB-style IDs + a dedicated `/knowls/` library**. ([LMFDB][4])
* Implement **AIM-style transclusion** (fragment files + click-to-expand). ([American Institute of Mathematics][1])
* Use MathJax/KaTeX re-typesetting after insertion (required for LaTeX-in-knowl).
* Enforce **context-neutral, axioms-first** knowls (AIM’s stated design principle). ([American Institute of Mathematics][1])

If you want this at *textbook scale*, seriously consider whether you want to author directly in PreTeXt (or at least borrow its conventions), because it already treats knowlization as a systematic publishing concern rather than an ad hoc widget. ([PreTeXt][9])

[1]: https://aimath.org/knowlepedia/ "Better browsing with knowls"
[2]: https://www.lmfdb.org/intro?utm_source=chatgpt.com "LMFDB - Introduction"
[3]: https://link.springer.com/article/10.1007/s10208-016-9306-z?utm_source=chatgpt.com "The L-Functions and Modular Forms Database Project"
[4]: https://www.lmfdb.org/knowledge/?utm_source=chatgpt.com "Knowledge database"
[5]: https://www.lmfdb.org/knowledge/show/doc.knowl.naming_conventions "LMFDB - Naming conventions for knowls (awaiting review)  "
[6]: https://ncatlab.org/nlab/show/writing%2Bin%2Bthe%2BnLab?utm_source=chatgpt.com "nLab writing in the nLab"
[7]: https://github.com/BooksHTML/knowls "GitHub - BooksHTML/knowls: Knowls provide a convenient way to add supplementary material to a web page."
[8]: https://pretextbook.org/doc/guide/html/glossary.html?utm_source=chatgpt.com "Glossary"
[9]: https://pretextbook.org/doc/guide/html/publication-file-online.html "Online (HTML) Options"
[10]: https://pretextbook.org/doc/guide/html/author-faq.html?utm_source=chatgpt.com "Chapter 9 Author FAQ: Frequently Asked Questions"
