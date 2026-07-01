+++
id = "topology/metric-sphere"
title = "Metric sphere"
kind = "knowl"
summary = "The set of points at exactly a fixed distance from a given center point in a metric space."
aliases = ["metric-sphere", "Metric sphere"]
domains = ["topology"]
legacy_source_path = "topology/metric-sphere.md"
+++

A **metric sphere** in a metric space $(X,d)$ is a set of the form
\[
S_d(x,r)=\{y\in X : d(x,y)=r\},
\]
where $x\in X$ and $r\ge 0$.

A sphere can be written as $\overline{B}_d(x,r)\setminus B_d(x,r)$, so it sits between the [[topology/open-ball|open ball]] and [[topology/closed-ball|closed ball]] of the same radius.

**Examples:**
- In $\mathbb{R}^n$ with the Euclidean metric, $S(x,r)$ is the usual sphere of radius $r$ centered at $x$.
- In $(\mathbb{R},|\cdot|)$, $S(x,r)=\{x-r,x+r\}$ for $r>0$, and $S(x,0)=\{x\}$.
