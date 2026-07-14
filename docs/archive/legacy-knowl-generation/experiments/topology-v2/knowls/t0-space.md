---
title: "T0 space"
description: "Kolmogorov separation axiom: distinct points are topologically distinguishable"
---

A **$T_0$ space** is a {{< knowl id="topological-space" section="topology-core" text="topological space" >}} $X$ such that for any two distinct points $x,y\in X$, there exists an {{< knowl id="open-set" section="topology-core" text="open set" >}} $U\subseteq X$ with either $x\in U$ and $y\notin U$, or $y\in U$ and $x\notin U$.

Equivalently, $X$ is $T_0$ if distinct points have distinct {{< knowl id="closure" section="topology-core" text="closures" >}}: if $x\neq y$, then $\overline{\{x\}}\neq \overline{\{y\}}$.

This is the weakest of the standard separation axioms; compare {{< knowl id="t1-space" text="T1 spaces" >}} and {{< knowl id="hausdorff-space" text="Hausdorff spaces" >}}.

**Examples:**
- Every {{< knowl id="t1-space" text="T1 space" >}} is $T_0$ (in particular, every {{< knowl id="metric-space" section="topology-metric" text="metric space" >}} is $T_0$).
- The Sierpiński space on $\{0,1\}$ with open sets $\varnothing,\{1\},\{0,1\}$ is $T_0$ but not $T_1$.
- A set with the indiscrete topology $\{\varnothing,X\}$ is not $T_0$ when $|X|\ge 2$.
