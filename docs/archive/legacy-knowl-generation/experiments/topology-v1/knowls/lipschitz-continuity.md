---
title: "Lipschitz continuity"
description: "A map whose output distances are bounded by a constant times input distances."
---

Let $(X,d_X)$ and $(Y,d_Y)$ be a {{< knowl id="metric-space" text="metric spaces" >}}. A map $f:X\to Y$ is **Lipschitz continuous** if there exists a constant $L\ge 0$ such that for all $x,y\in X$,
$$
d_Y(f(x),f(y)) \le L\, d_X(x,y).
$$

Every Lipschitz map is {{< knowl id="uniformly-continuous-map" text="uniformly continuous" >}}. In normed vector spaces, bounded {{< knowl id="linear-map" text="linear maps" >}} are Lipschitz with constant given by the {{< knowl id="operator-norm" text="operator norm" >}}.

**Examples:**
- On $\mathbb{R}$, the affine map $f(x)=ax+b$ is Lipschitz with constant $|a|$.
- Any constant map is Lipschitz with constant $0$.
