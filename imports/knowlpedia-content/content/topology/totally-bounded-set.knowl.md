+++
id = "topology/totally-bounded-set"
title = "Totally bounded set"
kind = "knowl"
summary = "A set in a metric space that can be covered by finitely many small balls for every radius."
aliases = ["totally-bounded-set", "Totally bounded set"]
domains = ["topology"]
legacy_source_path = "topology/totally-bounded-set.md"
+++

A **totally bounded set** is a subset $A\subseteq X$ of a [[topology/metric-space|metric space]] $(X,d)$ such that for every $\varepsilon>0$ there exist points $x_1,\dots,x_n\in X$ with
\[
A \subseteq \bigcup_{k=1}^n B(x_k,\varepsilon),
\]
where $B(x_k,\varepsilon)$ is the [[topology/open-ball|open ball]] of radius $\varepsilon$ around $x_k$.

Total boundedness is equivalent to the existence of finite [[topology/epsilon-net|epsilon-nets]] at every scale, and (together with [[topology/complete-metric-space|completeness]]) it characterizes [[topology/compact-set|compactness]] in metric spaces.

**Examples:**
- In $\mathbb{R}$ with the usual metric, the interval $[0,1]$ is totally bounded.
- The set of integers $\mathbb{Z}\subseteq\mathbb{R}$ (usual metric) is not totally bounded.
