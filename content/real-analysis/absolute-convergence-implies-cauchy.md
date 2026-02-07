---
title: "Absolute convergence implies Cauchy"
description: "An absolutely convergent series has Cauchy partial sums."
---

**Absolute convergence implies Cauchy:** Let $\sum_{n=1}^\infty a_n$ be a series of real or complex numbers, and let $s_n=\sum_{k=1}^n a_k$ be its {{< knowl id="partial-sums" text="partial sums" >}}. If
\[
\sum_{n=1}^\infty |a_n|
\]
converges, then $(s_n)$ is a Cauchy sequence; equivalently, for every $\varepsilon>0$ there exists $N$ such that for all integers $m>n\ge N$,
\[
\left|\sum_{k=n+1}^m a_k\right|<\varepsilon.
\]

This is the series form of the {{< knowl id="cauchy-criterion-in-rk" text="Cauchy criterion" >}} and is a standard route to {{< knowl id="absolute-convergence-implies-convergence" text="absolute convergence implies convergence" >}}.
