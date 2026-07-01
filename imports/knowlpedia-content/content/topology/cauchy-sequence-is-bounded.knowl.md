+++
id = "topology/cauchy-sequence-is-bounded"
title = "Cauchy sequence is bounded"
kind = "knowl"
summary = "In a metric space, every Cauchy sequence is bounded"
aliases = ["cauchy-sequence-is-bounded", "Cauchy sequence is bounded"]
domains = ["topology"]
legacy_source_path = "topology/cauchy-sequence-is-bounded.md"
+++

**Cauchy sequence is bounded:** Let $(X,d)$ be a [[topology/metric-space|metric space]] and let $(x_n)$ be a [[topology/cauchy-sequence|Cauchy sequence]] in $X$. Then $\{x_n:n\in\mathbb{N}\}$ is a [[topology/bounded-set|bounded set]]; equivalently, there exist $x_0\in X$ and $R>0$ such that $d(x_n,x_0)\le R$ for all $n$.

This is often paired with [[topology/complete-metric-space|completeness]] results: Cauchy behavior already forces the sequence to stay inside some [[topology/closed-ball|closed ball]].
