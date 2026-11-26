# Coverage report: reduction-zeros

State: complete. 59 proof knowls in `knowlpedia-content/content/proofs/grh/reduction-zeros/`, the area page `proofs/grh/reduction-zeros.knowl.md`, and the sidecar `concepts/reduction-zeros.tsv` (62 lines).

Counts: 10 definitions, 18 theorems, 22 lemmas, 9 propositions. proof_status: 47 full, 2 outline, 0 cited, 0 statement.

Nothing was compiled. Every assigned file was read completely once (statements, proofs and head comments). The human proofs were written from that reading and checked by redoing the computations by hand; they were not re-compared line by line with the Lean text after writing.

## Files

| File | Lines | Read | Knowls |
|---|---|---|---|
| `Statements.lean` | 16 | full | dirichlet-l-nonvanishing-right-of-half, dirichlet-l-zeros-on-line, riemann-zeta-zeros-on-line |
| `Main.lean` | 22 | full | main-theorems |
| `New/Main.lean` | 65 | full | zeros-on-line-from-half-plane, zeta-zeros-on-line-from-half-plane |
| `New/Reduction/Zeros/Criterion.lean` | 91 | full | one-sided-criterion |
| `New/Reduction/Zeros/PrimeError.lean` | 445 | full | weight-lambda-k, log-deriv-mean, prime-remainder, growth-of-prime-remainder, mertens-type-bound, g-one-and-chowla-selberg-constant, dirichlet-series-of-weight, laplace-transform-of-prime-remainder, g-q-at-one-is-real, residues-of-log-deriv-mean, prime-remainder-is-polar |
| `New/Reduction/Zeros/PrimeNumberTheorem.lean` | 239 | full | prime-remainder-as-integral, prime-remainder-varies-slowly, bound-for-log-deriv-mean-near-one, pnt-for-prime-remainder |
| `Lib/Analytic/EntireLFunction.lean` | 209 | full | polar-function, quad-twist-not-principal, entire-l-basic-properties (outline), dirichlet-series-of-chi-lambda, residue-of-log-deriv-entire-l |
| `Lib/Analytic/Landau.lean` | 261 | full | landau-lemma, landau-lemma-with-simple-pole, measure-for-one-sided-bound, no-pole-right-of-beta |
| `Lib/Analytic/ZeroSymmetry.lean` | 82 | full | euler-factors-nonvanishing, zero-symmetry |
| `Lib/Analytic/PolyaVinogradov.lean` | 205 | full | gauss-sum-modulus, polya-vinogradov |
| `Lib/Analytic/DirichletTheta.lean` | 527 | full | theta-series-of-coefficients, mellin-of-theta-series, poisson-summation-for-character-theta (outline), riemann-formula-for-character |
| `Lib/Analytic/QuadraticTwist.lean` | 837 | full | theta-tail-integral-and-mollifier, zero-forces-large-tail-integral, jacobi-symbol-sums, mean-value-theta-jacobi, legendre-as-jacobi-of-odd-part, twist-of-primitive-is-primitive, bad-primes-are-rare, choice-of-prime |
| `Lib/Analytic/Primes.lean` | 453 | full (long lines cut at 400 characters on screen; no proof step was lost that I noticed) | totient-lower-bound, zero-free-disc-uniform, newman-circle-bound, prime-in-log-window |
| `Lib/Analytic/PrimeNumberTheorem/LFunctionGrowth.lean` | 388 | full | regularised-l-function, linear-bound-regular-l, bound-regular-l-near-one-line |
| `Lib/Analytic/PrimeNumberTheorem/ZeroFreeRegion.lean` | 205 | full | lower-bound-right-of-one, zero-free-region |
| `Lib/Analytic/PrimeNumberTheorem/Tauberian.lean` | 378 | full | taylor-coefficient-as-gamma-mean, cauchy-estimate-for-slope, tauberian-theorem |

## Outlines and what is only asserted

* `entire-l-basic-properties`: continuation of L(s, chi), non-vanishing on Re s >= 1 and the non-zero residue at 1 are Mathlib facts, cited, not proved.
* `poisson-summation-for-character-theta`: Poisson summation for the weights exp(-pi z^2) and z exp(-pi z^2) with a shift (`New.poisson_summation_gaussianMonomial`) is taken from Mathlib's functional equations of the Hurwitz theta kernels and is not reproved; the rest is complete.

Knowls marked full nevertheless cite standard theorems by placeholder (functional equation, 3-4-1 inequality, Chebyshev bound, three-lines theorem, Abel summation, divergence of sum log p / p in a class, Dirichlet series facts). These are Mathlib results in the source as well.

## Doubts and points to check

1. `New.grh` and how `OneSidedBound` feeds the criterion are in another area. The criterion needs the bound R(x) <= x^(beta-1) for all large real x; the reading guide mentions a bound at integers x (`eventually_primeRemainder_natCast_le`). I assume the other chapter bridges this (the slow-variation lemma here would do it), but I did not read it. The remark at the end of `one-sided-criterion` quoting the constant (64 phi(q0) + 3) x^(-1/2 + 6 eps) is taken from the guide, not from the Lean file.
2. Fully qualified names of declarations from `Lib/General/NumberTheory/ImaginaryQuadraticField.lean` are written `New.entireL`, `New.quadTwist`, `New.chiK`, `New.chowlaSelbergConst`; the namespace was inferred from the file heads, not checked at the declaration.
3. Lean conventions replaced by ordinary mathematics: Gamma factors with value 0 at poles (I use the entire function 1/Gamma_R); the logarithmic derivative with value 0 at zeros; the residue formula with s(1-s) in the denominator at s = 1 (I define r(1) = 0); R_q defined in Lean for all real x (I define it for x > 0). Each is noted in a Remarks section.
4. `choice-of-prime`: the Lean proof first reduces to beta < 1; my proof omits this reduction as unnecessary. `isPolar_primeRemainder` assumes d = 7 mod 8 but uses only d odd; stated as in Lean, with a note.
5. `mean-value-theta-jacobi`: the constant in part 2/3 is written as sqrt(C)/delta as in Lean; the interchange of the double series with the sum over v is justified by absolute convergence, stated briefly.
6. In `zero-free-region` part 2 I take l >= N to get N <= e^l (Lean does the same with l + 1 <= e^l).
7. Existing-corpus links (complex-analysis/…, measure-theory/…, linear-algebra/cauchy-schwarz-inequality, algebra-rings/chinese-remainder-theorem) were chosen by title from the index; I did not open each target to confirm it states exactly the form used. `real-analysis/gamma-function` covers positive real arguments only, so the complex Gamma function is recorded in the sidecar as needing a knowl.
8. Small helper lemmas (measurability, integrability, coercions, `laplace_pow`, `image_inv_const_mul_Ioo`, etc.) are folded into the proofs that use them and listed in the `lean` field of those knowls. `prerequisites` is left empty everywhere, as the guide asks for drafts with placeholders.
