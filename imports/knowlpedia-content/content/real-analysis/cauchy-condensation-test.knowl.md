+++
id = "real-analysis/cauchy-condensation-test"
title = "Cauchy condensation test"
kind = "knowl"
summary = "A convergence test for nonincreasing nonnegative series using dyadic subsequences."
aliases = ["cauchy-condensation-test", "Cauchy condensation test"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/cauchy-condensation-test.md"
+++

**Cauchy condensation test:** Let $(a_n)$ be a nonincreasing sequence of real numbers with $a_n\ge 0$. Then the [[real-analysis/series|series]] $\sum_{n=1}^\infty a_n$ [[real-analysis/convergent-series|converges]] if and only if the condensed series
\[
\sum_{k=0}^\infty 2^k\,a_{2^k}
\]
converges.

This test is especially effective for borderline cases where comparison with $\sum 1/n^p$ is delicate; it is often used alongside the [[real-analysis/integral-test|integral test]] and the [[real-analysis/comparison-test|comparison test]].
