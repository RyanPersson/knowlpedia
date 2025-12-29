---
title: "Lipschitz continuity"
description: "A quantitative continuity condition: |f(x)-f(y)| ≤ L|x-y| for some constant L."
---

Let $(X,d_X)$ and $(Y,d_Y)$ be {{< knowl id="metric-space" text="metric spaces" >}} and let $f:E\to Y$ with $E\subseteq X$. The function $f$ is **Lipschitz continuous** on $E$ if there exists a constant $L\in[0,\infty)$ such that
$$\forall x,y\in E,\ d_Y\!\bigl(f(x),f(y)\bigr)\le L\, d_X(x,y).$$
Any such $L$ is called a **Lipschitz constant** for $f$ on $E$.

Lipschitz continuity is stronger than {{< knowl id="uniform-continuity" text="uniform continuity" >}} and provides explicit control of error propagation. It is ubiquitous in analysis and differential equations.

**Examples:**
- $f:\mathbb{R}\to\mathbb{R}$, $f(x)=ax+b$ is Lipschitz with constant $L=|a|$.
- On $\mathbb{R}$, the function $f(x)=|x|$ is Lipschitz with constant $L=1$.
- $f(x)=\sqrt{x}$ is not Lipschitz on $[0,1]$ (the slope blows up near $0$), but it is Lipschitz on $[\delta,1]$ for any fixed $\delta>0$.
