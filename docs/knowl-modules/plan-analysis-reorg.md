# Analysis Reorganization Plan

**Created:** 2026-01-02
**Status:** Ready to execute
**Branch:** `refactoring-analysis` (in content submodule)

## Summary

We are reorganizing the monolithic `analysis` section (332 knowls) into topic-focused modules. This involves:
1. Creating new section directories
2. Moving existing knowl files
3. Updating all cross-references to use correct `section` parameters

## What's Been Done

1. **Consolidated 7 duplicate knowls** (committed to main):
   - `bijective-function`, `cartesian-product`, `domain`, `codomain` → `shared-foundations`
   - `linear-map`, `vector-space` → `linear-algebra`
   - `subsequence` → `analysis`
   - `diffeomorphism` kept in both (different definitions for ℝⁿ vs manifolds)

2. **Added `morphism` to shared-foundations** - foundational concept for structure-preserving maps

3. **Created proposed structure** in `docs/knowl-modules/proposed-analysis-reorg.md`

4. **Created branch** `refactoring-analysis` in content submodule

## Key Files to Reference

| File | Purpose |
|------|---------|
| `docs/knowl-modules/proposed-analysis-reorg.md` | Complete list of knowls per new section |
| `docs/v2-knowl-generation/workflow.md` | Oracle batch generation workflow |
| `docs/v2-knowl-generation/prompt-template.md` | Prompt template with anti-pattern rules |
| `docs/knowl-generation/orchestration.md` | Detailed Oracle automation guide |
| `scripts/validate-knowls.py` | Validates all knowl references |
| `tmp/needs-review.md` | Tracking doc for issues |

## Proposed New Sections

From the 332 `analysis` knowls:

| New Section | Count | Description |
|-------------|-------|-------------|
| `topology-core` | 22 | Topological spaces, open/closed, bases, continuity |
| `topology-metric` | 23 | Metric spaces, completeness, Cauchy sequences |
| `topology-compactness` | 27 | Compact sets, Heine-Borel, sequential compactness |
| `topology-connectedness` | 10 | Connected/path-connected sets |
| `topology-separation` | 6 | T0, T1, Hausdorff spaces |
| `topology-baire` | 8 | Baire category, meager/residual sets |
| `measure-theory` | 27 | Sigma-algebras, measures, Lebesgue |
| `analysis-real-foundations` | 34 | Real numbers, sup/inf, sequences |
| `analysis-series` | 30 | Series, convergence tests, power series |
| `analysis-calculus-1d` | 29 | Derivatives, MVT, Taylor |
| `analysis-multivariable` | 31 | Partial derivatives, Jacobian, implicit function |
| `analysis-integration` | 38 | Riemann integral, FTC, change of variables |
| `analysis-uniform-convergence` | 29 | Uniform convergence, Arzelà-Ascoli |

**Deferred:** Complex analysis (3), functional analysis (5) - will be separate sections later

## Execution Steps

### Step 1: Create New Directories
```bash
cd content
for dir in topology-core topology-metric topology-compactness topology-connectedness topology-separation topology-baire measure-theory analysis-real-foundations analysis-series analysis-calculus-1d analysis-multivariable analysis-integration analysis-uniform-convergence; do
  mkdir -p "$dir"
done
```

### Step 2: Move Files
For each new section, move the listed files from `analysis/` to the new directory. See `proposed-analysis-reorg.md` for the complete file lists.

### Step 3: Update Cross-References
After moving files, all references like:
```markdown
{{< knowl id="metric-space" >}}
```
from files NOT in `topology-metric` need to become:
```markdown
{{< knowl id="metric-space" section="topology-metric" >}}
```

### Step 4: Create _index.md for Each Section
Each new section needs an `_index.md` with proper structure.

### Step 5: Validate
```bash
python3 scripts/validate-knowls.py
```

### Step 6: Test Build
```bash
hugo server
# Navigate to new sections, verify rendering
```

## Important Notes

- **Hugo layouts:** The consolidated `layouts/_default/single.html` handles all sections dynamically - no per-section layouts needed
- **Branch:** Work is on `refactoring-analysis` branch in content submodule
- **Cross-section links:** MUST include `section` parameter when linking to different sections
- **Oracle workflow:** Use 6 parallel batches for any regeneration work

## Questions to Clarify

1. Should we regenerate knowls fresh via Oracle, or just reorganize existing files?
2. What order to tackle sections? (Suggest: topology-* first, then analysis-*)
3. How to handle knowls that could belong to multiple sections?
