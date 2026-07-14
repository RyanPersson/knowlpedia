---
title: "T1 space"
description: "A topological space in which all single points are closed."
---

A **$T_1$ space** is a {{< knowl id="topological-space" text="topological space" >}} $(X,\tau)$ in which every singleton set $\{x\}$ is a {{< knowl id="closed-set" text="closed set" >}}.

Equivalently, for any distinct points $x\neq y$, there exists an open set $U$ with $x\in U$ and $y\notin U$. Another equivalent form is: for each $x\in X$, the {{< knowl id="complement" text="complement" >}} $X\setminus\{x\}$ is open.

Every $T_1$ space is automatically {{< knowl id="t0-space" text="T0" >}}. In particular, every {{< knowl id="hausdorff-space" text="Hausdorff space" >}} is $T_1$. Many familiar examples come from {{< knowl id="metric-space" text="metric spaces" >}}, whose induced topologies are always $T_1$.

**Examples:**
- **Metric spaces:** In any metric space, singletons are closed, so the space is $T_1$ (indeed, Hausdorff).
- **Cofinite topology:** On an infinite set $X$, let the open sets be $\varnothing$ together with all subsets whose complements are finite. Then each singleton $\{x\}$ is closed (its complement is cofinite, hence open), so the space is $T_1$, but it is not Hausdorff (any two nonempty open sets intersect).
