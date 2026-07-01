+++
id = "topology/neighborhood"
title = "Neighborhood"
kind = "knowl"
summary = "A set that contains an open set around a given point."
aliases = ["neighborhood"]
domains = ["topology"]
legacy_source_path = "topology/neighborhood.md"
+++

A **neighborhood** of a point $x$ in a [[topology/topological-space|topological space]] $(X,\mathcal{T})$ is a subset $N\subseteq X$ such that there exists an [[topology/open-set|open set]] $U\in\mathcal{T}$ with $x\in U\subseteq N$. Equivalently, $N$ is a neighborhood of $x$ if and only if $x\in \operatorname{int}(N)$, where [[topology/interior|interior]] is taken in $X$.

Neighborhoods give a point-based way to express concepts like [[topology/limit-point|limit points]] and [[topology/continuous-map|continuity]] without referring directly to all open sets.

**Examples:**
- In $\mathbb{R}$ with the usual topology, $(x-\varepsilon,x+\varepsilon)$ is a neighborhood of $x$ for any $\varepsilon>0$.
- In a [[topology/metric-space|metric space]], every [[topology/open-ball|open ball]] centered at $x$ is a neighborhood of $x$.
- In $\mathbb{R}$, the closed interval $[x-1,x+1]$ is a neighborhood of $x$ (it contains the open interval $(x-1,x+1)$).
