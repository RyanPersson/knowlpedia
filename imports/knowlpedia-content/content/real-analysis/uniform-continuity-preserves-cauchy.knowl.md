+++
id = "real-analysis/uniform-continuity-preserves-cauchy"
title = "Uniform continuity preserves Cauchy sequences"
kind = "knowl"
summary = "Uniformly continuous maps send Cauchy sequences to Cauchy sequences"
aliases = ["uniform-continuity-preserves-cauchy", "Uniform continuity preserves Cauchy sequences"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/uniform-continuity-preserves-cauchy.md"
+++

Let $(X,d_X)$ and $(Y,d_Y)$ be [[topology/metric-space|metric spaces]] and let $f:X\to Y$ be [[real-analysis/uniform-continuity|uniformly continuous]].

**Proposition**: If $(x_n)$ is a [[topology/cauchy-sequence|Cauchy sequence]] in $X$, then $(f(x_n))$ is a Cauchy sequence in $Y$.

This is an important structural feature: uniform continuity is exactly the hypothesis needed to transport [[topology/complete-metric-space|completeness]] properties through a map.
