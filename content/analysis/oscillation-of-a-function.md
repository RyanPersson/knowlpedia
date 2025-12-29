---
title: "Oscillation of a function"
description: "The quantity sup f − inf f on a set, measuring variation in values."
---

Let $f:E\to\mathbb{R}$ be a bounded function and let $A\subseteq E$ be nonempty. The **oscillation** of $f$ on $A$ is
$$\operatorname{osc}(f;A):=\sup\{f(x):x\in A\}-\inf\{f(x):x\in A\}.$$

For Riemann integration, oscillation on subintervals controls the gap between upper and lower sums: on an interval $I$, the contribution to $U(f,P)-L(f,P)$ is the oscillation on $I$ times the interval length.

**Examples:**
- If $f$ is constant on $A$, then $\operatorname{osc}(f;A)=0$.
- For $f(x)=x$ on $A=[0,1]$, $\operatorname{osc}(f;A)=1-0=1$.
- For $f=\mathbf{1}_{\mathbb{Q}}$ on any nontrivial interval $I\subset\mathbb{R}$, $\operatorname{osc}(f;I)=1-0=1$.
