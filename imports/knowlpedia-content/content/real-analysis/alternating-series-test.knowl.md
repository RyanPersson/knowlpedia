+++
id = "real-analysis/alternating-series-test"
title = "Alternating series test"
kind = "knowl"
summary = "A convergence test for alternating series with decreasing term magnitudes tending to zero."
aliases = ["alternating-series-test", "Alternating series test"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/alternating-series-test.md"
+++

**Alternating series test (Leibniz):** Let $(a_n)$ be a sequence of real numbers such that

1. $a_n\ge 0$ for all $n$,
2. $(a_n)$ is decreasing, and
3. $a_n\to 0$.

Then the [[real-analysis/series|series]] $\sum_{n=1}^\infty (-1)^{n-1}a_n$ [[real-analysis/convergent-series|converges]].

A common consequence is an error bound for [[real-analysis/partial-sums|partial sums]]: if $s$ is the limit and $s_N=\sum_{n=1}^N (-1)^{n-1}a_n$, then $|s-s_N|\le a_{N+1}$. This test is a basic source of [[real-analysis/conditionally-convergent-series|conditional convergence]] and uses the necessary condition [[real-analysis/terms-go-to-zero|terms go to zero]].
