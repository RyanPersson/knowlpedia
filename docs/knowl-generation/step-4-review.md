# Step 5: Review for Correctness and Rigor

## Your Task

Systematically review all knowls from Step 4 for mathematical correctness, logical consistency, and appropriate rigor. Flag any errors, ambiguities, or issues. Provide corrected versions where needed.

## Input

You will receive the complete set of cross-linked knowls from Step 4.

## Output Format

Produce a review report with the following structure:

```markdown
# Knowl Review Report: [Subject] — [Level]

## Summary
- Total knowls reviewed: [N]
- Issues found: [M]
- Critical errors: [X]
- Minor issues: [Y]
- Suggestions: [Z]

## Critical Errors
[Issues that make the content mathematically incorrect]

## Minor Issues
[Issues that affect clarity or completeness but are not incorrect]

## Suggestions
[Optional improvements that could enhance the knowls]

## Detailed Findings

### [slug].md
**Status:** [PASS | NEEDS CORRECTION | FLAG FOR REVIEW]
**Issues:**
- [Description of issue]
**Correction:**
[If applicable, the corrected content]

---
[Repeat for each knowl with findings]

## Knowls Passed Without Issues
- [slug].md
- [slug].md
...
```

## Review Criteria

### 1. Mathematical Correctness

Check each statement for:

**Definitions:**
- Is the definition logically well-formed?
- Does it match the standard/accepted definition?
- Are all terms in the definition either primitive or previously defined?
- Are quantifiers correct (∀ vs ∃, order of quantifiers)?

**Theorems/Lemmas/Propositions:**
- Is the statement true as written?
- Are all hypotheses stated?
- Is the conclusion correctly formulated?
- Are edge cases handled (empty set, zero, trivial cases)?

**Examples:**
- Are the examples actually instances of the definition?
- Are numerical computations correct?
- Do counterexamples actually fail the relevant condition?

### 2. Logical Consistency

- Do definitions align with how terms are used in theorems?
- Are there contradictions between knowls?
- Is notation consistent across knowls (same symbol for same concept)?
- Do dependency relationships make sense (no circular definitions)?

### 3. Completeness

- Are all hypotheses explicitly stated?
- Are domains and codomains specified for functions?
- Are sets vs elements distinguished clearly?
- Is it clear what structure is being assumed?

### 4. Rigor Level Appropriateness

- Does the formality match the course level?
- Are measure-theoretic distinctions made when needed (500+ level)?
- Are set-theoretic issues addressed when relevant?
- Is categorical language used appropriately for the level?

### 5. Common Error Patterns

Watch specifically for:

| Error Type | Example |
|------------|---------|
| Missing quantifiers | "If $f$ is continuous, $f$ is bounded" (should be "on a compact set") |
| Implicit assumptions | "Let $G/H$ be the quotient" (H must be normal) |
| Domain errors | "√x is continuous" (only for x ≥ 0) |
| Notation ambiguity | Using $\subset$ for both strict and non-strict containment |
| Off-by-one errors | "The symmetric group $S_n$ has $n$ elements" (should be $n!$) |
| Order of operations | "ab⁻¹" in a non-abelian group (is it $a \cdot b^{-1}$ or $(ab)^{-1}$?) |
| Vacuous truth issues | "All elements of ∅ have property P" (true but possibly misleading) |
| Finite vs infinite | Theorem stated for finite groups but applied to infinite |

### 6. Cross-Link Validity

- Do all linked knowls exist?
- Are links pointing to the correct knowl (not a similarly-named one)?
- Is the display text appropriate for the link target?

## Issue Severity Classification

**Critical Error** — Must be fixed:
- Mathematical statement is false
- Definition is non-standard in a misleading way
- Missing hypothesis makes theorem false
- Example contradicts definition

**Minor Issue** — Should be addressed:
- Ambiguous phrasing that could confuse
- Missing edge case in examples
- Notation inconsistency
- Incomplete hypothesis (but inferable from context)

**Suggestion** — Optional improvement:
- Better example could be added
- Proof sketch would be helpful
- Additional context would aid understanding
- Minor rewording for clarity

## Example Review Entry

```markdown
### quotient-group.md
**Status:** NEEDS CORRECTION
**Issues:**
1. [Critical] Definition does not explicitly require $H$ to be a normal subgroup. As written, the quotient is only defined for normal subgroups, but this constraint is missing.
2. [Minor] Example uses $\mathbb{Z}/n\mathbb{Z}$ notation without defining it.

**Correction:**
Replace:
> Let $G$ be a group and $H$ a subgroup. The *quotient group* $G/H$ is...

With:
> Let $G$ be a group and $H \trianglelefteq G$ a {{</* knowl id="normal-subgroup" text="normal subgroup" */>}}. The *quotient group* $G/H$ is the set of left cosets $\{gH : g \in G\}$ with the operation $(aH)(bH) = (ab)H$.

---

### subgroup.md
**Status:** PASS
No issues found.
```

## Special Attention Areas

For specific subjects, pay extra attention to:

**Analysis:**
- Pointwise vs uniform convergence
- Open vs closed intervals in hypotheses
- Continuity at endpoints
- Measure zero vs empty set

**Algebra:**
- Left vs right actions/cosets
- Normal vs arbitrary subgroups
- Ring with unity vs without
- Commutativity assumptions

**Topology:**
- Hausdorff assumptions
- Compactness vs sequential compactness
- Connectedness vs path-connectedness
- Base point choices

**Linear Algebra:**
- Finite vs infinite dimensional
- Field assumptions
- Column vs row vector conventions
- Ordered vs unordered bases

## Final Output

After the detailed review, provide:

1. **Corrected knowls** — Complete updated markdown for any knowl that needs changes
2. **List of passed knowls** — Confirmation that remaining knowls are correct
3. **Unresolved flags** — Any issues requiring human judgment (e.g., notational conventions, level-appropriateness questions)

```markdown
## Corrected Knowls

**`[slug].md`** *(corrected)*
```markdown
[complete corrected content]
```

---

## Unresolved Flags
- [slug].md: [Issue requiring human decision]
...
```
