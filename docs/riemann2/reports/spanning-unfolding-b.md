# Coverage report: spanning-unfolding-b

## Split of the folder `New/Spanning/Unfolding`

`ls` shows 19 files (not 22). In-folder imports: AmplitudeSums←CutoffIntegral; BesselFormula←PoincareSeries; BesselLevelStructure←Setup; Climbing←AmplitudeSums; CutoffIntegral←Packing; FillingAdmissible←FrameMass, PoincareSeries, ReducedGroups; Link←Terms; MomentBounds←SquareExpansion; Moments←MomentBounds; Packing←ReducedPoints; PoincareSeries←AmplitudeSums; ReducedGroups←Climbing; SeriesPeriod←BesselFormula, FillingAdmissible; Terms←BesselLevelStructure; TermStructure←Climbing. FrameMass, ReducedPoints, Setup, SquareExpansion import nothing from the folder.

Order by imports, ties alphabetical (repeatedly take the alphabetically first file whose in-folder imports are all listed):

1 FrameMass, 2 ReducedPoints, 3 Packing, 4 CutoffIntegral, 5 AmplitudeSums, 6 Climbing, 7 PoincareSeries, 8 BesselFormula, 9 ReducedGroups, 10 FillingAdmissible, 11 SeriesPeriod | 12 Setup, 13 BesselLevelStructure, 14 SquareExpansion, 15 MomentBounds, 16 Moments, 17 Terms, 18 Link, 19 TermStructure.

**Split (corrected by the coordinator):** the sibling `spanning-unfolding-a` has files 1–11; this area has exactly the last 8: Setup, BesselLevelStructure, SquareExpansion, MomentBounds, Moments, Terms, Link, TermStructure. No knowls were written here for ReducedGroups, FillingAdmissible or SeriesPeriod.

Working order (a valid import order among the 8): Setup, BesselLevelStructure, Terms, Link, TermStructure, SquareExpansion, MomentBounds, Moments.



## Setup.lean (761 lines) — read in full, proofs verbatim

Knowls (12): `filling-data` (definition), `filling-unitary-groups` (construction), `filling-level-and-reduction` (definition), `filling-classes-and-terms` (definition), `filling-constants` (notation), `filling-admissible` (definition), `class-unipotent-discrete` (lemma, full), `class-cutoff` (construction), `box-partition-of-unity` (definition), `filling-amplitude` (definition), `frame-products-at-infinity` (lemma, full), `unipotent-character-agreement-stability` (definition).

Notes. The Lean docstrings index the frame from 1 in places and from 0 in others; the knowls use \(f_0,\dots,f_\varrho\) (0-based, as the code does). `frameScaleProd`, `unipotentCovolume` are plain numbers; their meaning as covolumes is proved in the sibling area. `classCutoff` depends on two arbitrary choices (`Classical.epsilon` for the residue domain, `choose` for the cutoff); stated as fixed choices. `filling-level-and-reduction`, `filling-classes-and-terms`, `filling-constants`, `unipotent-character-agreement-stability` each group several small definitions of the file that are only used together (a deliberate departure from one-declaration-per-knowl; none bundles a definition with a theorem).

## BesselLevelStructure.lean (949 lines) — read in full, proofs verbatim

Knowls (16): `class-basis` (definition), `terms-compose-like-a-groupoid` (lemma, full), `bessel-groups-in-the-lattice-basis` (lemma, full), `unipotent-character-at-infinity` (lemma, full), `bessel-function-under-unipotent-translation` (lemma, full), `finite-head-weight` (definition), `lattice-middle-form-is-unimodular` (lemma, full), `eichler-map-in-bessel-unipotent-group` (lemma, full), `self-duality-of-integral-adeles` (lemma, full), `principal-level-is-congruence-subgroup` (lemma, full), `strong-approximation-for-bessel-unipotent-group` (theorem, full), `unipotent-character-on-level-cosets` (lemma, full), `bessel-subgroup-terms-in-principal-level` (lemma, full), `rational-unipotent-terms-reach-all-reductions` (theorem, full), `bessel-subgroup-reductions-reached-by-rational-terms` (lemma, full), `freeness-in-small-rank` (lemma, full).

Notes. Several Lean proofs end in `aesop`/`simp` on block matrices (`toLatticeBasis_mem_besselU`, `inclHFin_mem_besselH`, `isUnimodular_latticeMiddleGram`, the unipotence part of `exists_mem_besselU_eq_eichlerMap`); the hand computations in the knowls are mine and were checked entry by entry against the definitions. The helper definitions `invAdjoint`, `idOrInvAdjoint`, `reduceAboveM` are folded into `principal-level-is-congruence-subgroup` (listed in its `lean`). `finHeadWeight` sits in this file but is not used in it. `eq_one_of_reduceAt_eq_one` carries `IsAdmissible` as an unused instance argument (noted in the knowl).

## Terms.lean (628 lines) — read in full, proofs verbatim

Knowls (14): definitions `cell-rank-of-a-term`, `common-link`, `class-coordinates`, `near-term`, `characters-agree`; notation `term-discriminant-norm-and-pair-count-scale`; lemmas/theorems (all full) `norm-identity-for-combinations-of-the-moved-frame`, `term-discriminant-is-totally-positive-or-zero` (theorem), `real-gram-discriminant-of-a-term`, `norm-one-pairs-at-infinite-places`, `frame-products-of-terms-are-integral`, `bounds-for-near-terms`, `terms-with-the-same-frame-image`, `tail-scale-inequalities`.

Notes. `HasCellRank` condition 2 at j = 0 uses the empty minor (= 1). In `frame-products-of-terms-are-integral` the identity "class coordinates fix the frame" is a `simp` computation in Lean; the knowl derives it from \(B_cF=F\). The Lean lemma `isIntegral_frameProducts` assumes admissibility but its proof does not use it.

## Link.lean (944 lines) — read in full, proofs verbatim

Knowls (12): `link-in-coordinates` (lemma, full), `norm-one-pairs-under-inversion-and-unipotent-multiplication` (lemma, full), `link-and-cells-are-invariant-under-the-unipotent-group` (theorem, full), `discriminant-and-link-on-the-big-cell` (theorem, full), `positive-space-and-link-maps` (definition), `rank-of-the-link` (lemma, full), `link-isometry` (construction), `link-is-graph-of-link-isometry` (theorem, full), `isotropic-complement-maps-onto-positive-space` (theorem, full), `link-is-its-own-orthogonal-complement` (lemma, full), `link-isometry-on-the-moved-frame` (theorem, full), `vanishing-of-the-term-discriminant` (theorem, full).

Notes. The map `perpToPositive` is described inside the statement of `isotropic-complement-maps-onto-positive-space` rather than in a knowl of its own. `discriminant-and-link-on-the-big-cell` rests on two statements of `Lib/DiscreteSeries/Bruhat/BigCell.lean` (block form and frame products of \(w_p\sigma\)), whose statements I read and quote; their proofs belong to another area.

## TermStructure.lean (897 lines) — read in full, proofs verbatim

Knowls (9): `spaces-of-the-two-frames` (definition), `frame-complement-and-linked-subspace` (theorem, full), `common-link-by-link-isometries` (theorem, full), `rank-of-the-linked-subspace` (theorem, full), `flags-of-a-term-and-the-cell-rank` (theorem, full), `unipotent-group-acts-on-the-structure-of-a-term` (theorem, full), `remaining-terms` (definition), `remaining-terms-stable-and-complement` (theorem, full).

Notes. Two inputs come from the sibling's file `Climbing.lean` and are quoted with their statements: `CharsAgree.exists_hasCellRank` and `CharsAgree.exists_coords_ne_zero_of_common_vector` (both need the primitive 5040-th root of unity). The map `framePerpToX₀` is described inside the theorem statement.

## SquareExpansion.lean (698 lines) — read in full, proofs verbatim

Knowls (10): `scalar-isometry` (definition), `avoiding-scalar-cosets` (definition), `terms-of-cell-rank-zero-are-scalar-multiples-of-the-bessel-subgroup` (theorem, full), `residues-near-the-reduced-bessel-group` (lemma, full), `blocks-of-the-bessel-subgroup` (theorem, full), `terms-off-the-bessel-subgroup-reduce-to-remaining-terms` (lemma, full), `expansion-of-the-squares` (theorem, full), `second-moment-near-the-bessel-subgroup` (theorem, full), `positive-type-function-is-largest-at-the-identity` (lemma, full).

Notes. The two main theorems are short deductions from results of other areas whose statements are quoted and linked: `secondMoment_remainingTerms_le`, `linkSecondMoment_le_of_le_meetNorm` (RemainingTerms/Sum), `secondMoment_sub_cut_le`, `sqrt_secondMoment_add_le` (RemainingTerms/Size), `amplitudeSum_mul_mul_inv`, `amplitudeSum_besselS_one_eq_ite` (AmplitudeSums), `amplitudeSum_eq_zero_of_not_charsAgree` (Climbing). "full" here means: complete relative to those linked statements. In `terms-of-cell-rank-zero-…` part 3, Lean obtains \(k_{f_0f_0}=\gamma_{f_0f_0}\) by `simp` with `classCoord_eq_fromBlocks`; the knowl argues that the row of the class coordinates at \(e_0\) is a unit row.

## MomentBounds.lean (517 lines) — read in full, proofs verbatim

Knowls (6): `second-moment-off-the-reduced-bessel-group` (lemma, full), `second-moment-over-the-scalar-cosets` (lemma, full), `second-moment-over-a-full-fixer` (lemma, full), `second-moment-over-open-elements-of-a-fixer` (lemma, full), `non-open-elements-carry-little` (lemma, full), `second-moment-over-the-whole-group` (theorem, full).

Notes. Inputs from other areas, quoted with their statements: `linkSecondMoment_isOpenElement_le` (MainTerm/EnergyEstimate — the main term), `card_mul_sum_det_eq_zero_le` (SecondMoment/PositiveType), `linkSecondMoment_le_of_le_meetNorm` (RemainingTerms/Sum). The identification of the two fixing conditions of the determinant sieve with stabilisers of frame vectors modulo \(w\) and its conjugate follows the Lean lemmas `mem_vectorFixer_false/true` (Climbing), which I did not open beyond their docstrings and use sites.

## Moments.lean (1253 lines) — read in full, proofs verbatim

Knowls (12): `amplitude-blocks` (definition), `bessel-translate` (definition), `hilbert-schmidt-norms-of-the-blocks` (lemma, full), `bessel-translate-is-a-unitary-representation` (theorem, full), `equivariance-of-maps-with-amplitude-blocks` (theorem, full), `second-moments-of-the-poincare-operators` (theorem, full), `remainder-against-a-central-idempotent` (lemma, full), `reduced-unipotent-character` (definition), `trace-of-the-twisted-translations` (lemma, full), `square-sum-of-the-induced-character` (theorem, **outline**), `trace-against-a-small-central-idempotent` (lemma, full), `good-forms-near-isometry` (theorem, full).

Notes. `square-sum-of-the-induced-character` is an outline: its Lean proof was read verbatim, but it works with objects over the product of completions at the chosen places (`IsFillingData`, `PlaceData`, `extendedBesselChar`, `massIntegral_le_main_add_error`, `exists_isFillingData`, from MainTerm and Frames) whose definitions I did not open; the knowl says exactly which steps are quoted. The inner product convention in `HasAmplitudeBlocks` (conjugate-linear in the first argument, Mathlib's) is stated in the knowl; the head comment's phrase "the blocks of P_s are the conjugates of the amplitude sums" depends on that convention.

## Summary

All 8 assigned files were read in full, proofs verbatim (6645 lines): Setup 761, BesselLevelStructure 949, Terms 628, Link 944, TermStructure 897, SquareExpansion 698, MomentBounds 517, Moments 1253.

89 proof knowls + the area page `proofs/grh/spanning-unfolding-b`. By kind: 22 definition, 3 construction, 2 notation, 37 lemma, 25 theorem. By status (62 lemmas/theorems): 61 full, 1 outline. 446 Lean declarations are listed in the `lean` fields (every declaration of the eight files that I identified is attached to some knowl; none is listed twice). Sidecar: `concepts/spanning-unfolding-b.tsv` (47 concepts).

### What "full" means here, and doubts

* "Full" is relative to linked statements of other areas whose statement I read and quote but whose proof belongs elsewhere. The heaviest such inputs: `secondMoment_remainingTerms_le`, `linkSecondMoment_le_of_le_meetNorm` (RemainingTerms/Sum); `linkSecondMoment_isOpenElement_le` (MainTerm/EnergyEstimate); `card_mul_sum_det_eq_zero_le`, `inner_hilbertSchmidtVector_translate`, `IsNearIsometry.proj_comp`, `hilbertSchmidtNorm_one_sub_mul_comp_sq_le` (SecondMoment); `amplitudeSum_mul_mul_inv`, `amplitudeSum_besselS_one_eq_ite`, `amplitudeSum_besselU_mul`, `amplitudeSum_eq_zero_of_not_charsAgree`, `CharsAgree.exists_hasCellRank`, `CharsAgree.exists_coords_ne_zero_of_common_vector` (sibling area a); `IsCentralProj.sum_norm_sq_conv_le` and the floor-group lemmas of `Lib/DiscreteSeries/Bruhat`.
* Where a Lean proof ends in `simp`/`aesop`/`grind` on block matrices, the hand computation in the knowl is mine (flagged per file above). I checked these against the definitions of the matrices, not by any tool.
* A few external `?lean:` names were taken from use sites rather than from their declarations and may need a namespace fix by the resolver: `New.IsCentralProj.isChar_card_mul_coeff`, `New.IsCentralProj.self_adjoint`, `New.conj_mem_unitriangular`, `New.frameMatrix_unitriangular`, `New.exists_eq_toBesselH`, `New.HasFiniteType.finite_classes`, `New.InCut`, `New.piTensorElem`, `New.WeilData`, `New.Floors.IntegralPlace.IsLargeLatticeData.massIntegral_le_main_add_error`, `New.Filling.meetsAt_of_mem_vectorFixer`. All others were grepped.
* Objects of other areas that I describe from their docstrings without opening the full definition: `BesselSystem` (opened), `IsLevel`, `mass`, `gramSchmidtMatrix`, `besselLength`, `InScalarCoset`/`MeetsAt`/`meetNorm`/`IsOpenElement`/`fixer`/`vectorFixer` (definitions opened), `WeilData` (not opened; described only as "includes a primitive 5040-th root of unity", following the docstrings in my files).
* Several definition knowls group small definitions of one file that are only used together (`filling-level-and-reduction`, `filling-classes-and-terms`, `filling-constants`, `unipotent-character-agreement-stability`, `positive-space-and-link-maps`, `spaces-of-the-two-frames`). None bundles a definition with a theorem; basic membership lemmas are listed in their `lean` fields.
* Indexing: the Lean docstrings sometimes write the frame as e₁,…,e_ϱ; the knowls use e₀,…,e_{ϱ−1} (the code's indexing) throughout.
* The literature named in the head of `Moments.lean` is listed in the area page as related work only; no locator was checked.
* `prerequisites` is left empty everywhere (placeholders remain), as the guide asks.
