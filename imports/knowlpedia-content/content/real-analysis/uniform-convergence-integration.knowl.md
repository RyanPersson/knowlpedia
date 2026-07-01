+++
id = "real-analysis/uniform-convergence-integration"
title = "Uniform convergence and integration"
kind = "knowl"
summary = "A uniformly convergent series of Riemann integrable functions may be integrated term by term."
aliases = ["uniform-convergence-integration", "Uniform convergence and integration"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/uniform-convergence-integration.md"
+++

**Uniform convergence and integration:** Let $f_n:[a,b]\to\mathbb{R}$ be [[real-analysis/riemann-integrable-function|Riemann integrable]] for all $n$, and let $s_N=\sum_{n=1}^N f_n$ be the partial sums. If $s_N\to s$ [[real-analysis/uniform-convergence|uniformly]] on $[a,b]$, then $s$ is [[real-analysis/riemann-integrable-function|Riemann integrable]] and
\[
\int_a^b s(x)\,dx \;=\; \lim_{N\to\infty}\int_a^b s_N(x)\,dx \;=\; \sum_{n=1}^\infty \int_a^b f_n(x)\,dx,
\]
where the series of real numbers on the right converges.

In applications, uniform convergence of $(s_N)$ is often established using the [[real-analysis/weierstrass-m-test|Weierstrass M-test]].
