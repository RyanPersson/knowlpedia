# Step 2: Sort Extracted Items by Dependency

## Your Task

Take the extraction report from Step 1 and sort all items into a linear sequence ordered by logical dependency. Also determine which prerequisite concepts need knowls created.

## Input

You will receive the extraction report from Step 1 containing:
- Extracted definitions, theorems, lemmas, etc.
- Dependencies noted for each item
- Prerequisites referenced but not defined
- Notational conventions

## Output Format

Produce two sections:

```markdown
# Dependency Analysis: [Course/Notes Title]

## Prerequisites to Create

Items referenced in the notes but not defined there. These should have knowls created (in Step 3) before the extracted content.

1. [Type]: [Name] — [Brief description of what's needed]
2. [Type]: [Name] — [Brief description]
...

## Sorted Sequence

All items (prerequisites + extracted) in dependency order:

1. [Type]: [Name] [P]
2. [Type]: [Name] [P]
3. [Type]: [Name] [E:5]
4. [Type]: [Name] [E:2]
...
```

Where:
- `[P]` = Prerequisite (you'll create in Step 3)
- `[E:N]` = Extracted item N from Step 1

## Sorting Process

### 1. Identify All Prerequisites

From the extraction report:
- Items listed in "Prerequisites (referenced but not defined)"
- Dependencies noted on extracted items that don't have matching extractions
- Implicit dependencies (e.g., "subgroup" requires "group")

Categorize prerequisites:
- **Essential**: Must have a knowl (core concepts used throughout)
- **Optional**: Could have a knowl (mentioned once, readers likely know it)
- **External**: Beyond scope, just mention but don't create (e.g., "real numbers")

```markdown
## Prerequisites to Create

### Essential Prerequisites
1. Definition: Group — foundational structure, referenced in 15+ items
2. Definition: Homomorphism — used in kernel, isomorphism theorems

### Optional Prerequisites (recommend including)
3. Definition: Binary operation — helps formalize group definition
4. Definition: Equivalence relation — used in coset discussion

### External (do not create, assume known)
- Real numbers and basic arithmetic
- Set theory fundamentals
- Function basics
```

### 2. Build Dependency Graph

For each item, list what it directly depends on:

```
Group → [Binary operation, Set]
Subgroup → [Group]
Coset → [Subgroup]
Lagrange's Theorem → [Coset, Order of group]
First Isomorphism Theorem → [Homomorphism, Kernel, Quotient group, Isomorphism]
```

### 3. Topological Sort

Order items so every dependency appears earlier:

**Rules:**
- Prerequisites before extracted items that use them
- Definitions before theorems that use them
- Lemmas before theorems they support
- Theorems before their corollaries

**Tie-breaking:**
- More fundamental concepts first
- Simpler concepts before complex
- Alphabetical when truly equivalent

### 4. Handle Circular or Missing Dependencies

**Apparent circular dependencies:**
- Identify which concept is truly primitive
- Usually the "structure" comes before "properties of the structure"

**Missing items:**
- If an extracted item references something not in the notes AND not in prerequisites, flag it:
```markdown
**Note:** Item 7 references "normal series" which is not defined or listed as prerequisite. Adding to prerequisites.
```

## Example Output

```markdown
# Dependency Analysis: Abstract Algebra I (Lecture Notes)

## Prerequisites to Create

### Essential Prerequisites
1. Definition: Set — foundational, assumed but worth having for completeness
2. Definition: Binary operation — needed to define algebraic structures
3. Definition: Function — needed for homomorphisms
4. Definition: Equivalence relation — needed for cosets/quotients
5. Definition: Partition — equivalence relation corollary, useful for cosets

### Optional Prerequisites (including)
6. Definition: Injection — for monomorphisms
7. Definition: Surjection — for epimorphisms
8. Definition: Bijection — for isomorphisms

### External (not creating)
- Integers, rationals, reals, complex numbers
- Basic logic and proof techniques
- Modular arithmetic (referenced but extensive)

## Sorted Sequence

1. Definition: Set [P]
2. Definition: Binary operation [P]
3. Definition: Function [P]
4. Definition: Injection [P]
5. Definition: Surjection [P]
6. Definition: Bijection [P]
7. Definition: Equivalence relation [P]
8. Definition: Partition [P]
9. Axiom: Group axioms [E:1]
10. Definition: Group [E:2]
11. Definition: Abelian group [E:3]
12. Definition: Order of a group [E:6]
13. Definition: Order of an element [E:7]
14. Definition: Subgroup [E:4]
15. Lemma: Subgroup criterion [E:12]
16. Definition: Cyclic group [E:8]
17. Proposition: Cyclic groups are abelian [E:20]
18. Definition: Coset [E:5]
19. Proposition: Cosets partition the group [E:21]
20. Definition: Index of a subgroup [E:9]
21. Theorem: Lagrange's Theorem [E:13]
22. Corollary: Order of element divides order of group [E:22]
23. Definition: Normal subgroup [E:10]
24. Definition: Quotient group [E:11]
25. Definition: Group homomorphism [E:14]
26. Definition: Kernel [E:15]
27. Definition: Image [E:16]
28. Proposition: Kernel is a normal subgroup [E:23]
29. Definition: Group isomorphism [E:17]
30. Theorem: First Isomorphism Theorem [E:18]
31. Theorem: Second Isomorphism Theorem [E:19]

## Dependency Notes

- Items 1-8 are prerequisites; content to be created in Step 3
- Items 9-31 are extracted; original text available from Step 1
- Corollary E:22 depends on Theorem E:13 (Lagrange)
- First Isomorphism Theorem requires: quotient group, homomorphism, kernel, isomorphism
```

## Validation Checklist

Before submitting:

- [ ] Every dependency of item N appears at position < N
- [ ] All "dependencies noted" from Step 1 are accounted for
- [ ] Prerequisites are categorized (essential/optional/external)
- [ ] No extracted item appears before its prerequisites
- [ ] Each entry has a clear reference ([P] or [E:N])

## After Completion

Output the complete dependency analysis. This will be passed to Step 3 for knowl creation. The `[E:N]` references link back to the original extracted text in Step 1.
