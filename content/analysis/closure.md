---
title: "Closure"
description: "The smallest closed set containing a given set, equivalently points arbitrarily close to it."
---

Let $(X,d)$ be a metric space and let $A\subseteq X$. The **closure** of $A$, denoted $\overline{A}$ (or $\operatorname{cl}(A)$), is the set
$$
\overline{A}:=\{x\in X : \forall r>0,\ B(x,r)\cap A\neq\varnothing\}.
$$
Equivalently, $\overline{A}$ is the intersection of all closed sets that contain $A$.

The closure adds to $A$ all points that can be approximated arbitrarily well by points of $A$. It is fundamental for density, limit points, and topological convergence.

**Examples:**
- In $\mathbb{R}$, $\overline{(0,1)}=[0,1]$.
- In $\mathbb{R}$, $\overline{\mathbb{Q}}=\mathbb{R}$ (rationals are dense).
- If $A$ is closed, then $\overline{A}=A$.
