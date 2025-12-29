---
title: "Uniform continuity"
description: "Continuity with a single δ(ε) working uniformly for all points in the domain."
---

Let $(X,d_X)$ and $(Y,d_Y)$ be metric spaces, let $E\subseteq X$, and let $f:E\to Y$. The function $f$ is **uniformly continuous on $E$** if
$$\forall \varepsilon>0,\ \exists \delta>0\ \text{such that}\ \forall x,y\in E,\ \bigl(d_X(x,y)<\delta \Rightarrow d_Y(f(x),f(y))<\varepsilon\bigr).$$

Uniform continuity strengthens pointwise continuity by requiring that the same $\delta$ works everywhere on $E$. It is essential for interchanging limits and integrals and for extension theorems; continuous functions on compact sets are uniformly continuous.

**Examples:**
- $f(x)=x^2$ is not uniformly continuous on $\mathbb{R}$, but it is uniformly continuous on every bounded interval $[a,b]$.
- $f(x)=x$ is uniformly continuous on $\mathbb{R}$.
- $f(x)=1/x$ is uniformly continuous on $[1,\infty)$ but not on $(0,1)$.
