# Coverage report: upper-elementary-divisors

Area: `src/New/UpperBound/ElementaryDivisors/` (10 files, 8308 lines). Single author, no subagents (an early attempt to spawn helpers was refused by the harness and nothing came of it).

Output: 67 proof knowls in `knowlpedia-content/content/proofs/grh/upper-elementary-divisors/`, the area page `proofs/grh/upper-elementary-divisors`, and 44 lines in `documents/riemann2/concepts/upper-elementary-divisors.tsv`.

Kinds: 16 definitions, 6 constructions, 25 lemmas, 7 propositions, 13 theorems (+ 1 page). Proof status (after the audit response): 45 full, 0 outline, 0 cited, 0 statement.

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
| ElementaryDivisorTheorem.lean | 1250 | full (the numerical lemmas in lines ~476–612 were read verbatim during the audit response) | edge-hecke-operator, large-degree-conditions, consequences-of-large-degree, edge-conditions, pairing-map-and-near-inverse, hecke-operator-factors-through-edges, few-further-generators, colength-of-factored-operator, elementary-divisors-of-edge-hecke-operator |

355 Lean declarations are listed in `lean = [...]` fields. 73 declarations of the folder are not listed anywhere: all are routine helpers (simp/apply lemmas, case splits such as `var_cases`, `mergedCoeff_add`, `one_lt_q`, …) folded into the proofs that use them.

## What is asserted rather than proved

- (Superseded by the audit response below: now proved in full.) `consequences-of-large-degree`: items 3, 5, 6 and the constant 27 are real-arithmetic consequences of `IsLargeDegree`; I read only their statements. They feed `edge-conditions` and `colength-of-factored-operator`, which are otherwise complete and are marked full relative to that lemma.
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

## Audit response

Source: `knowlpedia-content/reviews/riemann2-audit/areas/upper-elementary-divisors.md` and the 30 rows of `findings.tsv` for this area. The two update folders contain no findings for this area; the only mention (`updates/b4aa180e/concepts.md`, Kronecker product) asks for the name "Kronecker product of matrices" over a commutative ring, which the sidecar already uses. No wrong `?lean:` names were listed for this area. All 30 findings were checked against the Lean lines and accepted; none rejected.

High
- area page — "positive root variable at the distinguished letter has an extra unit of weight": accepted; section 1 now states the weights as +P^[s-i]/(q-1) at Y_s, -P^[s-i]/(q-1) at X_s, with 1 added at Y_i (weight q/(q-1)), as in `defectWeight`. (The knowl `defect-of-monomial` already had this.)
- conjugation-invariant-average — "unequal weights do not force vanishing over arbitrary rings": accepted; the property is now stated under the hypotheses of the Lean lemma (W local, O a domain of characteristic 0 with a positive integer non-unit), with a remark that it can fail otherwise; W is declared local in the definition (as `New.levi` requires).

Medium
- area page — "Nakayama uses reductions after division by w^(c-1)": accepted; section 10 now introduces S as containing the reductions of all h with w^(c-1)h in C and says the Nakayama step uses this.
- area page — "numerical conditions alone are insufficient for the stated theorem": accepted; the displayed theorem now names the valuation domain of characteristic 0, p non-unit, the finite edge data and the intertwining; the opening paragraph says which coefficient rings occur.
- conjugation-invariant-average — "comparison concerns every conjugate": accepted; summary rewritten.
- deep-forms-have-heavy-monomial — "shallow variables need order one": accepted; kappa = 1 on non-deep variables added to the statement.
- depth-of-monomial — "depth scaling need not be a twisted group element": accepted; rephrased as a tensor product of symmetric powers of letterwise diagonal matrices.
- determinant-of-step-map — "Lebesgue measure undefined for some allowed sets": accepted; part 3 now says outer measure for arbitrary sets.
- edges-and-halfway-lattices — "normalised basis uses an inverse that may not exist": accepted; the normalised monomials are now described only for a domain with w nonzero.
- existence-of-average — "good support of one polynomial does not imply agreement": accepted; summary rewritten (degree at most D, every Levi conjugate, modulo J).
- origin-functions — "saturation can include vectors that vary over one origin": accepted; defined as the w-power saturation, with the interpretation restricted to w a non-zero-divisor.
- power-packing — "power substitution commutes, the packing has extra moving factors": accepted; summary rewritten.

Low
- area page and substitution-operator — "the cycle axiom permits algebraic twists" (two findings): accepted; both remarks now say that a general cycle gives no algebraic formula, only the congruence modulo p.
- adjoint-weights — "degree-zero case of the logarithmic bound": accepted; n+m = 0 treated first.
- defect-of-steps — "coincident root indices": accepted; the case a = a' is treated first.
- defect-weight-bounds — "weight formulas assume a != a'": accepted; the proof starts from the indicator formula and uses the separate values only in part 1.
- edge-conditions — "precision zero uses a truncated predecessor": accepted; property 5 reads w^max(c-1,0), and c_0 is defined.
- edge-hecke-operator — "illustration omits its uniformizer assumption": accepted.
- edges-and-halfway-lattices — "quotients of dimension r require r <= k": accepted.
- edges-and-halfway-lattices — "divided-power stability has additional hypotheses": accepted; the remark now states the characteristic-0 domain hypothesis.
- elementary-divisors-of-edge-hecke-operator — "the abstract image need not be a lattice": accepted; summary says "image submodule".
- few-forms-of-bounded-defect — "volume bound needs a nonnegative upper endpoint": accepted; B >= 0 added.
- gauss-filtration — "Gauss groups have a wider domain": accepted; defined for any family of subgroups, filtration property stated under the axioms.
- interlacing-determinant — "final step refers to x_1 in rank one": accepted.
- lattices-of-forms-are-stable — "cancel the common factorial actually produced": accepted; n! is cancelled.
- step-map-pieri-cone-slab — "definition includes q = 0": accepted; q != 0.
- sum-of-dimensions-of-deep-forms — "divisor constant undefined at rank zero": accepted; k > 0, with the source's convention noted.
- unipotent-points-for-deep-forms — "low-power span indexed on a page that never defines it": accepted; `New.FrobeniusCycle.lowPowerForms` moved to `points-satisfy-low-power-equations`, where the span is defined.
- volume-of-pieri-cone-in-slab — "zero-dimensional case": accepted; k = 0 treated first.

Other items from the coordinator
- `consequences-of-large-degree`: I have now read the proofs of the numerical lemmas (lines 476-612 of `ElementaryDivisorTheorem.lean`) verbatim and written the proof out in full, following them (the audit ledger's summary agrees). Status raised from outline to full. This removes the only caveat on `edge-conditions` and `colength-of-factored-operator`.
- `New.levi` and `New.parahoric`: opened in `Lib/General/Groups/BesselGroups.lean`. `levi W tau` = matrices of GL_k(W), W local, with (i,j) entry 0 whenever tau(i) != tau(j); `parahoric W tau` = preimage under reduction of the matrices over the residue field that are block triangular for the order-reversed labelling, i.e. (i,j) entry in the maximal ideal whenever tau(i) < tau(j). Both agree with the conventions used in the knowls; the only change was to state that W is local where the Levi subgroup is introduced in `conjugation-invariant-average`. Doubt 5 of this report is thereby settled.
- Nothing here implies a change in another area.
