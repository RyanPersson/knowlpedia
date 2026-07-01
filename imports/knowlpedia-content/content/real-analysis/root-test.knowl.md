+++
id = "real-analysis/root-test"
title = "Root test"
kind = "knowl"
summary = "A convergence test using the limsup of the nth roots of the term magnitudes."
aliases = ["root-test", "Root test"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/root-test.md"
+++

**Root test:** For a [[real-analysis/series|series]] $\sum_{n=1}^\infty a_n$, define
\[
L=\limsup_{n\to\infty}\sqrt[n]{|a_n|},
\]
where $|a_n|$ denotes the [[real-analysis/absolute-value|absolute value]] of the term.

- If $L<1$, then $\sum_{n=1}^\infty a_n$ is [[real-analysis/absolutely-convergent-series|absolutely convergent]] (hence [[real-analysis/convergent-series|convergent]]).
- If $L>1$ (including $L=\infty$), then $\sum_{n=1}^\infty a_n$ is [[real-analysis/divergent-series|divergent]].
- If $L=1$, the test is inconclusive.

The root test is especially natural for [[real-analysis/power-series|power series]] and is closely related to the [[real-analysis/cauchy-hadamard-theorem|Cauchy–Hadamard theorem]]; compare also the [[real-analysis/ratio-test|ratio test]].
