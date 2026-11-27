# Coverage report: spanning-core

Author run in two sessions (the first was cut by a rate limit). State at the end of the second session.

## Summary

- 66 proof knowls in `knowlpedia-content/content/proofs/grh/spanning-core/`, plus the area page `proofs/grh/spanning-core.knowl.md`, the sidecar `concepts/spanning-core.tsv` (78 concepts).
- All 17 assigned files were read completely, proofs and tactic lines included, and translated (the last seven in a third session). 28 theorems, 14 lemmas, 15 definitions, 9 constructions; 25 full, 17 outline.

## Files

| File | Lines | Read | Knowls |
|---|---|---|---|
| `SecondMoment/PositiveType` | 211 | full | function-of-positive-type, character-sum-bound-by-stabilisers (full), singular-minors-have-small-mass (full) |
| `SecondMoment/FewTranslates` | 551 | full | hilbert-schmidt-norm-of-a-linear-map, near-isometry-in-mean-square, near-isometry-from-small-defect (full), near-isometry-after-projection (full), spread-family-of-linear-maps, cauchy-schwarz-for-translates (full), one-translate-from-second-moment (full), few-spread-maps-span-almost-everything (full), restricting-maps-to-a-subspace (full) |
| `SecondMoment/SpanningTheorem` | 368 | full | dimension-of-the-target (outline), scaled-poincare-map, unfolding-of-the-scaled-poincare-map (outline), bad-types-are-rare (outline), good-poincare-map-is-a-near-isometry (outline), second-moment-of-the-poincare-map (outline), translates-of-the-good-poincare-map-spread (full, given the linked items) |
| `Multiplicities/HeckeEigensystems` | 490 | full | spherical-hecke-algebra-away-from-the-level, hecke-operators-at-split-places, hecke-eigensystem-part, eigensystem-parts-decompose-the-forms (outline), hecke-projector-onto-an-eigensystem (full), hecke-action-on-good-forms |
| `Multiplicities/EqualMultiplicities` | 412 | full | translation-as-a-hecke-operator (full), rallis-series-is-a-hecke-operator (full), equal-traces-on-good-forms (outline), equal-multiplicities-of-eigensystems (full, given equal traces) |
| `Bessel/Basic` | 1057 | full | bessel-length, norm-bound-from-frame-and-dual-columns (full), orthogonal-frame-of-a-point, bessel-length-versus-orthogonal-frame (full), frame-gram-matrix-of-an-isometry (full), bessel-lattice-basis, frame-discriminant (full), link-of-an-isometry, cut-pair-of-bessel-functions, schur-bound-for-a-bessel-function, local-bounds-of-a-bessel-function, bessel-system |
| `Bessel/GramSection` | 692 | full | open-cell-of-frame-matrices, gram-section, gram-section-is-a-section (outline), bounds-for-the-gram-section (full), fibres-of-the-frame-gram-map (full) |
| `Bessel/Orthonormality` | 217 | full | normalisation-of-a-bessel-function (full) |
| `Bessel/MeanValue` | 621 | full | coordinates-on-frames-over-a-gram-matrix (outline), mean-value-inequality-over-the-gram-section (outline) |
| `Bessel/SobolevBound` | 655 | full | unfolding-bound-on-the-real-group (full), integral-over-the-section-orbit (full), sobolev-bound-at-the-gram-section (outline) |
| `Bessel/Average` | 161 | full | bessel-period-group-and-average |
| `Bessel/OpenCellBound` | 725 | full | sizes-near-a-point-of-the-open-cell (full), norm-bound-from-the-length-at-the-section (full), open-cell-bound, open-cell-bound-exists (outline) |
| `Bessel/OpenCellPairing` | 274 | full | one-pairing-on-the-open-cell (full, given the linked items) |
| `Bessel/LargeFunction` | 771 | full | bessel-system-of-discrete-series-type, stationary-point-with-large-period (outline), bessel-average-properties (outline) |
| `Bessel/CutTailBound` | 465 | full | cut-of-a-bessel-function, cut-pair-from-the-bessel-average (outline) |
| `Bessel/SchurBound` | 323 | full | schur-bound-holds-for-functions-fixed-by-the-kernel (outline) |
| `Bessel/FillingData` | 552 | full | bessel-systems-exist-at-the-real-places (outline), filling-data-of-admissible-data |

## What "outline" means in each case

- **dimension-of-the-target**: the chain of equalities is the Lean proof; each link is a Lean statement of another area (algebraic forms on a definite space, class sums and the mass, Harish-Chandra's formal degree formula), used as stated and named in the proof.
- **unfolding-of-the-scaled-poincare-map**: reduces to `New.Filling.Fits.petersson_poincare` and `New.Data.poincare_eq_poincareMap_comp` (unfolding area).
- **bad-types-are-rare**: parts 1, 2 proved; part 3 quotes `New.re_coeff_one_sub_sum_tupleIdem_le` and five size inequalities proved in Lean by the automatic `le_of_hasLogBound`, which I did not re-derive by hand.
- **good-poincare-map-is-a-near-isometry**, **second-moment-of-the-poincare-map**: direct applications of two theorems of `New/Spanning/Unfolding/Moments`.
- **eigensystem-parts-decompose-the-forms**: spanning rests on the library statement `IsUnitary.le_span_hecke_eigenvectors` (spectral theorem), whose exact hypotheses I read only at the call site.
- **equal-traces-on-good-forms**: rests on the library comparison of traces `New.trace_eq_of_isCuspidalAt` and on `New.isCuspidalAt_convIndicator_tupleIdem`; both statements were opened and are quoted.
- **gram-section-is-a-section**: the isometry property is reduced, as in Lean, to an identity `y* J y = x* J x` of explicit block matrices; Lean proves it by `simp` + `grind` entrywise, and I did not carry out that computation by hand.
- **coordinates-on-frames-over-a-gram-matrix**, **mean-value-inequality-over-the-gram-section**: the structure of the changes of variables is given; the Jacobian lemmas (`lintegral_eq_unipotent_coords`, `lintegral_eq_polar`, `exists_measurePreserving_hermCorner`, `lintegral_eq_det_mul_comp_*`) and the fibre-measure criterion `LeFibreMeasure.of_coordinates`, `LeGramFibre.mconv_fixerHaar_le` are library statements quoted from their use; I did not open their definitions in `Lib/DiscreteSeries/Haar`.
- **sobolev-bound-at-the-gram-section**: the Sobolev trace inequality `New.sobolev_trace_cube` is quoted (its constant is read off the call site, not from its own statement), and differentiation under the integral is described, not redone.

- **open-cell-bound-exists**: the existence of tubes (`RealPlace.exists_tube`, statement opened) and the invariance `IsBesselFunction.enorm_integral_besselS_mul` are quoted; the rest follows the Lean proof step by step.
- **stationary-point-with-large-period**: the two appendix theorems `IsSteep.exists_isStationary` and `IsPosition.period_lower_bound_of_surjective` carry the analysis; I read them only at the call sites and did not open `New/Appendix/DiscreteSeries`. The notions `IsSteep`, `IsPosition`, `LowersFlag`, `InducesOn`, `positionGroup`, `laplaceIntegrand` are described from the docstrings of this file.
- **bessel-average-properties**, **cut-pair-from-the-bessel-average**, **schur-bound-holds-for-functions-fixed-by-the-kernel**: library statements on the discrete series coefficient (`norm_dsCoeff_le_pow`, `lintegral_decay_le`, `isIdempotentKernel_dsCoeffInFrame`, `integral_tail_le`, `exists_smear_dsCoeffSmooth_eq`, `IsKHighest.norm_apply_le_of_mem_filtration`, `lintegral_sq_convolve_convolve_le`, `integral_inner_translate`) are quoted from call sites, not from their own statements.
- **bessel-systems-exist-at-the-real-places**: assembles the above; `Floors.exists_hasLocalBounds_of_isCutBessel` (Frames area) and `Data.exists_isSteep` are quoted from the call; about fifteen size inequalities are discharged in Lean by `le_of_hasLogBound` and not re-derived.

## Doubts and things to check

1. **Library lemmas.** In the third session I opened the statements of `exists_mul_unipotentOf_dualCols_eq`, `witt`, `exists_embedH_eq_of_fix_frameCols`, `norm_sub_le_of_holomorphic_bdd`, `measurePreserving_conj_bessel`, `lintegral_orbitMeasure_lintegral`, `sobolev_trace_cube`: all quotations agreed in substance; the wording for `sobolev_trace_cube` in sobolev-bound-at-the-gram-section was made exact (hypothesis `0 < eps <= 1`, integrals rather than means, constant `(2/eps (1+(|L| Lambda)^2))^|D|`). Still quoted from call sites only: `exists_besselU_mul_toBesselH`, `exists_mem_besselU_frameMatrix_eq`, `identDistrib_orbitMeasure_comp`, `isUnimodularHaar_besselHaar₀`, the Jacobian lemmas of MeanValue, and the discrete series statements listed above.
2. **Namespaces of `?lean:` placeholders.** I checked by hand: `New.Filling.HasAmplitudeBlocks.*`, `New.Filling.Fits.petersson_poincare`, `New.Filling.Fits.poincareMap`, `New.RealPlace.fixerHaar`, `New.RealPlace.unipotentOf`, `New.RealPlace.liftUnitriangular`, `New.frameVector`, `New.realFrameGram`, `New.hermOfReal`, `New.LeGramFibre`, `New.Space.formRep`, `New.Gf`, `New.trace_eq_of_isCuspidalAt`, `New.Orbital.harish_chandra_degree_and_orbital`. Not checked individually (taken from the docstrings' `New.…` spellings or from dot-notation): `New.Shape.Form.floorGroup`, `New.Floors.FloorGroups.weylElem`, `New.HasHeckePolynomial`, `New.haarU`, `New.volU`, `New.SieveSystem`, `New.headWeight`, `New.goodTuples`, `New.IsLabel`, `New.stdLevel`, `New.heckeSplit`, `New.universalLevelAlgebra`. An automatic check I ran misbehaved, so a mechanical pass is advisable.
3. **Statement surprises.**
   - `card_mul_sum_det_eq_zero_le` does not require `A₀ v ≠ 0`; the stabiliser hypotheses are for all `v ≠ 0`.
   - `IsSpread` uses `finrank`, so the share is 0 when the target is zero or infinite-dimensional; `isSpread_of_second_moment` has no nontriviality hypothesis.
   - `HasLocalBounds` and `pairingBoundSq` use truncated subtraction of naturals (`k - n^7`, `k - 1`); noted in the knowl.
   - `BesselSystem.irreducible` is stated as "commutant is scalar", not as irreducibility of a representation.
   - `heckeOperator (w, i)` is 0 when `w` is not split off the level, so eigensystems are functions on all pairs.
   - In `Bessel/Basic`, `besselLength ≥ 0` is all Lean proves; I state `≥ 1`, which is immediate from the definition.
4. **bessel-lattice-basis**: I describe the base ring as "commutative ring with involution" and `N = p p̄` with `p` a unit, as in `gram_besselLatticeBasis`; the Lean definition `latticeMiddleGram` itself takes any `N`.
5. **The scratchpad collision** of the first session: the eight files were moved back and their headers fixed in the second session; in the third session I re-read all eight bodies in full and found them intact (no foreign text, one References section each).
6. `prerequisites` are left empty everywhere (placeholders remain).

7. In sizes-near-a-point-of-the-open-cell the operator norm bound is the Lean entrywise bound `l * l * M^2 <= M^4`; I state it that way.
8. The local-bounds knowl says "floor group of level rho"; in Lean it is `floorGroup 𝔰.ϱ` and I did not open its definition (described from the docstring of `HasLocalBounds`).

## Not done

- Nothing of the assignment is unread. Not attempted: hand verification of the entrywise identity for the Gram section, and opening the appendix/library statements listed under "outline".
