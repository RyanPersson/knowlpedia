---
title: "T1 space"
description: "A space in which every singleton set is closed."
---

A **T1 space** is a {{< knowl id="topological-space" text="topological space" >}} $X$ such that for every point $x\in X$, the singleton $\{x\}$ is a {{< knowl id="closed-set" text="closed set" >}} in $X$.
Equivalently, for any distinct points $x\neq y$ there exists an {{< knowl id="open-set" text="open set" >}} containing $x$ but not $y$, and (symmetrically) an open set containing $y$ but not $x$.

The T1 axiom strengthens {{< knowl id="t0-space" text="T0" >}} and is implied by the {{< knowl id="hausdorff-space" text="Hausdorff" >}} condition.

**Examples:**
- Every {{< knowl id="metric-space" text="metric space" >}} is T1.
- On an infinite set $X$, the cofinite topology (open sets are $\varnothing$ and complements of finite sets) is T1 but not Hausdorff.
