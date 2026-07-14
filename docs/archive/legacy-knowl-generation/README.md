# Legacy Knowlpedia Generation Experiments

> **Historical and noncanonical.** These files preserve earlier AI-assisted knowl-generation experiments. They are evidence, not current instructions. Use the current `.agents/skills/knowlify-document/` workflow for new work.

This archive was copied from the sibling `knowlpedia` repository on 2026-07-10. The source checkout was at commit `1bf7251d08020a3dc52beacdd17abe12c72a9c9b`. Source files were left in place; this is a preservation snapshot, not a destructive move.

## Why this lives here

The experiments concern content generation, cross-linking, validation, and agent orchestration for the refactored knowl system. The `agent-coordination` repository is intentionally only a high-level workspace map, so the detailed archive belongs beside the implementation it informs.

## Contents

- `guidance-snapshots/`: legacy v1, v2, extraction, and paper-companion instructions.
- `tool-snapshots/`: old index, term-resolution, diff-planning, batching, and validation code retained for reference.
- `experiments/topology-v1`, `topology-v2`, `topology-v3`: a particularly useful common 95-knowl prompt-evolution benchmark.
- `experiments/v3-batches`, `geometry-bundles-batches`, `production-batches`: representative batch prompts and outputs.
- `production-notes/`: phase notes, review lists, proof-sketch audits, and earlier module-reorganization records.
- `CATALOG.yaml`: machine-readable provenance and status.
- `LESSONS.md`: a short synthesis of durable observations and superseded assumptions.

## How to use it

1. Start with `LESSONS.md`.
2. Treat every claim as a historical observation until reproduced against the current compiler and current models.
3. Use the topology v1/v2/v3 directories as a regression corpus when comparing prompts or subagent strategies.
4. Promote only reproduced findings into the current skill or compiler tests.

The archive intentionally excludes old WordPress/site-generator research, browser/session state, caches, public builds, and environment-specific credentials.
