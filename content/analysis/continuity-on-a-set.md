---
title: "Continuity on a set"
description: "A function is continuous on E if it is continuous at every point of E."
---

Let $(X,d_X)$ and $(Y,d_Y)$ be metric spaces, let $E\subseteq X$, and let $f:E\to Y$. The function $f$ is **continuous on $E$** if it is continuous at every point of $E$, i.e.
$$\forall x_0\in E,\ \forall \varepsilon>0,\ \exists \delta>0\ \text{such that}\ \forall x\in E,\ \bigl(d_X(x,x_0)<\delta \Rightarrow d_Y(f(x),f(x_0))<\varepsilon\bigr).$$

Continuity "on a set" is the standard notion for stating global theorems (e.g., continuous images of compact sets are compact).

**Examples:**
- $f(x)=\sin x$ is continuous on $\mathbb{R}$.
- $f(x)=1/x$ is continuous on $(0,\infty)$ and on $(-\infty,0)$, but not continuous on $\mathbb{R}$ as a whole since $0$ is not in its domain.
- The function $f(x)=\sqrt{x}$ is continuous on $[0,\infty)$.
