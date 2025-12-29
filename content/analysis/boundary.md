---
title: "Boundary"
description: "The set of points where every neighborhood meets both the set and its complement."
---

Let $(X,d)$ be a {{< knowl id="metric-space" text="metric space" >}} and let $A\subseteq X$. The **boundary** of $A$, denoted $\partial A$, is
$$\partial A := \overline{A}\setminus \operatorname{int}(A).$$
Equivalently,
$$\partial A = \overline{A}\cap \overline{X\setminus A}$$
(see {{< knowl id="closure" text="closure" >}} and {{< knowl id="interior" text="interior" >}}). Equivalently again, $x\in\partial A$ iff every {{< knowl id="open-ball" text="open ball" >}} $B(x,r)$ meets both $A$ and $X\setminus A$.

Boundaries isolate the "edge" of a set and play a key role in topology and analysis (e.g., in describing discontinuity sets and in integration theory).

**Examples:**
- In $\mathbb{R}$, $\partial(0,1)=\{0,1\}$.
- In $\mathbb{R}^2$, the boundary of the open unit disk $B(0,1)$ is the unit circle $S(0,1)$.
- If $A=\mathbb{Q}\subseteq\mathbb{R}$, then $\partial A=\mathbb{R}$ (every interval meets both $\mathbb{Q}$ and $\mathbb{R}\setminus\mathbb{Q}$).
