+++
id = "real-analysis/conditionally-convergent-series"
title = "Conditionally convergent series"
kind = "knowl"
summary = "A convergent series that is not absolutely convergent."
aliases = ["conditionally-convergent-series", "Conditionally convergent series"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/conditionally-convergent-series.md"
+++

A **conditionally convergent series** is a series $\sum_{n=1}^\infty a_n$ that is [[real-analysis/convergent-series|convergent]] but not [[real-analysis/absolutely-convergent-series|absolutely convergent]], meaning that $\sum_{n=1}^\infty a_n$ converges while $\sum_{n=1}^\infty |a_n|$ diverges.

Conditional convergence is fragile under [[real-analysis/rearrangement-of-series|rearrangements]]: the [[real-analysis/riemann-rearrangement-theorem|Riemann rearrangement theorem]] shows that rearranging terms can change the sum or destroy convergence. Many standard examples are produced using the [[real-analysis/alternating-series-test|alternating series test]].

**Examples:**
- The alternating harmonic series $\sum_{n=1}^\infty \frac{(-1)^{n-1}}{n}$ converges conditionally.
- The alternating series $\sum_{n=1}^\infty \frac{(-1)^{n-1}}{\sqrt{n}}$ converges conditionally.
