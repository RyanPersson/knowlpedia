---
title: "Series of functions"
description: "An infinite sum ∑ f_n defined via convergence of partial sums as functions."
---

Let $X$ be a set and let $(Y,d_Y)$ be a {{< knowl id="metric-space" text="metric space" >}} (typically $Y=\mathbb{R}$ or $\mathbb{C}$). A **series of functions** on $X$ is a formal expression
$$\sum_{n=1}^\infty f_n,$$
where each $f_n:X\to Y$. The associated **{{< knowl id="partial-sums" text="partial sums" >}}** are the functions
$$S_N(x):=\sum_{n=1}^N f_n(x).$$
One says the series **{{< knowl id="pointwise-convergence" text="converges pointwise" >}}** (respectively, **{{< knowl id="uniform-convergence-of-a-sequence-of-functions" text="converges uniformly" >}}**) if $S_N$ converges pointwise (respectively, uniformly) to some function $S:X\to Y$.

Series of functions are used to define analytic expansions (power series, Fourier series) and to build functions by approximations. The mode of convergence determines which operations can be interchanged with summation.

**Examples:**
- On $(-1,1)$, $\sum_{n=0}^\infty x^n$ is a series of functions with partial sums $S_N(x)=\sum_{n=0}^N x^n$.
- On $\mathbb{R}$, $\sum_{n=1}^\infty \frac{\sin(nx)}{n^2}$ is a series of functions (Fourier-type).
- The {{< knowl id="weierstrass-m-test" text="Weierstrass M-test" >}} gives a standard sufficient condition for uniform convergence of such series.
