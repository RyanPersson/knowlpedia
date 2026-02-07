---
title: "Hölder continuity"
description: "A condition controlling how fast a function can change, generalizing Lipschitz continuity by allowing a power less than one."
---

A **Hölder continuous map** between metric spaces $(X,d_X)$ and $(Y,d_Y)$ is a map $f\colon X\to Y$ such that there exist constants $C\ge 0$ and $\alpha\in(0,1]$ with
\[
d_Y\bigl(f(x),f(y)\bigr)\le C\,\bigl(d_X(x,y)\bigr)^{\alpha}
\quad\text{for all } x,y\in X.
\]

When $\alpha=1$, Hölder continuity is exactly {{< knowl id="lipschitz-continuity" text="Lipschitz continuity" >}}. For any $\alpha\in(0,1]$, Hölder continuity implies {{< knowl id="uniformly-continuous-map" text="uniform continuity" >}}.

**Examples:**
- The function $f(x)=\sqrt{x}$ on $[0,1]$ is Hölder continuous with exponent $\alpha=\tfrac12$.
- For $\alpha\in(0,1]$, the function $f(x)=|x|^{\alpha}$ on $\mathbb{R}$ is Hölder continuous with exponent $\alpha$.
