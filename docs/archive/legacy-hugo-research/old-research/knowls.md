# Research Task: Knowls for Mathematical Writing

## Background
"Knowls" are an innovation from the American Institute of Mathematics (AIM) - clickable inline elements that expand to show additional content (definitions, proofs, references) without navigating away from the page.

## Objective
Research existing knowl implementations and determine the best approach for implementing knowls in a static math blog.

## Reference Implementation: LMFDB

### LMFDB (lmfdb.org) - PRIMARY REFERENCE
- L-functions and Modular Forms Database
- **This is the gold standard for our purposes**
- Study their knowl implementation carefully

### Why LMFDB, NOT nLab
nLab uses hyperlinks for definitions, which leads to:
- "TVTropes failure mode" / combinatorial explosion
- Reader gets lost following link after link
- Destroys readability and focus

LMFDB's approach keeps the reader on the page:
- Definitions expand inline
- No navigation away from content
- Maintains reading flow while providing depth
- Avoids the Wikipedia/nLab rabbit hole problem

### AIM (American Institute of Mathematics)
- Original creators of the knowl concept
- Check: Any open-source implementation?
- Look for: Documentation, design rationale, their own usage

### Anti-patterns to Avoid
- Hyperlink-based definitions (nLab style)
- Anything that takes reader off-page
- Nested knowls that create their own rabbit holes

## Technical Questions

1. **Existing Libraries**
   - Is there a knowl.js or similar library?
   - Any Jekyll/Hugo/Quarto plugins?
   - jQuery vs vanilla JS implementations?

2. **Content Structure**
   - How to store definitions? Separate files? Inline data attributes?
   - Database vs static JSON vs markdown files?
   - How to link terms to their definitions?

3. **Authoring Experience**
   - What's the syntax for marking a term as a knowl?
   - How to author the definition content?
   - Can definitions be nested (knowls within knowls)?

4. **Math in Knowls**
   - Can knowl content contain LaTeX?
   - Rendering timing (when does MathJax process knowl content?)

5. **Implementation Approaches**

   **Option A: Build custom**
   - Simple JS that expands/collapses content
   - Data stored in JSON or as hidden elements
   - Full control, maintenance burden

   **Option B: Adapt existing library**
   - Fork nLab's approach if open source
   - Modify for static site context

   **Option C: Use HTML details/summary**
   - Native HTML5 disclosure widget
   - Style to look inline
   - Simplest, least flexible

   **Option D: Tooltip/popover libraries**
   - Tippy.js, Floating UI, etc.
   - Adapt for longer definition content

## UX Considerations

- Click vs hover to expand?
- Expand inline vs popover vs side panel?
- Multiple knowls open simultaneously?
- Mobile experience?
- Accessibility (screen readers)?

## The Vision (from user)
"Any term that's an axiomatically defined term like 'vector space' - I want the reader to be able to click on the word and a tiny little fold-out section pops out below the word listing the low-level axiomatic description."

Goal: All layers of abstraction collapsible down to axioms. No prerequisite knowledge needed.

## Content Management Questions

- How to build a library of mathematical definitions?
- Start from scratch or leverage existing definition databases?
- Version control for definitions?
- Cross-referencing between definitions?

## Deliverable
1. Summary of how nLab and AMS implement knowls
2. Technical recommendation for implementation approach
3. Proposed syntax for authoring knowls
4. Prototype code snippet (if feasible)
5. Content management strategy for definitions
