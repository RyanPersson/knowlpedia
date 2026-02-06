# Knowlpedia Execution Roadmap (Factory, Verification, Scale)

This document turns the long-term vision into parallelizable, branch-friendly workstreams.

## 1) North Star

Build a system that produces standardized, readable mathematical knowls with the strongest feasible verification:

1. Formal verification against Mathlib where possible.
2. Human SME sign-off where formal sync is unavailable.
3. Citation-backed alignment to literature for broader coverage.

## 2) Program Architecture (Three Verification Tracks)

1. Formal sync track
- Source: Mathlib declarations.
- Engine: deterministic DAG flattening + canonical axiom extraction (`leanknowl`).
- Output: pass/fail + diff artifact for Mathlib-covered concepts.

2. Human review track
- Source: selected high-value knowls.
- Engine: rubric-based SME review workflow.
- Output: signed review metadata (reviewer, date, scope, confidence).

3. Citation alignment track
- Source: citable definitions from papers/books/notes.
- Engine: retrieval + alignment scorer + provenance recording.
- Output: citation bundle + alignment confidence.

## 3) Shared Contract (Required First)

All tracks must write to a common verification schema. Suggested minimal fields:

```yaml
verification:
  formal_sync:
    status: pass|fail|not_applicable
    source: "mathlib"
    source_version: "<commit-or-tag>"
    checked_at: "YYYY-MM-DD"
    artifact_path: "artifacts/formal-sync/<slug>.json"
  human_review:
    status: approved|needs_revision|not_reviewed
    reviewer: "<name-or-id>"
    reviewed_at: "YYYY-MM-DD"
    notes: "<optional>"
  citation_alignment:
    status: pass|partial|fail|not_run
    citations:
      - id: "<bib-id-or-url>"
        locator: "<page/section>"
    score: 0.0
    checked_at: "YYYY-MM-DD"
  overall_confidence:
    tier: A|B|C|D
    rationale: "<short text>"
```

## 4) Parallelizable Workstreams (Branch Plan)

Use one branch per workstream; merge behind feature flags if needed.

1. `ws/schema-and-artifacts`
- Define schema and artifact directory conventions.
- Add schema validation script and CI check.

2. `ws/formal-sync-mvp`
- Consume `leanknowl` output.
- Implement knowl-vs-canonical comparison and report generation for a pilot set.

3. `ws/citation-alignment-mvp`
- Add citation metadata format.
- Implement retrieval + match scoring prototype for one section.

4. `ws/human-review-workflow`
- Define review rubric + status model.
- Add reviewer tooling for approval/revision loop.

5. `ws/quality-score-attention`
- Add quality scorer that explicitly penalizes verbosity drift.
- Track concise-correctness metrics per section.

6. `ws/dashboard-reporting`
- Build section-level report pages/JSON summaries:
  coverage, failures, confidence tiers, stale verifications.

7. `ws/pipeline-integration`
- Wire generation -> fix -> validate -> verify -> score into one reproducible run command.

## 5) Iteration Cadence

Run in short cycles (1-2 weeks), each with:

1. Pilot scope (one section or 20-50 knowls).
2. Automated report output.
3. Clear pass/fail gates.
4. Retro on false positives/false negatives in verification.

## 6) Acceptance Gates by Phase

Phase 1 (Foundation):
- Schema stable and versioned.
- Artifacts generated in CI for pilot section.

Phase 2 (Verification MVPs):
- Formal sync MVP working on selected Mathlib-backed knowls.
- Citation alignment MVP producing reproducible scored output.
- Human review metadata end-to-end supported.

Phase 3 (Operationalization):
- Unified dashboard and confidence tiers in place.
- Section-level SLAs (e.g., % with non-D confidence).

## 7) Branching and Merge Rules

1. No branch may invent a new schema field without updating schema docs and validators.
2. Verification branches must output machine-readable artifacts, not only markdown prose.
3. Any scoring change must include a before/after report on a fixed benchmark subset.
4. Merge only with deterministic rerun instructions documented.

## 8) First 30-Day Concrete Plan

1. Week 1
- Finalize schema + validator (`ws/schema-and-artifacts`).

2. Week 2
- Formal sync MVP on 20-30 core algebra knowls (`ws/formal-sync-mvp`).

3. Week 3
- Citation alignment MVP on one section (`ws/citation-alignment-mvp`).

4. Week 4
- Confidence aggregation + section report (`ws/dashboard-reporting`).

## 9) Why This Decomposition Works

It separates concerns cleanly:

- Extraction/certification logic can evolve independently.
- Human workflow does not block formal automation.
- Scoring/reporting creates objective iteration pressure.
- Branches remain mergeable because contract-first design prevents interface drift.

