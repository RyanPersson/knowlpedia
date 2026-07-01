+++
id = "topology/metric-induced-topology"
title = "Metric-induced topology"
kind = "knowl"
summary = "The topology on a metric space in which a set is open if it contains an open ball around each of its points."
aliases = ["metric-induced-topology", "Metric-induced topology"]
domains = ["topology"]
legacy_source_path = "topology/metric-induced-topology.md"
+++

The **metric-induced topology** on a metric space $(X,d)$ is the collection $\tau_d$ of subsets $U\subseteq X$ such that for every $x\in U$ there exists $r>0$ with $B_d(x,r)\subseteq U$, where $B_d(x,r)$ is the [[topology/open-ball|open ball]] of radius $r$ centered at $x$.

This makes $(X,\tau_d)$ a [[topology/topological-space|topological space]]; equivalently, the family of open balls forms a [[topology/basis-of-topology|basis]] for $\tau_d$, and the [[topology/open-set|open sets]] are precisely unions of open balls.

**Examples:**
- On $\mathbb{R}^n$ with the Euclidean metric, $\tau_d$ is the usual topology of Euclidean space.
- On a set $X$ with the discrete metric, $\tau_d$ is the discrete topology (every subset is open).
