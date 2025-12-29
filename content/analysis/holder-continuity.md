---
title: "Hölder continuity"
description: "A quantitative continuity condition d(f(x),f(y)) ≤ C d(x,y)^α for some α∈(0,1]."
---

Let $(X,d_X)$ and $(Y,d_Y)$ be metric spaces and let $f:E\to Y$ with $E\subseteq X$. The function $f$ is **Hölder continuous** on $E$ with exponent $\alpha\in(0,1]$ if there exists a constant $C\ge 0$ such that
$$\forall x,y\in E,\quad d_Y\!\bigl(f(x),f(y)\bigr)\le C\, d_X(x,y)^{\alpha}.$$
Any such $C$ is called a **Hölder constant** for $(f,\alpha)$ on $E$.

Hölder continuity interpolates between plain uniform continuity and Lipschitz continuity: the case $\alpha=1$ is Lipschitz continuity. Hölder estimates are common in approximation and regularity theory (e.g., controlling oscillation on small scales).

**Examples:**
- If $f$ is Lipschitz on $E$ with constant $L$, then $f$ is Hölder on $E$ for every $\alpha\in(0,1]$ with constant $C=L\cdot(\operatorname{diam}(E))^{1-\alpha}$ (when $\operatorname{diam}(E)<\infty$).
- On $[0,1]$, the function $f(x)=\sqrt{x}$ is Hölder with exponent $\alpha=\tfrac12$ (one can show $|\sqrt{x}-\sqrt{y}|\le \sqrt{|x-y|}$).
- The function $f(x)=x$ on $\mathbb{R}$ is Hölder for every $\alpha\in(0,1]$ (take $C=1$ for $\alpha=1$, and adjust constants for $\alpha<1$ on bounded sets).
