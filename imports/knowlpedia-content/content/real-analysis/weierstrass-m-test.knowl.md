+++
id = "real-analysis/weierstrass-m-test"
title = "Weierstrass M-test"
kind = "knowl"
summary = "A comparison test giving uniform convergence of a series of functions from an absolutely convergent numerical majorant."
aliases = ["weierstrass-m-test", "Weierstrass M-test"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/weierstrass-m-test.md"
+++

**Weierstrass M-test:** Let $E$ be a set and let $f_n:E\to\mathbb{R}$ (or $\mathbb{C}$) be functions. Assume there exist numbers $M_n\ge 0$ such that
\[
|f_n(x)|\le M_n \quad \text{for all }x\in E\text{ and all }n,
\]
and the numerical series $\sum_{n=1}^\infty M_n$ is a [[real-analysis/convergent-series|convergent series]]. Then the [[real-analysis/series-of-functions|series of functions]] $\sum_{n=1}^\infty f_n$ converges [[real-analysis/uniform-convergence|uniformly]] on $E$. Moreover, for each $x\in E$ the series $\sum_{n=1}^\infty |f_n(x)|$ converges.

This is a standard sufficient condition for uniform convergence, phrased in terms of bounding the tails of the [[real-analysis/partial-sums|partial sums]] by an ordinary numerical series.
