# Step 5: Review for Correctness, Rigor, and Fidelity

## Your Task

Review all knowls from Step 4 for:
1. **Mathematical correctness** — Are statements true and precise?
2. **Fidelity to source** — Do extracted items preserve the author's intent?
3. **Consistency** — Are notation and conventions uniform?
4. **Completeness** — Are prerequisites properly created?

Flag errors, ambiguities, and deviations. Provide corrections where needed.

## Input

You will receive:
1. The complete set of cross-linked knowls from Step 4
2. The original extraction report from Step 1 (for source comparison)
3. The source lecture notes (if available for reference)

## Output Format

```markdown
# Knowl Review Report: [Course/Notes Title]

## Summary
- Total knowls reviewed: [N]
- Prerequisite knowls: [P]
- Extracted knowls: [E]
- Issues found: [M]
  - Critical errors: [X]
  - Fidelity issues: [F]
  - Minor issues: [Y]
  - Suggestions: [Z]

## Critical Errors
[Mathematically incorrect content]

## Fidelity Issues
[Deviations from source that change meaning]

## Minor Issues
[Clarity, completeness, or style problems]

## Suggestions
[Optional improvements]

## Detailed Findings

### [slug].md [P|E:N]
**Status:** [PASS | NEEDS CORRECTION | FLAG FOR REVIEW]
**Category:** [Critical | Fidelity | Minor | Suggestion]
**Issue:** [Description]
**Source comparison:** [If relevant, quote original]
**Correction:**
[Corrected content if applicable]

---

## Knowls Passed Without Issues
- [slug].md [P]
- [slug].md [E:3]
...
```

## Review Criteria

### 1. Mathematical Correctness

#### For All Items

| Check | What to Verify |
|-------|----------------|
| Logical precision | Quantifiers correct? Hypotheses complete? |
| Truthfulness | Is the statement actually true? |
| Well-formedness | Is the definition/statement syntactically valid? |
| Edge cases | Are boundary conditions handled? |

#### Common Errors

| Error Type | Example | Fix |
|------------|---------|-----|
| Missing quantifier | "If f is continuous, f is bounded" | Add "on a compact set" |
| Wrong quantifier order | "∃ε ∀δ" vs "∀ε ∃δ" | Check limit definitions |
| Implicit assumptions | "Let G/H be the quotient" | H must be normal |
| Domain errors | "log(x) is continuous" | Only for x > 0 |
| Off-by-one | "S_n has n elements" | Has n! elements |

### 2. Fidelity to Source

#### Preserve Author Intent

The extracted knowls should faithfully represent the source:

**Acceptable changes:**
- Formatting standardization (LaTeX syntax, whitespace)
- Adding front matter
- Adding examples when none existed
- Minor clarifications that don't change meaning

**Problematic changes:**
- Replacing author's definition with a "more standard" one
- Changing notation without necessity
- Adding hypotheses the author didn't include
- Removing conditions the author emphasized

#### Fidelity Check Process

For each extracted knowl:
1. Compare the "Original text" from Step 1 with the knowl content
2. Verify mathematical content is equivalent
3. Confirm notation matches or deviation is justified
4. Check that added content (examples, context) aligns with source perspective

**Example fidelity issue:**

*Source (Step 1 extraction):*
> A topological space X is compact if every open cover has a finite subcover.

*Knowl (Step 3):*
> A topological space $X$ is **sequentially compact** if every sequence has a convergent subsequence.

*Issue:* Wrong definition! Source defines compactness via open covers; knowl uses sequential compactness. These are not equivalent in general topological spaces.

### 3. Prerequisite Quality

#### For Created Prerequisites (`[P]`)

- Is the definition standard and correct?
- Does it match the level of the source notes?
- Is it compatible with how the term is used in extracted knowls?
- Are examples appropriate?

#### Consistency with Extracted Content

Check that prerequisites align with how terms are used:

*Potential issue:*
- Prerequisite defines "ring" with unity
- Extracted content uses "ring" without assuming unity
- **Flag:** Clarify which convention the source uses

### 4. Notation Consistency

#### Across All Knowls

| Check | Issue Example |
|-------|---------------|
| Same symbol, same meaning | $\subset$ means strict subset in one knowl, non-strict in another |
| Same concept, same symbol | Group identity is $e$ in some knowls, $1$ in others |
| LaTeX consistency | `\mathbb{R}` vs `\mathbf{R}` vs `\mathbb R` |
| Delimiter consistency | All using `$...$` for inline, `$$...$$` for display |

#### Create Notation Reconciliation

If inconsistencies exist, recommend a conventions knowl or standardization.

### 5. Cross-Link Validation

- Do all linked slugs correspond to actual knowl files?
- Are links mathematically appropriate (linking to the right concept)?
- Is display text accurate for the target?
- Are there missing links that should be added?

### 6. Completeness

- Are all stated dependencies satisfied?
- Are there implicit prerequisites that weren't created?
- Do theorems have all necessary hypotheses?
- Are examples adequate and correct?

## Severity Classification

**Critical Error** — Must fix before use:
- Mathematical statement is false
- Definition contradicts how term is used elsewhere
- Missing hypothesis makes theorem false
- Broken cross-links (slug doesn't exist)

**Fidelity Issue** — Deviation from source:
- Author's formulation replaced without justification
- Notation changed in confusing way
- Added content contradicts source perspective
- Removed important qualification from original

**Minor Issue** — Should address:
- Ambiguous phrasing
- Incomplete examples
- Notation inconsistency
- Missing but inferable hypothesis

**Suggestion** — Optional:
- Additional example would help
- Proof sketch could be added
- Context could be expanded
- Minor rewording for clarity

## Example Review Entries

```markdown
### quotient-group.md [E:24]
**Status:** NEEDS CORRECTION
**Category:** Critical
**Issue:** Definition does not require normality of H.
**Source comparison:**
> Original: "If H is a normal subgroup of G, then G/H forms a group..."
> Knowl: "Let G be a group and H a subgroup. The quotient G/H is..."
**Correction:**
Replace opening with:
> Let $G$ be a {{</* knowl id="group" text="group" */>}} and $H \trianglelefteq G$ a {{</* knowl id="normal-subgroup" text="normal subgroup" */>}}. The *quotient group* $G/H$...

---

### contraction.md [P]
**Status:** FLAG FOR REVIEW
**Category:** Fidelity
**Issue:** Prerequisite uses Lipschitz constant < 1, but source notes use "strictly less than 1" phrasing inconsistently. Some extracted theorems may assume ≤ c < 1, others c ≤ k for fixed k < 1.
**Recommendation:** Review source for which convention is intended; standardize all references.

---

### lagranges-theorem.md [E:21]
**Status:** PASS
No issues found. Statement matches source, notation consistent, links valid.
```

## Final Output

### 1. Corrected Knowls

For each knowl needing changes:

~~~markdown
**`[slug].md`** *(corrected)* [P|E:N]
```markdown
[complete corrected content]
```
~~~

### 2. Passed Knowls

```markdown
## Knowls Passed
- group.md [P]
- subgroup.md [E:4]
- lagranges-theorem.md [E:21]
...
```

### 3. Unresolved Flags

Issues requiring human judgment:

```markdown
## Flags for Human Review
1. **contraction.md**: Lipschitz constant convention — verify with source
2. **ring.md**: Unity assumption — source is ambiguous, pick one and document
3. **compact.md vs sequentially-compact.md**: Source uses terms interchangeably in metric space context — separate or merge?
```

### 4. Consistency Recommendations

```markdown
## Recommended Standardizations
1. Use $e$ for group identity throughout (currently mixed with $1$)
2. Use $\trianglelefteq$ for normal subgroup (currently mixed with $\unlhd$)
3. Add notation-conventions.md documenting: [list conventions]
```
