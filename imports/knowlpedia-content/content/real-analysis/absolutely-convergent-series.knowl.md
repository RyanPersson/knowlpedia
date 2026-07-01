+++
id = "real-analysis/absolutely-convergent-series"
title = "Absolutely convergent series"
kind = "knowl"
summary = "A series that converges after taking absolute values term-by-term."
aliases = ["absolutely-convergent-series", "Absolutely convergent series"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/absolutely-convergent-series.md"
+++

An **absolutely convergent series** is a series $\sum_{n=1}^\infty a_n$ such that the series of absolute values $\sum_{n=1}^\infty |a_n|$ is a [[real-analysis/convergent-series|convergent series]].

Absolute convergence is stronger than ordinary convergence: see [[real-analysis/absolute-convergence-implies-convergence|absolute convergence implies convergence]]. It also ensures stability under [[real-analysis/rearrangement-of-series|rearrangements]], formalized by [[real-analysis/rearrangement-theorem-absolute|the rearrangement theorem for absolutely convergent series]].

**Examples:**
- $\sum_{n=1}^\infty \frac{1}{n^2}$ is absolutely convergent.
- $\sum_{n=1}^\infty \frac{(-1)^n}{n^2}$ is absolutely convergent, since $\sum_{n=1}^\infty \left|\frac{(-1)^n}{n^2}\right|=\sum_{n=1}^\infty \frac{1}{n^2}$ converges.
