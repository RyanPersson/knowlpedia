---
title: "Holder continuity"
description: "A regularity condition stronger than continuity, measured by a power law."
---

Let $(X,d_X)$ and $(Y,d_Y)$ be metric spaces. A map $f:X\to Y$ is **Hölder continuous** if there exist constants $C>0$ and $\alpha\in(0,1]$ such that for all $x,y\in X$,
$$
d_Y(f(x),f(y)) \le C\, d_X(x,y)^\alpha.
$$

Hölder continuity implies {{< knowl id="uniformly-continuous-map" text="uniform continuity" >}}. When $\alpha=1$, this reduces to {{< knowl id="lipschitz-continuity" text="Lipschitz continuity" >}}.

**Examples:**
- On $[0,1]\subseteq\mathbb{R}$, the map $f(x)=\sqrt{x}$ is Hölder continuous with exponent $\alpha=1/2$.
- Any Lipschitz map is Hölder continuous (take $\alpha=1$).
