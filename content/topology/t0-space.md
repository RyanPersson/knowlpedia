---
title: "T0 space"
description: "A space where distinct points can be distinguished by membership in an open set."
---

A **T0 space** is a {{< knowl id="topological-space" text="topological space" >}} $X$ such that for any distinct points $x\neq y$ in $X$, there exists an {{< knowl id="open-set" text="open set" >}} $U$ with either $x\in U$ and $y\notin U$, or $y\in U$ and $x\notin U$.

This is the weakest of the common separation axioms; it is implied by being {{< knowl id="t1-space" text="T1" >}}, and hence by being {{< knowl id="hausdorff-space" text="Hausdorff" >}}.

**Examples:**
- The Sierpiński space on $\{0,1\}$ with open sets $\varnothing$, $\{1\}$, and $\{0,1\}$ is T0 but not T1.
- Any {{< knowl id="metric-space" text="metric space" >}} is T0 (in fact, it is Hausdorff).
