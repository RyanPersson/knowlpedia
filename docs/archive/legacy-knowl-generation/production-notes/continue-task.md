# Continue Task: Analysis Reorganization Pipeline

**Created:** 2026-01-13
**Status:** Paused - waiting for iTerm restart to enable Chrome launching

## Context

We are reorganizing the `analysis/` section (332+ knowls) into topic-focused modules using the Oracle tool to launch GPT-5.2-pro subagents for batch knowl generation.

## What's Been Done

1. **Read and understood** the v2-knowl-generation workflow docs
2. **Deleted** v1-topology, v2-topology, v3-topology test directories
3. **Moved** existing sections to preserve them:
   - `shared-foundations` → `shared-foundations-old`
   - `linear-algebra` → `linear-algebra-old`
4. **Created** new empty directories:
   - `shared-foundations/`
   - `linear-algebra/`
   - `topology/`
   - `measure-theory/`
   - `real-analysis/`
5. **Created** `scripts/prepare-batches.py` - parses `proposed-analysis-reorg.md` and generates batch prompts
6. **Generated** batch prompts for shared-foundations:
   - `tmp/batches/shared-foundations/batch1.md` (17 slugs)
   - `tmp/batches/shared-foundations/batch2.md` (17 slugs)
   - `tmp/batches/shared-foundations/batch3.md` (16 slugs)

## Next Steps

1. **Start Chrome** with remote debugging:
   ```bash
   /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
     --remote-debugging-port=9222 \
     --user-data-dir=~/.oracle/browser-profile
   ```

2. **Run Oracle** for shared-foundations:
   ```bash
   ~/.oracle/oracle-parallel.sh \
     -pf tmp/batches/shared-foundations/batch1.md \
     -pf tmp/batches/shared-foundations/batch2.md \
     -pf tmp/batches/shared-foundations/batch3.md \
     --sessions-file tmp/batches/shared-foundations/sessions.txt
   ```

3. **Parse Oracle output** and extract knowls to `content/shared-foundations/`

4. **Repeat for remaining sections:**
   - linear-algebra (26 slugs → 2 batches)
   - topology (87 slugs → 4 batches)
   - measure-theory (22 slugs → 1 batch)
   - real-analysis (187 slugs → 8 batches)

5. **Validate** with `python3 scripts/validate-knowls.py`

## Key Files

| File | Purpose |
|------|---------|
| `docs/knowl-modules/proposed-analysis-reorg.md` | Master list of slugs per section |
| `scripts/prepare-batches.py` | Generates batch prompts from proposed reorg |
| `tmp/batches/*/` | Generated batch prompts |
| `docs/v2-knowl-generation/workflow.md` | Full Oracle workflow reference |

## Batch Sizes

| Section | Slugs | Batches |
|---------|-------|---------|
| shared-foundations | 50 | 3 |
| linear-algebra | 26 | 2 |
| topology | 87 | 4-5 |
| measure-theory | 22 | 1 |
| real-analysis | 187 | 8-10 |

## Hugo Server

The dev server should be restarted with drafts:
```bash
hugo server --bind 0.0.0.0 -D
```

And the feedback API:
```bash
python3 scripts/feedback-api.py
```
