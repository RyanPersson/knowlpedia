---
title: "T1 space"
description: "Separation axiom where singletons are closed"
---

A **$T_1$ space** is a {{< knowl id="topological-space" section="topology-core" text="topological space" >}} $X$ in which every singleton $\{x\}$ is {{< knowl id="closed-set" section="topology-core" text="closed" >}}.

Equivalently, $X$ is $T_1$ if for every pair of distinct points $x\neq y$, there exists an {{< knowl id="open-set" section="topology-core" text="open set" >}} $U$ with $x\in U$ and $y\notin U$ (and, by symmetry, also an open set $V$ with $y\in V$ and $x\notin V$).

Every $T_1$ space is {{< knowl id="t0-space" text="T0" >}}, and every {{< knowl id="hausdorff-space" text="Hausdorff" >}} space is $T_1$.

**Examples:**
- Every {{< knowl id="metric-space" section="topology-metric" text="metric space" >}} is $T_1$.
- On an infinite set $X$, the cofinite topology (open sets are $\varnothing$ and complements of finite sets) is $T_1$ but not Hausdorff.
- The Sierpiński space on $\{0,1\}$ with open sets $\varnothing,\{1\},\{0,1\}$ is not $T_1$ since $\{0\}$ is not closed.
