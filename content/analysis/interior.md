---
title: "Interior"
description: "The largest open set contained in a given set."
---

Let $(X,d)$ be a {{< knowl id="metric-space" text="metric space" >}} and let $A\subseteq X$. The **interior** of $A$, denoted $\operatorname{int}(A)$ (or $A^\circ$), is the set
$$\operatorname{int}(A):=\{x\in A : \exists r>0\ \text{with}\ B(x,r)\subseteq A\}$$
(see {{< knowl id="open-ball" text="open ball" >}}).

Equivalently, $\operatorname{int}(A)$ is the union of all {{< knowl id="open-set" text="open sets" >}} contained in $A$. The interior captures the points of $A$ that are not "on the edge" (compare with {{< knowl id="boundary" text="boundary" >}}).

**Examples:**
- In $\mathbb{R}$, $\operatorname{int}([0,1])=(0,1)$.
- In $\mathbb{R}^2$, the interior of the closed unit disk $\overline{B}(0,1)$ is the open unit disk $B(0,1)$.
- If $A=\mathbb{Q}\subseteq\mathbb{R}$, then $\operatorname{int}(A)=\varnothing$.
