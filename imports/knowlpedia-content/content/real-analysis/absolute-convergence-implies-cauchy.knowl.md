+++
id = "real-analysis/absolute-convergence-implies-cauchy"
title = "Absolute convergence implies Cauchy"
kind = "knowl"
summary = "An absolutely convergent series has Cauchy partial sums."
aliases = ["absolute-convergence-implies-cauchy", "Absolute convergence implies Cauchy"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/absolute-convergence-implies-cauchy.md"
+++

**Absolute convergence implies Cauchy:** Let $\sum_{n=1}^\infty a_n$ be a series of real or complex numbers, and let $s_n=\sum_{k=1}^n a_k$ be its [[real-analysis/partial-sums|partial sums]]. If
\[
\sum_{n=1}^\infty |a_n|
\]
converges, then $(s_n)$ is a Cauchy sequence; equivalently, for every $\varepsilon>0$ there exists $N$ such that for all integers $m>n\ge N$,
\[
\left|\sum_{k=n+1}^m a_k\right|<\varepsilon.
\]

This is the series form of the [[real-analysis/cauchy-criterion-in-rk|Cauchy criterion]] and is a standard route to [[real-analysis/absolute-convergence-implies-convergence|absolute convergence implies convergence]].
