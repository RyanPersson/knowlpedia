# Research Task: Math Rendering Performance (SSR/Pre-rendering)

## Problem Statement
Client-side MathJax rendering causes noticeable multi-second delays on math-heavy pages. The user has observed this on other math blogs - the page loads, then there's a visible "flash" as LaTeX source transforms into rendered equations.

This is unacceptable UX for a blog that may have very long, equation-dense posts.

## Objective
Research approaches to pre-render or server-side render mathematical notation so pages load with math already rendered.

## Approaches to Investigate

### 1. Build-time Pre-rendering
- Render LaTeX to HTML/SVG/MathML during static site build
- No client-side rendering needed
- Questions:
  - Which tools support this? (remark-math, rehype-katex, etc.)
  - How does it integrate with Jekyll/Hugo/Quarto/etc.?
  - Output format: SVG vs MathML vs HTML+CSS?
  - File size implications?

### 2. KaTeX vs MathJax
- KaTeX is known to be much faster than MathJax
- Can KaTeX be pre-rendered at build time?
- Feature comparison: Does KaTeX support all LaTeX the user might need?
- Are there math features only MathJax supports?

### 3. Server-Side Rendering (for static sites)
- Can MathJax run in Node.js during build?
- mathjax-node, mathjax-node-page packages
- Output formats and trade-offs

### 4. Hybrid Approaches
- Pre-render most math, client-side render edge cases?
- Progressive enhancement strategies
- Lazy loading math on scroll?

### 5. Static Site Generator Support
- Does Quarto pre-render math? (likely yes - scientific focus)
- Hugo math rendering options
- Jekyll plugins for pre-rendered math
- Which SSG makes this easiest?

## Technical Questions

1. What's the actual rendering pipeline for pre-rendered math?
2. File size impact of SVG vs MathML vs HTML output?
3. Accessibility implications of each approach?
4. Can knowls contain pre-rendered math? (important for our use case)
5. Copy-paste behavior: can readers copy equations as LaTeX?
6. How do existing math-heavy static blogs handle this?

## Examples to Study
- Find math blogs with fast load times, inspect their approach
- Quarto documentation sites
- Academic paper hosting sites

## Deliverable
1. Comparison of pre-rendering approaches
2. Recommendation for our SSG choice (may influence main SSG decision)
3. Specific toolchain/plugin recommendations
4. Any gotchas or limitations to be aware of
5. Example config if available
