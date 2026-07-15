## 0. What you are trying to eliminate

* **Client-side math typesetting**: the browser downloads HTML containing TeX delimiters (e.g. `\( … \)`, `$$ … $$`), then runs a JavaScript “math engine” that **parses TeX**, **builds a DOM (Document Object Model) subtree**, and inserts it into the page. The visible delay/flash is the period between “HTML painted” and “math subtree inserted and laid out”.
* **Pre-rendering / build-time rendering**: the math engine runs **during the site build** (locally or in CI), and the emitted HTML already contains the math markup (MathML / HTML / SVG). The browser only **lays out** what is already there; it does not typeset.

The UX problem you describe is exactly what pre-rendering is meant to solve.

---

## 1. Output formats you can pre-render to

### 1.1 MathML

* **MathML**: an XML vocabulary embedded in HTML via `<math>…</math>` that represents the *structure* of a formula (roughly an abstract syntax tree for math).
* **Browser support**: modern Chromium-based browsers support MathML Core; MDN lists full support in Chrome/Edge starting at version 109. ([MDN Web Docs][1])
* **Performance**: fastest “time-to-first-correct-math” because there is no typesetting JS step; the browser renders `<math>` immediately.
* **Accessibility**: generally strong because MathML is semantic.
* **Gotcha (fonts)**: Chromium can render MathML but may need an explicit math font to look good; people often set a font like STIX Two Math for `math { font-family: … }`. ([Giles Thomas][2])
* **Copy/paste as TeX**: not automatic; you typically need an additional layer (e.g., store original TeX in an attribute and add a copy handler) if you want “copy gives TeX”.

### 1.2 HTML+CSS (KaTeX-style or MathJax “CommonHTML/CHTML”)

* **HTML+CSS math output**: the formula becomes a nested `<span>…</span>` structure styled with CSS and fonts.
* **KaTeX default output**: KaTeX can emit **HTML+MathML together** (`htmlAndMathml`)—HTML for visual rendering plus MathML for accessibility. ([KaTeX][3])
* **Performance**: no client-side parsing/typesetting, but the page can become large (lots of nested spans).
* **Copy/paste as TeX**: KaTeX provides a **copy-tex** extension that makes copying the rendered formula put the original LaTeX on the clipboard (requires small JS, but not typesetting JS). ([KaTeX][4])
* **Gotcha (fonts)**: you must ship the KaTeX or MathJax fonts (or load them) for consistent rendering.

### 1.3 SVG

* **SVG math output**: math becomes an `<svg>…</svg>` graphic (vector).
* **Performance**: no typesetting JS, but SVG output is often verbose (large). ([Stack Overflow][5])
* **Typography**: consistent and self-contained; can avoid webfont issues (MathJax docs note SVG output avoids font-loading constraints). ([MathJax Documentation][6])
* **Accessibility**: not inherently semantic unless you add annotations/alt text.

### 1.4 Raster images (PNG, etc.)

* Generally worst for accessibility and scaling; usually only chosen as a last resort.

---

## 2. Build-time toolchains that actually eliminate client-side MathJax delays

### 2.1 Unified/Remark/Rehype pipeline (best-in-class if you’re in the Node/JS ecosystem)

Key components:

* **remark**: Markdown processor producing an AST (abstract syntax tree).
* **remark-math**: parses `$…$` / `$$…$$` into math nodes. ([GitHub][7])
* **rehype**: HTML processor.
* **rehype-katex**: renders math **at compile time**, producing KaTeX HTML (no client-side typesetting JS needed). ([unified][8])
* **rehype-mathjax**: analogous compile-time rendering using MathJax. ([GitHub][7])

Where this is “native”:

* Docusaurus explicitly instructs `remark-math` + `rehype-katex` for math. ([Docusaurus][9])
* Astro/Eleventy/Next (static export)/etc. can do the same pattern.

**Practical implication**: you can get **KaTeX pre-rendered HTML** (often with embedded MathML for accessibility), *and* you can still add your own JS for knowls without any math rendering delay.

### 2.2 Hugo (as of v0.132.0+) now has first-party server-side KaTeX rendering

This is a major recent change.

* Hugo introduced `transform.ToMath` (new in v0.132.0) which uses an **embedded KaTeX instance** to render TeX to:

  * `mathml` (default, no CSS required),
  * `html`, or
  * `htmlAndMathml` (requires KaTeX CSS). ([Hugo][10])
* Hugo’s **Passthrough extension** can preserve math delimiters (so Markdown doesn’t mangle underscores, etc.) and then a **passthrough render hook** can call `transform.ToMath` at build time. ([Hugo][11])

This is the cleanest “static blog” answer if you want:

* zero client-side math typesetting,
* minimal build complexity (no Node toolchain required),
* and a direct path to knowls (your knowls JS becomes independent from math).

### 2.3 Quarto / Pandoc

Quarto exposes Pandoc’s HTML math methods:

* `mathjax` (client-side),
* `katex` (client-side),
* `mathml` (convert TeX → MathML),
* `gladtex` (post-process to images),
* `webtex` (remote images), etc. ([Quarto][12])

So Quarto can eliminate the MathJax flash **if you choose `mathml`**. ([Quarto][12])

**Trade-off**: the “TeX accepted” is effectively “what Pandoc’s math parser accepts”, which is broad but not literally “all TeX + arbitrary packages”.

### 2.4 Jekyll / kramdown

There are genuinely build-time KaTeX options:

* `kramdown-math-katex` converts TeX math to KaTeX HTML server-side. ([GitHub][13])
* Plugins like `jekyll-katex` advertise compile-time rendering. ([GitHub][14])

**Gotcha**: GitHub Pages’ default Jekyll build restricts plugins; in practice you do your own build via GitHub Actions if you want non-whitelisted plugins.

---

## 3. KaTeX vs MathJax in this specific “SSR/pre-render” context

### 3.1 Feature coverage

* **KaTeX**: fast and SSR-friendly; supports a large subset of TeX/LaTeX; see the KaTeX supported-functions table. ([KaTeX][15])
  Example limitation: `align` environment isn’t supported (KaTeX recommends `aligned`). ([KaTeX][16])
* **MathJax**: broader TeX extension ecosystem; MathJax v3+ is explicitly designed to be faster and easier to use with Node for server-side/preprocessing. ([MathJax Documentation][17])

### 3.2 SSR tooling maturity

* **KaTeX SSR**: extremely straightforward (`renderToString`, or `rehype-katex`, or Hugo `transform.ToMath`). ([unified][8])
* **MathJax SSR**: fully possible, but more configuration-heavy (choose input jax + output jax, manage fonts/CSS). MathJax docs show Node “direct” usage that outputs HTML + the required CSS. ([MathJax Documentation][18])

### 3.3 Copy/paste as TeX

* KaTeX’s **copy-tex** extension is purpose-built for this. ([KaTeX][4])
* MathJax can preserve TeX provenance in attributes in some pipelines (the server-side docs discuss `data-latex` attributes in internal MathML/CHTML), but you’d typically still write your own “copy as TeX” UI if you are not running MathJax client-side. ([MathJax Documentation][18])

---

## 4. Knowls + pre-rendered math (your key integration question)

A **knowl** (in the LMFDB sense) is essentially: click → inject/expand hidden HTML content in-place.

You have two workable architectures:

### 4.1 Knowl content is shipped as pre-rendered HTML fragments (recommended)

* Store each knowl’s body as HTML that already contains:

  * MathML, or
  * KaTeX HTML(+MathML).
* On expansion, you inject the fragment into the DOM. No math engine runs, so there is no flash.

This is easiest with:

* Hugo: render knowl pages/partials and inject.
* Unified pipeline: build knowl fragments through the same remark/rehype pipeline as posts.

### 4.2 Knowl content contains raw TeX, and you typeset on expansion (not recommended for your UX goal)

* You must run KaTeX/MathJax on the injected node, which reintroduces local flashes and performance variance (though smaller than whole-page typesetting).

If you do this anyway, KaTeX “auto-render” is usually the lighter option, but it is still client-side typesetting.

---

## 5. File size + performance trade-offs (qualitative, but decision-relevant)

Let “math-heavy page” mean hundreds–thousands of expressions.

### 5.1 MathML

* Usually the smallest semantic representation.
* Fastest paint of “correct math”.
* Main risk: typography differences across platforms unless you provide a math font. ([Giles Thomas][2])

### 5.2 KaTeX HTML(+MathML)

* Often larger than MathML-only because you carry both:

  * the HTML structure for layout,
  * and MathML for accessibility. ([KaTeX][3])
* Still excellent UX because there is no runtime typesetting.
* You must load KaTeX CSS/fonts (but that is a normal static asset load, not multi-second parsing work).

### 5.3 MathJax SVG

* Often the largest (SVG verbosity is a known issue). ([Stack Overflow][5])
* Self-contained rendering, fewer font problems.

---

## 6. Recommendation for SSG choice (based on “math must be pre-rendered”)

### If you want to stay close to your original candidate set (Jekyll/Hugo/Quarto)

1. **Hugo (strong recommendation now)**
   Reason: first-party build-time KaTeX rendering via `transform.ToMath` (MathML default; `htmlAndMathml` available), using passthrough render hooks. ([Hugo][10])
   This directly targets your “no flash on long posts” requirement with minimal moving parts.

2. **Quarto (good if you accept MathML-only output)**
   Set `html-math-method: mathml` to avoid client-side MathJax. ([Quarto][12])
   Choose Quarto if you also want Pandoc/Quarto-native academic features (citations, crossrefs, multi-format output). Just be aware you’re living inside Pandoc’s math support.

3. **Jekyll (viable, but operationally heavier)**
   Use `kramdown-math-katex` or a KaTeX render plugin to pre-render. ([kramdown.gettalong.org][19])
   But you will almost certainly want to build via GitHub Actions rather than GitHub Pages’ default Jekyll pipeline.

### If you are willing to expand beyond that set

A JS-based SSG with `remark-math` + `rehype-katex` is the most common “modern static math site” pattern because it gives SSR math with very direct control. ([unified][8])

---

## 7. Concrete config/toolchain snippets

### 7.1 Hugo: build-time math (no client-side MathJax)

**`hugo.toml` (enable passthrough delimiters)**

```toml
[markup]
  [markup.goldmark]
    [markup.goldmark.extensions]
      [markup.goldmark.extensions.passthrough]
        enable = true
        [markup.goldmark.extensions.passthrough.delimiters]
          block = [['\\[', '\\]'], ['$$', '$$']]
          inline = [['\\(', '\\)']]
```

This is exactly the documented pattern. ([Hugo][11])

**`layouts/_markup/render-passthrough.html` (render TeX at build time)**

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

Pattern is from Hugo docs. ([Hugo][11])

**Conditionally include KaTeX CSS only on pages that used math** (also documented). ([Hugo][11])

If you want *pure MathML with no CSS*, set `output` to `"mathml"` or omit it (default is `mathml`). ([Hugo][10])

### 7.2 Quarto: force MathML output (no MathJax flash)

```yaml
format:
  html:
    html-math-method: mathml
```

Math methods list (including `mathml`) is in Quarto docs. ([Quarto][12])

### 7.3 Unified pipeline (works in Astro/Eleventy/etc.): compile-time KaTeX

Core fact: `rehype-katex` renders at compile time and removes the need for client-side typesetting JS. ([unified][8])

(Exact wiring differs by SSG, but the plugin pair is stable: `remark-math` + `rehype-katex`.) ([GitHub][7])

---

## 8. Practical “gotchas” to plan for

1. **Macros**

   * Hugo `transform.ToMath` supports a `macros` map; KaTeX also supports macro configuration generally. ([Hugo][10])
     Decide whether you want:
   * per-page macros,
   * site-wide macro dictionary,
   * or a “prelude” file.

2. **Strictness / failure mode**

   * KaTeX can error on unsupported TeX (`throwOnError` / `strict`). Hugo exposes these controls. ([Hugo][10])
     You want a deterministic policy: either fail the build, or render a visible error box.

3. **Equation numbering / labels**

   * KaTeX support here is more limited than “full LaTeX + amsmath” expectations; plan your cross-reference system at the SSG layer (e.g., HTML anchors + your own numbering) rather than assuming `\label/\ref` behaves like LaTeX.

4. **Fonts (especially for MathML-only)**

   * If you go MathML-only for speed, budget time for typography tuning (math font selection). ([Giles Thomas][2])

5. **Knowl injection must not escape HTML**

   * Your knowl loader should insert as HTML (not text) or your pre-rendered math markup will be escaped and displayed literally.

6. **Copy-as-TeX**

   * If you care about this UX, KaTeX’s copy-tex extension is the most direct approach. ([KaTeX][4])
     (It’s small JS and does not reintroduce typesetting delays.)

---

## Bottom line

If the non-negotiable requirement is: **no multi-second delay and no visible “math flash” on long, equation-dense pages**, then you should choose an SSG path where math is emitted as **MathML and/or pre-rendered KaTeX HTML** at build time.

Given current (post-2024) tooling, the simplest high-performance choices are:

* **Hugo v0.132.0+ with passthrough render hooks + `transform.ToMath`** (MathML default; optional KaTeX HTML+MathML). ([Hugo][10])
* **Quarto with `html-math-method: mathml`** if you want Quarto’s academic publishing features and can live within Pandoc’s math parsing. ([Quarto][12])
* **JS SSG + `remark-math` + `rehype-katex`** if you want maximum flexibility and are happy with a Node-based build. ([unified][8])

[1]: https://developer.mozilla.org/en-US/docs/Web/MathML?utm_source=chatgpt.com "MathML - MDN Web Docs - Mozilla"
[2]: https://www.gilesthomas.com/2025/02/mathml-fonts-on-chromium-based-browsers?utm_source=chatgpt.com "Getting MathML to render properly in Chrome, Chromium ..."
[3]: https://katex.org/docs/options.html?utm_source=chatgpt.com "Options"
[4]: https://katex.org/docs/libs?utm_source=chatgpt.com "Extensions & Libraries"
[5]: https://stackoverflow.com/questions/79788241/how-to-render-mathjax-inside-of-an-svg?utm_source=chatgpt.com "How to render MathJax inside of an SVG - javascript"
[6]: https://docs.mathjax.org/en/v3.2/web/hosting.html?utm_source=chatgpt.com "Hosting Your Own Copy of MathJax"
[7]: https://github.com/remarkjs/remark-math?utm_source=chatgpt.com "remark and rehype plugins to support math"
[8]: https://unifiedjs.com/explore/package/rehype-katex/?utm_source=chatgpt.com "rehype-katex - unified"
[9]: https://docusaurus.io/docs/markdown-features/math-equations "Math Equations | Docusaurus"
[10]: https://gohugo.io/functions/transform/tomath/ "transform.ToMath"
[11]: https://gohugo.io/render-hooks/passthrough/ "Passthrough render hooks"
[12]: https://quarto.org/docs/output-formats/html-basics.html "HTML Basics – Quarto"
[13]: https://github.com/kramdown/math-katex?utm_source=chatgpt.com "kramdown math engine for conversion to HTML"
[14]: https://github.com/linjer/jekyll-katex?utm_source=chatgpt.com "linjer/jekyll-katex"
[15]: https://katex.org/docs/supported.html?utm_source=chatgpt.com "Supported Functions · KaTeX"
[16]: https://katex.org/docs/issues?utm_source=chatgpt.com "Common Issues"
[17]: https://docs.mathjax.org/en/v3.0/upgrading/whats-new-3.0.html?utm_source=chatgpt.com "What's New in MathJax v3.0"
[18]: https://docs.mathjax.org/en/v4.0/server/direct.html "Linking to MathJax Directly in Node — MathJax 4.0 documentation"
[19]: https://kramdown.gettalong.org/math_engine/katex.html?utm_source=chatgpt.com "Math Engine KaTeX - Kramdown"
