---
title: "Saddle-Point (Laplace) Method in One Dimension"
description: "Refined asymptotics for integrals of exp(n f(x)) near a nondegenerate maximizer, giving Gaussian prefactors beyond the Laplace principle."
---

This lemma refines the {{< knowl id="laplace-principle-lemma" text="Laplace principle" >}} by identifying the leading prefactor when the maximum is attained at a nondegenerate interior point.

## Statement (one-dimensional nondegenerate maximum)
Let $f:[a,b]\to\mathbb{R}$ be twice continuously differentiable and suppose:
- $f$ has a unique global maximum at an interior point $x_0\in(a,b)$,
- $f''(x_0)<0$ (nondegenerate maximum),
- $g:[a,b]\to\mathbb{R}$ is continuous with $g(x_0)\neq 0$.

Define
$$
I_n = \int_a^b e^{n f(x)}\, g(x)\,dx.
$$

Then, as $n\to\infty$,
$$
I_n
={}
e^{n f(x_0)}\, g(x_0)\,
\sqrt{\frac{2\pi}{n\,|f''(x_0)|}}\,
\big(1+o(1)\big).
$$

Under higher smoothness assumptions on $f$ and $g$, one can obtain a full asymptotic expansion in powers of $1/n$.

## Key hypotheses and conclusions
**Hypotheses**
- A unique interior maximizer $x_0$ for $f$.
- Nondegeneracy: $f''(x_0)<0$.
- Mild regularity of $g$ and $f$ near $x_0$.

**Conclusions**
- The integral is asymptotically Gaussian around $x_0$ after Taylor expansion of $f$:
  the leading exponential growth is $e^{n f(x_0)}$, and the subexponential prefactor is of order $n^{-1/2}$.
- This yields a quantitative refinement of the Laplace principle:
  $\frac1n\log I_n \to f(x_0)$.

In statistical mechanics, saddle-point estimates justify mean-field and variational approximations of partition functions (for example, after introducing an order parameter or via Hubbard–Stratonovich transforms) and they often explain the appearance of Gaussian fluctuations around equilibrium points.