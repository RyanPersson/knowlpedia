---
title: "Stirling's approximation"
description: "Asymptotic formulas and bounds for factorials and log-factorials for large n."
---

Stirling's approximation gives accurate large-$n$ estimates for the factorial (factorial function) and related quantities such as binomial and multinomial coefficients.

## Core asymptotic form
For integers $n \to \infty$,
$$
n! \sim \sqrt{2\pi n}\left(\frac{n}{e}\right)^n.
$$
A common refined statement is
$$
n! = \sqrt{2\pi n}\left(\frac{n}{e}\right)^n\left(1+O\!\left(\frac1n\right)\right).
$$

## Logarithmic form
Taking logs (natural logarithm),
$$
\log(n!) = n\log n - n + \tfrac12\log(2\pi n) + O\!\left(\frac1n\right).
$$
This form is often numerically stable and is the starting point for entropy-based approximations (see {{< knowl id="entropy-multinomial-coefficients" >}}).

## Explicit error bounds (one standard version)
There are classical two-sided bounds of the form
$$
\sqrt{2\pi}\,n^{n+\frac12}e^{-n}\,e^{\frac{1}{12n+1}}
\;<\;
n!
\;<\;
\sqrt{2\pi}\,n^{n+\frac12}e^{-n}\,e^{\frac{1}{12n}}.
$$

Equivalently, for $n\ge 1$,
$$
\frac{1}{12n+1}
\;<\;
\log(n!) - \Bigl(n+\tfrac12\Bigr)\log n + n - \tfrac12\log(2\pi)
\;<\;
\frac{1}{12n}.
$$

## Asymptotic series refinement
Stirling's approximation admits an asymptotic expansion in inverse powers of $n$:
$$
n! \sim \sqrt{2\pi n}\left(\frac{n}{e}\right)^n
\left(1+\frac{1}{12n}+\frac{1}{288n^2}-\frac{139}{51840n^3}+\cdots\right),
$$
which is useful for high-precision approximations (typically truncated after a few terms).

## Typical use cases
- Approximating combinatorial counts such as $\binom{n}{k}$ and multinomial coefficients.
- Converting counts into entropy-like expressions in information theory and large deviations (see {{< knowl id="method-of-types" >}}).
- Approximating integrals via local quadratic expansions (conceptually similar to {{< knowl id="laplaces-method" >}}).
