# Knowl Generation Workflow

This directory contains instructions for generating a complete set of mathematical knowls (definitions, theorems, lemmas, etc.) for a university-level math course.

## Overview

The workflow consists of 4 steps. Steps 1-2 are sequential; Step 3 is **parallelizable** across multiple agents.

| Step | File | Input | Output |
|------|------|-------|--------|
| 1 | `step-1-enumeration.md` | Subject + Level | Categorized list of all items |
| 2 | `step-2-dependency-sort.md` | List from Step 1 | Topologically sorted sequence + slug manifest |
| 3 | `step-3-create-and-link.md` | Slug manifest + batch assignment | Knowls with `{{</* knowl */>}}` links included |
| 4 | `step-4-review.md` | All knowls from Step 3 | Review report + corrected knowls |

## Parallelization (Step 3)

Step 3 is designed for parallel execution:

1. **Slug Manifest**: Step 2 outputs a complete list of all slugs (filenames)
2. **Batch Assignment**: Divide the sorted list into batches (e.g., items 1-40, 41-80, etc.)
3. **Parallel Agents**: Each agent receives:
   - The full slug manifest (for cross-linking)
   - Its assigned batch of knowls to create
4. **Independent Execution**: Agents create knowls with all links included—no sequential dependency

```
Agent A: Creates items 1-40 with links to any of the 400 slugs
Agent B: Creates items 41-80 with links to any of the 400 slugs
Agent C: Creates items 81-120 with links to any of the 400 slugs
...
```

## Usage

### Running the Workflow

**Step 1:**
```
Subject: Real Analysis
Level: 400-level
Scope: Single-variable, Riemann integration (not Lebesgue)

[Paste contents of step-1-enumeration.md]
```

**Step 2:**
```
[Paste contents of step-2-dependency-sort.md]

---

Input from Step 1:
[Paste the enumeration output]
```

**Step 3 (parallel):**
```
[Paste contents of step-3-create-and-link.md]

---

## Slug Manifest
[Full list of all slugs from Step 2]

## Your Batch
Process items 1-40:
[Items 1-40 from sorted list]
```

**Step 4:**
```
[Paste contents of step-4-review.md]

---

[All knowls from all Step 3 agents]
```

## Course Level Guidelines

| Level | Typical Courses | Rigor Expectation |
|-------|----------------|-------------------|
| 200-level | Calculus sequence, Linear Algebra I | Computational focus, informal definitions acceptable |
| 300-level | Intro to Proofs, Abstract Algebra I, Analysis I | First exposure to rigor, ε-δ definitions, basic proofs |
| 400-level | Algebra II, Real Analysis, Topology I | Full undergraduate rigor, Rudin/Dummit level |
| 500-level | Graduate Algebra, Measure Theory, Functional Analysis | Graduate rigor, Folland/Lang level |
| 600-level | Specialized topics, research preparation | Research-level precision |

## Output Structure

After completing all steps, you will have:

```
content/glossary/
  [subject-slug]/
    group.md
    subgroup.md
    lagranges-theorem.md
    ...
```

Or integrate directly into the existing `content/glossary/` structure.

## Quality Checklist

Before deploying generated knowls:

- [ ] All cross-links resolve (no broken `{{</* knowl */>}}` references)
- [ ] Mathematical content reviewed by subject-matter expert
- [ ] Test build with `hugo server` — no KaTeX errors
- [ ] Spot-check knowl expansion in browser
- [ ] Verify nested knowls display correctly

## Customization

### Adjusting Rigor Level

Edit the "Level Appropriateness" sections in Step 3 and Step 4 to match your pedagogical goals.

### Adding Fields

To add custom front matter fields (e.g., `prerequisites`, `related`, `source`), modify the YAML template in Step 3.

### Notation Conventions

If your course uses non-standard notation, add a "Notation" section to Step 3 specifying your conventions.

## File List

- `README.md` — This file
- `step-1-enumeration.md` — Generate complete item list
- `step-2-dependency-sort.md` — Sort by logical dependency + generate slug manifest
- `step-3-create-and-link.md` — Create knowl content with links (parallelizable)
- `step-4-review.md` — Review for correctness
