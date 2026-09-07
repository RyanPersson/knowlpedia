# Missing links and dependency gaps

The goal is to let a reader expand the mathematical ingredients needed to
understand a knowl's minimal core. A phrase match alone is not a reason to add
a link, create a definition, or add a prerequisite edge. Preserve the minimal
statement and its hypotheses; put explanations in expandable sections.

## Stages

1. **Inventory and discovery (implemented).** Run the production corpus audit,
   preserve the baseline counts, and establish a separate linking-review ledger.
   Existing refactor reviews do not count as completed linking reviews.
2. **Calibrate across subjects.** Read candidate-rich and candidate-free knowls
   in algebra, geometry, analysis, probability, and mathematical physics. Review
   at least 20 of each across these subjects. Check target definitions and
   conventions, not just titles. Record rejected matches as well as useful ones
   in review evidence. Revise discovery rules before scaling up.
3. **Link existing definitions.** Prioritize missing links in the core, then
   supporting sections. Review single-word terms and ambiguous titles separately.
   Work in batches of 100 source knowls after calibration. Preserve displayed
   wording, math delimiters, and self-contained definitions. Keep link insertion
   commits separate from mathematical rewrites.
4. **Fill actual definition gaps.** Review recurring unknown phrases and explicit
   reports (starting with Poincaré disk). Search titles, aliases, body text, and
   neighboring definitions before creating anything. Classify each as an existing
   target, missing alias, locally defined notation, distinct missing concept, or
   false positive. Write new knowls only for independently reusable concepts;
   verify hypotheses/conventions and cite mathematical evidence. Link their uses
   in a subsequent batch. Re-run discovery as the vocabulary expands.
5. **Review prerequisite structure.** Ordinary links may point to examples or
   later results. Add prerequisite edges only for genuine defining dependencies.
   Check the DAG after each batch; never remove necessary hypotheses to break a
   cycle. Repair circular exposition at the definition boundary.
6. **Validate coverage.** Re-run both production and development audits and
   compiler validation. Inspect rendered inline cores and expanded sections.
   Sample knowls with no findings to expose blind spots, including notation-heavy
   definitions. Finish only after every eligible knowl has a current linking
   review or an explicitly recorded blocker; a small candidate count is not proof
   of completeness.

## Run discovery

From the application repository:

```sh
.venv/bin/python scripts/audit_missing_links.py \
  --content-package ../knowlpedia-content \
  --seeds ../knowlpedia-content/reviews/missing-links/seeds.txt \
  --report tmp/missing-links/audit.json
.venv/bin/python scripts/link_review_progress.py \
  --audit tmp/missing-links/audit.json \
  --ledger ../knowlpedia-content/reviews/missing-links/reviews.json \
  --report tmp/missing-links/progress.json
.venv/bin/python scripts/audit_dependency_graph.py \
  --content-package ../knowlpedia-content --profile production \
  --report tmp/missing-links/dependencies.json
```

Repeat discovery with `--profile development` for development-only content.
The report uses relative source paths, exact line/column positions, context,
source hashes, canonical targets, ambiguity, and core/supporting priority.
`findings` contains known-term matches and explicit missing link/prerequisite
IDs. `possible_missing_definitions` groups unknown phrases with source counts
and all occurrences, plus lexical related-target suggestions (not semantic resolutions). Compiler validation messages are included separately.
The report is read-only: it never changes content or starts model sessions.

Review queues have different meanings:

- `unlinked_phrase`: title/alias/plural match, not already linked in that section.
  Single-word candidates need extra scrutiny. A link in Examples does not hide
  a missing link in the core. Repetition within the same section is suppressed.
- `ambiguous_phrase`: multiple canonical targets claim the phrase; choose only
  after reading the mathematical context.
- `broken_link` / `missing_prerequisite_target`: explicit unresolved IDs, which
  might be typos rather than absent concepts.
- `possible_missing_definition`: two/three-word phrases ending in a mathematical
  noun, recurring in at least three source knowls by default, plus seed phrases
  regardless of frequency. These are discovery hints, not verified dependencies.

The scanner excludes metadata, headings, references, code, math, existing links,
HTML tags/comments, and containers as source knowls. Emphasized prose is scanned.
It joins words across a single line break, never across a blank paragraph.
The compiler supplies profile selection and redirect resolution. Generated
plurals are heuristic, not a linguistic authority. The scanner is conservative
Markdown handling, not a full Markdown parser; unusual nested syntax, TeX
terminology, synonyms, inflections, accents/spelling variants, and rare unknown
phrases remain manual-review work. Some unknown phrases are defined locally.
Counts measure discovery volume, not mathematical errors or recall.

The existing `interlink_content.py` remains available for explicitly accepted
candidates from **its own report**. Its IDs and narrower scan differ from this
audit; do not feed new audit IDs to it. Review and edit new-audit findings in
source for now. Avoid introducing an automatic rewriting layer before the
candidate quality is measured.

## Progress convention

Store append-only entries in the content repository's
`reviews/missing-links/reviews.json`, in chronological order:

```json
{
  "id": "subject/knowl-id",
  "outcome": "corrected",
  "source_sha256": "SHA-256 of the complete source AFTER review and edits",
  "evidence": "Which phrases and target definitions were checked, conventions verified, changes made, and false positives rejected."
}
```

Outcomes are `corrected`, `reviewed_unchanged`, and `blocked`. Use `blocked`
when a required definition or convention remains unresolved. A completed entry
must review the whole knowl's linking needs, not merely one matched phrase.
The latest entry per knowl controls progress. Always generate a **fresh** audit
before counting: hash-mismatched reviews are stale and return to the remaining
queue. Both blocked and unreviewed knowls remain unfinished. This scoped ledger
does not certify a full mathematical review or increment the refactor ledger.

Keep full generated reports under ignored `tmp/`; commit the compact baseline,
seed terms, review ledger, and reviewed source changes. No content corrections
are implied by the initial baseline audit.

## Initial production baseline

The first run found 3,499 canonical knowls, including 57 containers excluded
from linking review, leaving 3,442 eligible knowls. There are 21,961 unlinked
phrase candidates (1,760 multiword candidates in cores), 376 ambiguous phrase
occurrences, and 768 candidate unknown phrases. There are no unresolved knowl
link IDs or prerequisite IDs. Ten existing alias-collision warnings remain
visible in the report. These counts include false positives and do not imply
that 768 definitions need to be written. The separate linking ledger starts
at zero completed reviews.
