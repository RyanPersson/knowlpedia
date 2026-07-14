---
title: "Hausdorff space"
description: "A topological space in which distinct points have disjoint neighborhoods."
---

A **Hausdorff space** (or **$T_2$ space**) is a {{< knowl id="topological-space" text="topological space" >}} $X$ such that for any two distinct points $x\neq y$ in $X$, there exist {{< knowl id="neighborhood" text="neighborhoods" >}} $U$ of $x$ and $V$ of $y$ with $U\cap V=\varnothing$.

Hausdorffness is a strong separation condition: every Hausdorff space is {{< knowl id="t1-space" text="T1" >}}. A central consequence is {{< knowl id="uniqueness-of-limits-hausdorff" text="uniqueness of limits of sequences" >}}, which underlies many arguments in analysis and topology. In particular, every {{< knowl id="metric-space" text="metric space" >}} is Hausdorff.

**Examples:**
- **Metric spaces:** If $x\neq y$ in a metric space, taking open balls of radius $d(x,y)/3$ around $x$ and $y$ gives disjoint neighborhoods, so the space is Hausdorff.
- **Indiscrete topology:** If $X$ has at least two points and the only open sets are $\varnothing$ and $X$, then no two distinct points can have disjoint neighborhoods, so the space is not Hausdorff.
