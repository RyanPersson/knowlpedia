# Coverage report: spanning-unfolding-a

## Split of the folder `New/Spanning/Unfolding`

`ls` shows **19** files, not 22 (the orchestrator's message said 22): AmplitudeSums, BesselFormula, BesselLevelStructure, Climbing, CutoffIntegral, FillingAdmissible, FrameMass, Link, MomentBounds, Moments, Packing, PoincareSeries, ReducedGroups, ReducedPoints, SeriesPeriod, Setup, SquareExpansion, Terms, TermStructure.

In-folder imports: BesselFormula←PoincareSeries; BesselLevelStructure←Setup; SeriesPeriod←BesselFormula, FillingAdmissible; CutoffIntegral←Packing; Link←Terms; PoincareSeries←AmplitudeSums; AmplitudeSums←CutoffIntegral; Climbing←AmplitudeSums; ReducedGroups←Climbing; Moments←MomentBounds; FillingAdmissible←FrameMass, PoincareSeries, ReducedGroups; Terms←BesselLevelStructure; MomentBounds←SquareExpansion; TermStructure←Climbing; Packing←ReducedPoints. (FrameMass, ReducedPoints, Setup, SquareExpansion import nothing from the folder.)

Order by imports, ties broken alphabetically (repeatedly take the alphabetically first file all of whose in-folder imports are already listed):

1. FrameMass  2. ReducedPoints  3. Packing  4. CutoffIntegral  5. AmplitudeSums  6. Climbing  7. PoincareSeries  8. BesselFormula  9. ReducedGroups  10. FillingAdmissible  11. SeriesPeriod  | 12. Setup  13. BesselLevelStructure  14. SquareExpansion  15. MomentBounds  16. Moments  17. Terms (or TermStructure, depending on the collation of `Terms`/`TermStructure`)  18. Link  19. TermStructure.

**My half (first 11):** FrameMass, ReducedPoints, Packing, CutoffIntegral, AmplitudeSums, Climbing, PoincareSeries, BesselFormula, ReducedGroups, FillingAdmissible, SeriesPeriod. The remaining 8 (Setup, BesselLevelStructure, SquareExpansion, MomentBounds, Moments, Terms, Link, TermStructure) belong to spanning-unfolding-b. Because the true count is 19, "first 11" and "last 11" would overlap in files 9–11 (ReducedGroups, FillingAdmissible, SeriesPeriod) if the sibling took the last 11; if the sibling uses a different tie-break, the split may differ. This needs a check by the orchestrator.

Note that this order puts the folder's *foundations* (Setup, BesselLevelStructure, Terms: the definition of the filling data, classes, cutoffs, amplitudes, terms) in the sibling's half; all those objects are linked from here by `?lean:` placeholders (`New.Filling`, `New.Filling.classUnipotent`, `New.Filling.classCutoff`, `New.Filling.termsOver`, `New.Filling.amplitude`, `New.Filling.amplitudeSum`, …), and I opened their definitions in `Setup.lean` (lines 58–761 read in full).

General remarks. Helper scripts: scratchpad subfolder `spanning-unfolding-a`. No subagents were used (an initial attempt to fork was refused by the harness before any work was delegated). Every proof marked `full` was read verbatim in Lean, tactic lines included; where the Lean proof ends in `simp`/`grind`/`aesop` on matrix entries, the hand computation in the knowl is mine and is flagged below.

## Summary

All 11 assigned files were read in full (8177 lines). 81 proof knowls + the area page.

| File | lines | knowls | Lean declarations covered | full | outline | definitions/constructions |
|---|---|---|---|---|---|---|
| FrameMass | 354 | 5 | 19 | 3 | 0 | 2 |
| ReducedPoints | 670 | 9 | 16 | 9 | 0 | 0 |
| Packing | 538 | 4 | 17 | 4 | 0 | 0 |
| CutoffIntegral | 749 | 7 | 30 | 6 | 0 | 1 |
| AmplitudeSums | 953 | 11 | 33 | 10 | 0 | 1 |
| Climbing | 1286 | 12 | 64 | 7 | 0 | 5 |
| PoincareSeries | 1027 | 9 | 59 | 6 | 1 | 2 |
| BesselFormula | 429 | 3 | 19 | 2 | 0 | 1 |
| ReducedGroups | 631 | 5 | 31 | 5 | 0 | 0 |
| FillingAdmissible | 785 | 9 | 28 | 5 | 3 | 1 |
| SeriesPeriod | 755 | 7 | 36 | 5 | 1 | 1 |
| **total** | 8177 | 81 | 352 | 62 | 5 | 14 |

By kind: 36 theorems, 12 propositions, 19 lemmas, 13 definitions, 1 construction, 1 page. By status: 62 full, 5 outline, 0 cited, 0 statement.

Outline knowls and what is asserted in each:
- `filling-data-fit-the-space-y0`: the block-matrix identity between the graded lattice basis of Y_0 and the lattice basis of the filling data (inside `New.Data.filling_fits`).
- `degree-of-bessel-systems-of-the-data`: the case check `targetParameter_sub_mem_Icc` and the identification of the degree with the product over pairs (`filling_besselDegree_eq_exp_sum`).
- `groups-of-a-graded-fitting-space`: the block-by-block check for the Bessel groups (`mem_besselGroup_iff_mem_besselS`).
- `bessel-character-extends-generic-character`: `shift_eq_smul_besselCharMatrix`.
- `ratio-of-main-and-identity-second-moments`: the logarithmic estimate `abs_log_mainSecondMoment_div_identitySecondMoment_sub_le` (a long automated linear-arithmetic proof).

## Cross-cutting doubts

1. **Split of the folder** (see top): 19 files, not 22; the foundations of this folder (Setup, BesselLevelStructure, Terms, Link) are in the other half. Roughly 240 distinct `?lean:` placeholders point outside this area; I checked mechanically that each last name component exists as a declaration or structure field in the source and that the namespace matches (5 mismatches found and fixed). Structure fields (`New.Filling.chosenPlaces`, `New.Filling.sourceLevel`, `New.Data.weight`, `New.Grading.genericConst`, fields of `IsDiscreteSeriesBessel`, `IsCutPair`) are linked by their field names; the resolver may need to map them to the structure's knowl.
2. **Size calculus.** Every inequality proved in Lean by `D.le_of_hasLogBound` / `D.nat_le_of_hasLogBound` is cited, not re-derived (about 20 uses in FrameMass and FillingAdmissible).
3. **Hand computations replacing `simp`/`grind`/`aesop`.** Where a Lean proof is an automated matrix-entry check, the knowl gives a hand computation that I verified myself (Eichler maps, unitriangularity, additivity of row entries, covolume exponents, Siegel constant identity, mean value algebra). These are faithful to the statements but are not line-by-line translations.
4. **Objects of other areas described here.** `G_1`, Bessel systems, decay majorants, `besselQuotMeasure`, spaces with a point, gradings, forms of a type, type kernels, algebraic forms, Schur matrices, the source function, the generic character: described from docstrings and signatures; the definitions I opened are listed per file above.
5. **Automatic linking pass.** After writing, I ran a script that links the first plain-text occurrence of about 30 standard terms per knowl (CM field, Haar measure, residue field, hermitian form, isometry, unitriangular, …) to `?c:` placeholders or existing ids; 204 links were added mechanically. Existing corpus ids used: `harmonic-analysis/haar-measure`, `algebra-commutative/residue-field`, `catalog/arithmetic/adeles-number-field-finite`, `algebra-fields-galois/number-field-discriminant`, `algebra-groups/orbit-stabilizer-theorem`; I trusted their titles and did not open them.
6. **Bundling.** Some knowls merge a definition with its basic lemmas, or several closely related lemmas (e.g. `lattices-of-unipotent-row-coordinates`, `space-fitting-filling-data`, `poincare-map-of-admissible-data`); the `lean` front matter lists every merged declaration.
7. Indexing of rows `a` from 0 (Lean) versus `e_1..e_ϱ` (text) — flagged in the CutoffIntegral section.
8. The scratchpad is shared: my first helper script was overwritten by another agent before use; nothing was lost, and all helpers now live in the subfolder `spanning-unfolding-a`.

# Per-file notes

## FrameMass.lean (354 lines) — read in full, proofs included

Knowls: `size-of-different-generator-at-infinite-places` (lemma, full), `unit-sphere-mass` (definition, with five proved properties), `frame-mass` (definition, with three proved properties), `product-of-frame-masses-upper-bound` (theorem, full), `product-of-frame-masses-and-open-cell-constant` (theorem, full; I re-did the logarithmic bookkeeping by hand and it closes).

Folded: `r_eq_k_add_two_mul_varrho_add_one`, `cast_card_Ico_k_r`, `sum_Ico_k_r_cast`, positivity lemmas.

Doubts: every numerical comparison "by the size calculus" (`D.le_of_hasLogBound`, `D.nat_le_of_hasLogBound`) is an automated magnitude comparison in Lean; the knowls cite it as an external item of the proof and do not re-derive the inequalities from the scale inequalities. The interpretation of `sph_l` as a sphere mass for a fibre measure is only a comment in the source; no statement about measures is proved in this file.

## ReducedPoints.lean (670 lines) — read in full, proofs and tactic lines included

Knowls: `eichler-map-is-isometry` (lemma, full; recomputed by hand), `eichler-elements-of-unipotent-congruence-subgroup` (lemma, full; unitriangularity re-derived by hand, the level step rests on four linked statements of the sibling half: `classCoord_conj_splitGram`, `isUnimodular_latticeMiddle`, `IsUnimodular.mem_unitaryLevel`, `principalLevel_eq_unitaryLevel`), `eichler-element-with-prescribed-row` (lemma, full), `frame-matrices-of-unipotent-congruence-subgroup` (proposition, full), `colouring-bound-for-weighted-sums` (lemma, full), `index-of-scaled-integral-lattice` (lemma, full, cites `submoduleIndex_colLattice_intVectors`), `reduction-of-unitriangular-matrices` (lemma, full; I also read the proof of the Lib lemma `Filling.existsUnique_mul_mem_box` it specialises), `unique-coset-moving-a-point-to-a-reduced-point` (theorem, full), `reduced-points-give-box-partition-of-unity` (theorem, full; items 1–3 are citations of `RemainingTerms/Box.lean`).

Doubts: in `eichler-elements…` the Lean proof of unitriangularity and of the row read-off is `simp`/`grind`/`aesop`; the hand computations in the knowls are mine and I checked them against the statements. The exact conjugation conventions (which of `u`, `uᴴ` carries the conjugate) are stated in matrix form as in Lean. The objects `G₁`, `gramSchmidtMatrix`, `basisScale`, `IsBoxPartitionOfUnity` belong to other areas; I opened their definitions.

## Packing.lean (538 lines) — read in full, proofs and tactic lines included

Knowls: `class-cutoff-translates-sum-to-one` (proposition, full; six items, merging `tsum_classCutoff_eq_one`, `measurable_classCutoff`, the box lemmas and the two existence lemmas), `rigidity-of-frames` (theorem, full; the six helper lemmas are folded into the three steps), `packing-of-frames` (theorem, full), `packing-of-weights` (lemma, full).

Doubts: in `rigidity-of-frames` Step 1 the identification of `h_1(y⁻¹f_b, (γ⁻¹y)⁻¹f_a)` with the frame product of the image of γ is `realFrameGram_eq_inner` + `realFrameGram_ratToInf` (other areas), which I cite by statement; the closure of terms under inverse/product used in `packing-of-frames` is `termsOver.inv`/`.mul` of the sibling half (Terms.lean), not opened. The norm on the space of families of frame vectors is the sup norm over places and frame indices of Euclidean norms (Lean's Pi norm).

## CutoffIntegral.lean (749 lines) — read in full, proofs and tactic lines included

Knowls: `amplitude-bounded-by-majorant` (lemma, full), `additivity-of-unipotent-row-entries` (lemma, full; the case analysis is re-derived by hand from the Lean proof, which ends in `grind`), `row-coordinates-of-real-unipotent-group` (construction), `integral-of-class-cutoff-over-fundamental-set` (lemma, full), `lattices-of-unipotent-row-coordinates` (proposition, full; merges the definitions `freeBlock`, `freeLattice` with eight lemmas), `fundamental-box-for-arithmetic-unipotent-group` (proposition, full; the exponent bookkeeping of `unipotentCovolume_eq_prod` and `prod_norm_basisScale_sq_div_eq` re-done by hand), `integral-of-class-cutoff-is-unipotent-covolume` (theorem, full).

Doubts: (1) Indexing: Lean counts rows `a : Fin ϱ` from 0 and the scale of `e_a` is `κ_v^(ϱ-a)/√N`; the knowls say "counted from 0" where exponents depend on it, but elsewhere write `e_1..e_ϱ`. (2) In `lattices-…` (i) the exact shape of the middle block (`h` times the lattice change of basis) is read from the `simp` call, not from an explicit formula; only the index `N^(-f)` of its determinant is used and that derivation is explicit in Lean. (3) The covolume formulas for the two lattices are Lib statements (`exists_fundamental_domain_classLattice`, `Filling.exists_fundamental_domain_im_skew`) cited by content.

## AmplitudeSums.lean (953 lines) — read in full, proofs and tactic lines included

Knowls: `scaled-bessel-length-product` (definition), `unfolding-class-cutoff-against-invariant-weights` (lemma, full), `summation-by-layers` (lemma, full; I wrote out the layer-cake computation, the Lean proof calls the Lib lemma `lintegral_rpow_neg_le_of_measure_sublevel_le`, whose statement I did not open — its use fixes the conclusion `≤ 2 K^d`), `sum-of-cutoffs-with-inverse-length-powers` (proposition, full), `cut-changes-kernel-little` (lemma, full), `convergence-of-block-sums` (theorem, full), `tail-bound-for-the-cut` (theorem, full; exponent arithmetic re-checked), `change-of-weight-in-block-sums` (theorem, full; rests on the Lib quotient-measure statements `identDistrib_orbitMeasure`, `IsCutoff.integral_orbitMeasure`, cited by content, and I added the elementary direct argument for the nonnegative case), `moving-a-block-by-the-bessel-subgroup` (proposition, full), `block-sums-under-unipotent-reductions` (theorem, full), `identity-block-of-the-bessel-subgroup` (theorem, full).

Folded: `tsum_integral_apply` (exchange of a coordinate with sum and integral; not used inside this file's main results), `sigmaFinite_orbitMeasure`, `le_scaledBesselLengthProd_pow_mul`, `Fintype S.ResidueGL`.

Doubts: (1) `besselQuotMeasure` is described from its use (Haar measure of G₁ weighted by a chosen cutoff for 𝖴); I did not open its definition line. (2) In `change-of-weight…` the Lean proof obtains the block as the integral over the "orbit measure"; my text phrases this as the integral over the quotient. (3) `tsum_integral_apply` has no knowl; if a later file uses it, it should be cited from here.

## Climbing.lean (1286 lines) — read in full, proofs and tactic lines included

Knowls: `prescribing-residues-above-the-level` (lemma, full), `meeting-places-and-meet-norm` (definition; `actionAt`, `MeetsAt`, `meetNorm`), `fixers-of-frame-vectors` (definition; `FrameVector`, `vectorFixer`, `fixer`), `open-element-of-residue-group` (definition), `scalar-coset-of-bessel-subgroup` (definition), `unitary-group-of-x0-in-lattice-basis` (proposition, full), `terms-with-disagreeing-characters-contribute-zero` (theorem, full), `common-vectors-of-two-flags` (definition, with four proved properties), `climbing-common-vectors-over-the-field` (theorem, full), `climbing-common-vectors-modulo-a-place` (theorem, full), `meet-norm-bounded-by-index-of-determinant` (theorem, full), `existence-of-cell-rank` (theorem, full — but see doubt 3).

Doubts.
1. `terms-with-disagreeing-characters…`: in Lean the adapted weight is `wt γ = (classCutoff c' (ratToInf γ)⁻¹ * reps.indicator 1 γ) • φ γ`, i.e. the class cutoff is evaluated at the single point γ⁻¹ of G_∞ (a number), not as a function of y. I first misread this and then rewrote the knowl to follow Lean literally; the orbit-sum computation in the knowl is mine (Lean: one `simp` line plus `tsum_indicator_smul_eq_tsum_stabilizer`).
2. `climbing-…-over-the-field`/`…-modulo-a-place`: the conjugation identity "γ w γ⁻¹ is the Eichler map along γ·(…)" is the content of the `simp` call proving `u * γ = γ * w`; the reduction formula of the integral Eichler map modulo a place is the last `simp` of `exists_eichler_mem_latticeStabilizer`. I state both as computations but did not expand every matrix entry. The exact formula of `eichlerMap` and of `simpleRootSum` is taken from the docstring/definition in other areas (`Lib/Adelic/Witt/WittTheorem`, `BesselLevelStructure`).
3. `existence-of-cell-rank`, step (c): rests on three statements of the sibling half (`NormOnePairOccursFrom.inv`, `exists_frameImage_eq_of_normOnePairOccursFrom`, `frameProducts_mulVec_of_frameImage_eq`); I re-derived the first and the third by hand in the knowl and cite the second by its statement. Kept `full`.
4. `meet-norm-…`: the theorem statement paraphrases `((framePair k)ᴴ * t)`; the two "last rows" are selected through an auxiliary bijection `ρ : W ≃ Unit ⊕ Unit` (`lastIndices`), which the knowl suppresses.

## PoincareSeries.lean (1027 lines) — read in full, proofs and tactic lines included

Knowls: `space-fitting-filling-data` (definition; `Fits`, `stdPrincipalLevel` and the identifications `ratEquiv`, `adelicEquiv`, `realHomeomorph`, `finiteEquiv`, `classPoint` with their compatibility lemmas), `poincare-series-of-bessel-functions` (definition; `cutBessel`, `poincareSeries`), `convergence-of-poincare-series` (proposition, full), `unfolding-of-poincare-series` (theorem, full), `poincare-series-are-forms` (theorem, full; defines `poincareMap`), `folding-of-poincare-series` (theorem, full), `petersson-products-of-poincare-series` (theorem, full), `groups-of-a-graded-fitting-space` (proposition, full), `source-forms-in-bessel-coordinates` (theorem, full).

Doubts.
1. This file sits on a large amount of machinery from `Lib/Adelic` and `Lib/DiscreteSeries` (spaces with a point, gradings, forms of a type, type kernels, quotient measures, algebraic forms, Schur matrices). I opened `Space`, `G`, `GInf`, `Gf`, `Γ`, `IsAutomorphic`, `IsForm`, `petersson`, `Form`, `formRep`, `realConv`, `typeKernel`, `HasLevel`, `levelOf`, `exists_form_eq_tsum`, `IsDiscreteSeriesBessel` (docstrings and signatures), but **not** `Grading`, `HCParam`, `IsIdempotentKernel`, `algFormRep`'s weight convention, `WeylIndex`, `schur`, `freeLevelEquiv`; the knowls describe those only through the statements used. In particular the definition knowl `space-fitting-filling-data` bundles one definition with five constructions and is closer to a "setting" page than the GUIDE would like; it could be split later.
2. `groups-of-a-graded-fitting-space` item 2 (Bessel groups): the Lean proof is a `simp`/`grind` case check on the three blocks; I did not re-derive it, and the definition of `Grading.besselGroup` was not opened. Treat item 2 (second half) as asserted.
3. `source-forms-in-bessel-coordinates`: the direction of the transposes/row-vector conventions is copied from the Lean statement.
4. The orientation of the Petersson product (conjugate-linear in the first argument) is from `Space.petersson`.

## BesselFormula.lean (429 lines) — read in full, proofs and tactic lines included

Knowls: `real-bessel-group-is-product-of-local-groups` (proposition, full), `bessel-character-of-fitting-space` (definition, with one proved property), `bessel-function-as-one-integral` (theorem, full).

Doubts: the local formula `IsDiscreteSeriesBessel.exists_eq_besselAverage` and the definitions `besselIntegrand`, `wave`, `dsCoeffInFrame`, `besselGraph`, `besselGraphMeasure`, `Grading.besselReal`, `Grading.leviPart`, `conjWeylRep` are from other areas; I used the docstrings of this file and the way they are unfolded in the proofs (`wave w = exp(w - conj w)` is inferred from `besselChar_inl_inv`), and did not open their definitions. The remark that `besselChar` extends the generic character is docstring-only and is flagged as such in the knowl.

## ReducedGroups.lean (631 lines) — read in full, proofs and tactic lines included

Knowls: `gluing-integral-isometries-at-chosen-places` (lemma, full), `reduced-unipotent-group` (theorem, full; the count of free entries re-done by hand), `reductions-are-products-over-places` (theorem, full), `reduced-levi-group` (theorem, full), `reduced-bessel-group` (theorem, full).

Folded: `mulEquivOfKerEq`, `unitriangularEquiv`, `card_unitriangular`, `exists_unitriangular_map_eq`, `splitGram_apply_eq_zero`, `map_matrix_one_apply`.

Doubts: `mem_unitaryLevel_of_besselU_mul`, `range_inclHFin`, `inclHFin_mem_besselH`, `exists_reduceFamily_eq` are cited by statement (the first is paraphrased from its two uses, with level 1 and level M; I did not open it). In `reductions-are-products…` the hypothesis in Lean is an arbitrary relation `r a b` on index pairs; "the Bessel subgroup is of this form by definition" corresponds to `fun _ ↦ Iff.rfl`.

## FillingAdmissible.lean (785 lines) — read in full, proofs and tactic lines included

Knowls: `filling-data-fit-the-space-y0` (theorem, **outline**: the block-matrix identity relating `gradedLatticeBasis` to the lattice basis of the filling data is asserted), `source-form-coordinates-of-the-data` (definition; `D.sourceFormCoords`, `D.goodProjTranslate`), `number-of-bessel-coordinates` (lemma, full), `degree-of-bessel-systems-of-the-data` (proposition, **outline**: the case check in item 1 and the identification of the degree with the product over pairs are asserted; the two-sided bound is derived), `number-of-classes-of-the-source-level` (theorem, full), `mean-value-bounds-for-the-main-second-moment` (theorem, full; algebra re-checked), `scaled-siegel-constant-bound` (lemma, full; algebra re-checked by hand), `ratio-of-main-and-identity-second-moments` (theorem, **outline**: item 2, the long `linarith` verification, is asserted; items 1 and 3 are derived), `filling-data-of-admissible-data-are-admissible` (theorem, full, every item cited).

Doubts: (1) The instance `D.filling.IsAdmissible` is anonymous in Lean; the Lean name recorded in the front matter of the last knowl (`New.Data.instIsAdmissibleFilling`) is a guess at the auto-generated name — the resolver should match on the file instead. (2) I did not open `logLevelTarget`, `targetParameter_eq`, `liftWeight`, `paramW`, `columnCount`, `gradedLatticeBasis`, `principalForms`, `e₀`; they are described from the docstrings in the head of this file and of the reading guide.

## SeriesPeriod.lean (755 lines) — read in full, proofs and tactic lines included

Knowls: `bessel-character-extends-generic-character` (proposition, **outline**: the matrix identity `shift = c · besselCharMatrix` is asserted), `class-sections-and-class-weights` (definition, with four proved properties), `bessel-function-paired-with-a-form-value` (theorem, full), `moving-the-quotient-to-the-bessel-group` (lemma, full), `bessel-quotient-as-union-of-class-quotients` (theorem, full), `poincare-series-represents-the-bessel-period` (theorem, full), `poincare-map-of-admissible-data` (theorem, full; also carries the definitions `D.besselPoint`, `D.besselForm`, `D.poincare`).

Doubts.
1. `poincare-map-of-admissible-data` merges a theorem with the definition of `D.poincare` (the map 𝒫 of the reading guide). Other areas will link `New.Data.poincare`; the resolver will land on this theorem knowl. If a separate definition knowl is preferred, split it.
2. The objects `Grading.sourceFn`, `Grading.unipotentChar`, `Grading.shift`, `Grading.genericConst`, `Grading.ratBessel`, `Grading.besselMeasure`, `WeilData.j`, `D.poincareAt` are from `Lib/Weil/Periods` and `New/UpperBound/Objects/PoincareMap`; I opened the docstrings/signatures of `sourceFn`, `besselMeasure`, `poincareAt`, `inner_poincareAt`, `integral_cutoff_swap`, `exists_integral_eq_mul_integral_besselReal`, `exists_besselU_approx`, not the others. The formula for `unipotentChar` (`ψ((ȷ/2) tr(𝔢 u))`) in the outline knowl is reconstructed from the proof of `besselChar_eq_unipotentChar` and should be checked against `Lib/Weil/Periods`.
3. In `bessel-quotient-…` item 1 (existence) the final computation "the element is ι(k) times the inverse of the approximation error" is the `simp` call proving `h_eq`; I state it without expanding.
4. The hypothesis `ȷ c_Y = -(M ϖ)⁻¹` for the data is proved in Lean by `simp [gradingY, filling, M, field]`; I describe it as "by definition".
