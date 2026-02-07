---
title: "Series of functions"
description: "An infinite sum of functions defined through its partial sums."
---

A **series of functions** on a set $X$ is an expression $\sum_{n=0}^\infty f_n$ where each $f_n:X\to\mathbb{R}$ (or $X\to\mathbb{C}$). Its **partial sums** are the functions
\[
s_N(x)=\sum_{n=0}^N f_n(x).
\]
The series is said to converge (pointwise or uniformly) if the sequence $(s_N)$ converges in the corresponding sense to a limit function $s$.

This is the function-level analogue of a numerical {{< knowl id="series" text="series" >}}, with {{< knowl id="partial-sums" text="partial sums" >}} taken pointwise in $x$. Many criteria for uniform convergence of series are packaged as theorems about sequences $(s_N)$, such as the {{< knowl id="weierstrass-m-test" text="Weierstrass M-test" >}}.

**Examples:**
- On $(-1,1)$, the {{< knowl id="power-series" text="power series" >}} $\sum_{n=0}^\infty x^n$ has partial sums $s_N(x)=(1-x^{N+1})/(1-x)$ and converges pointwise to $1/(1-x)$.
- On $\mathbb{R}$, the series $\sum_{n=1}^\infty \frac{\sin(nx)}{n^2}$ converges uniformly by comparison with $\sum_{n=1}^\infty 1/n^2$ (an application of the {{< knowl id="weierstrass-m-test" text="M-test" >}}).
