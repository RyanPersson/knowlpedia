---
title: "Equicontinuous family"
description: "A family of functions sharing a common continuity modulus at each point"
---

Let $(X,d_X)$ and $(Y,d_Y)$ be {{< knowl id="metric-space" text="metric spaces" >}}, and let $\mathcal{F}$ be a family of functions $f:X\to Y$.

The family $\mathcal{F}$ is **equicontinuous at $x_0\in X$** if
$
\forall \varepsilon>0\ \exists \delta>0\ \forall f\in\mathcal{F}\ \forall x\in X:\
d_X(x,x_0)<\delta \implies d_Y\bigl(f(x),f(x_0)\bigr)<\varepsilon.
$
The family $\mathcal{F}$ is **equicontinuous on $X$** if it is equicontinuous at every $x_0\in X$ (with $\delta$ allowed to depend on $x_0$ and $\varepsilon$, but not on $f$).

Equicontinuity is stronger than "each $f$ is {{< knowl id="continuity-at-a-point" text="continuous" >}}": it requires a uniform (in $f$) control of how values change near each point. It is a key hypothesis in the {{< knowl id="arzela-ascoli-theorem" text="Arzelà–Ascoli theorem" >}}.

**Examples:**
- If every $f\in\mathcal{F}$ is {{< knowl id="lipschitz-function" text="Lipschitz" >}} with a common Lipschitz constant $L$ (i.e., $d_Y(f(x),f(y))\le L d_X(x,y)$ for all $f$), then $\mathcal{F}$ is equicontinuous.
- On $[0,2\pi]$, the family $\{x\mapsto \sin(nx)\}_{n\in\mathbb{N}}$ is not equicontinuous: oscillations become arbitrarily rapid as $n\to\infty$.
