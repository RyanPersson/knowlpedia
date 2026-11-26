# Coverage report: upper-objects

Files in import order. Status is updated as each file is finished.

| File | Lines | Read | Knowls |
|---|---|---|---|
| Objects/LiftLawsModuloN.lean | 936 | full | split-level, data-modulo-n, mirabolic-subgroup-at-split-level, up-operator, ramified-vector-at-split-level, lift-law, lift-law-vanishing-on-ramified-vectors, mirror-lift-through-direct-lift, glued-double-lift, chain-of-glued-lifts-becomes-direct |
| Objects/LabelsAndIndexTypes.lean | 427 | full | primitive-polynomial, primitive-polynomial-scaling-and-norm, good-tuple-of-labels, index-sets-of-the-hermitian-spaces, signs-and-parameter-of-w, good-idempotent, good-idempotent-kills-hyperplane-sums (outline: cites New.hyperplaneSum_mul_labelIdem) |
| Objects/Weights.lean | 659 | full | weights-of-the-definite-spaces, columns-of-the-weights, branching-exponent-formula |
| Objects/InsertBlock.lean | 336 | full | centre-system, centre-system-parameter-has-gap, inserting-a-block-satisfies-the-block-rule (outline: cites New.isBlockRule_iff_of_character(_conj)) |
| Objects/AuxiliaryPair.lean | 1141 | full (proofs of the last third read quickly) | descent-pair, block-datum, block-datum-laws (outline), normalized-descent, lift-hecke-polynomial, descent-pair-fitting-parameters, highest-vector-polynomial-is-an-edge (outline), normalized-descent-is-a-transposed-lift (outline). Many notions (LevelPlaces, Space, AutChar, WeylIndex, letterPoly, mixedCartan, stdClassSum, IsJointHarmonic, IsEdge) come from Lib and are linked by ?lean placeholders; normalisation of the class sum and quotient measure not unfolded. |
| Objects/LiftChains.lean | 628 | full | chain-of-lifts, chain-equivariance, jointly-invariant-combination, jointly-invariant-chain-is-a-plain-sum (outline: class integral = class sum cited), chosen-places-and-chosen-group-order (outline), free-levels-at-the-chosen-places (outline: cites New.Variety.classAut_eq_bot) |
| Objects/Parameters.lean | 991 | first 330 lines full; rest statements + comments, proofs skimmed | grid-nodes, properties-of-grid-nodes (outline), grid-centres (outline), grid-steps-correspond (outline). Doubt: the precise mechanism in paramsCorrespond_neg_gridParam_insert_first (opposite space, weights N - gw) was not checked line by line. |
| Objects/Columns.lean | 1012 | head + all statements and definitions; proofs skimmed only | level-places-of-the-data, source-form, branching-map-and-restriction-to-y (outline), lift-kernels-of-the-chain, chain-datum-and-composite-lift, glued-datum-in-the-schrodinger-model (outline). Doubt: exact normalisations inside thetaKernel/jetScale and of schrodingerOpAt are in other areas; pointwise form of the gluing paraphrased. |
| Objects/Rows.lean | 874 | head + all statements and definitions; proofs not read | spaces-y-and-w (outline), target-form, principal-forms-are-finite-dimensional (outline), descent-pairs-of-the-data (outline), point-datum-on-y (outline). Doubt: the shift by u in paramsCorrespond_descentPair and the column formulas of the descent pair were not verified line by line. |
| Objects/RowChain.lean | 457 | head + statements; proofs not read | lower-chain, lower-chain-level-and-equivariance (outline) |
| Objects/PoincareMap.lean | 259 | head + statements; proofs skimmed | poincare-map (outline) |
| Objects/CharactersAtLevel.lean | 200 | head + statements; proofs skimmed | chains-kill-ramified-source-forms (outline). Doubt: in part 4 the explicit psi is my own standard formula, the Lean proof uses a library lemma not opened. |
| Kernels/JetConjugatesAndBounds.lean | 896 | head + all statements and doc comments; proofs not read | jet-conjugation (statement), archimedean-bounds-for-jets (outline from the comments) |
| Kernels/ThetaLiftGauge.lean | 562 | head + all statements and doc comments; proofs not read | gauge-bounds-for-one-lift (statement), vacuum-data-of-functions-modulo-an-ideal (statement) |
| Kernels/DefiniteKernelSize.lean | 374 | head + statements; proofs not read | definite-kernel-scale (statement) |

## Summary

61 knowls in `content/proofs/grh/upper-objects/` plus the area page `content/proofs/grh/upper-objects.knowl.md`.

By kind: 29 definition, 3 construction, 10 lemma, 3 proposition, 16 theorem.
By proof_status (37 knowls carry one; four of them are definition/construction pages that contain proved properties): 12 full, 21 outline, 4 statement.

Fully translated and checked against the Lean proofs: LiftLawsModuloN, LabelsAndIndexTypes (except the cited Green-character lemma), Weights, InsertBlock (except the cited reformulation of the block rule), the equivariance lemmas of LiftChains.

## Not fully covered

* Parameters.lean (from line 330), Columns.lean, Rows.lean, RowChain.lean, PoincareMap.lean, CharactersAtLevel.lean: every definition and every statement is translated, but the proofs were only skimmed or not read; the proof sections are outlines assembled from the statements and comments.
* The three Kernels files: only heads, statements and doc comments were read (budget). Their knowls have status "statement" or an outline taken from the comments. These files deserve a second pass by an author with budget: the Cauchy estimate (`norm_jet_translate_le`), the existence of the jet conjugation, the gauge criterion (`omega_mem_raises_of_schurJet_le`) and `IsModKernelScale`.
* Routine lemmas without their own knowl are listed in the `lean` front matter of the knowl into which they are folded. Not listed anywhere (pure plumbing): `scalarFin_atPlace`, `atPlace_embedGL_diagN`, `isSchwartzBruhat_liftFn(_mul)`, the `HasLogBound` instances, `n_zero/n_succ/k_le_n/n_pos/n_even`, `liftWeight_add/succ`, the small arithmetic lemmas of Parameters.lean (`sum_ite_lt_*`, `max_min_succ_sub_max_min_mem_Icc`, `liftWeight_add_gap_le`, ...), `restrictToYOfEq_apply`, `piN_ne_zero`, `card_Y_le`.

## Doubts and surprises

1. `HCParam.HasGap h`: I state the gap condition as "entries of lambda at coordinates of opposite signs are at least h apart" (from the file heads); in `hasGap_gridParam` the Lean comment says doubled entries differ by at least 2*gap. I did not open the definition of `HasGap` (another area) to confirm the normalisation.
2. In `mirror/glued` lemmas the representations are of abstract groups GL(E_P) with no continuity; I say so explicitly.
3. `diagN n S` in LiftLawsModuloN allows a subset S of P; I present only S = P there and the general case in the Schrödinger-model knowl.
4. `columnCount`, `keptColumns`, `columnsY` use truncated subtraction; I state them with max(.,0) and note that no truncation occurs for admissible data.
5. `chains-kill-ramified-source-forms` part 4: the explicit psi with phi = psi - z psi is my own (standard) formula; the Lean proof goes through a library lemma I did not open.
6. `grid-steps-correspond` part 3 (first block of an interval) and `descent-pairs-of-the-data` part 2 (shift by u): mechanism described from comments, not verified line by line.
7. `normalized-descent`: the normalisation of `stdClassSum` and of the quotient measure is left to the Lean definitions (other areas); the theorem's constant d*[K_0:K_O] is copied from the Lean statement.
8. `good-idempotent`: I describe C[G-bar] as the tensor product of the group algebras; the Lean `piTensorElem` is the corresponding multiplicative map.
9. The split-level knowl links `New.WeilData` and `New.stdLattice.selfDualAddChar` by placeholder; I did not verify the fully qualified namespace of `selfDualAddChar` (declared inside `Lib/Weil/Construction/FiniteMultiplier.lean`; the Objects file opens it as `stdLattice.selfDualAddChar`).
10. Several `?lean:` targets are guessed fully-qualified names of declarations in other areas (e.g. `New.Space.Form`, `New.Grading.besselGroup`, `New.Variety.classAut_eq_bot`, `New.Seesaw.integralAway`, `New.Parameters.jetScale`); the resolver may need to fix namespaces.

# Second pass (verbatim re-read)

| File | Second-pass reading | Result |
|---|---|---|
| Kernels/JetConjugatesAndBounds.lean | verbatim, full | jet-conjugation split into definition + existence-of-jet-conjugation (outline: cites exists_isJetConjugate_translates, ScalesTranslations.exists_map_schrodingerOp, eq_zero_of_jetSeries_eq_zero); new knowl bounds-for-the-vacuum-and-its-conjugates (outline); archimedean-bounds-for-jets proof rewritten from the Lean (outline, cited items listed). Statement corrections: sigma is any automorphism of C; log 0 convention noted. |
| Kernels/ThetaLiftGauge.lean | verbatim, full | new definition knowl gauge-raising-data; gauge-bounds-for-one-lift rewritten with proof (outline; seven cited statements listed with content); vacuum-data lemma proof rewritten (outline; cites Fourier inversion lemma). |
| Kernels/DefiniteKernelSize.lean | verbatim, full | definite-kernel-scale: explicit constant added; proof rewritten. FIRST-PASS ERROR corrected: integrality does not come from the clearing statement of the gauge bounds but from norm_jet_jetSeries_le_one applied at scale conj(delta) d c_0. |
| Objects/Parameters.lean (from line 330) | verbatim, full | properties-of-grid-nodes: proofs of 4, 5, 6 rewritten from the Lean (outline: arithmetic by omega not expanded); grid-centres now full; grid-steps-correspond now full (doubt 6a settled: opposite space on the smaller node, then IsBlockRule.neg, content stated). Doubt 1 settled: HasGap h means 2h <= |l_i - l_j| for doubled entries, i.e. |lambda_i - lambda_j| >= h, as written. |
| Objects/Columns.lean | verbatim, full | glued-datum-in-the-schrodinger-model: proof rewritten from the Lean (outline; cites schrodingerAct/schrodingerOp facts and pairWeil_schrodingerOp_of_mem_supportedOn); definitions in level-places-of-the-data, source-form, branching-map-and-restriction-to-y, lift-kernels-of-the-chain, chain-datum-and-composite-lift re-checked against the source, no statement errors found. |
| Objects/Rows.lean | verbatim, full | spaces-y-and-w: existence proof now given (outline; three cited library statements with content); descent-pairs-of-the-data now full (doubt on the shift by u settled: IsBlockRule.shift; column counts verified as the steps of an explicit list); principal-forms-are-finite-dimensional (outline; the two cited theorems stated); point-datum-on-y now full. |
| Objects/RowChain.lean | verbatim, full | lower-chain (definition re-checked), lower-chain-level-and-equivariance now full (cites IsArrow.formRep_formLift and toAlgForm_formRep with content). |
| Objects/PoincareMap.lean | verbatim, full | poincare-map re-checked; statements and proofs agree with the Lean. |
| Objects/CharactersAtLevel.lean | verbatim, full | chains-kill-ramified-source-forms now full; doubt 5 settled: the Lean uses New.Data.exists_eq_sub_scalingGenerator (existence of psi); my explicit psi is kept with its verification. Added doubleLiftChain_eq_zero_of_ramified to the lean list. |
| Objects/AuxiliaryPair.lean | read verbatim in the first pass (whole file); in the second pass the cited library statements behind the outline knowls were opened | normalized-descent: the class sum is now defined exactly (sum over double cosets of f(g_c)/#(Gamma ∩ g_c K g_c^-1)); normalized-descent-is-a-transposed-lift: content of integral_mul_eq_classIntegral and classIntegral_eq_classSum stated (constant d*[K_0:K_O] confirmed); block-datum-laws and highest-vector-polynomial-is-an-edge stay outline (they cite pairWeil_modDatum_stdLevel, isJointHighest_prod_det_pow_staircaseWeight, IsJointHarmonic.exists_eq_smul_of_row_weight, isEdge_of_isJointHarmonic, MixedCartanEmbedding.top/intertwines; these were not opened). |
| Objects/LiftChains.lean | read verbatim in the first pass; cited statements opened | jointly-invariant-chain-is-a-plain-sum now full (class integral defined; Kernel.lift is a class integral with vol K = 1); free-levels-at-the-chosen-places now full (statement of Variety.classAut_eq_bot checked: needs at least two infinite places, norms product > (2n)^[E:Q]). |

## State after the second pass

64 knowls + area page. By kind: 31 definition, 3 construction, 11 lemma, 3 proposition, 16 theorem.
proof_status (only on lemma/proposition/theorem, 30 knowls): 16 full, 14 outline, 0 statement.
`proof_status` was removed from the 8 definition/construction knowls that carried one (their proved properties remain in a Proof section of the same page).

New knowls in the second pass: jet-conjugation (now a pure definition), existence-of-jet-conjugation, bounds-for-the-vacuum-and-its-conjugates, gauge-raising-data.

Full (16): mirabolic... (definition, no status), lift-law-vanishing-on-ramified-vectors, mirror-lift-through-direct-lift, glued-double-lift, chain-of-glued-lifts-becomes-direct, primitive-polynomial-scaling-and-norm, columns-of-the-weights, branching-exponent-formula, centre-system-parameter-has-gap, chain-equivariance, jointly-invariant-chain-is-a-plain-sum, free-levels-at-the-chosen-places, grid-centres, grid-steps-correspond, descent-pairs-of-the-data, lower-chain-level-and-equivariance, chains-kill-ramified-source-forms (the list of files gives the exact set; `grep proof_status` is authoritative).

Outline (14), with what is asserted without proof named in each page: good-idempotent-kills-hyperplane-sums, inserting-a-block-satisfies-the-block-rule, block-datum-laws, highest-vector-polynomial-is-an-edge, normalized-descent-is-a-transposed-lift, properties-of-grid-nodes (linear arithmetic not expanded), glued-datum-in-the-schrodinger-model, principal-forms-are-finite-dimensional, existence-of-jet-conjugation, bounds-for-the-vacuum-and-its-conjugates, archimedean-bounds-for-jets, gauge-bounds-for-one-lift, vacuum-data-of-functions-modulo-an-ideal, definite-kernel-scale.

## First-pass errors corrected in the second pass

1. definite-kernel-scale: the integrality proof was attributed to the wrong statement (the "clearing" bound for gauges); it is `norm_jet_jetSeries_le_one` at scale conj(delta)*d*c_0 with delta = M^2. The explicit constant c = (M^2)^(2f|N||L|) * vacuumScale^(|N||L|) * (M^2 d c_0)^deg was missing.
2. archimedean-bounds-for-jets: sigma is an arbitrary automorphism of C (reduced to one over K with the same absolute values); the first pass did not say so. Proof steps were guessed from comments and are now taken from the Lean.
3. gauge-bounds-for-one-lift: the letter d was used both for the point and for the prime of the parameters; the cited inputs were not identified. Fixed.
4. normalized-descent: the class sum was left unspecified; now exact.
5. chains-kill-ramified-source-forms: the source of phi = psi - z psi is now the Lean lemma; the explicit formula is verified in the text.
6. descent-pairs-of-the-data: truncated subtractions in the column counts now marked.
No false mathematical statement was found in the first-pass statements of Parameters, Columns, Rows, RowChain, PoincareMap; the changes there are to proofs.

## Remaining doubts

* `?lean:` names: every external name was checked to exist by its last component (grep of declarations); the namespace prefix was confirmed from usage for most, but not mechanically for all (e.g. `New.Grading.*`, `New.Space.Form`, `New.Parameters.intVacuum`, `New.LevelPlaces.LevelForm`).
* Outline knowls of AuxiliaryPair: the five library statements listed above were not opened; their content is paraphrased from the calling code.
* properties-of-grid-nodes: the integer arithmetic closed by `omega`/`grind` in the Lean is stated with its inputs but not expanded.
* The exact shape of the congruence condition in `levelX` ("last row congruent to (0,...,0,1) modulo pi_N") is taken from the doc comment of `congruenceGL ... Sum.inr`, whose definition was not opened.
