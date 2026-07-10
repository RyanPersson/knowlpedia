# Step 1: Identify Paper Prerequisites

## Your Task

Scan the provided academic paper and identify all mathematical concepts, definitions, and results that the paper **uses**. These are the prerequisites a reader needs to "unknowl" while reading.

## Input

You will receive:
- **Paper**: The full text of a mathematical paper (LaTeX, PDF text, or markdown)
- **Target audience** (optional): e.g., "advanced undergraduate"

## Output Format

```markdown
# Prerequisite Analysis: [Paper Title]

**Authors:** [Authors]
**Field:** [Primary mathematical field]
**Target audience:** [Inferred or specified]

## Core Prerequisites

Essential concepts used throughout the paper. Reader must know these.

| Concept | First Occurrence | Usage Frequency | Notes |
|---------|------------------|-----------------|-------|
| [Term] | Section/Page | high/medium/low | [Brief note] |
| ... | ... | ... | ... |

## Secondary Prerequisites

Concepts used in specific sections or proofs. Helpful but not essential.

| Concept | Where Used | Notes |
|---------|------------|-------|
| [Term] | [Section] | [Brief note] |
| ... | ... | ... |

## Notation

Non-standard or field-specific notation the paper uses without definition.

| Notation | Meaning | Standard? |
|----------|---------|-----------|
| $[symbol]$ | [meaning] | [yes/no/field-specific] |
| ... | ... | ... |

## Assumed Background

Broad areas the paper assumes familiarity with (not individual knowls, but context):
- [e.g., "Basic measure theory at the level of Folland Ch. 1-2"]
- [e.g., "Familiarity with category theory notation"]

## Recommended Knowl Set

Prioritized list of concepts to create knowls for:

### High Priority (create these)
1. [Concept] — [why essential]
2. [Concept] — [why essential]
...

### Medium Priority (recommended)
1. [Concept] — [why helpful]
...

### Low Priority (standard background, skip unless audience needs)
1. [Concept]
...
```

## Identification Guidelines

### What to Include

**Include as prerequisites:**
- Terms used without definition: "Let $X$ be a Banach space..."
- Results cited without proof: "By the Hahn-Banach theorem..."
- Notation assumed known: "$L^p$ spaces", "$\sigma$-algebra"
- Concepts in hypothesis: "Assume $f$ is measurable..."

### What to Exclude

**Do NOT include:**

- elementary terms (set, function, integer) unless audience needs them
- Concepts mentioned only in references/related work

### Frequency Assessment

- **High**: Used in main theorem statements, appears in multiple sections
- **Medium**: Used in proofs or specific lemmas
- **Low**: Mentioned once or in remarks

### Audience Calibration

Adjust the prerequisite list based on target audience:

| Audience | Include | Exclude |
|----------|---------|---------|
| Advanced undergrad | Field axioms, basic topology | — |
| Beginning graduate | Specialized theorems | Measure theory basics |
| Specialist | Cutting-edge results | Standard field knowledge |

## Example Output (abbreviated)

```markdown
# Prerequisite Analysis: "Spectral Properties of Composition Operators"

**Authors:** Smith, Jones
**Field:** Functional Analysis / Operator Theory
**Target audience:** Graduate student in analysis

## Core Prerequisites

| Concept | First Occurrence | Usage Frequency | Notes |
|---------|------------------|-----------------|-------|
| Banach space | Abstract, §1 | high | Paper works in general Banach spaces |
| Composition operator | §1.1 | high | Central object of study |
| Spectrum of an operator | §2 | high | Main focus of results |
| Compact operator | §3 | medium | Key theorem hypothesis |
| Hardy space $H^p$ | §4 | medium | Main example class |

## Secondary Prerequisites

| Concept | Where Used | Notes |
|---------|------------|-------|
| Fredholm operator | §5, Thm 5.3 | One theorem only |
| Carleson measure | §4.2 | Technical lemma |

## Notation

| Notation | Meaning | Standard? |
|----------|---------|-----------|
| $C_\varphi$ | Composition operator induced by $\varphi$ | Field-specific |
| $\sigma(T)$ | Spectrum of operator $T$ | Standard |
| $\sigma_p(T)$ | Point spectrum | Standard |

## Recommended Knowl Set

### High Priority
1. Banach space — foundational for all results
2. Composition operator — must understand to read paper
3. Spectrum of an operator — main object of study
4. Compact operator — key hypothesis in main theorems

### Medium Priority
1. Hardy space — main example, but §4 is self-contained
2. Bounded linear operator — probably known, but quick reference helps

### Low Priority
1. Fredholm operator — only §5
2. Carleson measure — technical, only one lemma
```

## After Completion

This analysis will be passed to Step 2 for knowl creation. Focus on the **High Priority** and **Medium Priority** items from the Recommended Knowl Set.
