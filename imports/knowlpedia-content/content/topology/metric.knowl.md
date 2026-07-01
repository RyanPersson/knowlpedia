+++
id = "topology/metric"
title = "Metric"
kind = "knowl"
summary = "A distance function on a set satisfying positivity, symmetry, and the triangle inequality."
aliases = ["metric"]
domains = ["topology"]
legacy_source_path = "topology/metric.md"
+++

A **metric** on a [[shared-foundations/set|set]] $X$ is a [[shared-foundations/function|function]] $d\colon X\times X\to[0,\infty)$ such that for all $x,y,z\in X$:

1. (Identity of indiscernibles) $d(x,y)=0$ if and only if $x=y$.
2. (Symmetry) $d(x,y)=d(y,x)$.
3. (Triangle inequality) $d(x,z)\le d(x,y)+d(y,z)$.

A metric is the basic structure underlying a [[topology/metric-space|metric space]]; it determines [[topology/open-ball|open balls]] and hence the [[topology/metric-induced-topology|metric-induced topology]].

**Examples:**
- On $\mathbb{R}^n$, the Euclidean metric $d(x,y)=\|x-y\|_2$.
- On any set $X$, the discrete metric $d(x,y)=0$ if $x=y$ and $d(x,y)=1$ otherwise.
