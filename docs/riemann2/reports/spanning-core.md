# Coverage report: spanning-core

Author run in two sessions (the first was cut by a rate limit). State at the end of the second session.

## Summary

- 52 proof knowls in `knowlpedia-content/content/proofs/grh/spanning-core/`, plus the area page `proofs/grh/spanning-core.knowl.md`, the sidecar `concepts/spanning-core.tsv` (67 concepts).
- 10 of the 17 assigned files were read completely, proofs and tactic lines included, and translated. **7 files of `Bessel/` were not read and have no knowls** (list below). Import order was followed; I stopped there because of budget.

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
| `Bessel/Average` | 161 | **not read** | none |
| `Bessel/OpenCellBound` | 725 | **not read** | none |
| `Bessel/OpenCellPairing` | 274 | **not read** | none |
| `Bessel/LargeFunction` | 771 | **not read** | none |
| `Bessel/CutTailBound` | 465 | **not read** | none |
| `Bessel/SchurBound` | 323 | **not read** | none |
| `Bessel/FillingData` | 552 | **not read** (only the line defining `New.Data.filling` was located) | none |

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

## Doubts and things to check

1. **Library lemmas quoted from call sites.** In several "full" proofs a step is a Lean statement of `Lib` that I paraphrased from how it is applied rather than from its own docstring: `exists_besselU_mul_toBesselH`, `exists_mem_besselU_frameMatrix_eq`, `exists_mul_unipotentOf_dualCols_eq` (in bessel-length-versus-orthogonal-frame), `witt` and `exists_embedH_eq_of_fix_frameCols` (in fibres-of-the-frame-gram-map), `norm_sub_le_of_holomorphic_bdd`, `measurePreserving_conj_bessel`, `identDistrib_orbitMeasure_comp`, `lintegral_orbitMeasure_lintegral`, `isUnimodularHaar_besselHaar₀`. The paraphrases are what the call needs, but the precise hypotheses of those lemmas should be confirmed by the author of the corresponding `Lib` area.
2. **Namespaces of `?lean:` placeholders.** I checked by hand: `New.Filling.HasAmplitudeBlocks.*`, `New.Filling.Fits.petersson_poincare`, `New.Filling.Fits.poincareMap`, `New.RealPlace.fixerHaar`, `New.RealPlace.unipotentOf`, `New.RealPlace.liftUnitriangular`, `New.frameVector`, `New.realFrameGram`, `New.hermOfReal`, `New.LeGramFibre`, `New.Space.formRep`, `New.Gf`, `New.trace_eq_of_isCuspidalAt`, `New.Orbital.harish_chandra_degree_and_orbital`. Not checked individually (taken from the docstrings' `New.…` spellings or from dot-notation): `New.Shape.Form.floorGroup`, `New.Floors.FloorGroups.weylElem`, `New.HasHeckePolynomial`, `New.haarU`, `New.volU`, `New.SieveSystem`, `New.headWeight`, `New.goodTuples`, `New.IsLabel`, `New.stdLevel`, `New.heckeSplit`, `New.universalLevelAlgebra`. An automatic check I ran misbehaved, so a mechanical pass is advisable.
3. **Statement surprises.**
   - `card_mul_sum_det_eq_zero_le` does not require `A₀ v ≠ 0`; the stabiliser hypotheses are for all `v ≠ 0`.
   - `IsSpread` uses `finrank`, so the share is 0 when the target is zero or infinite-dimensional; `isSpread_of_second_moment` has no nontriviality hypothesis.
   - `HasLocalBounds` and `pairingBoundSq` use truncated subtraction of naturals (`k - n^7`, `k - 1`); noted in the knowl.
   - `BesselSystem.irreducible` is stated as "commutant is scalar", not as irreducibility of a representation.
   - `heckeOperator (w, i)` is 0 when `w` is not split off the level, so eigensystems are functions on all pairs.
   - In `Bessel/Basic`, `besselLength ≥ 0` is all Lean proves; I state `≥ 1`, which is immediate from the definition.
4. **bessel-lattice-basis**: I describe the base ring as "commutative ring with involution" and `N = p p̄` with `p` a unit, as in `gram_besselLatticeBasis`; the Lean definition `latticeMiddleGram` itself takes any `N`.
5. **The scratchpad collision** of the first session (a foreign `k.sh`) wrote eight of my files into `upper-elementary-divisors/` with a foreign header; I moved them back, corrected `id`, `lean_files`, `proof_status`, and removed the duplicated References sections. I re-checked all 12 files of that batch (one `+++` pair, one References section, right `lean_files`), but the bodies were not re-read word by word.
6. `prerequisites` are left empty everywhere (placeholders remain).

## Not done

- Knowls for the seven unread `Bessel` files, in particular `New.Data.filling` (FillingData), `New.BesselSystem.IsOpenCellBound` (OpenCellBound/OpenCellPairing), the existence of Bessel systems (LargeFunction, CutTailBound, SchurBound, `New.Data.exists_besselSystem`). Links to them use `?lean:` placeholders.
