+++
id = "topology/continuous-on-compact-bounded-corollary"
title = "Continuous function on a compact set is bounded"
kind = "knowl"
summary = "Continuous functions on compact domains have finite upper and lower bounds"
aliases = ["continuous-on-compact-bounded-corollary", "Continuous function on a compact set is bounded"]
domains = ["topology"]
legacy_source_path = "topology/continuous-on-compact-bounded-corollary.md"
+++

**Corollary**: Let $(X,d)$ be a [[topology/compact-set|compact]] [[topology/metric-space|metric space]] and let $f:X\to\mathbb{R}$ be [[real-analysis/continuity-on-a-set|continuous]]. Then $f$ is [[topology/bounded-set|bounded]]: there exists $M<\infty$ such that $|f(x)|\le M$ for all $x\in X$.

**Connection to parent theorem**:
By the [[topology/extreme-value-theorem|extreme value theorem]], $f$ attains a [[real-analysis/maximum|maximum]] $M_+$ and a [[real-analysis/minimum|minimum]] $M_-$. Then $|f(x)|\le \max\{|M_+|,|M_-|\}$.
