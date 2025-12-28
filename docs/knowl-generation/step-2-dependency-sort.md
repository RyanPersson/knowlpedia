# Step 2: Sort by Dependency

## Your Task

Take the enumerated list of definitions, theorems, lemmas, propositions, and corollaries from Step 1 and **sort them into a single linear sequence ordered by logical dependency**.

## Input

You will receive a categorized list from Step 1 containing:
- Definitions
- Axioms
- Theorems
- Lemmas
- Propositions
- Corollaries

## Output Format

Produce a single markdown code block containing a **flat, ordered list** where each item can only depend on items that appear earlier in the list.

```markdown
# [Subject] — [Level] Dependency-Sorted Sequence

1. [Type]: [Name]
2. [Type]: [Name]
3. [Type]: [Name]
...
```

Where `[Type]` is one of: `Definition`, `Axiom`, `Theorem`, `Lemma`, `Proposition`, `Corollary`.

## Sorting Rules

### 1. Topological Ordering by Dependency

An item X **depends on** item Y if:
- X's statement uses a concept defined in Y
- X's proof requires Y as a prerequisite
- X is a corollary of Y

**Constraint**: For every item in position n, all items it depends on must appear in positions < n.

### 2. Dependency Precedence

When determining order:

1. **Axioms** come first (they depend on nothing within the system)
2. **Definitions** come before any theorem/lemma/proposition that uses them
3. **Lemmas** come before the theorems they support
4. **Theorems** come before their corollaries
5. **Foundational definitions** (e.g., "group") come before specialized ones (e.g., "normal subgroup")

### 3. Tie-Breaking

When two items have no dependency relationship between them:
- Place the more fundamental/general concept first
- Place simpler concepts before more complex ones
- When still tied, use alphabetical order

### 4. Circular Dependencies

Mathematical definitions occasionally have apparent circular dependencies (e.g., "ring" and "ideal" are sometimes introduced together). Resolve these by:
- Identifying which concept is truly primitive
- If genuinely co-dependent, place the structural definition first (the "thing") before the relational definition (properties of the thing)

## Example

**Input** (abbreviated):
```markdown
## Definitions
- Group
- Subgroup
- Coset
- Normal subgroup
- Quotient group
- Group homomorphism
- Kernel

## Axioms
- Group axioms

## Theorems
- Lagrange's Theorem
- First Isomorphism Theorem

## Lemmas
- Subgroup criterion

## Corollaries
- Order of element divides order of group
```

**Output**:
```markdown
# Group Theory — Dependency-Sorted Sequence

1. Axiom: Group axioms
2. Definition: Group
3. Definition: Subgroup
4. Lemma: Subgroup criterion
5. Definition: Coset
6. Theorem: Lagrange's Theorem
7. Corollary: Order of element divides order of group
8. Definition: Normal subgroup
9. Definition: Quotient group
10. Definition: Group homomorphism
11. Definition: Kernel
12. Theorem: First Isomorphism Theorem
```

**Rationale**:
- Group axioms → Group (axioms define the group)
- Group → Subgroup (subgroup requires group)
- Subgroup → Subgroup criterion (criterion is about subgroups)
- Subgroup → Coset (cosets are defined via subgroups)
- Coset → Lagrange's Theorem (theorem counts cosets)
- Lagrange → Order divides (direct corollary)
- Subgroup → Normal subgroup (special type of subgroup)
- Normal subgroup → Quotient group (quotient requires normality)
- Group → Homomorphism (maps between groups)
- Homomorphism → Kernel (kernel of a homomorphism)
- Quotient group + Kernel + Homomorphism → First Isomorphism Theorem

## Validation Checklist

Before submitting your sorted list, verify:

- [ ] Every definition used in item n is defined in some item < n
- [ ] Every theorem/lemma cited in item n appears in some item < n
- [ ] Axioms appear at or near the beginning
- [ ] No corollary appears before its parent theorem
- [ ] The sequence makes pedagogical sense (could be taught in this order)

## After Completion

Once you have produced the dependency-sorted sequence, it will be passed to Step 3 for knowl creation. Do not proceed to Step 3 yourself—output only the sorted list.
