# Coverage report: derivatives-divisibility (complete)

Output: 39 knowls in `knowlpedia-content/content/proofs/grh/derivatives-divisibility/`, the area page
`proofs/grh/derivatives-divisibility.knowl.md`, the sidecar `concepts/derivatives-divisibility.tsv` (43 rows).

Kinds: 3 notation, 12 definition, 2 construction, 9 lemma, 4 proposition, 9 theorem.
proof_status: 26 full, 1 outline (size-of-the-different, part 3). The 12 remaining are definitions/notation
(some definition knowls carry short proofs of their listed properties).

All ten files were read completely (heads, statements, proofs). None was compiled.

| Lean file | lines | read | knowls |
|---|---|---|---|
| Divisibility/NormalForm.lean | 419 | full | coupling, coupling-sum, normal-form, normal-form-modulo-pi, normal-form-substitution, normal-form-valuation, normal-form-integrality, coupling-sum-derivatives |
| Divisibility/NullFrames.lean | 447 | full | elimination-of-congruences, deduction-term, change-of-directions |
| FormalGroup/FrobeniusCongruence.lean | 431 | full | frobenius-congruence-for-theta, supersingular-coefficient-unit |
| FormalGroup/Exponent.lean | 749 | full | exponent-series, exponent-on-one-curve |
| FormalGroup/Resolution.lean | 255 | full | resolution-of-the-identity, integral-above-p, theta-product |
| FormalGroup/ThetaProducts.lean | 479 | full | partner-of-a-place, normal-form-of-theta-products |
| Divisibility/Count.lean | 829 | full | legendre-bound-for-jets, product-of-minors, predicted-divisibility, count-with-charges, the-count, schur-entry-to-minor-product |
| Field/PrimeDecomposition.lean | 878 | full | different-of-e, frobenius-on-generators, decomposition-of-primes-in-e, place-permutation |
| Field/WeilData.lean | 545 | full | places-above-split-primes, weil-data-of-e, vacuum-root |
| Field/ChosenPlaces.lean | 455 | full | chosen-places-and-characters, critical-pair, size-of-the-different |

Plus three setting knowls with `lean = []` (p-adic-setting, cm-curve-setting, field-setting) that restate
notation owned by other areas (Lib/CM/FormalGroup/PrimeNotation, Lib/CM/Sigma, New/Reduction/Data/FieldsAndPlaces)
with `?lean:` links, so that the cores of the other knowls stay short.

## Choices that the orchestrator should know

- To stay within budget, several Lean declarations are merged per knowl (the `lean` front-matter lists them all).
  In particular: `CongruenceChoice`, `congruenceModulus`, `newDirection` live inside change-of-directions;
  `IsChargeExponent`, `fillingCharge`, `directionSubst`, `columnDetProd` inside count-with-charges;
  `deductionAt`, `eraseHeightOne` inside predicted-divisibility; `relDifferentGen` and `deltaE` inside different-of-e;
  `galOfPlaceInt`, the action on finite places and `frobElem` inside frobenius-on-generators; the idele `α` inside
  weil-data-of-e; `IsChosen`, `chiMLocal`, `chiZero`, `chiM` inside chosen-places-and-characters. If the resolver needs
  one knowl per such definition, these should be split out.
- Three knowls of kind `definition` (partner-of-a-place, predicted-divisibility, critical-pair) also contain a lemma
  with proof and carry `proof_status = "full"`.
- Routine helper lemmas (coercions, `simp` lemmas, `PairingSide`, small norm computations) are folded into proofs.

## Doubts and gaps

1. size-of-the-different, part 3 (`New.Data.hasLogBound_deltaE`): the comparison with x^10 and x^12 is done in Lean
   by instance search plus `grind` with `D.scale_inequalities`; I did not reconstruct the numerical inequality
   (it needs the size of towerDeg ~ x^11 from the data). Marked outline.
2. `New.Parameters.constantBound`: I did not open its definition; the knowl states only what the Lean proof uses
   (it contains the sum of |log|Phi_{q0}'(w)|| over primitive q0-th roots as a summand, the rest being nonnegative).
3. Proofs marked full rely on library lemmas cited by `?lean:` links whose statements I read but whose proofs I did
   not (e.g. `New.CMLattice.exists_polynomial_of_even`, `New.CMLattice.exists_scaled_formalParam`,
   `New.norm_coeff_expSubst_le_one`, `New.sum_schur_smul_nablaBasis`, `New.GL.linearIndependent_nablaBasis_mul_detPow`,
   `New.nonempty_splittingChar`, `New.AutChar.exists_hasWeight_of_prod_eq_one`, `New.WeilData.exists_chiFin_pow_eq_prod`).
   A few `?lean:` names were inferred from dot-notation and should be checked by the resolver:
   `New.IsSeriesGenerator.expSubst_mem_of_pow_mem`, `New.IsSeriesGenerator.mem_of_expSubst_smul_eq`,
   `New.CMLattice.IsIsogeny`, `New.Cohomology.upsilon_atUniformizer_eq_neg_one`, `New.nonempty_splittingChar`,
   `New.congruencePart_eq_sum`, `New.jet_subst_linearSeries`, `New.Parameters.cmCurve`, `New.Parameters.constantBound`.
4. decomposition-of-primes-in-e, self-conjugate places, case p = d: follows the Lean proof, using
   `New.Parameters.d_pow_ne_neg_one` (d^n is never -1 mod q0) as a black box.
5. different-of-e step 2 cites two standard facts as `?c:` concepts that come from Mathlib
   (`conductor_mul_differentIdeal`, `IsDedekindDomain.map_differentIdeal_dvd_differentIdeal`); the precise
   hypotheses of the second (linear disjointness / coprime differents) are stated loosely in the knowl and in the sidecar.
6. Conventions worth a second look: |x|_v at an infinite place is |Phi_v(x)| (not squared), as in the source's
   `v x`; `floor(log_p 0) = 0` and `floor(log_3 0) = 0` (Lean's `Nat.log`); the deduction term counts columns of
   height 0 among the "low" columns (as the Lean definition does).
7. The count is stated in Lean as a norm inequality; count-with-charges states it as a valuation inequality
   (equivalent when the jet is nonzero; trivial otherwise), the-count as the norm inequality.
8. `Space.jetSeries_mul_eq_rescale` (Resolution.lean) is only mentioned in a remark of theta-product, not given a knowl.
9. `prerequisites = []` everywhere (placeholders pending), as the guide prescribes for drafts.
