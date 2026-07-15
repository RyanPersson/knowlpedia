# Math Blog Project Plan

## Vision
Create a mathematics blog where all abstractions can be collapsed down to axioms, making dense mathematical language accessible to mathematicians, AI, and non-experts alike.

## DECIDED ARCHITECTURE

```
Hugo (v0.132+) + Build-time KaTeX (htmlAndMathml) + Custom Knowls + Giscus + Form Submission
```

**See:** `SYNTHESIS.md` for rationale, `IMPLEMENTATION.md` for roadmap.

## Platform
GitHub Pages with Hugo static site generator.

---

## Core Requirements

### 1. Math Typesetting (CRITICAL)
- Inline math expressions (e.g., `$x \in V$`)
- Block/display math (e.g., `$$\int_0^\infty ...$$`)
- Must render properly, not just display raw LaTeX
- MathJax or KaTeX integration

### 2. Knowls (CRITICAL)
- Clickable terms that expand inline to show definitions
- Example: clicking "vector space" reveals the axiomatic definition below the word
- Invented by AMS; see nLab (ncatlab.org) for reference implementation
- Goal: every defined term traces back to axioms
- Need to research: existing implementations, how to build custom, content management for definitions

### 3. Commenting System (IMPORTANT)
- User-friendly for non-GitHub users (many mathematicians don't have accounts)
- Ideally supports LaTeX in comments
- Open source preferred
- Options to research: Giscus, Utterances, Commento, Remark42, Hyvor Talk, others

---

## Open Questions

- [ ] Which static site generator best supports math + is extensible for knowls?
- [ ] Is there an existing knowl plugin/library, or do we need custom JS?
- [ ] What commenting system balances LaTeX support + accessibility?
- [ ] How to structure/manage the knowl definition database?
- [ ] Build process: local preview with math rendering?

---

## Research Tasks
See subdocuments in `/research/` directory:
1. `research/static-site-generators.md` - Framework comparison
2. `research/commenting-systems.md` - Comment system options
3. `research/knowls.md` - Knowl implementation research

---

## Status
**Phase: Architecture Decided → Ready for Implementation**

Next: Begin Phase 1 (Hugo setup + math rendering)
