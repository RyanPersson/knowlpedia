---
title: "Hölder continuity"
description: "A continuity condition controlled by a power of the distance"
---

A map $f:(X,d_X)\to(Y,d_Y)$ between {{< knowl id="metric-space" text="metric spaces" >}} is **Hölder continuous** with exponent $\alpha\in(0,1]$ if there exists $C\ge 0$ such that
\[
d_Y\bigl(f(x),f(y)\bigr)\le C\,d_X(x,y)^{\alpha}\quad\text{for all }x,y\in X.
\]

The case $\alpha=1$ is exactly {{< knowl id="lipschitz-continuity" text="Lipschitz continuity" >}}. Any Hölder map is {{< knowl id="uniformly-continuous-map" text="uniformly continuous" >}}.

**Examples:**
- On $[0,1]$, $f(x)=\sqrt{x}$ is Hölder with exponent $1/2$ (one can take $C=1$).
- For $\alpha\in(0,1)$, the function $f(x)=x^{\alpha}$ on $[0,1]$ is Hölder with exponent $\alpha$.
