---
title: "T1 space"
description: "A topological space in which points are closed, equivalently distinct points can be separated by open sets."
---

A **$T_1$ space** is a {{{< knowl id="topological-space" section="topology-core" text="topological space" >}}} $X$ such that for any distinct points $x\neq y$ there exist {{{< knowl id="open-set" section="topology-core" text="open sets" >}}} $U,V$ with $x\in U$, $y\notin U$ and $y\in V$, $x\notin V$.

Equivalently, $X$ is $T_1$ if and only if every singleton $\{x\}$ is a {{{< knowl id="closed-set" section="topology-core" text="closed set" >}}}. Every $T_1$ space is automatically {{{< knowl id="t0-space" text="T0" >}}}, and every {{{< knowl id="hausdorff-space" text="Hausdorff space" >}}} is $T_1$.

**Examples:**
- Every {{{< knowl id="metric-space" section="topology-metric" text="metric space" >}}} is Hausdorff, hence $T_1$.
- On an infinite set $X$ with the cofinite topology (open sets are $\varnothing$ and complements of finite sets), the space is $T_1$ but not Hausdorff.
