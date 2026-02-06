# AGENT START HERE (Knowlpedia)

This file is the fast onboarding guide for coding agents working in `knowlpedia/`.

## 1) Mission and Scope

Knowlpedia is the **pipeline + infrastructure repo** for producing mathematical knowls.

- Primary goal: build and improve the factory that generates/validates knowls.
- Non-goal (by default): manually author large batches of knowl content.
- Live corpus is in sibling repo: `../knowlpedia-content/`.

## 2) Repo Role in the 3-Repo System

- `knowlpedia/` (this repo): workflow docs, prompt templates, scripts, Hugo infra.
- `knowlpedia-content/`: generated/curated knowl markdown corpus used by site.
- `leanknowl/`: R&D for deterministic Mathlib-aligned definition extraction.

## 3) Quick Orientation

Read in this order:

1. `docs/v2-knowl-generation/README.md`
2. `docs/v2-knowl-generation/workflow.md`
3. `docs/v2-knowl-generation/anti-patterns.md`
4. `docs/v2-knowl-generation/validation.md`
5. `scripts/tests/knowl_tests.py`
6. `scripts/validate-knowls.py`

Then inspect relevant scripts:

- `scripts/prepare-batches.py`
- `scripts/extract-knowls.py`
- `scripts/fix-knowls.py`

## 4) Current Pipeline Surface Area

Main pipeline families:

- `docs/knowl-generation/`: classic 4-step generation flow.
- `docs/v2-knowl-generation/`: hardened workflow with anti-pattern prevention + validation.
- `docs/v3-knowl-generation/`: newer positive-framing prompt style.
- `docs/knowl-extraction/`: extract knowls from existing notes/material.
- `docs/knowl-paper-companion/`: short recall-oriented paper companion knowls.

## 5) Quality Model (Current vs Target)

Current strength:

- Structural validation (broken links, malformed shortcodes, anti-pattern scans).

Current gap:

- Objective quality scoring for mathematical correctness + attention efficiency.

Target verification tracks (run in parallel):

1. **Formal sync track** (via `leanknowl`): deterministic checks for Mathlib-covered concepts.
2. **Human SME track**: manual sign-off for domains where expert review is available.
3. **Literature citation track**: map knowls to citable source definitions and score fidelity.

## 6) “Confidence Flag” Direction

Each knowl should eventually carry machine-readable verification metadata, e.g.:

- `verification.formal_sync`: pass/fail + source hash/version + last checked date
- `verification.human_review`: reviewer + scope + date
- `verification.lit_citation`: citation list + match score
- `verification.overall_confidence`: derived tier (A/B/C or numeric)

This schema is not fully implemented yet; agents should preserve this direction in design choices.

## 7) Immediate Engineering Priorities

1. Define and implement a stable verification metadata schema.
2. Add a corpus scoring pass that penalizes verbosity drift and rewards concise correctness.
3. Wire section-level dashboards (quality, confidence, coverage, broken refs, unresolved citations).
4. Integrate Lean-sync outputs (from `leanknowl`) into validation/reporting.
5. Add citation-alignment tooling for non-Mathlib knowls.

## 8) Operational Commands

Common checks:

```bash
python3 scripts/validate-knowls.py
python3 scripts/tests/knowl_tests.py
```

Section-focused:

```bash
python3 scripts/tests/knowl_tests.py --section algebra-groups
```

## 9) Agent Working Rules

- Prefer improving pipeline reliability, testability, and evaluation over bulk content generation.
- Keep edits small, testable, and script-first.
- Preserve shortcode correctness and anti-pattern constraints.
- If changing workflow docs, keep v2/v3 guidance internally consistent.

