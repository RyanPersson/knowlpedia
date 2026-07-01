+++
id = "topology/t1-space"
title = "T1 space"
kind = "knowl"
summary = "A space in which every singleton set is closed."
aliases = ["t1-space", "T1 space"]
domains = ["topology"]
legacy_source_path = "topology/t1-space.md"
+++

A **T1 space** is a [[topology/topological-space|topological space]] $X$ such that for every point $x\in X$, the singleton $\{x\}$ is a [[topology/closed-set|closed set]] in $X$.
Equivalently, for any distinct points $x\neq y$ there exists an [[topology/open-set|open set]] containing $x$ but not $y$, and (symmetrically) an open set containing $y$ but not $x$.

The T1 axiom strengthens [[topology/t0-space|T0]] and is implied by the [[topology/hausdorff-space|Hausdorff]] condition.

**Examples:**
- Every [[topology/metric-space|metric space]] is T1.
- On an infinite set $X$, the cofinite topology (open sets are $\varnothing$ and complements of finite sets) is T1 but not Hausdorff.
