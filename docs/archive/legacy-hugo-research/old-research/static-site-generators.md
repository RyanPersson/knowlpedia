# Research Task: Static Site Generators for Math Blogs

## Objective
Identify the best static site generator for a mathematics blog hosted on GitHub Pages.

## Critical Requirements
1. **Native or excellent LaTeX/MathJax/KaTeX support**
   - Inline math with `$...$` syntax
   - Display math with `$$...$$` syntax
   - Should render in preview, not just production

2. **Markdown-based content authoring**

3. **Extensibility for custom features**
   - Must be able to add custom JavaScript (for knowls)
   - Custom CSS/styling
   - Potential plugin architecture

4. **GitHub Pages compatible**
   - Can deploy via GitHub Actions or native GH Pages build

## Candidates to Research

### Jekyll
- Native GitHub Pages support
- Look for: math plugins, theme ecosystem, ease of customization
- Check: kramdown math support, mathjax integration examples

### Hugo
- Very fast builds
- Look for: math shortcodes, theme options
- Check: goldmark extensions, custom shortcode capability

### Quarto
- Built for scientific/technical publishing
- Native math support expected
- Check: GitHub Pages deployment, customization options, learning curve

### Eleventy (11ty)
- Highly flexible
- Look for: markdown-it plugins for math
- Check: plugin ecosystem, community examples

### Astro
- Modern, component-based
- Look for: MDX support with math, extensibility

### Others
- Docusaurus (if relevant)
- MkDocs (usually for docs, but worth checking)
- Zola (Rust-based)

## Questions to Answer

1. Which generator has the smoothest out-of-box math experience?
2. Which is most extensible for custom JS features like knowls?
3. Build complexity / local development experience?
4. Are there existing math-focused blog templates/themes?
5. Community size / likelihood of long-term maintenance?

## Deliverable
Summary comparison table with recommendations, including:
- Math support quality (1-5)
- Extensibility (1-5)
- Ease of setup (1-5)
- GitHub Pages compatibility notes
- Links to example math blogs using each platform
