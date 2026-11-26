# Coverage report: reduction-main

51 proof knowls in `knowlpedia-content/content/proofs/grh/reduction-main/` plus the area page `proofs/grh/reduction-main.knowl.md`; sidecar `concepts/reduction-main.tsv` (56 concepts).
Kinds: 20 definition, 2 construction, 2 notation, 14 lemma, 13 theorem. proof_status: 23 full, 5 outline (target-lattice, auxiliary-forms, data-exist, sparse-places-exist, data-sizes). `prerequisites = []` everywhere (placeholders present).

| Lean file | lines | read | knowls | notes |
|---|---|---|---|---|
| New/Reduction/Lattices/Colength.lean | 264 | full | colength-divides, colength-calculus, onto-up-to-colength, onto-up-to-colength-product, colength-of-matrix-image, colength-bounds-length | full proofs |
| New/Reduction/Lattices/Heights.lean | 234 | full | prime-padic-iso, height-bound, log-product-formula, height-calculus, height-product-formula | full; extension of embeddings to isomorphisms C ≅ F and algebraicity of H cited from Lib |
| New/Reduction/Lattices/TwistedLattice.lean | 516 | full | twisted-lattice (incl. integral vectors, "carries with loss"), index-bound, index-calculus, covolume-bound, covolume-calculus, twisted-lattice-volume, gram-determinant-valuation, covolume-add-index-nonneg | full; Hadamard/Fischer/Cauchy–Schwarz for Gram determinants cited |
| New/Reduction/Data/FieldsAndPlaces.lean | 526 | full | parameters, field-e-and-its-places, field-e-properties | full |
| New/Reduction/Data/AdmissibleData.lean | 362 | full | data (incl. constantBound, logLevelMin), sparse-set-of-places, data-derived-quantities, prime-sum | logLevelMin_mem_Icc and rootDiscr lemmas are folded into data-exist |
| New/Reduction/Data/Magnitudes.lean | 612 | head, all statements, about half the proofs | log-bound-calculus, parts of data-derived-quantities and data-sizes | the instance-by-instance exponent bookkeeping is described, not reproduced |
| New/Reduction/Data/LevelAndTwists.lean | 395 | full | twist, m-fold-twist, lift-characters, target-parameter, rows of data-sizes | weight/level estimates only tabulated (outline) |
| New/Reduction/Data/Sizes.lean | 239 | full | data-sizes | outline: comparisons by `le_of_hasLogBound` asserted |
| New/Reduction/Data/Existence.lean | 925 | head, all main statements, proofs of Behrend/sparse/primes/level/final assembly; NOT read: lines ~368–484 (helper lemmas on least powers, floors), ~680–800 (`IsLargeScale` consequences, `exists_hasFields`) | sparse-places-exist, data-exist | outline |
| New/Reduction/PrimeSums.lean | 301 | full | main-amount-and-total-remainder, total-remainder-formula, prime-sum-bounds | full |
| New/Reduction/IntegralTargetForms.lean | 120 | full | target-lattice | outline: rests on results of other areas (trivial stabilisers, integrality of inner products, injectivity of the chain) |
| New/Reduction/ShortAndEnough.lean | 457 | full | gain-normalisation, normalized-poincare, theorem-a-short-forms, theorem-a-index, theorem-b-enough-forms | full relative to quoted external theorems |
| New/Reduction/MainInequality.lean | 158 | full | star-inequality | full |
| New/Reduction/OneSidedBound.lean | 269 | full | prime-remainder-bound-from-data, one-sided-bound, grh | full |
| New/Determinant/Twist/FitTwists.lean | 235 | full | regular-family-of-twists (bundles ratio, ramified/main pairs, budget, denominators, small ratios, regular) | definitions only |
| New/Determinant/Twist/LongForms.lean | 250 | full | auxiliary-forms (outline), inverse-ratio-height, theorem-c-integral-forms-long | |

## Integers vs. reals in OneSidedBound (settled)
The criterion `New.LFunction_ne_zero_of_primeRemainder_le` needs `∀ᶠ x : ℝ in atTop, primeRemainder d q₀ x ≤ x^(β-1)`. The data exist only at integer `x`, giving `New.eventually_primeRemainder_natCast_le` (`∀ᶠ x : ℕ`, constant 64φ(q₀)+3, exponent −1/2+6ε). The bridge is inside `New.eventually_primeRemainder_le_rpow`: `primeRemainder_sub_primeRemainder_floor_le` (R(y) − R(⌊y⌋) ≤ 26/y for y ≥ 2, from the slow-variation lemma `abs_primeRemainder_sub_le` of area reduction-zeros), `natFloor_rpow_le_two_mul_rpow` (⌊y⌋^t ≤ 2y^t for −1 ≤ t ≤ 0), composition with `tendsto_nat_floor_atTop`, and absorbing the constant 2C+26 into y^δ (ε replaced by 7δ). So `eventually_primeRemainder_le_rpow` is a statement over real y, exactly as the criterion requires. Written out in knowl `one-sided-bound`, Step 2.

## Doubts and surprises
- `Data` is a structure with ranges, not explicit values; scale conditions are stated on stored logarithms. `P.q₂`, `P.bigOmega` depend on s.
- Weight off the b-places is natural-number division `x*b/x₁` (exact because q₁x₁ | b).
- `CriticalPair.ratio` is a quotient of absolute values coerced to ℂ; if the denominator vanished Lean's value is 0 (noted in the knowl).
- `HeightLe` is a relation with a common multiplier; I describe its relation to the Weil height only as a remark (not proved in Lean).
- In `grh` the excluded case χ = 1, ρ = 1 concerns Lean's junk value at the pole.
- `divisibilityError` and `seesawConst` are `Classical.choose` choices; stated as "fixed once and for all".
- data-sizes: bounds x¹⁰ ≤ rd_E ≤ x¹² are instances from another file (not located); several numerical comparisons were only spot-checked (those used in Theorems A–C and star_inequality were checked by hand).
- Bundling: `regular-family-of-twists` and `data-derived-quantities` hold several small definitions each; could be split if the one-concept rule is enforced strictly. `IsNegligible`, `RankOneIndex` only mentioned.
- Existing-corpus IDs used were checked by opening the files (module, dvr, length-module, smith-normal-form-theorem [PID case only], number-field, field-automorphism, algebraic-closure, norm-field, cyclotomic-extension [title only], cyclotomic-polynomial, primitive-root-of-unity, imaginary-quadratic-field, class-number, ideal-class-group, algebraic-integer).
- Lean names in ?lean: placeholders for other areas: namespaces verified for most (New.Data.*, New.exists_isRegularFamily, New.IsSpread.exists_few_le_finrank_iSup_range); NOT verified: `New.Data.chiZero`, `New.Data.chiM`, `New.Data.chiMLocal`, `New.WeilData.upsilonU1`, `New.AutChar.HasWeight`, `New.Data.singleLift`, `New.Data.goodForms`, `New.DescentPair.IsOrthogonalToFalseLifts`, `New.DescentPair.IsTestForm`, `New.Data.CriticalPair.HasLiftRank`, `New.Data.chiMLocal_zpow_ne_one_iff_isChosen`, `New.LevelPlaces.LevelForm.integralForms`, `New.Data.e₀`, `New.Data.compositeLift`, `New.Data.IsChainDatum`, `New.Data.lowerChain`, `New.Data.turnRatio`, `New.Data.quotientRatio`, `New.Parameters.vacuumBoundConst`.
