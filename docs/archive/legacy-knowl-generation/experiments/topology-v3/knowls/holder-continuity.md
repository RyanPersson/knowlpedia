---
title: "Hölder continuity"
description: "A continuity condition controlled by a power of distance."
---

A map $f:(X,d_X)\to(Y,d_Y)$ is **Hölder continuous** with exponent $\alpha\in(0,1]$ if there exists a constant $C\ge 0$ such that
\[
d_Y(f(x),f(y))\le C\,d_X(x,y)^\alpha\quad\text{for all }x,y\in X.
\]

When $\alpha=1$, this is exactly {{{< knowl id="lipschitz-continuity" text="Lipschitz continuity" >}}}, so Hölder continuity interpolates between mere {{{< knowl id="uniformly-continuous-map" text="uniform continuity" >}}} and Lipschitz control.

**Examples:**
- On $[0,1]\subset\mathbb{R}$ with the usual metric, $f(x)=\sqrt{x}$ is Hölder continuous with exponent $\alpha=\tfrac12$.
