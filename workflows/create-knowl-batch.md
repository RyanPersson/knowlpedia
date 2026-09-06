# Create and integrate a knowl batch

Use this workflow for a source-guided or subject-guided expansion of
knowlpedia-content. It treats deduplication, atomic scope, interlinking, and
rendered output as parts of authorship rather than cleanup deferred until the
end.

The commands below assume that knowlpedia and knowlpedia-content are sibling
repositories and that the shell is in knowlpedia.

## 1. Establish the working state

Inspect both repositories and record the current branch and starting commits
before auditing the corpus. Preserve a user-provided feature branch; do not
switch branches as a workflow prerequisite. If a new branch is needed, create
the same feature branch name in both repositories.

Record the two starting commits in a batch plan under docs/.

## 2. Build a semantic inventory before assigning IDs

Extract the source's definitions, theorems, constructions, prerequisites, and
important relationships. Search the complete corpus by:

- likely title and spelling variants;
- standard synonyms and historical terminology;
- notation and common aliases;
- neighboring subject indexes;
- definitions embedded in broader or older knowls.

Do not equate a new title with a new concept. Read plausible owners and decide
whether each item is:

- an existing knowl to reuse;
- an existing knowl to expand;
- a genuinely new atomic knowl;
- a theorem or relationship rather than a definition;
- a deferred research topic.

Reserve accepted IDs in the batch plan before writing files. If one page owns
multiple independently reusable concepts, split it. If two proposed pages
describe the same object from different presentations, choose one canonical
owner and link the presentations. Preserve stable IDs and incoming URLs; use
redirect_to and redirect_sections when consolidation changes ownership.

## 3. Research conventions and scope

Use primary papers for technically distinctive claims and standard texts or
monographs for established definitions. Resolve, rather than conceal:

- hypotheses and quantifiers;
- domains and codomains;
- left/right or sign conventions;
- normalization factors;
- smooth versus nonsmooth formulations;
- dimension restrictions;
- competing meanings of the same notation.

Put the adopted convention in the knowl. Add a warning or comparison section
when a nearby convention could cause a real misunderstanding.

Record exact inspected source locators for nontrivial claims. Elementary
claims can instead carry specific direct verification with no external source
claim. Return unresolved entries as targeted reviews, and provide partial
per-ID checkpoints before expanding a lane. Repeated general assurances and
unrelated references do not complete a review.

## 4. Write atomic knowls with short cores

Each file begins with valid front matter containing at least id, title, kind,
summary, aliases, domains, and section_mode.

The text before the first level-two heading is the collapsible core. Keep it
compact but self-contained: state the definition or theorem with all necessary
hypotheses and the conventions needed to interpret it. Include a brief verbal
explanation when formulas alone obscure the structure. Put longer motivation,
examples, equivalent formulations, and literature discussion in progressive
sections; never defer a qualification that changes the core statement.

Add knowl links while writing when the intended target is unambiguous. Link a
technical term on its first useful occurrence; do not saturate prose with
repeated links.

End substantive pages with references that identify a relevant section,
theorem, chapter, or other locator whenever practical.

## 5. Close dependencies and discovery

Update an existing subject index only when the repository's discovery model
requires it. A permanent dependency-ordered expansion index is optional and
must not be introduced solely to close a batch. If one is useful, it should:

- lists the new and reused prerequisites;
- explains the bridges between subject areas;
- records dimension and convention warnings;
- lists research directions that were intentionally deferred.

Read the completed index as a dependency graph. Check for undefined technical
terms, missing reverse links, unexpected namespaces, and concepts that were
accidentally duplicated across subject clusters.

## 6. Run the interlinker as a reviewed report

Create a path manifest containing the new knowl files, one repository-relative
path per line. Generate candidates without editing:

~~~bash
.venv/bin/python scripts/interlink_content.py \
  --content-root ../knowlpedia-content/content \
  --paths-file /tmp/knowl-batch-paths.txt \
  --include-aliases \
  --include-plurals \
  --report /tmp/knowl-batch-interlink.jsonl
~~~

Review every proposed target in mathematical context. Reject merely textual
matches, including the same words used in a different subject, a broad umbrella
page when an atomic owner exists, or a complex analogue where the prose means a
quaternionic or octonionic object. Apply accepted links and rerun the report.

## 7. Seed and review dependency metadata

Treat links in the compact definition core as candidate prerequisites. Generate
a deterministic sample report before editing metadata:

~~~bash
.venv/bin/python scripts/generate_dependency_metadata.py \
  --content-root ../knowlpedia-content/content \
  --paths-file /tmp/knowl-batch-paths.txt \
  --sample-size 20 \
  --seed 20260827 \
  --report /tmp/knowl-batch-dependencies.jsonl
~~~

Inspect the sample semantically. Definition-core links can still name a
consequence, comparison, convention, or example. If example material is present
in the core, repair the knowl by moving it under a descriptive `##` section;
do not complicate the dependency heuristic to accommodate malformed structure.

Apply the reviewed scope only after the sample behaves conservatively:

~~~bash
.venv/bin/python scripts/generate_dependency_metadata.py \
  --content-root ../knowlpedia-content/content \
  --paths-file /tmp/knowl-batch-paths.txt \
  --report /tmp/knowl-batch-dependencies.jsonl \
  --apply
~~~

Generated metadata starts with `dependency_review_count = 0`. A later human or
AI dependency review must inspect the complete list, correct it, and increment
the counter. The generator preserves metadata with a positive review count. A
dependency review is distinct from a targeted or full content review: it
verifies the complete prerequisite list and its provenance, but does not
certify the prose.

## 8. Record review evidence and validate structure

Maintain reviews/refactor-ledger.json. Each entry declares scope (full,
targeted, or dependencies) and outcome (corrected, reviewed_unchanged,
redirected, or new). Full reviews also record the current source sha256 and
concrete source evidence; a later edit invalidates that full review. Targeted
reviews record their bounded claim or section. Dependency reviews record the
complete list reviewed. A metadata-only prerequisite change is not a content
correction.

Use the progress script to report the fixed baseline and pending IDs:

~~~bash
python3 scripts/review_progress.py --content-repo ../knowlpedia-content --output docs/refactor-progress.md
python3 scripts/review_progress.py --content-repo ../knowlpedia-content --json
~~~

The cumulative refactor baseline is fixed at the content commit recorded in
the ledger (currently ea7256bd). Do not replace it with a moving branch tip.

## 9. Validate source and structure

Run the cheap checks first:

~~~bash
git -C ../knowlpedia-content diff --check
make test
make audit-sections
make audit-external-links
make audit-scope
~~~

The scope audit is a review report. Inspect every new-page finding; do not
silence it mechanically. A finding may reveal a bundled definition or a
semantic duplicate that title matching missed.

## 10. Build and inspect rendered output

For a live-site-only development build, explicitly exclude unrelated optional
content sources:

~~~bash
make build EXTRA_CONTENT_SOURCES=
make check-rendering
~~~

Then run the authoritative production build:

~~~bash
make build-production
~~~

make build-production composes only knowlpedia-content, compiles the production
profile, checks profile isolation, and runs
scripts/check_rendering_errors.py. The checker reports compiler error markers,
unrendered math delimiters and LaTeX, stray visible backslashes, raw wikilinks,
broken local links, missing knowl targets, and forbidden development-only
artifacts.

Automated HTML checks are necessary but not sufficient. Serve the production
output and inspect in a browser:

- the permanent batch index;
- at least one representative core from every major subject cluster;
- long displays and notation-heavy definitions;
- expanded sections and several newly added knowl links;
- the generated side-by-side review.

Look specifically for raw delimiters or backslashes, text accidentally absorbed
into math, malformed subscripts, oversized formulas, awkward line wrapping,
broken links, and cores that are too long to work well inline. A browser
spot-check is a required completion step for a knowl batch.

## 11. Generate a review and commit

After committing the content branch, generate a review directly from the
content repository so optional content sources are not composed:

~~~bash
.venv/bin/python scripts/generate_content_review.py \
  --content-repo ../knowlpedia-content \
  --output public-imported/review/content-changes \
  --left-label "baseline · existing" \
  --right-label "working tree · proposed" \
  --heading "Knowl changes" \
  --include-added
~~~

Keep mathematical authorship, broad mechanical interlinking, and application
tooling in separate commits when that separation makes the review clearer.
Before committing, run git diff --check against the working tree and inspect
the generated review. For a cumulative final review, use the fixed baseline
explicitly (ea7256bd..HEAD) after the content commit. Before handoff, confirm
both worktrees are clean and report:

- branch and commit IDs;
- numbers of new and expanded knowls;
- validation results and any pre-existing warnings;
- the direct preview URLs for the expansion index and diff.
