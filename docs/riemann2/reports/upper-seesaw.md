# Coverage report: upper-seesaw (complete pass; all 15 files visited)

Lean folder: `src/New/UpperBound/Seesaw` (15 files, 9049 lines). Files are processed in import order.
Reading mode "filtered" = all doc comments, statements, in-proof comments and `have/obtain/calc` steps read; pure tactic lines skipped.

| File | Lines | Read | Knowls |
|---|---|---|---|
| AdmissibleCombinations | 907 | full to line 640, rest filtered | integral-away, admissible-combination, admissible-combination-substitution (full), admissible-combination-calculus (full), translation-groups, split-squarefree-factorisation, graded-lattice-basis, graded-lattice-basis-unimodular (full), graded-gram-signature (full), l-adic-units-multiplier-and-characters (outline), moved-vacuum-admissible (outline), schrodinger-operator-admissible (outline) |
| StandardLines | 569 | filtered | standard-lattice-membership (full), string-lattices-line-by-line (full), string-sum-lattice-criteria (outline), shift-of-string-lattice (full, relative to the previous), generator-of-plus-over-minus (full) |
| Sandwich | 267 | filtered | lattice-splitting-and-scalings (outline), lattice-bounds-induction-step (outline) |
| GluedLevel | 165 | filtered | glued-level-congruences (outline) |
| EdgePairEvaluation | 1199 | filtered | finite-zero-term (construction, proof outline), zero-term-lattice (outline), double-lift-data (construction), double-lift-evaluation-equivariant (outline), tower-gradings-and-evaluated-data (construction) |
| IntegralAsCosetSum | 426 | filtered | cover-multiplicity (definition with proved properties), cut-with-multiplicities-dividing-powers (full), integral-as-sum-over-cut (outline) |
| LevelIdeles | 154 | filtered | tower-lattice-data (outline) |
| Frequency | 346 | filtered | shift-maps-lattices (outline) |
| NeighbourLattice | 1041 | filtered (statements and comments; proof steps of the second half skimmed) | neighbour-lattice (construction), neighbour-lattice-representatives (outline) |
| NeighbourVacuum | 379 | statements and comments | neighbour-vacuum (outline; also defines glued translates and admissible evaluations) |
| AdmissibleEvaluation | 812 | statements and comments | admissible-evaluation-of-edge-pairs (outline), lifting-conditions-for-the-two-pairs (outline) |
| UnfoldingStages | 1170 | statements and comments | double-unfolding-integral (outline), unfolding-stages (construction), unfolding-stage-as-coefficient-of-chain (outline), support-of-unfolding-stages (outline) |
| GoodDatum | 575 | statements and comments | point-data-admissible (outline), evaluated-data-admissible (outline) |
| Cut | 373 | statements and comments | stage-cuts (outline), cut-sum (full) |
| SeesawIdentity | 666 | statements and comments; proofs of `seesaw_identity`, `exists_lowerChainUpTo_poincareAt_eq`, `exists_isAdmissibleCombination_seesawDatum` read in full | top-of-the-chain (outline), iterated-unfolding (outline), seesaw-datum (construction with outlined properties), lower-chain-of-poincare-series (full), seesaw-identity (full) |

## Doubts so far

- `?lean:` targets outside the area were named from the Lean text; a few namespaces were inferred rather than checked (`New.WeilData`, `New.Space.ω`, `New.AutChar`, `New.Space.lattice`, `New.Grading.latticeMinus/latticePlus/stringPower/stringSum/stringMapFin/besselFin/HasLatticeBounds/HasBoundedOrbit/inclXFin`).
- string-sum-lattice-criteria: the valuation of the coefficient of the string powers (`Grading.powerCoeff`, in Lib) is only asserted.
- lattice-bounds-induction-step: the duality between Lambda+ and Lambda- (Lib/Weil/Periods/GradedLattice) is asserted; the definition of `HasLatticeBounds` was inferred from the file head (`Q̄^k Λ⁻ ⊆ Λ'⁻ ⊆ Q^(-k) Λ⁻`), not read in Lib.
- glued-level-congruences part 2: corner entry for odd s not re-derived.
- EdgePairEvaluation: the exact definition of `stackedStringMapFin`, `arrowTensor`, `arrowProduct`, `tripleWeil`, `liftWeilFin` live in Lib (`Lib/Weil/DualPair/TwoEdges`) and were not read; the knowls describe them as the Lean comments do. In tower-gradings-and-evaluated-data the target index set of the second tensor factor is described loosely. The hypothesis details of `doubleLiftEvalY` (which `p` with p p̄ = N is used: written as π_N) were inferred.
- NeighbourLattice: the Lean name of the unit of norm -1 (`normNegOne`, namespace guessed as `New.Weil`) and of `IsSplitLevel` were not checked; sign conventions in part 4 of neighbour-lattice-representatives (z - n(y) versus z + n(y)) follow the Lean statements but the proof sketch glosses the sign change.
- UnfoldingStages: the definition of `Grading.unfoldStep`, `sourceFn`, `IsEquivariant`, `constTermAtStringMap` (Lib/Weil/Periods/Unfolding) was not read; unfolding-stages describes the step in words. In support-of-unfolding-stages the base case and the exact use of `HasBoundedOrbit` in the induction are paraphrased from the in-proof comments; the identity conj(generator)/alpha = conj(q)/a is my own reading of how the Frequency lemma is instantiated (the Lean comment says the scaling is `star (twistIdele) / ideleA`).
- SeesawIdentity: iterated-unfolding part 4 (the induction `exists_integral_mul_lowerChainUpTo_eq_cutSum`) was read through its comments only; the description of how the real integrals are absorbed into the function a(ξ) is a paraphrase. top-of-the-chain cites Schur orthogonality/branching as the mechanism on the strength of the in-proof comments; the Lean proof was not followed line by line.
- "full" for seesaw-identity and lower-chain-of-poincare-series means: the assembly from the linked items was checked line by line against the Lean proof; the linked items themselves are mostly outlines.

## Summary

- Knowls: 48 in `proofs/grh/upper-seesaw/` plus the area page. By kind: 5 definitions, 7 constructions, 21 lemmas, 3 propositions, 12 theorems. By proof_status: 13 full, 26 outline (definitions/constructions carry none, except two that include proved properties).
- Reading depth: because of the size (9049 lines), only `AdmissibleCombinations` (first 640 lines) was read verbatim; all other files were read through a filter that keeps every doc comment, every statement, in-proof comments and (for the first half of the files) the `have/obtain/calc` skeleton, but drops tactic lines. No file was skipped. Consequently most analytic results are `outline`.
- Not given their own knowl (folded into others or omitted as routine): small matrix/valuation helper lemmas in every file; `Seesaw.selfOrConj`, `vanishingAbove`, `kroneckerOne` (described inside neighbour-lattice); `New.Data.lt_m_of_le`; measurability/integrability side lemmas of IntegralAsCosetSum and UnfoldingStages.
- Linking: standard terms were linked on first occurrence per knowl partly by a mechanical pass (terms such as hermitian space, theta lift, root of unity, isotropic); a few first occurrences may read slightly oddly and some standard terms inside mathematics-heavy sentences remain unlinked.
- Concept sidecar: `concepts/upper-seesaw.tsv` (46 rows). Existing corpus ids were taken from the index by title; only `place-of-global-field` and `group` were opened and checked, the others (`hermitian-matrix`, `subring`, `field-automorphism`, `bilinear-map`, `index-of-subgroup`, `stabilizer`, `haar-measure`, `automorphic-form`, `adeles-number-field-finite`, `non-archimedean-absolute-value`, `number-field`) were not opened.
- An early attempt to split the work among subagents failed (limit reached, nothing was spawned); all work is by one author.

## Second pass (verbatim re-reading)

Read verbatim (statements, proofs, tactic lines): NeighbourLattice lines 618–1041, NeighbourVacuum (all), AdmissibleEvaluation (all), GoodDatum (all), UnfoldingStages (all), Cut (all), SeesawIdentity (all), Sandwich (all), GluedLevel (all). Lib definitions opened and now stated from the source: `Grading.unfoldStep`, `Grading.constTerm`/`constTermAtStringMap`, `Grading.IsEquivariant`, `Grading.sourceFn`, `Seesaw.arrowProduct`, `Seesaw.arrowTensor` (injective, range = finite part), `Seesaw.tripleWeil`, `Seesaw.liftWeilFin`, `Seesaw.doubleLiftGluing` (with `poleColumn`, `poleRow`), `Data.gluedVacuum`/`translateDatum`/`gluedTensor`, `Grading.powerCoeff`/`stringPower`, `Grading.HasLatticeBounds`/`HasBoundedOrbit`, the composition and commutation laws of `finHeisenbergOp`, the duality lemmas `star_smul_latticePlus_le(_latticeMinus)`.

Knowls re-verified against the Lean proofs in this pass, with status after the pass:

| Knowl | Status | Note |
|---|---|---|
| neighbour-lattice-representatives | full (was outline) | rewritten; part 4 (uniqueness above N) added as its own part |
| neighbour-vacuum | full (was outline) | rewritten from the proof; composition laws and join formula linked |
| admissible-evaluation-of-edge-pairs | outline | rewritten; only the block identity `latticeLift_eq_latticeUnitary_add_isotropic` (a `simp` unfolding of the splitting) is asserted; depends on zero-term-lattice (outline) |
| lifting-conditions-for-the-two-pairs | full (was outline) | both computations redone by hand and checked against Lean |
| point-data-admissible | full (was outline) | scalar c: unit away from q and of absolute value 1 at all conjugates (not only for Q empty) |
| evaluated-data-admissible | full (was outline) | |
| double-unfolding-integral | outline | structure checked line by line; constant is κκ'/z₀; Lib inputs `theta_arrowProduct`, `integral_besselMeasure_eq_of_mean`, `constTerm_mul` asserted |
| unfolding-stages | (construction) | definition of the step now stated from `unfoldStep`/`constTerm` |
| unfolding-stage-as-coefficient-of-chain | outline | proof matches Lean; rests on double-unfolding-integral and on `IsEquivariant.eq_sourceFn` |
| support-of-unfolding-stages | full (was outline) | induction rewritten from the Lean proof; the Frequency lemma is applied with b = generator of the modulus and conj(b)/α = conj(q)/a (confirmed: `rw [ideleA, twistIdele, star_div, div_div_div_cancel_right]`); vanishing uses the external theorem `New.Data.doubleLiftChain_eq_zero_of_ramified` |
| stage-cuts | outline | proof matches Lean; finiteness input `Grading.exists_finite_representatives` (Lib) and lifting-the-exponent `pow_pow_mem_localCongruence` asserted |
| cut-sum | full | size argument corrected (terms bounded by 1 and number of terms by C; previously claimed μ = 1) |
| top-of-the-chain | outline | rewritten: constant is C·dim·c with c the product of powers of conjugates of conj(π_N); the two Lib lemmas `integral_algFormCoeff_blockEmb`, `integral_mul_eq_classIntegral` are asserted. The earlier "Schur orthogonality" paraphrase is removed |
| iterated-unfolding | full (was outline) | part 4 rewritten from the Lean induction; external inputs linked (`integral_mul_poincareAt`, arrow lemmas) |
| seesaw-datum | full (was outline) | invariance proof rewritten |
| lower-chain-of-poincare-series, seesaw-identity | full | unchanged, re-read |
| lattice-splitting-and-scalings | full (was outline) | conj by the Lib duality lemma |
| lattice-bounds-induction-step | full (was outline) | duality and Iwasawa lemma linked |
| glued-level-congruences | full (was outline) | corner entry settled: at each place at most one of the two divisions matters (matches `isIntMatrix_scaleAt_mul_sub_one_mul_scaleAt`) |
| string-sum-lattice-criteria | full (was outline) | `powerCoeff` read: c^(i−⌊s/2⌋) for 2i<s, −N·c^(i−⌊(s−1)/2⌋) otherwise (the first pass had guessed N^(-1)); exponent bookkeeping done by hand |

Counts after the second pass: 48 knowls; proof_status full 25, outline 14.

External `?lean:` names: all checked by grepping the declarations and their namespaces. Corrected: `New.Space.IsThetaLift` (was `New.IsThetaLift`), `New.IsArrow.integral_mul_formLift_swap`. Confirmed as written: `New.WeilData`, `New.Space.ω`, `New.Space.lattice`, `New.Weil.normNegOne`, `New.IsSplitLevel`, `New.Data.TameChar.normQ`, `New.Data.ChainTensor.IsInvariant`, `New.Seesaw.doubleLiftGluing`, `New.doubleLiftChain`, `New.rankTwist`, the `New.Grading.*` and `New.Data.*` names. `New.Grading.inclXFin`/`besselFin` were confirmed by file and surrounding namespace, not by an explicit `namespace New` line.

## What remains (not re-read verbatim in the second pass)

In import order: AdmissibleCombinations lines 640–907 (moved vacua, Schrödinger operators: read in the first pass with the `have` skeleton), StandardLines (all; its knowls were derived by hand and one was upgraded after reading `powerCoeff`), EdgePairEvaluation (all: finite-zero-term, zero-term-lattice, double-lift-data, double-lift-evaluation-equivariant remain as written in the first pass, except that the definitions of the middle and last double lift were read verbatim), IntegralAsCosetSum (all), LevelIdeles (all), Frequency (all), NeighbourLattice lines 1–617 (first pass, with `have` skeleton). No new knowls were split off in the second pass; candidates that remain folded: `Seesaw.conjTranspose_mulVec_mem_weightedTranslations`, `Seesaw.exists_finHeisenbergOp_vacElem_eq_of_coprime` (stated as a remark in neighbour-vacuum), `Data.finHeisenbergOp_generator_smul_pointDatumY` (inside the support theorem), `Data.card_le_residueMatrixCount` (inside stage-cuts).

## Third pass (completion of the verbatim reading)

Read verbatim in this pass: AdmissibleCombinations lines 640–907, StandardLines (all), EdgePairEvaluation (all), IntegralAsCosetSum (all proofs; the doc comments had been read before), LevelIdeles (all), Frequency (all), NeighbourLattice lines 1–617 (definitions, structures and all lemmas up to `star_neighbourAxis_dotProduct`; lines 470–617 are definitions and one-line lemmas that were printed in full in the first pass). With this, every file of the folder has been read in full, proofs included.

| Knowl | Status after this pass | Note |
|---|---|---|
| moved-vacuum-admissible | full (was outline) | rewritten from the Lean proof; Lib statements `Space.omega_finHeisenbergOp`, `Space.omega_vacElem_sum`, `norm_finMultiplier_sq` linked |
| schrodinger-operator-admissible | full (was outline) | the point-mass formula `Modulus.schrodingerOp_single_eq_mean_translate_projOn` linked |
| l-adic-units-multiplier-and-characters | full (was outline) | Lib statements `AlgHeckeChar.norm_padic_eq_one`, `IsSaturating.v_det_saturatingElem`, `AutChar.HasWeight.norm_padic_eq_prod` linked |
| finite-zero-term | outline | rewritten from the Lean proofs; general support property (matrices M, M') added as property 5 because Frequency uses it; the mixed-model statements (`IsAdapted.slice_omega_vacElem`, `IsAdapted.exists_map_vacVector_apply_zero_omega_eq`, the law of the mixed model for translations) are asserted by name |
| zero-term-lattice | full (was outline) | Lib statements linked (`exists_eq_radicalElement_mul_levi_mul_isAdapted`, `exists_eq_smul_omega_vacElem`, `omega_vacElem_sum`); depends on finite-zero-term (outline) |
| double-lift-data | (construction) | re-checked against the structures and the two instances |
| double-lift-evaluation-equivariant | outline | re-read; asserted: `zeroTerm_omega_of_inclMatrix`, `homTarget_zeroTerm_pairWeil`, and the final comparison of the exponents of υ (Lean: `match_scalars <;> omega`), which I did not recompute |
| tower-gradings-and-evaluated-data | (construction) | confirmed: the last double lift uses p = π_N (`D.piN_mul_star`) |
| integral-as-sum-over-cut | full (was outline) | cutoff and integration in stages linked (`hasCutoff_of_proper`, `integral_quotMeasure_stages`) |
| cover-multiplicity, cut-with-multiplicities-dividing-powers | full | confirmed |
| tower-lattice-data | full (was outline) | Lib statements linked |
| shift-maps-lattices | full (was outline) | rewritten middle part (the matrix W and the projection onto negative degree); `Grading.exists_splitting_constTerm` linked; depends on finite-zero-term (outline) |
| standard-lattice-membership, string-lattices-line-by-line, string-sum-lattice-criteria, shift-of-string-lattice, generator-of-plus-over-minus | full | confirmed against the Lean proofs |
| neighbour-lattice | (construction) | the two identities for the neighbour coefficients are now derived in the text (they had been marked "not re-derived") |
| integral-away, admissible-combination(-substitution, -calculus), translation-groups, split-squarefree-factorisation, graded-lattice-basis(-unimodular), graded-gram-signature | full / definitions | these were read verbatim in the first pass (lines 1–640) and the remaining rules (`smul_mem`, `normUnit_smul`, `pure`) are now confirmed verbatim |

New knowls split off: `adjoint-on-weighted-translations` (full), `vacuum-translate-away-from-level` (full), `point-datum-periods` (full, includes the twist idele). `Data.card_le_residueMatrixCount` stays inside stage-cuts (a three-line counting argument).

Counts now: 51 knowls (5 definitions, 7 constructions, 24 lemmas, 3 propositions, 12 theorems); proof_status full 35, outline 7.

Policy used for "full": every step is a computation given in the text, a linked item of this area, or a linked Lean statement of another area or of Lib whose content is stated in the sentence that cites it. A full knowl can therefore rest on an outlined one (for example zero-term-lattice and shift-maps-lattices on finite-zero-term).

Namespaces: the two inferred ones were confirmed (`New.Grading.exists_isGraded`, `New.Data.isArrow_swap_thetaKernelY_datumY`); `New.Grading.inclXFin`/`besselFin` confirmed by the `namespace New`/`namespace Grading` lines of `Lib/Weil/Periods/Grading.lean`. Links added in this pass were checked the same way; one was corrected (`New.Rows.span_piM`).

Remaining doubts: (a) the exponent comparison in double-lift-evaluation-equivariant; (b) the block identity in admissible-evaluation-of-edge-pairs; (c) the mixed-model inputs of finite-zero-term are cited by Lean name without restating them exactly; (d) concept linking of standard terms was partly mechanical (first pass) and was not redone.

## Audit response

Source: `knowlpedia-content/reviews/riemann2-audit/areas/upper-seesaw.md` and the 49 rows of `findings.tsv` for this area (the two `updates/*` folders contain no rows, ledger entries or sidecar corrections for upper-seesaw). The audited snapshot already contained the third pass (51 knowls), so no finding was "already resolved". Every finding was checked against the Lean lines cited; all 48 findings on this area's pages are accepted, one concerns another area. No `proof_status` changed (35 full, 7 outline).

High
- area page — The string description stops one stage before the top — accepted — notation paragraph now restricts "X_j plus a string" to j<m, mentions the middle vector of norm −N only for odd strings, and describes Y_m as the standard space of rank n_m−1 of codimension one in X_m; the same is stated in tower-gradings-and-evaluated-data.
- iterated-unfolding — The top stage has zero string vectors — accepted — string length in part 4 is max(0, m−2−k), with the case k=m−1 identified with the last grading.
- neighbour-lattice-representatives — The quotient modulo β can be infinite — accepted — part 2 and its proof use D_β (the number of matrices modulo β if finite, 0 otherwise, as Lean's `Nat.card`); the infinite case is treated separately; summary changed. neighbour-vacuum uses the same D_β.
- support-of-unfolding-stages — The lattice bounds use the chosen modulus — accepted — Q is now the chosen modulus of the tame character (`TameChar.Q`), not the set of ramified places; same wording corrected in stage-cuts, point-datum-periods, point-data-admissible, tower-lattice-data, seesaw-identity, evaluated-data-admissible and the area page.
- unfolding-stages — Restrict unipotent covariance to degree at least two — accepted — property 2 states the transformation law on U^{≥2} only (`IsEquivariant.unipotent_mul`), with the remark that it is the whole unipotent radical for odd strings.

Medium
- area page — The summary extends the coefficient bounds to all twists — accepted — summary qualified (integral away from the modulus; bounded when the modulus is empty).
- area page — A tame character carries a chosen supporting modulus — accepted — notation paragraph rewritten.
- admissible-combination — The example conflates modulus, denominator and empty-modulus condition — accepted — remark rewritten with n=q, p=(Q=∅), d=𝒞^{2m} before and d=1 after the rescaling.
- admissible-evaluation-of-edge-pairs — Split level omits residue degree one — accepted — hypothesis spelled out (N splits completely, residue fields Z/N, N a uniformiser).
- double-lift-data — Give the scaled finite translation vector — accepted — the translation is ρ_f(α^{-1}(S^♭)_f) with S^♭ the coordinates in the frame of the Hom space; the self-link is removed (also the structural check).
- double-unfolding-integral — Rank twists and adelic coefficients — accepted — complement now names the rank twists a_o υ^{⌊r/2⌋}, b_o υ^{⌊r/2⌋} and defines t(φ(x)) as t(ρ(x_∞)^{-1}φ(x_f)).
- evaluated-data-admissible — Excluding the π_N places does not prove coprimality — accepted — gcd(N,q)=1 now taken from the defining condition gcd(MN,q)=1 of a tame character (`TameChar.coprime`).
- evaluated-data-admissible — Third matrix shape — accepted — the three exponent bounds are n_m², n_m², 2n_m².
- graded-lattice-basis — Mixed entries unspecified — accepted — all unlisted pairings are 0.
- graded-lattice-basis — Odd length alone does not prevent self-duality — accepted — remark now says the failure is at the places where N is not a unit.
- integral-as-sum-over-cut — Scalar for an arbitrary archimedean function — accepted — κ defined with the totalised (Bochner) integral convention.
- iterated-unfolding — Supply a graded point in the Bessel orbit — accepted — part 3 of lattice-bounds-induction-step is invoked for the existence of a graded translate.
- lifting-conditions-for-the-two-pairs — Lengths 1,0,0 do not define the last double lift — accepted — c_Y=c_{Y'} (consecutive strings) is a stated hypothesis of both cases.
- lower-chain-of-poincare-series — Use Petersson nondegeneracy — accepted — the last step takes x to be the difference of the two forms.
- neighbour-lattice — Qualify the identification with the zero-term lattice — accepted — remark now states the hypotheses and links part 1 of admissible-evaluation-of-edge-pairs.
- neighbour-vacuum — Explicit sum versus sum over all classes — accepted — summary and a sentence before the theorem distinguish the two.
- neighbour-vacuum — The denominator can be zero — accepted — D_β with the finite-or-zero convention.
- point-data-admissible — Chosen modulus — accepted — wording and summary.
- point-datum-periods — Prescribed modulus set — accepted — wording.
- schrodinger-operator-admissible — The projection averages over the conjugate places — accepted — P^𝔪 and the lifted function are now defined precisely.
- seesaw-identity — Terminal identity in joint invariance — accepted — the bullet states b_j in the level for j<m and b_m=1; seesaw-datum property 1 likewise; the support condition is made explicit.
- stage-cuts — Chosen modulus — accepted — wording.
- stage-cuts — The initial cut needs invariance of the chosen level — accepted — the case j=0 is now argued separately (image of the level of X_0 lies in the chosen level; multiplicity 1).
- top-of-the-chain — Adelic coefficient of the upper form — accepted — t(ψ(h)) defined as t(ρ(h_∞)^{-1}ψ(h_f)).
- tower-gradings-and-evaluated-data — Target of the evaluated datum — accepted — second factor is Hom(X_{2i+1},X_{2i+2}); last grading described (definite part of n_m−1 vectors, constant 1).
- unfolding-stage-as-coefficient-of-chain — Odd string length in the uniqueness step — accepted — the step cites `IsEquivariant.eq_sourceFn` with the odd length m−1−(2i+2).
- unfolding-stages — Rational points over the fixed field — accepted — R(E) replaced by R(F)=Γ∩R, F=E⁺, in unfolding-stages, iterated-unfolding, integral-as-sum-over-cut, top-of-the-chain.

Low
- area page — Seven outline labels include a construction — accepted — wording "of the 42 items with a proof-status label".
- admissible-evaluation-of-edge-pairs — K undefined — accepted — K defined before C=cK.
- admissible-evaluation-of-edge-pairs — Stale dependency status — accepted — remark updated (zero-term-lattice is full, finite-zero-term is the outline).
- double-unfolding-integral — Extend the pure tensor calculation by linearity — accepted.
- evaluated-data-admissible — Summary identifies modulus norm with conductor norm — accepted — summary reworded.
- moved-vacuum-admissible — Two undefined symbols — accepted — ψ and c_0 identified.
- neighbour-lattice — Representatives in y/N — accepted — integer representative in {0,…,N−1}.
- neighbour-vacuum — Scalar pairings for matrices — accepted — convention stated before the formulas.
- schrodinger-operator-admissible — Support idempotent dropped — accepted — 1_S inserted, y_b written as conj(1_S ϖ^{-1} z_b).
- seesaw-datum — Empty-modulus condition on both size bounds — accepted.
- shift-maps-lattices — Finite frame versus finite group point — accepted — frames are B, B′, points p=x_f, p′=x′_f.
- standard-lattice-membership — Separate subscript for the distinguished coordinate — accepted — y_e, c_e.
- string-lattices-line-by-line — Coordinate changed in the lift — accepted — z_e, y_e.
- tower-lattice-data — Level places include all of the assigned modulus — accepted — wording.
- unfolding-stage-as-coefficient-of-chain — Absorb the scalar z — accepted — the complement is applied to z·v.
- unfolding-stages — Separate the terminal function from the recurrence — accepted — index ranges stated.
- upper-divisibility/chain-datum-as-a-weak-chain-datum — two quoted names — not this area's page; for the owner: the names are `New.Seesaw.IsAdmissibleCombination` (and its `bind`), with the page `proofs/grh/upper-seesaw/admissible-combination-substitution`, and `New.Space.omega_projOn`.

Other audit files
- structural-checks: self-link in double-lift-data removed; `lean_files` of vacuum-translate-away-from-level now also lists `EdgePairEvaluation.lean`.
- lean-references: `New.Grading.besselFin` and `New.Grading.inclXFin` are confirmed as written; the other entries naming Seesaw declarations concern pages of upper-divisibility (`New.Seesaw.isAdmissibleCombination_schrodingerOp_of_reduction`, `New.Seesaw.poleColumn`, `New.Seesaw.poleRow`).
- Sidecar: the row "Conductor of a Hecke character" was removed (no longer used); third column is `NEW` or a corpus id in all 44 rows.
- Agreement with the corrected upper-objects knowls was checked for the objects quoted here (spaces Y_j with string indices 0..2ϱ−j, idele a=α/conj(chosen idele), lattice scale exponent ⌈(m−j)/2⌉, chain datum, joint invariance with b_m=1, composite lift): consistent. Grid centres, signs of W_j and descent pairs are not quoted in this area.
