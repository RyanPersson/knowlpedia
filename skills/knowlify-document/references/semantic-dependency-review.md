# Semantic Dependency Review

Use this review to discover concepts that need new knowls. It is deliberately separate from lexical candidate scanning, which can only match phrases against knowls that already exist.

## Inputs

- the untouched source document;
- every knowl authored for the document;
- the complete inventory of knowl IDs, titles, summaries, and aliases;
- the current term map and link-decision ledger.

## Agent task

Read each definition as a learner following its prerequisite links. Identify the first unexplained concept that blocks the definition or a stated equivalent criterion. For each candidate:

1. quote or cite the exact file and occurrence;
2. state why it is a dependency rather than incidental language;
3. search IDs, titles, aliases, summaries, and bodies for an existing semantic match;
4. classify it as `must-have`, `useful`, or `incidental`;
5. recommend a canonical ID and the existing prerequisites the new knowl should link.

Use these classifications:

- `must-have`: part of a definition, hypothesis, construction, or equivalence that the reader cannot reasonably unpack from linked prerequisites;
- `useful`: recurring standard terminology whose local occurrence is already explained enough to proceed;
- `incidental`: ordinary language, a one-off example, notation defined inline, or a concept outside the document's intended prerequisite depth.

## Adjudication

Create all approved `must-have` entries. Add `useful` entries only when they recur, substantially reduce duplicated explanation, or are central to the source's pedagogical goal. Do not create entries merely to maximize link density.

After authoring, repeat the review on the new knowls. Stop when every remaining `must-have` candidate is either linked to an existing knowl, defined inline by design, or recorded as a deliberate boundary with a reason.

For larger clusters, use independent agents on disjoint conceptual regions, then have the lead agent normalize rankings and resolve overlaps. Agents should return evidence and recommendations, not silently create an unbounded dependency tree.
