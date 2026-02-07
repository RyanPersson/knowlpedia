---
title: "Weierstrass M-test"
description: "A comparison test giving uniform convergence of a series of functions from an absolutely convergent numerical majorant."
---

**Weierstrass M-test:** Let $E$ be a set and let $f_n:E\to\mathbb{R}$ (or $\mathbb{C}$) be functions. Assume there exist numbers $M_n\ge 0$ such that
\[
|f_n(x)|\le M_n \quad \text{for all }x\in E\text{ and all }n,
\]
and the numerical series $\sum_{n=1}^\infty M_n$ is a {{< knowl id="convergent-series" text="convergent series" >}}. Then the {{< knowl id="series-of-functions" text="series of functions" >}} $\sum_{n=1}^\infty f_n$ converges {{< knowl id="uniform-convergence" text="uniformly" >}} on $E$. Moreover, for each $x\in E$ the series $\sum_{n=1}^\infty |f_n(x)|$ converges.

This is a standard sufficient condition for uniform convergence, phrased in terms of bounding the tails of the {{< knowl id="partial-sums" text="partial sums" >}} by an ordinary numerical series.
