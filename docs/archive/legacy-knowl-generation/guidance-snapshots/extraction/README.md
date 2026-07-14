# Knowl Extraction Workflow

This directory contains instructions for extracting mathematical knowls from existing lecture notes or course materials.

## Overview

Unlike the **generation** workflow (which creates knowls from a subject specification), this workflow **extracts** knowls from existing documents, preserving the author's formulations while standardizing format.

| Step | File | Input | Output |
|------|------|-------|--------|
| 1 | `step-1-extraction.md` | Lecture notes | Catalogued items with source text |
| 2 | `step-2-dependency-sort.md` | Extraction from Step 1 | Sorted sequence + prerequisites list |
| 3 | `step-3-knowl-creation.md` | Steps 1 + 2 output | Markdown file for each knowl |
| 4 | `step-4-cross-linking.md` | Knowls from Step 3 | Knowls with `{{</* knowl */>}}` links |
| 5 | `step-5-review.md` | Linked knowls + source | Review report + corrections |

## Key Differences from Generation Workflow

| Aspect | Generation | Extraction |
|--------|------------|------------|
| Source of content | Agent's mathematical knowledge | Provided lecture notes |
| Author voice | Standardized | Preserved where possible |
| Prerequisites | Assumed at level | Identified from gaps in notes |
| Fidelity checks | N/A | Critical (Step 5) |
| Notation | Standardized | Matches source |

## Usage

### Preparing Input

**Supported source formats:**
- Markdown (`.md`)
- LaTeX (`.tex`)
- Plain text
- PDF text extraction
- Handwritten notes (transcribed)

**Recommended preparation:**
1. Combine all lecture notes into a single document or ordered set
2. Note any non-standard notation or conventions
3. Identify the course level for rigor calibration

### Running the Workflow

**Step 1:**
```
[Paste contents of step-1-extraction.md]

---

Source Format: LaTeX
Course Context: Undergraduate Abstract Algebra (400-level)

Lecture Notes:
[Paste or attach lecture notes]
```

**Step 2:**
```
[Paste contents of step-2-dependency-sort.md]

---

Extraction Report from Step 1:
[Paste extraction output]
```

**Steps 3-5:** Follow the same pattern, passing forward outputs.

### Handling Large Note Sets

For courses with extensive notes:

1. **Step 1**: Can process in chunks (Lectures 1-5, then 6-10, etc.)
   - Combine extraction reports before Step 2

2. **Step 2**: Process complete extraction at once
   - Dependency analysis needs full picture

3. **Step 3**: Process in batches
   - Prerequisites first
   - Then extracted items in groups of 15-25

4. **Steps 4-5**: Can batch if needed

## Workflow Outputs

### Knowl Files

```
content/glossary/
  [course-slug]/
    group.md              # Prerequisite (created)
    subgroup.md           # Extracted from Lecture 2
    coset.md              # Extracted from Lecture 3
    lagranges-theorem.md  # Extracted from Lecture 3
    ...
```

### Metadata

Each knowl includes:
```yaml
---
title: "Coset"
type: "definition"
summary: "A translate of a subgroup"
source: "Lecture 3, page 12"  # Traceability to source
build:
  list: local
---
```

### Review Report

Step 5 produces a report documenting:
- Issues found and corrections made
- Fidelity to source assessment
- Items requiring human review
- Notation standardization recommendations

## Quality Considerations

### Preserving Author Voice

The extraction workflow prioritizes fidelity:
- Keep author's mathematical formulations
- Maintain their notation choices
- Preserve their pedagogical ordering
- Add only minimal enhancements

### When to Deviate

Deviate from source only when:
- Source contains mathematical errors
- Formatting prevents proper rendering
- Notation is ambiguous or inconsistent
- Critical hypotheses are missing

Document all deviations in Step 5 review.

### Common Extraction Challenges

| Challenge | Approach |
|-----------|----------|
| Informal definitions | Formalize while preserving intent |
| Missing hypotheses | Add explicitly, note in review |
| Inconsistent notation | Standardize, document choices |
| Implicit prerequisites | Identify and create in Step 2-3 |
| Multiple definitions of same term | Create both, note relationship |

## Integration with Existing Knowls

If you have existing knowls from other sources:

1. **Merge prerequisites**: Don't duplicate existing definitions
2. **Check consistency**: Verify notation matches
3. **Cross-link**: New knowls can reference existing ones
4. **Namespace if needed**: Use subdirectories for course-specific content

## File List

- `README.md` — This file
- `step-1-extraction.md` — Extract items from lecture notes
- `step-2-dependency-sort.md` — Sort and identify prerequisites
- `step-3-knowl-creation.md` — Create knowl content
- `step-4-cross-linking.md` — Add inter-knowl links
- `step-5-review.md` — Review for correctness and fidelity
