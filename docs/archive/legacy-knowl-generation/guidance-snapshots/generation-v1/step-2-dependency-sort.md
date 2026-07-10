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

Produce **two outputs**:

### 1. Dependency-Sorted Sequence

A flat, ordered list where each item can only depend on items that appear earlier in the list.

```markdown
# [Subject] — [Level] Dependency-Sorted Sequence

1. [Type]: [Name] → `slug.md`
2. [Type]: [Name] → `slug.md`
3. [Type]: [Name] → `slug.md`
...
```

Where `[Type]` is one of: `Definition`, `Axiom`, `Theorem`, `Lemma`, `Proposition`, `Corollary`.

### 2. Slug Manifest

A complete list of all slugs for cross-referencing (used by Step 3 agents for linking):

```markdown
# Slug Manifest

group.md
subgroup.md
coset.md
lagranges-theorem.md
...
```

### Slug Convention

Convert names to URL-friendly slugs:
- Lowercase
- Replace spaces with hyphens
- Remove apostrophes, parentheses, and special characters
- Examples:
  - "Lagrange's Theorem" → `lagranges-theorem.md`
  - "Group" → `group.md`
  - "L^p spaces" → `lp-spaces.md`
  - "First Isomorphism Theorem" → `first-isomorphism-theorem.md`

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

1. Axiom: Group axioms → `group-axioms.md`
2. Definition: Group → `group.md`
3. Definition: Subgroup → `subgroup.md`
4. Lemma: Subgroup criterion → `subgroup-criterion.md`
5. Definition: Coset → `coset.md`
6. Theorem: Lagrange's Theorem → `lagranges-theorem.md`
7. Corollary: Order of element divides order of group → `order-divides-group-order.md`
8. Definition: Normal subgroup → `normal-subgroup.md`
9. Definition: Quotient group → `quotient-group.md`
10. Definition: Group homomorphism → `group-homomorphism.md`
11. Definition: Kernel → `kernel-group.md`
12. Theorem: First Isomorphism Theorem → `first-isomorphism-theorem-groups.md`

# Slug Manifest

group-axioms.md
group.md
subgroup.md
subgroup-criterion.md
coset.md
lagranges-theorem.md
order-divides-group-order.md
normal-subgroup.md
quotient-group.md
group-homomorphism.md
kernel-group.md
first-isomorphism-theorem-groups.md
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

Once you have produced the dependency-sorted sequence and slug manifest, they will be passed to Step 3 agents for knowl creation. Each Step 3 agent receives:
1. The complete slug manifest (for cross-linking)
2. A batch of items from the sorted sequence (their assignment)

Do not proceed to Step 3 yourself—output only the sorted list and slug manifest.
