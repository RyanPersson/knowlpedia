# Knowl Generation Workflow

This directory contains instructions for generating a complete set of mathematical knowls (definitions, theorems, lemmas, etc.) for a university-level math course.

## Overview

The workflow consists of 5 sequential steps, each performed by an agent seeing only that step's instructions:

| Step | File | Input | Output |
|------|------|-------|--------|
| 1 | `step-1-enumeration.md` | Subject + Level | Categorized list of all items |
| 2 | `step-2-dependency-sort.md` | List from Step 1 | Topologically sorted sequence |
| 3 | `step-3-knowl-creation.md` | Sorted list from Step 2 | Markdown file for each knowl |
| 4 | `step-4-cross-linking.md` | Knowls from Step 3 | Knowls with `{{</* knowl */>}}` links |
| 5 | `step-5-review.md` | Linked knowls from Step 4 | Review report + corrected knowls |

## Usage

### Running the Workflow

For each step, provide the agent with:
1. The instruction document for that step
2. The output from the previous step (except Step 1)
3. The subject and level parameters (Step 1 only)

### Example Invocation

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

**Steps 3-5:** Follow the same pattern.

### Batch Processing for Large Courses

Step 3 (knowl creation) may require multiple agent calls for large courses. Specify ranges:

```
Process items 1-25 of the following sorted list:
[Paste step-3-knowl-creation.md instructions]
[Paste sorted list]
```

Then:
```
Process items 26-50...
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

Edit the "Level Appropriateness" sections in Steps 3 and 5 to match your pedagogical goals.

### Adding Fields

To add custom front matter fields (e.g., `prerequisites`, `related`, `source`), modify the YAML template in Step 3.

### Notation Conventions

If your course uses non-standard notation, add a "Notation" section to Step 3 specifying your conventions.

## File List

- `README.md` — This file
- `step-1-enumeration.md` — Generate complete item list
- `step-2-dependency-sort.md` — Sort by logical dependency
- `step-3-knowl-creation.md` — Create knowl content
- `step-4-cross-linking.md` — Add inter-knowl links
- `step-5-review.md` — Review for correctness
