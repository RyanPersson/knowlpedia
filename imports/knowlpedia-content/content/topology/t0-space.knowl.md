+++
id = "topology/t0-space"
title = "T0 space"
kind = "knowl"
summary = "A space where distinct points can be distinguished by membership in an open set."
aliases = ["t0-space", "T0 space"]
domains = ["topology"]
legacy_source_path = "topology/t0-space.md"
+++

A **T0 space** is a [[topology/topological-space|topological space]] $X$ such that for any distinct points $x\neq y$ in $X$, there exists an [[topology/open-set|open set]] $U$ with either $x\in U$ and $y\notin U$, or $y\in U$ and $x\notin U$.

This is the weakest of the common separation axioms; it is implied by being [[topology/t1-space|T1]], and hence by being [[topology/hausdorff-space|Hausdorff]].

**Examples:**
- The Sierpiński space on $\{0,1\}$ with open sets $\varnothing$, $\{1\}$, and $\{0,1\}$ is T0 but not T1.
- Any [[topology/metric-space|metric space]] is T0 (in fact, it is Hausdorff).
