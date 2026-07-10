# v3 Knowl Regeneration - Handoff Document

Created: 2026-01-22

## Context

We identified 78 knowls with "proof sketch" anti-pattern sections. These need to be regenerated using the new v3 positive-framing prompt (which never mentions "proof" at all, avoiding the "pink elephant" problem).

## What's Ready

### Batch Files
Location: `tmp/v3-batches/`

| File | Section | Slugs |
|------|---------|-------|
| `stat-mech-batch1.md` | stat-mech | 20 |
| `stat-mech-batch2.md` | stat-mech | 20 |
| `stat-mech-batch3.md` | stat-mech | 20 |
| `stat-mech-batch4.md` | stat-mech | 3 |
| `stat-mech-lattice-batch1.md` | stat-mech-lattice | 4 |
| `thermodynamics-batch1.md` | thermodynamics | 11 |

### Oracle Config
```
tmp/v3-batches/oracle-config.txt
```

### Staging Directory
```
content/v3-regenerated/
```
New knowls will be placed here for comparison before replacing originals.

### Slug Mapping
```
tmp/v3-batches/slug-section-map.txt
```
Maps each slug to its original section (for moving files after review).

## Next Steps

### 1. Run Oracle
```bash
~/.oracle/oracle-parallel.sh \
  --config /Users/ryanpersson/anki/code/blog/tmp/v3-batches/oracle-config.txt \
  --sessions-file /Users/ryanpersson/anki/code/blog/tmp/v3-batches/sessions.txt
```

Runtime: ~20-40 minutes (6 batches in parallel).

### 2. Parse Oracle Output
After oracle completes, extract knowls from session logs:

```bash
python3 scripts/parse-oracle-output.py \
  --sessions-file tmp/v3-batches/sessions.txt \
  --output-dir content/v3-regenerated/
```

(Script may need to be created - see `docs/v3-knowl-generation/workflow.md` for extraction code.)

### 3. Validate
```bash
# Check for proof sketches (should be zero)
grep -ri "proof" content/v3-regenerated/ | grep -i "sketch\|idea\|outline"

# Check for related sections (should be zero)
grep -ri "## related\|see also" content/v3-regenerated/

# Run anti-pattern tests
python3 scripts/tests/knowl_tests.py
```

### 4. Compare with Originals
Create a comparison page or manually review side-by-side.

### 5. Replace Originals
Use the slug-section mapping to move files:
```bash
# For each slug in mapping, copy from v3-regenerated to original section
```

## Key Files

| File | Purpose |
|------|---------|
| `docs/v3-knowl-generation/README.md` | v3 philosophy overview |
| `docs/v3-knowl-generation/prompt-template.md` | The positive-framing prompt |
| `docs/v3-knowl-generation/workflow.md` | Step-by-step process |
| `scripts/prepare-v3-batches.py` | Creates batch prompts from flagged files |
| `tmp/proof-sketch-flagged.txt` | Original list of 78 flagged files |

## Hugo Server
Hugo server is running in background on port 1313. Use `scripts/hugo-server.sh status` to check.
