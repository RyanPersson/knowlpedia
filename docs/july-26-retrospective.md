# July 26 knowl-generation retrospective

The July 2026 expansion added a large, connected collection of knowls covering
operator algebras, noncommutative geometry, noncompact representation theory,
functional and harmonic analysis, smooth and complex geometry, symplectic
geometry, principal bundles, and gauge theory.

This document records the reusable parts of that process. It is a retrospective,
not a rigid specification: future expansions should adapt the batch sizes and
review depth to the subject matter and available resources.

## Sources of truth

The generation process did not rely on a special knowl-generation skill. It was
built from the repository's existing content model and tooling:

- `knowlpedia-content/EDITORIAL.md` defines the two-speed editorial model.
- Existing knowls establish front-matter, naming, namespace, link, and
  mathematical notation conventions.
- The compiler and its tests define what the site accepts and how progressive
  sections are rendered.
- The subject index knowls define the navigational structure into which new
  material must be integrated.

The repository-level agent guidance also reserves the `knowlify-document` skill
for cases where a user explicitly requests that skill. A general corpus
expansion should therefore use the repository's files and scripts unless the
request says otherwise.

## Editorial contract

Every ordinary definition or theorem knowl should support two reading speeds.

The text before the first level-two heading is the canonical core. It should:

- name the definiendum or theorem immediately;
- include the hypotheses required for correctness;
- be concise enough to work when expanded inline;
- define notation needed to understand the statement;
- link genuine prerequisites already represented in the corpus.

Material that rewards slower reading belongs in progressive sections such as:

- equivalent characterizations;
- intuition or a guiding picture;
- examples and non-examples;
- consequences and related constructions;
- conventions, scope, and warnings;
- references.

This separation is especially important for convention-sensitive subjects.
For example, a core definition should choose and state one convention, while a
later section can explain competing uses in the literature.

Typical front matter is:

```toml
+++
id = "namespace/stable-id"
title = "Human-readable title"
kind = "definition"
summary = "A one-sentence description."
aliases = ["Alternate name"]
domains = ["primary-domain", "secondary-domain"]
section_mode = "progressive"
+++
```

IDs should be stable, descriptive, and placed in the namespace that best owns
the concept. Aliases are useful both for discovery and for later interlinking,
but they should represent genuine names rather than every phrase that might
refer to the object.

## 1. Turn topics into coverage maps

A request for "more von Neumann algebras" or "more symplectic geometry" is a
research region, not yet an authoring manifest. Begin by expanding each region
into several kinds of entries:

- foundational objects and definitions;
- standard maps and morphisms;
- constructions and universal properties;
- equivalences and characterization theorems;
- important examples and counterexamples;
- structural theorems;
- prerequisites that live in adjacent subjects.

Independent coverage proposals can be useful for broad subjects because they
expose different curricular paths and reduce the chance that one outline's
blind spots become gaps in the corpus. Parallel planning is optional; the
important output is a set of explicit candidate records with a proposed title,
ID, namespace, kind, and short rationale.

Prefer dependency-aware coverage over indiscriminate completeness. A reader
should be able to move from prerequisites through definitions to the major
constructions and theorems without repeatedly encountering undefined central
terms.

## 2. Deduplicate semantically against the corpus

Deduplication must happen before authorship. Comparing proposed filenames alone
is not sufficient.

For every candidate, search the current corpus using:

- IDs and paths;
- titles and aliases;
- singular, plural, hyphenated, and spelling variants;
- equivalent mathematical formulations;
- neighboring index entries and incoming links.

Classify each proposal as one of:

1. a genuinely new knowl;
2. an expansion or correction of an existing knowl;
3. an alias of an existing concept;
4. a section that belongs inside another knowl;
5. out of scope for the current expansion.

For example, "normal state," "ultraweakly continuous state," and "a state in
the predual" may be equivalent descriptions that belong in one central knowl
rather than three separate pages. Conversely, closely related notions such as
strict and weak summability can require distinct knowls when their hypotheses,
uses, or literature differ materially.

This step should produce the canonical manifest used by authors. Once an ID is
assigned, avoid letting separate batches silently invent competing IDs for the
same concept.

## 3. Partition the manifest by mathematical neighborhoods

Divide the accepted manifest into coherent, mostly disjoint batches. Good batch
boundaries follow mathematical neighborhoods or filesystem namespaces, for
example:

- states, positive functionals, and GNS representations;
- von Neumann algebra types and projection comparison;
- group C*-algebras and crossed products;
- smooth vectors and noncompact Lie-group representations;
- Kähler and holomorphic geometry;
- moment maps and symplectic reduction.

Each authoring assignment should state:

- the exact knowl IDs it owns;
- the files or namespaces it may modify;
- nearby existing knowls it should inspect;
- the editorial contract;
- the expected literature standard;
- the requirement to preserve current delimiter and linking conventions;
- the checks it should run before handing work back.

Keeping ownership explicit limits collisions when authorship is parallel and
also makes a sequential workflow easier to audit.

## 4. Author from the dependency neighborhood

Before writing a knowl, inspect its likely prerequisites, sibling concepts, and
subject index. This establishes local notation and prevents the new page from
restating material the corpus already explains.

A strong knowl commonly develops in this order:

1. exact definition or theorem statement;
2. explanation of the displayed maps or equations;
3. equivalent formulations;
4. representative examples and non-examples;
5. important consequences or relationships;
6. convention-sensitive cautions;
7. literature references.

Not every knowl needs every section. A short elementary definition may need
only its core and an example, while an advanced definition such as a summable
Fredholm module benefits from sections on parity, topology, conventions, and
its Chern character.

Avoid padding. The aim is enough documentation to make the knowl useful as a
learning node, not a miniature textbook chapter detached from the rest of the
site.

## 5. Cite literature that supports the content

References should be selected during authorship, not added decoratively at the
end.

Prefer:

- foundational papers for historically or technically distinctive results;
- standard graduate texts or monographs for established definitions;
- DOI, publisher, author-maintained, journal, or institutional records;
- citations that identify a relevant chapter, section, or theorem.

Use the literature to resolve real mathematical questions: hypotheses,
normalizations, topology, sign conventions, terminology, and equivalence
claims. When sources use different conventions, state the convention adopted
by the knowl and summarize the alternative in a scope or remarks section.

The reference list does not replace mathematical review. Formulas, quantifiers,
domains, codomains, and stated implications still require direct inspection.

## 6. Perform index and dependency closure

After the first authoring pass, treat the new files as a graph rather than a
list.

Update the relevant subject indexes and create a durable expansion index when
the batch is large enough to benefit from provenance and review tracking. Then
look for:

- new knowls absent from every index;
- central prerequisites referenced in prose but missing from the corpus;
- pairs of knowls that should link to one another;
- concepts placed in an unexpected namespace;
- duplicate definitions introduced by separate neighborhoods;
- dependency chains that terminate in undefined technical terms.

Index closure is not merely navigation work. Reading the complete index often
reveals conceptual gaps that are hard to see while reviewing individual files.

## 7. Interlink against the complete corpus

Authors should add obvious knowl links while writing, but author-local linking
will rarely be exhaustive. The full corpus contains more titles and aliases
than any one author is likely to keep in context.

Run a separate interlinking pass after the files have stabilized. The
repository's `scripts/interlink_content.py` builds candidates from corpus titles
and aliases and inserts links conservatively. Its tests live in
`tests/test_interlink_content.py`.

Automated linking must avoid:

- text already inside a knowl link;
- code, URLs, front matter, and other unsafe contexts;
- ambiguous common words;
- self-links;
- overlapping matches;
- link saturation.

Review the resulting diff semantically. A textual match is not always the same
mathematical concept in context, and a technically valid link can still make a
sentence harder to read.

It can be useful to repeat this stage: an initial pass exposes aliases or
ambiguities, a review improves the term map or matching rules, and a later pass
captures safe links that were previously missed.

## 8. Validate in layers

Validation should move from cheap structural checks to full rendered output:

1. inspect `git status` and confirm the intended file set;
2. check front matter, duplicate IDs, and link targets;
3. run the compiler test suite;
4. run the progressive-section audit;
5. build the complete development content package;
6. run rendering-error checks;
7. build with the production profile;
8. inspect representative pages from each major subject area.

Representative visual inspection matters even when the compiler passes. It can
catch awkward cores, oversized equations, broken prose around displays,
unhelpful section boundaries, excessive linking, and math that is technically
valid but difficult to read.

Keep generated build directories and temporary validation copies out of the
content commit. These artifacts can consume substantial workspace capacity
during a large expansion even though the canonical source files remain small.

## 9. Commit in reviewable stages

Where practical, keep conceptually different transformations separate:

- semantic content creation and expansion;
- index integration;
- mechanical interlinking;
- compiler or tooling changes;
- delimiter or formatting normalization.

This makes large diffs easier to audit and lets later maintainers distinguish
authored mathematics from mechanical edits. Before publishing, verify the
branch relationship, rerun the relevant production checks, and confirm that
only canonical source and intended tooling changes are tracked.

## Lessons from the July expansion

The two-speed editorial model scaled well. Short formal cores remained useful
inline, while progressive sections supported substantially deeper exposition.

Semantic deduplication was more important than string deduplication. Broad
mathematical subjects naturally produce multiple names and equivalent
formulations for the same concept.

Parallel authorship worked best with explicit, disjoint ownership and a shared
editorial contract. Regardless of how much concurrency is appropriate for a
future project, bounded manifests and clear handoff criteria remain useful.

Index closure found omissions that ordinary file review did not. A permanent
expansion index also made the result easier to browse and audit.

Finally, interlinking needs its own corpus-wide stage. Authors supplied many
good local links, but a later scripted and reviewed pass was necessary to take
advantage of the vocabulary already present across Knowlpedia.
