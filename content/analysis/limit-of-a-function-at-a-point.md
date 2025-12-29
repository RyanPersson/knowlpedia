---
title: "Limit of a function at a point"
description: "The value L that f(x) approaches as x approaches x0, defined by an ε–δ condition."
---

Let $(X,d_X)$ and $(Y,d_Y)$ be {{< knowl id="metric-space" text="metric spaces" >}}, let $E\subseteq X$, let $x_0\in X$ be a {{< knowl id="limit-point-accumulation-point-cluster-point" text="limit point" >}} of $E$ (meaning every {{< knowl id="neighborhood" text="neighborhood" >}} of $x_0$ meets $E\setminus\{x_0\}$), and let $f:E\to Y$. We say that **$f(x)$ tends to $L\in Y$ as $x\to x_0$**, written
$$\lim_{x\to x_0} f(x)=L,$$
if
$$\forall \varepsilon>0,\ \exists \delta>0\ \text{such that}\ \forall x\in E,\ \bigl(0<d_X(x,x_0)<\delta \Rightarrow d_Y(f(x),L)<\varepsilon\bigr).$$

This definition captures the local behavior of $f$ near $x_0$ independent of the value of $f$ at $x_0$. It is the foundation for {{< knowl id="continuity-at-a-point" text="continuity" >}} and {{< knowl id="differentiability-one-variable" text="differentiation" >}}.

**Examples:**
- For $f:\mathbb{R}\setminus\{0\}\to\mathbb{R}$ given by $f(x)=\sin x/x$, one has $\lim_{x\to 0} f(x)=1$ (a standard analytic limit).
- For $f(x)=x^2$ on $\mathbb{R}$, $\lim_{x\to a} f(x)=a^2$ for every $a\in\mathbb{R}$.
- If $f(x)=1/x$ on $\mathbb{R}\setminus\{0\}$, then $\lim_{x\to 0} f(x)$ does not exist in $\mathbb{R}$.
