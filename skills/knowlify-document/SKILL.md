---
name: knowlify-document
description: Integrate a mathematical document or conversation into Knowlpedia by inventorying its terminology, reusing existing knowls, authoring missing definitions, inserting expandable semantic links without changing the source text, building an index of additions, and validating the compiled interactive result. Use for requests to “knowlify” notes, transcripts, papers, lessons, or Markdown/LaTeX documents in the Knowlpack-based knowlpedia-content and knowl-system-refactor workspace.
---

# Knowlify Document

Turn a source document into a fidelity-preserving Knowlpack page whose mathematical terms expand inline.

## Workflow

1. Locate the compiler repo and its canonical content package. Read the package and compiler guidance before editing. Never edit generated output or importer scratch data.
2. Check repository status and branch. Preserve unrelated changes. Put canonical content work on a feature branch when the content repository is on a live branch.
3. Save an untouched Markdown/LaTeX source copy. Treat it as the fidelity oracle.
4. Extract a glossary in three layers:
   - concepts explicitly defined or central to the argument;
   - prerequisites appearing inside those definitions;
   - named examples, constructions, and notation that benefit from expansion.
5. Inventory existing knowls with `scripts/inventory_knowls.py`. Reuse a knowl only when its mathematical setting matches. For example, a smooth principal bundle knowl does not define a torsor on an étale site.
6. Make a coverage table mapping every glossary item to an existing ID or a proposed new ID. Consolidate aliases; do not create duplicate knowls for plurals, notation, or equivalent phrasings.
7. Run a semantic dependency audit before authoring. Give an agent the source document, the proposed knowl set, and the full knowl inventory. Ask it to identify concepts that are required to understand a definition but have no suitable standalone knowl. Rank each candidate `must-have`, `useful`, or `incidental`, cite exact source occurrences, and verify absence by ID, title, aliases, and body search. Read `references/semantic-dependency-review.md` for the protocol.
8. Author the approved missing knowls in small, disjoint batches. Keep the canonical core definition-first and sufficient on its own. Put motivation, examples, equivalent characterizations, interpretation, and warnings under descriptive `##` headings so the compiler can progressively disclose them. Link prerequisites semantically. Prefer a 60–140 word core; allow the complete knowl to grow through focused optional sections.
9. Run `scripts/audit_candidate_links.py` across every authored knowl. This lexical pass finds unlinked phrases whose knowls already exist; it does not decide whether a new knowl should be created. Treat its output as candidates, not automatic edits. Have an independent agent or human mark each high-confidence item `accept`, `reject`, or `defer`, with a reason. Read `references/link-review.md` for the decision policy.
10. Apply only accepted candidates with `scripts/apply_candidate_link_decisions.py`. Preserve the complete JSONL decision ledger beside the knowlification source. Rerun discovery and require no unexplained high-confidence candidates.
11. Rerun the semantic dependency audit on the newly authored knowls. Follow prerequisite edges recursively until no unexplained `must-have` gaps remain. Do not require a knowl for every noun phrase: inline definitions, incidental examples, and ordinary mathematical language may remain unlinked when they are not genuine comprehension dependencies.
12. Audit authored files before building:
   - delimit inline math with `\(...\)` and display math with `\[...\]`;
   - use `[[target/id|visible label]]`, wrapping a whole math label rather than placing a wikilink inside math delimiters;
   - reject raw TeX commands in prose and unresolved targets;
   - distinguish definitions from synthesis theorems or examples through `kind` and title.
13. Create a term map and run `scripts/link_terms.py`. Link every substantive mathematical phrase occurrence in prose, while leaving code and math delimiters intact. Do not link generic words such as “map,” “point,” or “space” unless the local phrase denotes a specific glossary concept.
14. Create a temporary index knowl listing every new definition, grouped pedagogically. Add a second section listing reused pre-existing coverage.
15. Run `scripts/audit_knowlification.py` with the untouched source, the index as an extra document, and `--check-pseudo-math`. Require zero missing targets, zero ordinary-parenthesis math candidates, and exact source fidelity after semantic-link wrappers are stripped.
16. Follow the project contract in `references/knowlpack-project.md` for full build, validation comparison, preview management, HTTP checks, and browser QA.

## Quality Gates

- Preserve the original wording, ordering, headings, code, and LaTeX. Knowlification adds wrappers; it does not silently rewrite the document.
- Verify every new knowl recursively: its own definition may introduce more missing concepts.
- Distinguish link integrity from link recall: zero broken targets does not prove that link-worthy terms were linked.
- Distinguish lexical recall from ontology coverage: a phrase scanner can suggest links to known IDs, but an agent must judge whether an absent prerequisite deserves a new knowl.
- Keep discovery, adjudication, application, and verification separate. Never let a lexical match directly mutate content.
- Treat compiler success as a smoke test. Open the index and transcript in a browser and click representative prose links, math-label links, and nested knowls.
- Measure compiled transcript size and embedded-template count. A document with many distinct targets may become large because the current compiler eagerly embeds direct fragments.
- Report the complete glossary, the new/reused split, validation deltas, source-fidelity result, page size, and final server links.

## Subagent Trials

When the user authorizes subagents, use them as independent authoring/evaluation surfaces:

- Assign disjoint ID batches and prohibit unrelated edits.
- Vary one prompt dimension at a time, such as concise prerequisite-first, axiomatically precise, or intuition-first.
- Inspect raw artifacts rather than trusting summaries.
- Feed concrete failures back through a repair prompt. In particular, search for invalid ordinary-parenthesis math before accepting intuition-first output.
- Normalize style and run one corpus-wide audit after merging all batches.

## Scripts

- `scripts/inventory_knowls.py CONTENT_ROOT [--format json|tsv]`: enumerate IDs, titles, aliases, and paths; fail on malformed front matter or duplicate IDs.
- `scripts/audit_candidate_links.py --content-root CONTENT --scope PATH --output CANDIDATES.jsonl`: scan prose outside protected spans and emit scored missing-link candidates.
- `scripts/apply_candidate_link_decisions.py --content-root CONTENT --candidates CANDIDATES --adjudication REVIEW.json --ledger DECISIONS.jsonl [--apply]`: hash-check, record, and optionally insert accepted wrappers.
- `scripts/link_terms.py --input SOURCE --map MAP.json --frontmatter FRONTMATTER --output DOCUMENT.knowl.md`: add literal, longest-match semantic links while protecting code and LaTeX spans.
- `scripts/audit_knowlification.py --content-root CONTENT --document DOCUMENT --original SOURCE`: validate targets and prove wrapper-only source fidelity.

Read `references/knowlpack-project.md` when operating in the Knowlpedia refactor workspace. Read `references/semantic-dependency-review.md` before searching for missing concepts, and `references/link-review.md` before adjudicating candidate links.
