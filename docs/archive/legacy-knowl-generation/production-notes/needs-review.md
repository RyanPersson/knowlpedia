# Content Needing Review

## Duplicate Knowls - RESOLVED (2026-01-02)

7 of 8 duplicates have been consolidated:

| Knowl | Canonical Location | Status |
|-------|-------------------|--------|
| `bijective-function` | `shared-foundations` | ✓ Consolidated |
| `cartesian-product` | `shared-foundations` | ✓ Consolidated |
| `domain` | `shared-foundations` | ✓ Consolidated |
| `codomain` | `shared-foundations` | ✓ Consolidated |
| `linear-map` | `linear-algebra` | ✓ Consolidated |
| `vector-space` | `linear-algebra` | ✓ Consolidated |
| `subsequence` | `analysis` | ✓ Consolidated |
| `diffeomorphism` | **Both kept** | See below |

### Diffeomorphism - Intentionally Kept as Two Knowls

The two diffeomorphism knowls have **genuinely different definitions**:

- `analysis/diffeomorphism.md`: C¹ bijection between open sets in ℝⁿ with C¹ inverse
- `fiber-bundles/diffeomorphism.md`: Smooth bijection between smooth manifolds with smooth inverse

These are not duplicates - they serve different contexts:
- The analysis version is appropriate for multivariable calculus (inverse function theorem, change of variables)
- The fiber-bundles version is the general definition on manifolds

**Decision:** Keep both. When a topology/smooth-manifolds section is created, the general definition could move there and the analysis version could reference it as "in the special case of open subsets of ℝⁿ..."

## Next Steps

- [ ] Extract topology from analysis (pending - another agent working on list)
- [ ] Factor manifold/differential-forms prerequisites from fiber-bundles (later)
- [ ] Consider adding `morphism` to shared-foundations as a foundational concept
