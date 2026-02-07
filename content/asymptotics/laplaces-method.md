---
title: "Laplace's method"
description: "Asymptotic evaluation of integrals dominated by a single interior maximizer of the exponent."
---

Laplace's method approximates integrals of the form
$$
I(n)=\int_a^b e^{n f(x)}\,g(x)\,dx
$$

for large $n$, when the main contribution comes from a neighborhood of the point where $f$ is maximal. It is the real-variable analogue of the complex {{< knowl id="saddle-point-method" >}}.

## One-dimensional interior-maximum theorem
Assume:
- $f$ is twice continuously differentiable on $(a,b)$ and has a unique maximizer $x_0\in(a,b)$,
- $f''(x_0)<0$,
- $g$ is continuous at $x_0$ and $g(x_0)\ne 0$.

Then as $n\to\infty$,
$$
\int_a^b e^{n f(x)}\,g(x)\,dx
\sim
e^{n f(x_0)}\,g(x_0)\,\sqrt{\frac{2\pi}{n\,|f''(x_0)|}}.
$$
More refined expansions are obtained by keeping higher-order terms of the local Taylor expansion.

## Sketch of why it works
Near the maximizer $x_0$, expand $f$ using a second-order Taylor approximation:
$$
f(x) = f(x_0) + \tfrac12 f''(x_0)(x-x_0)^2 + \text{higher-order terms}.
$$

For large $n$, the factor $e^{n f(x)}$ is sharply peaked at $x_0$, and the integral is well-approximated by replacing the exponent with its quadratic part and extending the local integral to all of $\mathbb{R}$, yielding a Gaussian integral.

## Multidimensional version (informal)
For $x\in\mathbb{R}^d$,
$$
I(n)=\int_{\Omega} e^{n f(x)} g(x)\,dx,
$$

if $f$ has a unique interior maximizer $x_0$ with negative definite Hessian $H = \nabla^2 f(x_0)$, then typically
$$
I(n)\sim e^{n f(x_0)}\,g(x_0)\,(2\pi/n)^{d/2}\,(\det(-H))^{-1/2}.
$$

## Common variants and caveats
- If the maximum occurs at an endpoint ($x_0=a$ or $x_0=b$), the leading order usually changes (often to an $n^{-1}$-type scale rather than $n^{-1/2}$).
- If there are multiple maximizers, the leading term is typically the sum of contributions from each (when they are well-separated and nondegenerate).
- If $f''(x_0)=0$ (degenerate maximum), the scale becomes $n^{-\alpha}$ for some $\alpha$ determined by the first nonzero derivative at $x_0$.

## Where it shows up
- Normal approximations and local limit behavior.
- Large-$n$ asymptotics of combinatorial sums via integral representations.
- As the real-variable building block for the complex steepest-descent/saddle-point techniques (see {{< knowl id="saddle-point-method" >}}).
