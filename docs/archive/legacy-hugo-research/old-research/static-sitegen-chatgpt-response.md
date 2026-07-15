## Terminology needed to interpret the tradeoffs

* **Static site generator (SSG)**: a build tool that takes *source* files (typically Markdown plus templates) and produces a directory of **static assets** (HTML/CSS/JS + images) that can be served without a backend.
* **GitHub Pages**: a hosting product that serves static assets from your repository. If you publish from a branch/folder, GitHub Pages will (by default) run a **Jekyll** build unless you disable it; alternatively you can deploy with a **custom GitHub Actions workflow**. ([GitHub Docs][1])
* **MathJax / KaTeX**: JavaScript libraries that render LaTeX-style math in the browser. KaTeX is typically faster; MathJax typically supports more LaTeX features. ([Squidfunk][2])
* **Preview**: a local dev server that rebuilds and refreshes the browser. For math, “preview renders math” usually means the browser you’re previewing in executes the math pipeline (either pre-rendered at build time or rendered by JS at runtime).

### A critical friction point in your requirements

Requiring **inline math** with `$…$` (not `\(...\)`) is doable everywhere, but it is *not* the default in several ecosystems (because `$` is common in non-math text, and because Markdown parsers may interpret `_` and `*` inside math unless you enable “passthrough”). Hugo’s official math doc explicitly calls out `$...$` as optional and warns about delimiter pitfalls. ([Hugo][3])
So “out-of-box” should be interpreted as: *you can get `$…$` + `$$…$$` working with a documented, standard setup; not necessarily zero config.*

---

## Summary comparison table (scores are for your specific constraints)

**Scale:** 1 = poor / high friction, 5 = excellent / low friction.

| Generator             | Math support quality | Extensibility for knowls/custom JS |                     Ease of setup | GitHub Pages compatibility notes                                             | Example math/technical sites                                                                                                        |
| --------------------- | -------------------: | ---------------------------------: | --------------------------------: | ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Quarto**            |                **5** |                                  4 |                                 4 | First-class GH Pages publishing (`quarto publish …`) and good preview        | Tran Thu Le “Creating a Math Blog with Quarto” ([tran-thu-le.github.io][4])                                                         |
| **Hugo**              |                **5** |                                  4 |                                 4 | Deploy via Actions (typical) or push built files; strong official math story | Hugo math doc (official) ([Hugo][3]); “Writing math with Hugo” ([misha.brukman.net][5])                                             |
| **MkDocs + Material** |                **5** |                                  4 |                               3–4 | Usually Actions deploy; great if your “blog” is actually docs/notes          | Material math reference + `$`/`$$` delimiters ([Squidfunk][2]); MkDocs Material guide example ([Ultimate MkDocs Material Guide][6]) |
| **Docusaurus**        |                    4 |                              **5** |                                 3 | Actions deploy; heavier stack; best if you want MDX/React components         | Official KaTeX support doc ([Docusaurus][7]); Docusaurus KaTeX reference site ([courses.dwf.dev][8])                                |
| **Astro**             |                    4 |                              **5** |                                 3 | Actions deploy; excellent modern DX; math via remark/rehype pipeline         | Astro remark/rehype support ([Astro Documentation][9]); AstroPaper LaTeX post ([astro-paper.pages.dev][10])                         |
| **Eleventy (11ty)**   |                  3–4 |                              **5** |                                 3 | Actions deploy; math via markdown-it plugins or MathJax include              | Eleventy Markdown system ([Eleventy][11]); “An eleventy blog with knitr” (MathJax, `$`/`$$`) ([knitr-11ty.djnavarro.net][12])       |
| **Jekyll**            |                    3 |                                3–4 | **4** (if you accept GH defaults) | Only SSG with “native” Pages build; plugin limits unless you build yourself  | GitHub Pages + Jekyll doc (notes default math config) ([GitHub Docs][13]); Jekyll+MathJax example ([Ben Lansdell][14])              |
| **Zola**              |                  2–3 |                                  4 |                                 4 | Actions deploy; math usually via theme/shortcodes + KaTeX/MathJax            | Zola “even” theme KaTeX toggle ([getzola.org][15]); Zola + KaTeX guide ([louveta.gitlab.io][16])                                    |

---

## Direct answers to your questions

### 1) Smoothest out-of-box math experience

**Quarto** and **Hugo** are the cleanest “math-first blogging” setups right now.

* **Quarto**: Math rendering is a first-class format option (default MathJax; switchable to KaTeX, MathML, etc.). ([Quarto][17])
* **Hugo**: Official documentation tells you how to preserve math delimiters and render either client-side (MathJax/KaTeX) or at build time; it also has a built-in KaTeX-based renderer (`transform.ToMath`). ([Hugo][3])

If your “blog” is closer to a structured notes site (navigation/search), **MkDocs Material** has extremely polished math support including `$…$` and `$$…$$` configuration examples. ([Squidfunk][2])

### 2) Most extensible for custom JS features like knowls

Top tier: **Astro**, **Eleventy**, **Docusaurus**.

* **Astro**: you’re explicitly in the remark/rehype ecosystem; you can add math parsing/rendering via `remark-math` + `rehype-katex` / `rehype-mathjax`. ([Astro Documentation][9])
* **Docusaurus**: official KaTeX support via remark/rehype plugins, plus you can build knowls as MDX/React components if you want deeper integration than “sprinkle JS.” ([Docusaurus][7])
* **Eleventy**: very flexible pipeline; just be careful which KaTeX plugin you pick (there are known vulnerabilities in some older markdown-it KaTeX packages). ([VulnInfo][18])

That said, for **LMFDB-style knowls** (mostly static HTML + a small JS controller), **Quarto/Hugo** are already “extensible enough” and often simpler because they don’t introduce SPA-like navigation concerns.

### 3) Build complexity / local development experience

* **Quarto**: `quarto preview` is explicitly designed to auto-render and refresh the browser. ([Quarto][19])
* **Hugo**: typically the fastest “save → refresh” loop; math requires the passthrough setup and either a math partial or `transform.ToMath`. ([Hugo][3])
* **Astro / Eleventy / Docusaurus**: good dev experience but you’re in Node tooling land (dependency churn, plugin version pinning occasionally matters). Docusaurus has historically required compatible versions of remark/rehype packages. ([Docusaurus][7])
* **Jekyll**: simplest on GitHub Pages *if* you accept GH’s build constraints; local Ruby toolchains can be annoying (less “complex” than Node, but more brittle on some machines).

### 4) Existing math-focused templates/themes

* **Quarto**: built-in blog support is a documented feature of “Quarto websites.” ([Quarto][20])
* **Hugo**: many academic themes exist, and math support is now part of official docs. ([Hugo][3])
* **Zola**: themes like “even” explicitly ship KaTeX support toggles. ([getzola.org][15])
* **MkDocs Material**: not a “blog theme” in the classic sense, but extremely strong for math-heavy notes with nav/search. ([Squidfunk][2])

### 5) Community size / long-term maintenance

What matters most here is: (i) visible recent updates in official docs, and (ii) institutional backing.

* **Quarto** is actively maintained and has official GH Pages publishing docs and preview tooling docs. ([Quarto][21])
* **Hugo** shows active releases and current official documentation for math. ([Hugo][3])
* **Docusaurus** docs are actively updated (and the project is widely used), but the JS ecosystem implies more version management. ([Docusaurus][22])
* **Jekyll** is stable and deeply integrated with GitHub Pages, but GH Pages imposes build constraints unless you use Actions. ([GitHub Docs][13])

---

## GitHub Pages deployment reality check (applies to all generators)

* If you publish directly from a branch/folder, GitHub Pages will run a Jekyll build by default; to use a non-Jekyll SSG, you generally build the site yourself and deploy the output (often via Actions) and/or disable Jekyll with `.nojekyll`. ([GitHub Docs][1])
* GitHub explicitly supports “custom workflows” for Pages, including templates for popular SSGs. ([GitHub Docs][23])

---

## Recommendations (ranked for your stated priorities)

### Recommendation A (default): **Quarto**

Choose Quarto if you want the **least friction** for math-heavy writing + a strong authoring/preview loop + straightforward injection of custom JS/CSS for knowls.

* Math rendering method is a documented option (MathJax default; switchable). ([Quarto][17])
* Preview is explicitly designed for live updates. ([Quarto][19])
* GH Pages publishing is directly supported by Quarto’s docs. ([Quarto][21])

### Recommendation B (close second): **Hugo**

Choose Hugo if you want **very fast builds**, a simple “static HTML” mental model (good for knowls), and you’re willing to do one careful math setup.

* Official math setup preserves `$$…$$` and can be configured for `$…$`. ([Hugo][3])
* You can render math at build time with an embedded KaTeX engine (`transform.ToMath`) if you want minimal client-side JS. ([Hugo][24])

### Recommendation C (if you want docs/notes UX): **MkDocs + Material**

Choose this if you want your “blog” to behave like a **navigable textbook** (sidebar, search, sections) and you’re happy with that UX.

* Material’s math integration is extremely explicit, including `$`/`$$` delimiter configs and the “instant loading” caveat (important for knowls too). ([Squidfunk][2])

### When to pick the others

* **Astro**: pick if you want a modern component model and are comfortable building your own pipeline using remark/rehype (`remark-math`, `rehype-katex`/`rehype-mathjax`). ([Astro Documentation][9])
* **Docusaurus**: pick if you want MDX/React as a core authoring primitive (knowls as components), and accept the heavier framework.
* **Jekyll**: pick only if you strongly value “GitHub Pages builds it for me” and you’re okay with the constraints of that environment.
* **Zola**: pick if you want a simple single-binary SSG and are fine with math via theme/shortcode conventions rather than a standardized, official pipeline.

---

## Example sites (one per platform, all math-capable)

* Jekyll: Ben Lansdell (MathJax + `$`/`$$` on GH Pages)
* Hugo: Misha Brukman (KaTeX/MathJax in Hugo)
* Quarto: Tran Thu Le (“Creating a Math Blog with Quarto”)
* Eleventy: “An eleventy blog with knitr” (MathJax configured for `$`/`$$`)
* Astro: AstroPaper docs post on adding LaTeX (remark/rehype + KaTeX)
* Docusaurus: Course Notes KaTeX reference (Docusaurus-based doc site)
* MkDocs Material: “Ultimate MkDocs Material Guide” math examples
* Zola: “even” theme KaTeX support (plus Zola KaTeX guides)

---

If you want a single “best” choice given your requirements (math-first, Markdown-first, custom JS knowls, GH Pages): **Quarto** is the strongest default, with **Hugo** as the best alternative if you value speed and a lighter toolchain.

[1]: https://docs.github.com/articles/creating-project-pages-manually?utm_source=chatgpt.com "Creating a GitHub Pages site"
[2]: https://squidfunk.github.io/mkdocs-material/reference/math/ "Math - Material for MkDocs"
[3]: https://gohugo.io/content-management/mathematics/ "Mathematics in Markdown"
[4]: https://tran-thu-le.github.io/?utm_source=chatgpt.com "TRAN Thu Le's Blog - Home"
[5]: https://misha.brukman.net/blog/2022/04/writing-math-with-hugo/?utm_source=chatgpt.com "Writing math with Hugo | Misha Brukman"
[6]: https://www.albrittonanalytics.com/features/latex-mathjax-examples/?utm_source=chatgpt.com "LaTeX/MathJax Examples - Ultimate MkDocs Material Guide"
[7]: https://docusaurus.io/docs/2.x/markdown-features/math-equations?utm_source=chatgpt.com "Math Equations"
[8]: https://courses.dwf.dev/docs/reference/docusaurus/katex "KaTeX Reference | Course Notes"
[9]: https://docs.astro.build/en/guides/markdown-content/ "Markdown in Astro | Docs"
[10]: https://astro-paper.pages.dev/posts/how-to-add-latex-equations-in-blog-posts/?utm_source=chatgpt.com "How to add LaTeX Equations in Astro blog posts"
[11]: https://www.11ty.dev/docs/languages/markdown/?utm_source=chatgpt.com "Markdown — Eleventy - 11ty"
[12]: https://knitr-11ty.djnavarro.net/posts/the-blogdown-of-theseus/ "An eleventy blog with knitr"
[13]: https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll "About GitHub Pages and Jekyll - GitHub Docs"
[14]: https://benlansdell.github.io/computing/mathjax/ "MathJax, Jekyll and github pages - Ben Lansdell"
[15]: https://www.getzola.org/themes/even/?utm_source=chatgpt.com "even"
[16]: https://louveta.gitlab.io/blog/katex/?utm_source=chatgpt.com "Adding KaTeX support to zola - Alexandre Louvet - GitLab"
[17]: https://quarto.org/docs/output-formats/html-basics.html?utm_source=chatgpt.com "HTML Basics"
[18]: https://security.snyk.io/package/npm/markdown-it-katex?utm_source=chatgpt.com "markdown-it-katex vulnerabilities"
[19]: https://quarto.org/docs/websites/?utm_source=chatgpt.com "Creating a Website"
[20]: https://quarto.org/docs/websites/website-blog.html?utm_source=chatgpt.com "Creating a Blog"
[21]: https://quarto.org/docs/publishing/github-pages.html?utm_source=chatgpt.com "GitHub Pages"
[22]: https://docusaurus.io/docs/markdown-features/math-equations?utm_source=chatgpt.com "Math Equations"
[23]: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages?utm_source=chatgpt.com "Using custom workflows with GitHub Pages"
[24]: https://gohugo.io/functions/transform/tomath/?utm_source=chatgpt.com "transform.ToMath"
