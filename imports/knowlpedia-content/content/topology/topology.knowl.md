+++
id = "topology/topology"
title = "Topology"
kind = "knowl"
summary = "A collection of subsets declared open, closed under unions and finite intersections."
aliases = ["topology"]
domains = ["topology"]
legacy_source_path = "topology/topology.md"
+++

A **topology** on a [[shared-foundations/set|set]] $X$ is a collection $\mathcal{T}\subseteq \mathcal{P}(X)$ such that:
- $\varnothing\in\mathcal{T}$ and $X\in\mathcal{T}$,
- if $\{U_i\}_{i\in I}\subseteq\mathcal{T}$ then $\bigcup_{i\in I}U_i\in\mathcal{T}$,
- if $U,V\in\mathcal{T}$ then $U\cap V\in\mathcal{T}$.

The elements of $\mathcal{T}$ are the [[topology/open-set|open sets]], and they determine notions such as [[topology/closed-set|closed sets]], [[topology/neighborhood|neighborhoods]], [[topology/interior|interior]], [[topology/closure|closure]], and [[topology/continuous-map|continuity]]. A [[topology/topological-space|topological space]] is a set together with a chosen topology.

**Examples:**
- The discrete topology on $X$, given by $\mathcal{T}=\mathcal{P}(X)$.
- The indiscrete topology on $X$, given by $\mathcal{T}=\{\varnothing,X\}$.
- The [[topology/metric-induced-topology|topology induced by a metric]] on a [[topology/metric-space|metric space]].
