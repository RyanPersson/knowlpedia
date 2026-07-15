This is a solved problem in the static site ecosystem, but the "default" configuration for most Scientific SSGs (like Quarto) is still client-side rendering because it is easier to set up.

To eliminate the "flash of unstyled math" (layout shift) and rendering delay, you must move the rendering logic from the **Browser** to the **Build Server**.

### Executive Summary: Recommended Approach

**Use Build-time KaTeX Pre-rendering.**
This is the industry standard for high-performance math blogs. It converts LaTeX to static HTML/CSS during the build.

* **Performance:** Zero layout shift. Math appears instantly with the rest of the text.
* **Overhead:** Zero client-side JavaScript execution for math.
* **Tooling:** `rehype-katex` (Node/JS ecosystem) or `jekyll-katex` (Ruby ecosystem).

---

### 1. Comparison of Pre-rendering Approaches

| Feature | **Build-time KaTeX** (Recommended) | **Build-time MathJax (SVG)** | **Native MathML** |
| --- | --- | --- | --- |
| **Output** | Static HTML + CSS | Inline `<svg>` tags | Native `<math>` tags |
| **Load Speed** | Instant (HTML) | Instant (SVG) | Instant |
| **File Size** | Low (uses shared CSS font) | High (path data repeated per eq) | Very Low |
| **Fidelity** | High (High-quality fonts) | Perfect (Vector paths) | Variable (Browser dependent) |
| **Copy/Paste** | Good (with extensions) | **Poor** (requires workarounds) | Good |
| **Complexity** | Medium (Requires Node/Ruby plugin) | High (Complex Node setup) | Low (Config change) |

**Why not MathJax SSR?**
MathJax server-side rendering (via `mathjax-full`) is significantly slower (10x-100x) than KaTeX during the build process. For a blog with thousands of equations, this increases build times from seconds to minutes. Additionally, MathJax SVG output bloats the HTML file size because it embeds path data for every symbol, whereas KaTeX reuses a single font file.

**Why not Native MathML?**
While browser support (Chrome 109+, Firefox, Safari) is finally "good enough" in 2025, styling inconsistencies remain. KaTeX HTML/CSS guarantees pixel-perfect consistency across all browsers.

---

### 2. SSG Support & Recommendations

You asked about Quarto, Hugo, and Jekyll. Here is how they handle pre-rendering:

#### **Quarto** (Current Status: **Misconception**)

* **Reality:** Quarto **does not** pre-render KaTeX/MathJax HTML by default. It relies on Pandoc, and Pandoc's `html-math-method: katex` configuration simply injects the *client-side* JS script tags.
* **The Fix:** You can set `html-math-method: mathml`. This forces Pandoc to emit purely static `<math>` tags. This is the fastest "no-code" solution but sacrifices typographic control.
* **For KaTeX HTML:** You would need a post-processing script (using `rehype`) to parse Quarto's HTML output and render the math before deployment.

#### **Jekyll** (Strong Candidate)

* **Approach:** Use the `jekyll-katex` gem.
* **Workflow:** In your liquid templates or markdown, the plugin intercepts the math blocks and renders them to HTML during `jekyll build`.
* **Pros:** Native integration, very stable.
* **Cons:** Ruby dependency (slows down builds if you have extensive other plugins).

#### **Hugo** (Fastest Build, Hardest Config)

* **Approach:** Hugo does not natively pre-render math. You must use a "Goldmark" markdown extension (requires Go knowledge to implement) OR a post-processing step.
* **Workflow:**
1. Build site with Hugo (`hugo`).
2. Run a Node.js script over the `public/` directory using `rehype-katex` to render math in the HTML files.


* **Pros:** Extremely fast site generation.

#### **Modern JS/TS Stack (Astro/Next.js)**

* If you are willing to leave Jekyll/Hugo, **Astro** is currently the best-in-class for this. It uses `remark-math` and `rehype-katex` natively in its config file. It is built for exactly this "ship zero JS" use case.

---

### 3. Technical Answers

**1. What's the rendering pipeline?**
Markdown Source `$$x^2$$`  AST (Abstract Syntax Tree)  Math Node Detection  Pass to KaTeX Library  Replace Node with `<span class="katex">...</span>` HTML string  Write to HTML file.

**2. File size impact?**

* **KaTeX:** Adds ~50KB (gzipped) for the CSS/Fonts (loaded once and cached). The HTML increase per equation is negligible (~300 bytes).
* **SVG:** Adds ~1-3KB *per equation* (no caching). A post with 50 equations could be 150KB larger.

**3. Can knowls contain pre-rendered math?**
**Yes.** This is a major advantage. If your knowls fetch HTML fragments (via AJAX or HTMX), that HTML will contain the pre-rendered static tags.

* *Result:* The knowl pops up instantly with the math visible. No need to trigger `MathJax.typeset()` or `renderMathInElement()` after the popup opens.

**4. Copy-paste behavior?**
KaTeX includes a "Copy-tex" extension. You can configure it so that when a user selects the rendered equation and hits Ctrl+C, it copies the original LaTeX source code (`\int x dx`) instead of the visual text. This is handled via a hidden MathML block or CSS magic.

---

### 4. Recommendation for Your Stack

If your priority is **mathematical fidelity** and **rigorous architecture**:

**Option A: The "Modern Standard" (Astro)**
Migrate to Astro. It treats markdown and math pre-rendering as first-class citizens.

* **Config:**
```javascript
// astro.config.mjs
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

export default defineConfig({
  markdown: {
    remarkPlugins: [remarkMath],
    rehypePlugins: [rehypeKatex] // This runs at build time!
  }
});

```



**Option B: The "Scientific Standard" (Quarto + MathML)**
Stick with Quarto but switch to MathML.

* **Config:** `_quarto.yml`
```yaml
format:
  html:
    html-math-method: mathml

```


* **Trade-off:** You lose the specific font rendering of Computer Modern (unless you load a web font manually), but it requires zero maintenance.

**Option C: The "Hacker" Approach (Hugo + Post-process)**
Use Hugo for speed, and a 20-line Node script to render the math after the build. This gives you the speed of Hugo and the quality of KaTeX.

### Next Step

Which direction interests you?

1. **Astro:** I can provide a `package.json` and config to spin up a prototype.
2. **Quarto:** I can show you how to inject the Computer Modern font so the `mathml` output looks like LaTeX.
3. **Hugo:** I can write the `post-build.js` script for you.