# Sol refactor: reader and pedagogy design

Date: 2026-07-10

The `sol-refactor` branch turns the static compiler/runtime prototype into a more intentional mathematical reading environment. It preserves the original architectural premise—portable source files compiled to static artifacts—while improving how readers find, open, and learn concepts.

## Product principles

1. **Keep the reader's place.** A linked term opens inline. Full-page navigation remains an ordinary link and works with modified click, context menus, and assistive technology.
2. **Definition first.** The inline core contains the smallest sufficient statement. Motivation, examples, equivalent characterizations, warnings, history, and proofs are progressively disclosed.
3. **Metadata is not prose.** Titles, summaries, and semantic kinds support search, full pages, and assistive technology. Inline expansion does not repeat them around a self-contained core.
4. **Local depth, bounded visual complexity.** Nested knowls remain recursive, but mobile panels stop accumulating indentation and Escape closes only the deepest open panel.
5. **Fast by construction.** Core fragments are static, nearby links are preloaded, optional sections are fetched only when opened inline, and the search index is loaded only when search is requested.
6. **No ornamental delay.** The interface contains no animations or transitions. State changes are immediate.
7. **Accessibility is structural.** Native links and details elements remain primary controls; focus is restored after closing; search is modal and keyboard accessible; touch targets are at least 44 pixels at the mobile breakpoint; foreground colors meet WCAG AA contrast.

## Compiler changes

Single-file knowls now participate in the structured model rather than compiling as one undifferentiated Markdown body.

- Text before the first `##` heading is the canonical core.
- If a file begins with `##`, the first section becomes the core so the inline panel is never empty.
- Later `##` blocks become typed Markdown sections with stable, deduplicated IDs.
- A standalone `**Example:**` or `**Examples:**` block becomes an examples section.
- Document, index, page, and section knowls remain continuous by default; `section_mode = "progressive"` or `section_mode = "continuous"` can override the default.
- Section metadata and fragment URLs are emitted in `registry.json`.
- A compact, on-demand `indexes/search.json` artifact contains titles, aliases, summaries, kinds, domains, and page URLs.
- Warning, remark, and interpretation paragraphs render as semantic callouts.

On the current corpus this exposes 2,257 optional sections across 1,289 of 2,143 knowls without requiring a destructive content migration. The compact search artifact is about 738 KiB and is fetched only when search is opened.

## Runtime changes

- A consistent sticky header provides home, search, and theme controls.
- Search opens with `/` or Command/Ctrl+K and ranks exact title, prefix, alias, ID, and summary matches.
- The global index is collapsed by mathematical area instead of rendering a 2,000-entry wall of text.
- Inline panels behave like inserted mathematical footnotes: the core appears immediately beside a quiet left rule, followed by optional-section labels and one full-page and one collapse control.
- The generic storage kind `knowl` is not shown to readers. Generic full pages also omit the redundant `Definition` heading above a self-contained core.
- Inline controls have no duplicated title, summary, `Explore` label, footer, or second full-page/close action.
- Optional sections load into the existing panel rather than creating a second navigation context.
- Keyboard-opened panels move focus to their close control; closing restores focus to the originating term.
- Escape closes search first, then only the deepest inline knowl.
- TFAE switchers now expose tab and tabpanel semantics.

## Content demonstration

The algebraic-geometry foundation path was edited as a representative pedagogical slice:

- Scheme separates the formal definition, a reading guide, and examples.
- Étale topology separates the cover axiom, intuition, and the field-extension example.
- A torsor on a site puts the definition first, then offers a guiding picture and an explanation of the canonical torsor map.
- Sieve separates the core closure property from generated, pullback, and motivational sections.
- Group scheme separates structural maps, functor-of-points language, actions, and warnings.
- Relative Kähler differentials separates the universal property, concrete presentation, and geometric meaning.
- Borel sigma-algebra keeps only its definition in the inline core; its relation to measurable spaces and examples are separately unfoldable.

## Verification

```bash
make test
make build
make build-content
make check-rendering
make test-ui PREVIEW_URL=http://127.0.0.1:8012
```

The browser smoke test covers search ranking, inline section loading, and mobile overflow. Manual browser checks cover nested panels, focus restoration, the deepest-first Escape behavior, dark/light themes, and representative full pages.
