# Coverage report: upper-elementary-divisors

Area: `src/New/UpperBound/ElementaryDivisors/` (10 files, 8308 lines). Single author, no subagents (an early attempt to spawn helpers was refused by the harness and nothing came of it).

Output: 67 proof knowls in `knowlpedia-content/content/proofs/grh/upper-elementary-divisors/`, the area page `proofs/grh/upper-elementary-divisors`, and 44 lines in `documents/riemann2/concepts/upper-elementary-divisors.tsv`.

Kinds: 16 definitions, 6 constructions, 25 lemmas, 7 propositions, 13 theorems (+ 1 page). Proof status: 44 full, 1 outline, 0 cited, 0 statement.

## Files (in import order)

All ten files were read completely and verbatim, tactic lines included, with one exception noted under ElementaryDivisorTheorem.

| File | Lines | Read | Knowls |
|---|---|---|---|
| TwistingData.lean | 445 | full | frobenius-cycle, twisted-action, maps-of-cycle-kill-maximal-ideal, depth-of-monomial, defect-of-monomial, defect-weight-bounds, translate-conditions |
| InvariantAverage.lean | 971 | full | adjoint-weights, conjugation-invariant-average, invariant-forms-vanish-on-unbalanced-monomials, density-of-points-over-local-ring, schur-algebra-of-levi, levi-points-span-schur-algebra, large-weight-submodule, dual-operator-conjugation, existence-of-average |
| PieriCone.lean | 531 | full | step-map-pieri-cone-slab, interlacing-determinant, determinant-of-step-map, signed-count-of-positive-steps, volume-of-cone-in-slab-signed-sum, volume-of-pieri-cone-in-slab |
| RootLemma.lean | 1069 | full | stepanov-count, gauss-filtration, substitution-respects-gauss-filtration, root-data, zeros-against-degree, root-lemma, large-defect-forces-divisibility |
| Depth.lean | 799 | full | unipotent-points-for-deep-forms, points-satisfy-low-power-equations, deep-forms-have-heavy-monomial, sum-of-dimensions-of-deep-forms |
| Edges.lean | 813 | full | edges-and-halfway-lattices, lattices-of-forms-are-stable, parahoric-preserves-halfway-lattice, edge-pairing, origin-functions, origin-functions-summand-of-small-colength, halfway-forms-divisible-at-large-defect |
| FrobeniusFactors.lean | 821 | full | substitution-operator, substitution-operator-conjugation, copy-weight, levels-of-substitution-operator, conjugated-frobenius-factors-level, weight-and-defect |
| DefectCount.lean | 987 | full | defect-cone, defect-of-steps, power-packing, least-height-term-at-a-flag, integral-shift-into-pieri-cone, bounded-defect-dimension-by-lattice-points, number-of-flags-bound, few-forms-of-bounded-defect |
| AveragingMap.lean | 622 | full | partial-average, contraction-change-of-frame, weight-and-defect-in-one-copy, averaging-map |
| ElementaryDivisorTheorem.lean | 1250 | full, except the proofs of the numerical lemmas in lines ~476–612 (statements and docstrings only) | edge-hecke-operator, large-degree-conditions, consequences-of-large-degree (outline), edge-conditions, pairing-map-and-near-inverse, hecke-operator-factors-through-edges, few-further-generators, colength-of-factored-operator, elementary-divisors-of-edge-hecke-operator |

355 Lean declarations are listed in `lean = [...]` fields. 73 declarations of the folder are not listed anywhere: all are routine helpers (simp/apply lemmas, case splits such as `var_cases`, `mergedCoeff_add`, `one_lt_q`, …) folded into the proofs that use them.

## What is asserted rather than proved

- `consequences-of-large-degree` (outline): items 3, 5, 6 and the constant 27 are real-arithmetic consequences of `IsLargeDegree`; I read only their statements. They feed `edge-conditions` and `colength-of-factored-operator`, which are otherwise complete and are marked full relative to that lemma.
- Results of other areas used by statement (linked `?lean:`), not re-proved here: `New.exists_le_weight_of_mem_vanishingIdeal_pow` (combinatorial Nullstellensatz with multiplicity; I read its statement and head comment, not its proof), `New.IsValuationPair.hermite` and `New.IsValuationPair.smith_normal_form` (Hermite/Smith forms over a valuation domain; statements inferred from their use, the declarations themselves were only located by grep), `New.fockPairing_linSubst`, the `New.ColengthDvd` calculus (`of_det_dvd`, `trans`, `map`, `colengthDvd_sup_span`, `IsOntoUpToColength`; I read the definitions and docstrings in `New/Reduction/Lattices/Colength.lean`), `New.levi`, `New.parahoric` (taken from the descriptions in the heads of my files; I did not open their definitions in `Lib/General/Groups/BesselGroups.lean` beyond locating them), and the Mathlib-level facts recorded in the sidecar (lattice point count `tendsto_card_div_pow_atTop_volume`, order of GL_k(F_q), Kummer bound, change of variables).

## Doubts and places to re-check

1. `zeros-against-degree`: the case analysis for the action of `g_r` followed by the substitution and the shift (Lean: `shiftCoeff_aeval_swapTransvection_X`) is proved in Lean by `simp`/`ring` per case; I verified the cases Y_i and the weights by hand, the cases s ≠ i only through the stated formula. Signs (`moveSign`) are summarised as "±".
2. `weight-and-defect`: the identity between the last potentials and (1 − 1/q) times the defect weight (`mul_defectWeight_eq_indexWeight_mul`) is a `simp` case check in Lean; I verified one of the four cases by hand.
3. `defect-of-steps` part 1: the Lean proof is a `simp`/`field` case check; the knowl gives a hand derivation of the telescoping (checked for both parities and against its use in `integral-shift-into-pieri-cone`).
4. `frobenius-cycle` remark "N is even": this is a consequence (proved in Lean as `card_isEven_add_self`/`two_le_card_letters`), not an axiom of the structure.
5. `parahoric`/`levi` conventions: stated as "entries (i,j) in the maximal ideal when τ(i) < τ(j)" and "zero when τ(i) ≠ τ(j)", following the heads of the files; for the two-block labelling this is "upper right block in the maximal ideal". Should be reconciled with whichever area writes the knowls for `New.levi` and `New.parahoric`.
6. `edge-hecke-operator`: the geometric interpretation (group Γ, δ, lattices) is only a comment in the source; the knowl says so. The interpretation of the parahoric cosets as "edges" in `edges-and-halfway-lattices` is likewise a comment.
7. `density-of-points-over-local-ring`: the vanishing criterion for homogeneous polynomials of degree ≤ |κ| is cited from Mathlib; my parenthetical sketch of why it holds is informal.
8. The concept "Colength divisibility" is a notion of the development owned by the lattices area (`New.ColengthDvd`); I linked it with `?lean:` and added a sidecar line only so that it is not lost.
9. External literature: only the citations given in the heads of the Lean files are reproduced, without locators beyond those given there; I did not compare any of them with the sources.

## Incident for the orchestrator

The scratchpad is shared between sibling agents. Early in my run I wrote a helper named `k.sh` at the top of the scratchpad, which collided with another author's helper of the same name; as a result eight knowls of another area (ids such as `spread-family-of-linear-maps`, `hilbert-schmidt-norm-of-a-linear-map`, `near-isometry-…`, `character-sum-bound-by-stabilisers`, `function-of-positive-type`, `singular-minors-have-small-mass`; Lean file `New/Spanning/SecondMoment/FewTranslates.lean`) were briefly written into my folder with my front-matter template. I restored the other author's `k.sh` within about a minute and moved my helper to a private subfolder. Those eight files are no longer in my folder (their owner appears to have removed or rewritten them); the `spanning-core` author's copies should be checked for a wrong `id`/`lean_files` line or a duplicated References section.
