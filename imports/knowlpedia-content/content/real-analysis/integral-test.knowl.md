+++
id = "real-analysis/integral-test"
title = "Integral test"
kind = "knowl"
summary = "A convergence test that compares a nonnegative decreasing series to an improper integral."
aliases = ["integral-test", "Integral test"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/integral-test.md"
+++

**Integral test:** Let $f:[1,\infty)\to[0,\infty)$ be continuous and decreasing, and define $a_n=f(n)$. Then the [[real-analysis/series|series]] $\sum_{n=1}^\infty a_n$ [[real-analysis/convergent-series|converges]] if and only if the improper integral
\[
\int_1^\infty f(x)\,dx
\]
converges (is finite).

Moreover, for each integer $N\ge 1$ one has the remainder bounds
\[
\int_{N+1}^\infty f(x)\,dx \;\le\; \sum_{n=N+1}^\infty a_n \;\le\; \int_N^\infty f(x)\,dx.
\]

This test complements the [[real-analysis/comparison-test|comparison test]] for nonnegative series and is often paired with the [[real-analysis/cauchy-condensation-test|Cauchy condensation test]] for slowly varying terms.
