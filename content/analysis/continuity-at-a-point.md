---
title: "Continuity at a point"
description: "A function is continuous at x0 if f(x)→f(x0) as x→x0."
---

Let $(X,d_X)$ and $(Y,d_Y)$ be {{< knowl id="metric-space" text="metric spaces" >}}, let $E\subseteq X$, and let $f:E\to Y$. The function $f$ is **continuous at a point** $x_0\in E$ if
$$\forall \varepsilon>0,\ \exists \delta>0\ \text{such that}\ \forall x\in E,\ \bigl(d_X(x,x_0)<\delta \Rightarrow d_Y(f(x),f(x_0))<\varepsilon\bigr).$$
Equivalently, $f$ is continuous at $x_0$ iff $\lim_{x\to x_0} f(x)=f(x_0)$ (see {{< knowl id="limit-of-a-function-at-a-point" text="limit of a function" >}}).

Continuity means that small changes in input near $x_0$ produce small changes in output. It is the basic regularity notion in analysis.

**Examples:**
- $f(x)=x^2$ is continuous at every $x_0\in\mathbb{R}$.
- The indicator function $\mathbf{1}_{\mathbb{Q}}:\mathbb{R}\to\mathbb{R}$ is discontinuous at every point.
- The step function $\mathbf{1}_{[0,\infty)}$ is discontinuous at $0$ but continuous at every $x_0\ne 0$.
