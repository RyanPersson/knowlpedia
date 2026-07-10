---
title: "Interior"
description: "The largest open set contained in a given set."
---

Let $(X,\tau)$ be a topological space and let $A\subseteq X$. The **interior** of $A$, denoted $\operatorname{int}(A)$, is the largest {{< knowl id="open-set" text="open set" >}} contained in $A$; equivalently,
$$
\operatorname{int}(A)=\bigcup\{U\subseteq A : U\in \tau\}.
$$

This definition packages “points of $A$ that are not on the boundary” using only {{< knowl id="union" text="unions" >}} of open subsets. It is dual to the notion of {{< knowl id="closure" text="closure" >}} via complements.

**Examples:**
- In $\mathbb{R}$ with the usual topology, $\operatorname{int}([0,1])=(0,1)$.
- If $A$ is open, then $\operatorname{int}(A)=A$.
- $\operatorname{int}(\varnothing)=\varnothing$ and $\operatorname{int}(X)=X$.
