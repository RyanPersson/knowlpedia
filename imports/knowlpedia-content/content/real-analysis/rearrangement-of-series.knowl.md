+++
id = "real-analysis/rearrangement-of-series"
title = "Rearrangement of a series"
kind = "knowl"
summary = "A series obtained by permuting the terms of another series."
aliases = ["rearrangement-of-series", "Rearrangement of a series"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/rearrangement-of-series.md"
+++

A **rearrangement of a series** $\sum_{n=1}^\infty a_n$ is a new series of the form $\sum_{n=1}^\infty a_{\sigma(n)}$, where $\sigma$ is a bijection of the positive integers.

For [[real-analysis/absolutely-convergent-series|absolutely convergent series]], every rearrangement converges to the same value (see [[real-analysis/rearrangement-theorem-absolute|the rearrangement theorem for absolutely convergent series]]), while for [[real-analysis/conditionally-convergent-series|conditionally convergent series]] the behavior can change drastically (see the [[real-analysis/riemann-rearrangement-theorem|Riemann rearrangement theorem]]).

**Examples:**
- Any rearrangement of $\sum_{n=0}^\infty \frac{1}{2^n}$ converges to the same sum.
- Rearrangements of $\sum_{n=1}^\infty \frac{(-1)^{n-1}}{n}$ can converge to different sums, or even diverge, depending on the permutation.
