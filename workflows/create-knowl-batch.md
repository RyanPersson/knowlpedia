# Create and integrate a knowl batch

Use this workflow for a source-guided or subject-guided expansion of
knowlpedia-content. It treats deduplication, atomic scope, interlinking, and
rendered output as parts of authorship rather than cleanup deferred until the
end.

The commands below assume that knowlpedia and knowlpedia-content are sibling
repositories and that the shell is in knowlpedia.

## 1. Synchronize and branch

Update develop in both repositories before auditing the corpus:

~~~bash
git switch develop
git pull --ff-only

git -C ../knowlpedia-content switch develop
git -C ../knowlpedia-content pull --ff-only
~~~

Create the same feature branch name in both repositories. Record the two
starting commits in a batch plan under docs/.

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
owner and link the presentations.

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

## 4. Write atomic knowls with short cores

Each file begins with valid front matter containing at least id, title, kind,
summary, aliases, domains, and section_mode.

The text before the first level-two heading is the collapsible core. Keep it
short and axiomatic: state the definition or theorem with all necessary
hypotheses, but defer motivation, examples, equivalent formulations, caveats,
and literature discussion to progressive sections.

Add knowl links while writing when the intended target is unambiguous. Link a
technical term on its first useful occurrence; do not saturate prose with
repeated links.

End substantive pages with references that identify a relevant section,
theorem, chapter, or other locator whenever practical.

## 5. Close indexes and dependencies

Add each new page to its subject index. For a large batch, create a permanent
dependency-ordered expansion index that:

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

## 7. Validate source and structure

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

## 8. Build and inspect rendered output

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

## 9. Generate a review and commit

After committing the content branch, generate a review directly from the
content repository so optional content sources are not composed:

~~~bash
.venv/bin/python scripts/generate_content_review.py \
  --content-repo ../knowlpedia-content \
  --output public-imported/review/content-changes \
  --left-ref develop \
  --right-ref HEAD \
  --left-label "develop · existing" \
  --right-label "HEAD · proposed" \
  --heading "Knowl changes" \
  --include-added
~~~

Keep mathematical authorship, broad mechanical interlinking, and application
tooling in separate commits when that separation makes the review clearer.
Before handoff, confirm both worktrees are clean and report:

- branch and commit IDs;
- numbers of new and expanded knowls;
- validation results and any pre-existing warnings;
- the direct preview URLs for the expansion index and diff.
