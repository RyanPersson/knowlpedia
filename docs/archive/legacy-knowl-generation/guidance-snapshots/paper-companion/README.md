# Paper Companion Knowl Workflow

Generate a companion glossary for reading a mathematical paper. The resulting knowls let readers quickly "unknowl" prerequisite concepts without leaving the paper.

## Purpose

Academic papers assume background knowledge. This workflow extracts that implicit knowledge into a set of compact knowls that serve as a quick-reference companion—helping readers recall concepts they've seen before but don't have memorized.

**Use case:** You're reading a paper on spectral theory and encounter "Let $T$ be a compact operator on a Banach space." You know what these terms mean, but the precise definitions aren't fresh. You expand the knowl, spend 10 seconds confirming "right, maps bounded sets to relatively compact sets," and return to the paper.

## Workflow Overview

| Step | File | Purpose |
|------|------|---------|
| 1 | `step-1-identify-prerequisites.md` | Scan paper, identify assumed knowledge |
| 2 | `step-2-create-knowls.md` | Create compact knowls for prerequisites |
| 3 | `step-3-review.md` | Quick review for correctness and fit |

## Key Differences from Other Workflows

| Aspect | Course Generation | Lecture Extraction | Paper Companion |
|--------|-------------------|-------------------|-----------------|
| Goal | Teach a subject | Digitize notes | Aid reading |
| Content source | Generated | Extracted from notes | Generated for context |
| Knowl length | Medium (with examples) | Varies | Short (quick recall) |
| Dependency depth | Full course graph | Within notes | Flat (all prerequisites) |
| Audience | Learners | Note users | Paper readers |

## Design Principles

### Optimize for Recall, Not Learning

These knowls assume the reader has encountered the concept before. They're reminders, not introductions.

**Good:** "A **Banach space** is a complete normed vector space. 

### Context-Sensitive

Tailor knowls to the paper's usage. A "compact operator" knowl for an operator theory paper emphasizes spectral properties; for a PDE paper, it might emphasize embedding theorems.

### Minimal Friction

Reader should expand a knowl, scan it in 10 seconds, and return to the paper without losing their place. If a knowl requires serious study, it's too long.

## Usage

### Step 1: Identify Prerequisites

```
[Paste step-1-identify-prerequisites.md]

---

Paper: [Paste paper text or attach PDF]
Target audience: Graduate student in [field]
```

### Step 2: Create Knowls

```
[Paste step-2-create-knowls.md]

---

Prerequisite Analysis:
[Paste Step 1 output]

Paper Context:
- Field: [e.g., Functional Analysis]
- Key notation: [any non-standard notation]
```

### Step 3: Review

```
[Paste step-3-review.md]

---

Knowls:
[Paste Step 2 output]

Paper: [Available for reference]
```

## Output Structure

```
content/glossary/
  papers/
    [paper-slug]/
      banach-space.md
      compact-operator.md
      spectrum.md
      ...
```

Or integrate into the main glossary if concepts are broadly useful.

## When to Use This Workflow

**Good fit:**
- Reading a paper outside your exact specialty
- Preparing to discuss a paper in a seminar
- Creating resources for a reading group
- Self-study of research literature

**Less suitable:**
- Papers in your core specialty (you likely know the prerequisites)
- Survey papers (they usually define terms themselves)
- Papers requiring fundamentally new background (use the course generation workflow instead)

## File List

- `README.md` — This file
- `step-1-identify-prerequisites.md` — Scan paper for assumed knowledge
- `step-2-create-knowls.md` — Create compact companion knowls
- `step-3-review.md` — Quick review for correctness and fit
