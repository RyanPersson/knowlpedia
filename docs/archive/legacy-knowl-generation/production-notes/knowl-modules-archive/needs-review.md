# Knowls Needing Review

## Anti-Patterns

### 1. Low-information "Related" sections
The antipattern is **vague lists of related concepts**. Files that construct explicit, meaningful relationships are acceptable.

**Status:** Fixed. Removed `## Related knowls` from yoneda-lemma.md. Remaining instances (functor.md, isomorphism-category.md, convex-lecture-notes.md) are acceptable.

### 2. Knowl shortcodes inside LaTeX
Embedding `{{< knowl ... >}}` inside `\[ ... \]` or `$$...$$` causes rendering issues.

**Status:** FIXED - All 14 instances resolved. Knowls moved to prose, plain LaTeX in equations.

### 3. Proof sketch sections
**Status:** Intentionally kept in convex-analysis only (58 files). Will add subknowls for actual proofs later.

---

## Geometry-Bundles Name Changes Needed

Long/awkward slugs that should be renamed:

| Current | Proposed |
|---------|----------|
| `lemma-local-gauge-transformation-law-ag-g-1ag-g-1dg` | `local-gauge-transformation-law` |
| `lemma-local-curvature-transformation-law-fg-g-1fg` | `curvature-gauge-transformation-law` |
| `atiyah-sequence-tpgtm0` | `atiyah-sequence` |
| `classification-theorem-principal-g-bundles-over-m-are-classified-by-homotopy-classes-mbg` | `classification-of-principal-bundles` |
| `construction-atiyah-algebroid-tpg-and-its-anchor-map-to-tm` | `atiyah-algebroid-construction` |
| `convention-ad-p-g-g-uses-conjugation-action-gh-ghg-1` | `convention-adjoint-bundle-conjugation-action` |
| `homotopy-class-mbg` | `homotopy-classes-into-classifying-space` |
| `pure-gauge-connection-ag-1dg-on-a-trivial-bundle` | `pure-gauge-connection` |
| `tfae-flat-principal-bundles-principal-g-bundle-pm` | `tfae-flat-principal-bundles` |
| `tfae-principal-connection-data-principal-g-bundle-pm` | `tfae-principal-connection-data` |
| `tfae-reduction-of-structure-group-to-hg-principal-g-bundle-pm` | `tfae-reduction-of-structure-group` |
| `tfae-tensorial-forms-vs-ad-valued-forms-principal-g-bundle-pm` | `tfae-tensorial-vs-adjoint-valued-forms` |
| `tfae-triviality-of-a-principal-g-bundle-principal-g-bundle-pm` | `tfae-trivial-principal-bundle` |

---

## Missing Knowls

### linear-algebra
- `linear-independence`, `basis`, `dimension`, `matrix-representation`, `diagonalizable`
- `real-numbers`, `complex-numbers`, `absolute-value`

### analysis
- `power-series`, `radius-of-convergence`, `fundamental-theorem-of-calculus`
- `partition-of-interval`, `monotone-function`, `sup-norm`, `open-cover`
- `sequential-compactness`, `lebesgue-criterion-riemann-integrability`
- `uniform-limit-theorem`, `limit-point`, `lipschitz-function`
- `change-of-variables-rk`, `antiderivative`, `uniform-convergence`
- `continuous-function`, `uniform-convergence-and-differentiation`
- `bounded-variation`, `total-variation`, `geometric-series`

---

## Cross-Section Reference Issues

| Section | Fixes needed | Missing knowls |
|---------|--------------|----------------|
| algebra-groups | 0 (FIXED) | 0 |
| algebra-modules | 0 | 6 |
| analysis | 62 | 42 |
| glossary | 22 | 0 |
| linear-algebra | 9 | 5 |
| shared-foundations | 2 | 0 |
| posts | 2 | 0 |

---

## Search Patterns

```bash
# Find "Related" patterns
grep -r "## Related" content/
grep -r "related notions" content/

# Find knowl shortcodes inside LaTeX
grep -r '={{< knowl' content/
grep -r '\\in {{< knowl' content/

# Find categorized sub-bullets
grep -rE '^- [A-Z][a-z]+:' content/
```
