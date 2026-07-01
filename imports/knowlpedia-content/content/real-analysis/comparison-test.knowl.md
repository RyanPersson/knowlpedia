+++
id = "real-analysis/comparison-test"
title = "Comparison Test"
kind = "knowl"
summary = "A nonnegative series is controlled by a larger or smaller nonnegative series."
aliases = ["comparison-test", "Comparison Test"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/comparison-test.md"
+++

**Comparison test:** Let $\sum_{n=1}^\infty a_n$ and $\sum_{n=1}^\infty b_n$ be [[real-analysis/series|series]] with $a_n\ge 0$ and $b_n\ge 0$ for all $n$.

- If $0 \le a_n \le b_n$ for all sufficiently large $n$ and $\sum b_n$ is a [[real-analysis/convergent-series|convergent series]], then $\sum a_n$ is convergent.
- If $0 \le a_n \le b_n$ for all sufficiently large $n$ and $\sum a_n$ is a [[real-analysis/divergent-series|divergent series]], then $\sum b_n$ diverges.

This test reduces many convergence questions to comparisons with standard benchmark series, and it is complemented by the [[real-analysis/limit-comparison-test|limit comparison test]] when direct inequalities are hard to establish.
