---
title: "Uniformly continuous map"
description: "A map whose continuity can be controlled uniformly over the whole domain."
---

Let $(X,d_X)$ and $(Y,d_Y)$ be {{< knowl id="metric-space" text="metric spaces" >}}. A map $f:X\to Y$ is **uniformly continuous** if for every $\varepsilon>0$ there exists $\delta>0$ such that for all $x,y\in X$,
$$
d_X(x,y)<\delta \implies d_Y(f(x),f(y))<\varepsilon.
$$

Uniform continuity implies ordinary {{< knowl id="continuous-map" text="continuity" >}} and, unlike pointwise continuity, it preserves Cauchy behavior: it sends {{< knowl id="cauchy-sequence" text="Cauchy sequences" >}} to Cauchy sequences. A standard sufficient condition is {{< knowl id="lipschitz-continuity" text="Lipschitz continuity" >}}.

**Examples:**
- Any isometry is uniformly continuous.
- On $\mathbb{R}$ with the usual metric, $f(x)=x^2$ is continuous but not uniformly continuous.
