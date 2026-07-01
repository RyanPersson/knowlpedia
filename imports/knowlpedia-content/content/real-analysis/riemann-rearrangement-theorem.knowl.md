+++
id = "real-analysis/riemann-rearrangement-theorem"
title = "Riemann rearrangement theorem"
kind = "knowl"
summary = "A conditionally convergent real series can be rearranged to converge to any real value or diverge."
aliases = ["riemann-rearrangement-theorem", "Riemann rearrangement theorem"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/riemann-rearrangement-theorem.md"
+++

**Riemann rearrangement theorem:** Let $\sum_{n=1}^\infty a_n$ be a real series that is [[real-analysis/convergent-series|convergent]] but not [[real-analysis/absolutely-convergent-series|absolutely convergent]] (equivalently, it is [[real-analysis/conditionally-convergent-series|conditionally convergent]]). Then:

- For every $L\in\mathbb{R}$, there exists a bijection $\pi:\mathbb{N}\to\mathbb{N}$ such that the rearranged series $\sum_{n=1}^\infty a_{\pi(n)}$ converges to $L$.
- There also exist rearrangements that diverge to $+\infty$, diverge to $-\infty$, or fail to have a limit.

This theorem highlights the sharp difference between conditional convergence and the stability enjoyed by [[real-analysis/rearrangement-theorem-absolute|absolutely convergent series under rearrangement]].
