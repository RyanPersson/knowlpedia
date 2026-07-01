+++
id = "topology/closed-set"
title = "Closed set"
kind = "knowl"
summary = "A subset whose complement is open in the ambient space."
aliases = ["closed-set", "Closed set"]
domains = ["topology"]
legacy_source_path = "topology/closed-set.md"
+++

A **closed set** in a [[topology/topological-space|topological space]] $(X,\mathcal{T})$ is a [[shared-foundations/subset|subset]] $F\subseteq X$ such that its complement $X\setminus F$ (the [[shared-foundations/set-difference|set difference]]) is a [[topology/open-set|open set]].

Closed sets are the natural targets of the [[topology/closure|closure]] operation: the closure of $A$ is the smallest closed set containing $A$. Closed sets also provide an equivalent formulation of [[topology/continuous-map|continuity]] via preimages of closed sets.

**Examples:**
- In $\mathbb{R}$ with the usual topology, $[0,1]$ is closed.
- In the discrete topology on $X$, every subset of $X$ is closed.
- In the indiscrete topology on $X$, the only closed sets are $\varnothing$ and $X$.
