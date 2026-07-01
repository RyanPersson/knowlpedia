+++
id = "real-analysis/abels-theorem"
title = "Abel's theorem"
kind = "knowl"
summary = "A boundary limit theorem relating a convergent series to its associated power series near the radius 1."
aliases = ["abels-theorem", "Abel's theorem"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/abels-theorem.md"
+++

**Abel's theorem:** Let $\sum_{n=0}^\infty a_n$ be a convergent series of real or complex numbers, with sum $s$. For $0\le x<1$, define
\[
f(x)=\sum_{n=0}^\infty a_n x^n.
\]
Then $f(x)$ is well-defined for every $0\le x<1$, and
\[
\lim_{x\to 1^-} f(x)=s.
\]

This connects ordinary [[real-analysis/convergent-series|convergence of series]] with boundary behavior of [[real-analysis/power-series|power series]] and complements radius-of-convergence results such as the [[real-analysis/cauchy-hadamard-theorem|Cauchy–Hadamard theorem]].
