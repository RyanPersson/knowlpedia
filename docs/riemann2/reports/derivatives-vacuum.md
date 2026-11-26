# Coverage report: derivatives-vacuum

STATUS: COMPLETE. All 13 assigned Lean files (6904 lines) were read in full, in import order, by one author (an attempted split into co-authors failed on the subagent limit).

Outputs:
- 95 proof knowls in `knowlpedia-content/content/proofs/grh/derivatives-vacuum/`: 21 definitions, 1 construction, 50 lemmas (38 full, 12 outline), 23 theorems (13 full, 10 outline).
- Area page `knowlpedia-content/content/proofs/grh/derivatives-vacuum.knowl.md` (links every knowl).
- Concept sidecar `documents/riemann2/concepts/derivatives-vacuum.tsv` (35 concepts).

Conventions and general caveats:
- "full" means: every step is an explicit computation, a linked knowl of this area, or a linked item of another area (`?lean:` placeholder) used as a black box. Items of other areas were not re-verified; where a proof here leans on an unlinked Lib lemma it is marked "outline" and the Lean name is given in the text.
- All scale inequalities that Lean proves with `D.le_of_hasLogBound` / `D.nat_le_of_hasLogBound` (instance search + `grind`) are asserted, not re-derived by hand. Affected: short-coprime-tight-frame, tight-frame-of-length-m, errors-covered-by-the-loss-product, size-of-the-sharpness-constant, and single inequalities (`d <= k`, `k <= 2^s`, `x^42 <= n#`, `kappa + x^42 <= 2b`) inside otherwise full proofs.
- Power series rings are written `R[\![X]\!]` in the knowls, because a literal double bracket collides with the knowl link syntax.
- Objects of other areas that appear in statements (Space, jetSeries, entireTheta, finitePart, CMLattice and its theta/sigma/y functions, multiSeriesRing, HasNormalForm, predictedDivisibility, Data and its fields, ...) are linked with `?lean:` placeholders and described in one phrase taken from the Lean docstrings, not redefined. 102 distinct external Lean names are referenced; each was checked to exist in the source by name (namespaces of a few lemmas such as `relDifferentGen_dvd_q₁`, `HasNormalForm.rescale`, `Space.exists_fourier_coefficients` were inferred from usage, not opened).
- Notation: `x_f` denotes `finVec x` (finite part `alpha x`), `gamma_f` denotes `finVec (finiteImage gamma)` (finite part `gamma`). `varpi` is the complex period factor, `varpi_p` the p-adic scale of the normal form; the Lean uses the same letter for the latter.

Most important doubts:
1. The definition knowls `theta-product`, `resolution-product`, `vacuum-expansion` state the twisted translation by the formula in the Lean docstrings (`exp(-m pi (z conj(l) + |l|^2/2)/A) g(z+l)`); I did not open the definition of `thetaShift`.
2. `normal-form-of-standard-data` and `least-valuation-along-couplings` paraphrase `HasNormalForm` (defined in another area) as `Theta(varpi z) = W exp(varpi^(p+1)/p * Xi)`; this is how the Lean proofs unfold it at inert primes, but for `p = d` the knowl only repeats the docstring.
3. `divisibility-of-derivatives-along-minors` does not restate the formula for the predicted divisibility (linked only).
4. In `integral-vacuum-in-rank-one` the constant is `ceil(M) + 2`; the bound `M <= e^M` is used as in Lean.

## Vacuum/TightFrames.lean (933 lines) — read in full

Knowls (all in `proofs/grh/derivatives-vacuum/`):

| slug | kind | status | Lean |
|---|---|---|---|
| cm-curve-and-period | definition | – | Parameters.cmCurve, cmPeriod, latticeModule_cmCurve |
| chowla-selberg-unit | definition | – | Parameters.chowlaSelbergUnit and its two properties |
| jet-scale | definition | – | Parameters.areaScale, periodFactor, jetScale |
| hermitian-product-of-lattice-vectors-is-integral | lemma | full | sum_mul_conj_mem_quadInt, exists_coe_eq_trace_of_isIntegral, coe_trace_eq_sum, mul_sum_mul_conj_mem_lattice |
| p-adic-size-of-vacuum-root | lemma | full | norm_iota_vacuumRoot, span_vacuumRoot_eq, adeleExtension_alpha, exists_norm_adeleExtension_alpha_mul_eq_one |
| p-adic-size-of-period-factor | lemma | full | norm_iota_periodFactor, norm_periodFactor_mul_conj_le_one, norm_iota_periodFactor_eq_one |
| roots-of-unity-tight-frame | lemma | full | isTightFrame_pow, isTightFrame_zeta_pow, IsTightFrame.mul_left |
| taylor-series-on-a-line-from-jet-series | lemma | outline | Space.taylor_line_eq_subst_jetSeries, iteratedDeriv_integral_exp_mul_realVac |
| vector-determined-by-jet-series | lemma | outline | Space.eq_zero_of_jetSeries_eq_zero |
| jet-series-of-product-of-linear-forms | lemma | full | Space.jetSeries_eq_prod_of_entireTheta_smul, jetSeries_eq_prod, theta_eq_prod_of_entireTheta_smul |
| resolution-product | definition | – | Parameters.IsResolutionProduct, resolutionShift, resolutionFormCoeff, resolutionLinearForm |
| resolution-product-theta-values-and-jets | lemma | full | IsResolutionProduct.theta_translate, jetSeries_translate |
| resolution-product-integral-values | lemma | full | IsResolutionProduct.norm_iota_apply_le_one |
| frame-forms-sum-to-standard-hermitian-form | lemma | full | sum_pullForm_resolutionLinearForm_apply |
| existence-of-resolution-product-along-tight-frame | theorem | outline | exists_isResolutionProduct_of_isTightFrame, normalizedShift_prod_comp_of_mem_lattice |

Doubts:
- The outlines rest on Lib results not opened here: the Fock reproducing formula (`Space.entireTheta_eq_integral`, `theta_integrated`, `jet_jetSeries_eq_theta`), `Space.exists_entireTheta_eq_of_isThetaFunction` (Fourier inversion), `Space.entireTheta_translate_finiteImage`, and the multiplier identities of `CMLattice` / `ThetaTori`. The statement of the twisted translation is taken from the Lean docstring, not from the definition of `thetaShift`.
- In `p-adic-size-of-vacuum-root` the independence of the place uses `valuation_map_relDifferentGen` (another file) as a black box.
- "full" here means: every step is an explicit computation or a linked item; items of other areas are linked as `?lean:` placeholders and were not re-verified.

## Vacuum/IntegralVacuum.lean (656 lines) — read in full

Knowls: theta-product (definition), existence-of-theta-products (lemma, full), vacuum-as-sum-of-translates (lemma, outline: rests on Lib `Space.exists_fourier_coefficients`), integral-vacuum-in-rank-one (theorem, outline: uniform bound of torsion values and the evaluation formula are Lib lemmas), integral-vacuum (definition), standard-data (definition), integral-vacuum-values (theorem, full), norm-bounded-by-values-at-finite-points (lemma, full), conjugates-of-jets-of-translates (theorem, full modulo the linked CM theorem `CMLattice.complex_multiplication_theta`).

Doubts: `finVec x` has finite part `α x`; I write `x_f` for it and `γ_f` for the finite vector with finite part `γ` (= finVec(finiteImage γ)). The vacuum scale is a `Classical.choose`; the knowl says "fixed once and for all".

## Vacuum/ShortVectors.lean (809 lines) — read in full

Knowls: tight-frame-operations (lemma, full), lattice-a0-is-galois-stable (lemma, full), orbit-tight-frame (lemma, full), dual-vectors (definition), dual-vectors-properties (lemma, full), tight-frame-of-length-prime-to-q1 (theorem, full), unit-linear-form (definition), existence-of-vector-with-unit-linear-form (lemma, full), tight-frames-of-all-large-lengths (lemma, full), short-coprime-tight-frame (theorem, outline), tight-frame-of-length-m (theorem, outline).

Doubts: the two outlines assert the final size comparisons, which Lean proves by its magnitude calculus (`D.le_of_hasLogBound`, instance search plus `grind`); I did not re-derive them by hand. `one_le_norm_phi_relDifferentGen` likewise.

## Vacuum/Scale.lean (154 lines) — read in full

Knowls: jets-along-homogeneous-polynomials (lemma, full), scaled-linear-forms-are-p-integral (lemma, full), modulus-of-jet-scale (theorem, outline: equality of areas of CM lattices with equal a1 rests on Lib isogeny lemmas).

Note: the file head mentions `New.Data.norm_conj_piMBar_mul_jetScale_sq` and `New.Data.norm_taylorScale_eq_one_of_not_dvd`; these are not declared in this file.

## Vacuum/JetIntegrality.lean (326 lines) — read in full

Knowls: jets-integral-in-derivative-stable-ring (lemma, full), jet-ring (definition), jet-ring-is-stable-under-derivatives (lemma, outline: several Lib facts on the formal group of the CM curve asserted), integrality-of-jets-of-theta-products (theorem, full given the previous two), stability-of-standard-data (theorem, outline: the formula for Weil operators on the vacuum and the unit multiplier are Lib lemmas).

## Vacuum/StandardDataProducts.lean (552 lines) — read in full

Knowls: resolution-from-tight-frame (lemma, full), product-of-translated-thetas-as-theta-power (lemma, outline: one-curve isogeny integrality is Lib), tight-frame-of-square-length-prime-to-p (lemma, full), vacuum-expansion (definition), existence-of-vacuum-expansion (theorem, outline: Fourier inversion asserted), standard-data-as-theta-products (theorem, full given linked items).

## Vacuum/Divisibility.lean (275 lines) — read in full

Knowls: integrality-of-derivatives-of-standard-data (theorem, full), normal-form-of-standard-data (theorem, outline), divisibility-of-derivatives-along-minors (theorem, outline; merges `norm_jet_minorProd_jetSeries_le` and `norm_schurJet_jetSeries_le_of_charges`).

Doubts: in the last knowl the definitions of predicted divisibility, charge condition, filling charge, erased diagram, gain per box are linked (`?lean:`) and not restated; the Lean docstring gives a formula for the predicted divisibility which I did not copy because I did not read its definition in `Divisibility/Count.lean`. The statement of the normal form paraphrases the docstring of `exists_hasNormalForm_jetSeries`; the precise definition is in `New.HasNormalForm` (other area).

## Sharpness/OneCurve.lean (354 lines) — read in full

Knowls: largest-coefficient-among-integral-series (lemma, full), submultiplicative-sequences (lemma, full), greatest-norm-of-derivatives (definition), greatest-norm-of-derivatives-is-submultiplicative (lemma, full given the linked addition formula), derivatives-of-the-formal-parameter (lemma, outline: `exists_scaled_formalParam` asserted), katz-divisibility-limit (theorem, full).

## Sharpness/LeastValuation.lean (613 lines) — read in full

Knowls: lowest-term-of-a-power-series (definition), copy-substitution (construction), least-valuation-relation (definition), least-valuation-rules (lemma, full), six-scaled-copies-are-a-unit (theorem, outline: `expSubst_sub_rescale_mem` asserted), least-valuation-with-a-unit-form (theorem, full), least-valuation-zero-when-forms-span (lemma, full), integral-series-in-parameters-after-scaling (lemma, outline).

## Sharpness/Couplings.lean (623 lines) — read in full

Knowls: coupling-family (definition), derivatives-of-exponential-factorizations (lemma, full), unit-coefficient-at-the-power-degree (lemma, outline: two Lib facts on the residues of derivatives of the coupling sum asserted), coefficient-of-a-product-of-couplings (theorem, full), least-valuation-along-couplings (theorem, full).

Doubt: I describe `HasNormalForm` at an inert prime as the displayed exponential factorization (as the Lean proof unfolds it via `partnerExponents_of_inert`); its general definition lives in `New/Derivatives/Divisibility/NormalForm.lean` (other area).

## Sharpness/NearPairs.lean (472 lines) — read in full

Knowls: sparseness-along-powers-of-minus-p (lemma, full given the linked sparseness condition), near-pair (definition), near-pairs-are-disjoint (lemma, full), loss-product (definition), legendre-bounds-for-the-data (lemma, full), partner-minimum-sum (definition), rate-minus-predicted-valuation (lemma, full), bound-for-the-partner-minimum-sum (lemma, full), errors-covered-by-the-loss-product (lemma, outline: scale inequalities asserted).

Doubt: "l0 is odd" (a power of 3) is used to pass from e < ceil(l0/2) to 2e < l0; Lean does this with `grind` from 2n <= l0 + 1.

## Sharpness/Cases.lean (690 lines) — read in full

Knowls: resolution-forms-of-a-frame (definition), properties-of-resolution-forms (lemma, full), least-valuation-zero-at-inert-primes (lemma, full), normal-form-along-a-tight-frame (lemma, outline), degree-near-the-weights (definition), valuation-bound-at-split-primes (lemma, full), valuation-bound-at-large-inert-primes (lemma, full), valuation-bound-at-small-non-split-primes (lemma, full), valuation-bound-on-twelve-copies (theorem, full).

Doubt: in properties-of-resolution-forms item 3 I say the level primes are congruent to 1 modulo a multiple of d; the Lean uses `D.levelPrime_modEq_one` and `Parameters.chiK_eq_one_of_modEq_one` whose exact moduli I did not open (the guide says p0, p1 are 1 mod q2^2 with q2 = (q0 d)^(s+6)).

## Sharpness/BoundAttained.lean (447 lines) — read in full

Knowls: twelve-space-and-indicator-data (definition), theta-product-times-monomials-as-a-vector (lemma, full), expansion-in-indicator-data (lemma, outline: Fourier inversion and the expansion of translates of the vacuum in indicator data are Lib lemmas), reduction-to-the-curve (theorem, full), size-of-the-sharpness-constant (lemma, outline: final scale inequality asserted), sharpness-of-the-valuation-bound (theorem, full).
