# Coverage report: derivatives-divisibility (complete)

Output (after the audit): 38 knowls in `knowlpedia-content/content/proofs/grh/derivatives-divisibility/`, the area page
`proofs/grh/derivatives-divisibility.knowl.md`, the sidecar `concepts/derivatives-divisibility.tsv` (46 rows).

Kinds: 2 notation, 12 definition, 2 construction, 9 lemma, 4 proposition, 9 theorem.
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

Plus two setting knowls with `lean = []` (p-adic-setting, cm-curve-setting; field-setting was removed after the audit, see below) that restate
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

## Audit response

Setting knowls: `field-setting` was deleted; all its links now point to `proofs/grh/reduction-main/field-e-and-its-places`
(finished owner), with `?lean:New.Parameters.placeOfInt`, `…chiK_eq_one_of_dvd`, `…dvd_d_add_one_div_four_of_dvd_q₁` links where
those facts are used; the local notation (nu_m, finite places, v•w) is defined in frobenius-on-generators and the area page.
`p-adic-setting` and `cm-curve-setting` are kept: no finished area owns `New.piPrime`, `New.valRingCp`, `New.CMLattice`, etc.
(library declarations); they already consist of `?lean:` links and should be retired when owners exist.
Literal `[[`/`]]` in mathematics replaced by `[\![`/`]\!]` in all 16 affected files (and removed from two TOML summaries).

- area page — High: coupling divisibility needs a bound on the exponential scale — accepted; §2 now states the norm condition |(varpi^(p+1)/p) pi| <= p^(-1/(p-1)) and the two conditions on Z, and notes that v(varpi)=rho_p, pi=pi_p supply it.
- area page — Medium: determinant norm lower bound / additive cost — accepted; §4 restated as a bound on the weighted sum of valuations, pairings only for non-exempt pairs.
- area page — Medium: Frobenius description is unramified — accepted; §5 restricts the Frobenius element to p not dividing q1 d and separates the residue congruence at p = d.
- cm-curve-setting — High: normalised sigma — accepted (checked `PeriodPair.σ`, Basic.lean); sigma is now defined by oddness, sigma'(0)=1 and its transformation law, linked `?lean:PeriodPair.σ`, distinguished from the classical sigma; theta defined via the explicit twisted translation. Sidecar: new rows "normalised sigma function of a lattice", "theta function of a lattice"; classical row corrected.
- the-count — High: missing integrality of H — accepted; remark now requires H in O[[y(u_j† z)]] and says why.
- chosen-places-and-characters — Medium: roots of unity are powers of zeta — accepted; Kronecker's theorem named (new sidecar row), parts 6 and 7 of reduction-main/field-e-properties linked.
- deduction-term — Medium: attainable cost, not minimum — accepted; remark rewritten.
- frobenius-congruence-for-theta — Medium: twisted torsion values — accepted; Step 1 defines G[u] = G(u) exp(-n pi |u|^2/(2A)) and uses it (links `New.CMLattice.torsionValue`, `…hasIntegralValues_theta`).
- frobenius-congruence-for-theta — Low: isogeny reference — accepted; `?lean:PeriodPair.IsIsogeny`.
- frobenius-on-generators — Medium: Euler's criterion alone insufficient — accepted; quadratic reciprocity with d ≡ 3 mod 4 and the case p = d inserted.
- partner-of-a-place — Medium: unit test on -p^e at e = 0 — accepted; fallback to the identity only when -p^e is not prime to q1.
- product-of-minors — Medium: direction of the Schur expansion — accepted; remark rewritten.
- weil-data-of-e — Medium: full group of roots of unity — accepted; field-e-properties part 6 linked.
- weil-data-of-e — Low: integral finite ideles in the normalisation of upsilon — accepted; wording fixed.
- count-with-charges — Low: floor(log_p 0) convention — accepted; stated in the truncated form.
- exponent-on-one-curve — Low: summary drops e = 0 — accepted; summary fixed.
- exponent-series — Low: property 3 holds at all primes — accepted (Lean `exists_rescale_theta_eq_mul_expSubst` has no non-split hypothesis); properties 2, 3 stated for every prime.
- normal-form-of-theta-products — Low: coefficient identity absent — accepted; multinomial formula of `New.coeff_subst_linearSeries` stated in Step 1.
- predicted-divisibility — Low: splitting terminology needs d ≡ 7 mod 8 — accepted; the knowl now assumes d ≡ 7 mod 8 and notes that the source works with the symbol (p/d) for any prime d.
- supersingular-coefficient-unit — Low: n = 0 in the differentiated power — accepted; n = 0 handled separately.

Rejected: none. proof_status changes: none (still 26 full, 1 outline). No change needed in other areas.
