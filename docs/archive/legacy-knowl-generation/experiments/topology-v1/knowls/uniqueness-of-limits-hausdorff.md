---
title: "Uniqueness of limits in Hausdorff spaces"
description: "In a Hausdorff space, a convergent sequence has at most one limit."
---

**Uniqueness of limits (Hausdorff spaces)**:  
Let $X$ be a {{< knowl id="hausdorff-space" text="Hausdorff space" >}}. If a {{< knowl id="convergent-sequence" text="sequence" >}} $(x_n)$ converges to $x$ and also converges to $y$, then $x=y$.

This is one of the most frequently used consequences of the Hausdorff separation axiom: distinct points can be separated by disjoint {{< knowl id="neighborhood" text="neighborhoods" >}}, and that separation forces limits to be unique.

**Proof sketch**:  
Assume $x\neq y$. By Hausdorffness, choose disjoint neighborhoods $U$ of $x$ and $V$ of $y$. Since $x_n\to x$, eventually $x_n\in U$, and since $x_n\to y$, eventually $x_n\in V$. For large $n$ this would force $x_n\in U\cap V=\varnothing$, a contradiction. Hence $x=y$.

**Examples:**
- In any metric space (hence Hausdorff), sequences cannot converge to two different points.
- In a non-Hausdorff space, a sequence can have multiple limits; for instance, in an indiscrete topology on a set with at least two points, every sequence converges to every point.
