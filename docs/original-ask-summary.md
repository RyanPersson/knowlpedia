# Original Ask Summary

Date captured: 2026-06-30

## Refactor 1: Next-Generation Knowl System

The desired direction is a partial refactor of the existing Knowlpedia system
into a richer, possibly separate project.

Core ideas:

- Move from a massive jumble of markdown files toward a more structured source
  model.
- Consider an actual database for performance, but weigh that against the goal
  of broad compatibility with GitHub Pages and static school webpages.
- Keep knowls minimal and axiomatic at their core.
- Give each knowl a full page.
- Let additional data unfold in-place, recursively, the same way current knowls
  fold and unfold.
- Eventually create lecture notes in this format.
- Support foldable proofs and subproofs.
- On a full knowl page, support unfoldable subsections such as:
  - exhaustive known examples
  - category-theoretic definitions, when applicable
  - subset and superset relationships
  - related objects, sets, and categories
  - TFAE/equivalent characterizations
  - Lean proofs and ordinary LaTeX proofs
- Develop a structured proof format inspired by Leslie Lamport's structured
  proofs.
- Make every proof step link to the axiom, lemma, definition, or prior result it
  uses.
- Allow definitions to expose alternate equivalent definitions, either through
  buttons/switchers or through a standard TFAE section.
- Preserve the ability to open a knowl full page in a tab, while still allowing
  inline expansion.
- Improve the mobile browser experience substantially.

Main architectural tension:

- LMFDB-style inspiration suggests databases can be powerful.
- The open source professor-friendly goal suggests that a mandatory database may
  be the wrong deployment dependency.
- A build-time database/index artifact may offer the performance benefits while
  keeping static publishing viable.

## Refactor 2: Local Live AI Math Workbench

The second project should be separate from the knowl-system refactor.

Desired use case:

- Host a local web app on the current machine or an Optiplex server.
- Expose it on the user's Tailscale network.
- View threads, knowls, and markdown files in real time from a Mac or phone.
- Ask AI agents math questions.
- Have agents answer by writing markdown or knowl-format files.
- Render those files live in the browser.
- Programmatically interlink rendered text to the knowl system.
- Let agents create new knowls as needed.
- Support TikZ diagrams, especially for category theory conversations.

Primary motivation:

- Current chat interfaces do not render TikZ/category-theory diagrams well.
- A Codex-like agent can write TikZ to files.
- A local live renderer can compile and display those diagrams while the user
  discusses them with AI.

## Coordination Request

Create a high-level coordination space where agents can leave notes about:

- what projects exist
- what work is ongoing
- what decisions have been made
- what should be picked up in fresh threads

This should avoid requiring every new agent to rediscover the workspace from
scratch.

