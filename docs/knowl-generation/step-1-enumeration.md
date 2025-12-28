# Step 1: Enumerate Definitions, Theorems, and Lemmas

## Your Task

Generate a **complete and exhaustive** list of all definitions, theorems, lemmas, propositions, and corollaries that would appear in a university course on the specified subject at the specified level.

## Input Parameters

You will be given:
- **Subject**: The mathematical topic (e.g., "Real Analysis", "Abstract Algebra", "Topology")
- **Level**: Course level indicator, one of:
  - `200-level`: Introductory undergraduate (e.g., Calculus-based, computational focus)
  - `300-level`: Intermediate undergraduate (e.g., first proofs course, introductory rigor)
  - `400-level`: Advanced undergraduate (e.g., Rudin-style analysis, Dummit & Foote algebra)
  - `500-level`: Beginning graduate (e.g., qualifying exam preparation, Folland, Lang)
  - `600-level`: Advanced graduate (e.g., research preparation, specialized monographs)
- **Scope constraints** (optional): Any specific inclusions or exclusions

## Output Format

Produce a single markdown code block containing the complete list. Use the following format:

```markdown
# [Subject] — [Level] Enumeration

## Definitions
- [Name of definition]
- [Name of definition]
...

## Axioms
- [Name of axiom or axiomatic system]
...

## Theorems
- [Name of theorem]
- [Name of theorem]
...

## Lemmas
- [Name of lemma]
...

## Propositions
- [Name of proposition]
...

## Corollaries
- [Name of corollary]
...
```

## Requirements

1. **Do NOT number the items.** Use simple bullet points only.

2. **Be exhaustive for the level.** Include everything a student would encounter in a standard course at this level. When in doubt, include it.

3. **Use standard mathematical names.** Use the most common/canonical name for each item:
   - Prefer "Heine-Borel Theorem" over "Theorem 2.41"
   - Prefer "Bolzano-Weierstrass Theorem" over "Sequential Compactness Theorem"
   - For unnamed results, use a descriptive name (e.g., "Continuity of monotone functions on intervals")

4. **Distinguish item types correctly:**
   - **Definition**: Introduces a new concept or object
   - **Axiom**: A foundational assumption (e.g., field axioms, ZFC axioms, group axioms)
   - **Theorem**: A major result, often named
   - **Lemma**: A helper result used to prove theorems
   - **Proposition**: A result of moderate importance
   - **Corollary**: A direct consequence of a theorem

5. **Include foundational prerequisites** that are explicitly used in the course, even if they come from earlier courses. For example, a 400-level real analysis course should include "Completeness of the real numbers" even though students learned it earlier.

6. **Scope by level appropriately:**
   - 300-level Real Analysis: ε-δ limits, continuity, basic differentiation/integration, sequences, series
   - 400-level Real Analysis: Metric spaces, compactness, connectedness, uniform convergence, Riemann integration, basic measure theory introduction
   - 500-level Real Analysis: Lebesgue measure and integration, L^p spaces, modes of convergence, Fubini/Tonelli, Radon-Nikodym

## Example

For input: **Subject**: Group Theory, **Level**: 300-level

```markdown
# Group Theory — 300-level Enumeration

## Definitions
- Group
- Abelian group
- Subgroup
- Trivial subgroup
- Proper subgroup
- Order of a group
- Order of an element
- Cyclic group
- Generator
- Symmetric group
- Alternating group
- Dihedral group
- Coset (left and right)
- Index of a subgroup
- Normal subgroup
- Quotient group
- Group homomorphism
- Group isomorphism
- Kernel of a homomorphism
- Image of a homomorphism
- Direct product of groups
- Simple group
- Center of a group
- Centralizer
- Normalizer
- Conjugacy class
- Group action
- Orbit
- Stabilizer

## Axioms
- Group axioms (closure, associativity, identity, inverses)

## Theorems
- Lagrange's Theorem
- Cayley's Theorem
- First Isomorphism Theorem
- Second Isomorphism Theorem
- Third Isomorphism Theorem
- Cauchy's Theorem (for finite groups)
- Sylow's First Theorem
- Sylow's Second Theorem
- Sylow's Third Theorem
- Fundamental Theorem of Finite Abelian Groups
- Orbit-Stabilizer Theorem
- Class Equation

## Lemmas
- Subgroup criterion (two-step subgroup test)
- Normal subgroup criterion
- Properties of cosets
- Homomorphism preserves identity and inverses

## Propositions
- Cyclic groups are abelian
- Subgroups of cyclic groups are cyclic
- Order of element divides order of group
- Groups of prime order are cyclic
- Center is a normal subgroup
- Kernel is a normal subgroup

## Corollaries
- Fermat's Little Theorem (as corollary of Lagrange)
- Euler's Theorem (as corollary of Lagrange)
- Groups of order p² are abelian
```

## After Completion

Once you have produced this list, it will be passed to Step 2 for dependency sorting. Do not proceed to Step 2 yourself—output only the enumeration.
