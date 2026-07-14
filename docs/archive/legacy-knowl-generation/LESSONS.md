# Lessons from the legacy experiments

## Durable observations worth retesting

- Separate enumeration, dependency analysis, authoring, cross-linking, and review. Combining them in one large generation prompt made omissions harder to see.
- Build a deterministic title/alias index before asking an agent to link content.
- Prefer the longest specific concept over a contained generic concept.
- Link a dependency at its first pedagogically useful introduction, not every occurrence.
- Suppress self-links and protect math, code, existing links, and metadata from lexical insertion.
- Treat ambiguous aliases as review candidates rather than guesses.
- Weave links into prose; dedicated “Related knowls” sections became repetitive and less useful.
- Structural validation and mathematical review answer different questions. Both are required.
- Small independent batches are easier to inspect and repair than large monolithic outputs.
- Persist review decisions. Otherwise agents repeatedly rediscover the same false positives.

## Findings that were useful but incomplete

- The old cross-linking pass told agents to notice missing links, but it did not first generate an exhaustive candidate ledger. This allowed omissions such as unlinked “sheaf” and “schemes” to pass review.
- The old index/alias tools resolved supplied terms, but did not scan prose to discover which terms had never been supplied.
- Grep-based anti-pattern checks caught known formatting failures but could not evaluate link appropriateness or missing links.
- Spot-checking 5–10 knowls was cheap, but did not provide batch-wide coverage evidence.

## Superseded or contradictory assumptions

- Earlier guidance recommended 20–25 slugs per batch; later production notes found roughly 4–6 more reliable. Current models should be benchmarked rather than inheriting either number.
- Some v1 instructions encouraged proof sketches; v2 prohibited them after they became filler. The current schema can represent proofs separately, so content type should drive the decision.
- Some documents required 2–3 examples in every definition; later prompts made examples conditional on pedagogical value.
- Oracle CLI, Chrome remote debugging, brittle log parsers, fixed section maps, and Hugo shortcode repair rules are implementation-era details.
- Timing and quality claims tied to older model versions are not forecasts for current subagents.

## Current hypothesis

Use deterministic code for high-recall candidate discovery and integrity checks. Use capable subagents for context-sensitive accept/reject decisions and mathematical review. Keep discovery, adjudication, application, and verification as separate auditable stages.

The topology v1/v2/v3 snapshot is useful for testing this hypothesis because the three generations cover essentially the same 95-term scope. Historical aggregate counts were approximately:

| Version | Words | Knowl links | Proof headings | Example sections |
| --- | ---: | ---: | ---: | ---: |
| v1 | 13,915 | 461 | 32 | 84 |
| v2 | 11,400 | 443 | 0 | 58 |
| v3 | 10,484 | 455 | 0 | 35 |

These counts measure output shape, not mathematical correctness.
