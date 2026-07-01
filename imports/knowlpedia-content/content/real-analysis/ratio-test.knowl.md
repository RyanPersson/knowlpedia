+++
id = "real-analysis/ratio-test"
title = "Ratio Test"
kind = "knowl"
summary = "A series converges absolutely if successive terms shrink by a uniform factor less than one."
aliases = ["ratio-test", "Ratio Test"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/ratio-test.md"
+++

**Ratio test:** Let $\sum_{n=1}^\infty a_n$ be a [[real-analysis/series|series]] with $a_n\ne 0$ for all sufficiently large $n$, and define
\[
L=\limsup_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|.
\]
- If $L<1$, then $\sum a_n$ is [[real-analysis/absolutely-convergent-series|absolutely convergent]] (hence convergent).
- If $L>1$ (including $L=\infty$), then $\sum a_n$ is [[real-analysis/divergent-series|divergent]].
- If $L=1$, the test is inconclusive.

The ratio test is particularly effective for factorials, exponentials, and power-series-like terms, and it is closely related to the [[real-analysis/root-test|root test]] and the [[real-analysis/cauchy-hadamard-theorem|Cauchy–Hadamard theorem]] for [[real-analysis/power-series|power series]].
