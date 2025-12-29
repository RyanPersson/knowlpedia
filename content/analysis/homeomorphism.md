---
title: "Homeomorphism"
description: "A bijection that is continuous with continuous inverse."
---

Let $(X,d_X)$ and $(Y,d_Y)$ be {{< knowl id="metric-space" text="metric spaces" >}}. A function $f:X\to Y$ is a **homeomorphism** if:
- $f$ is {{< knowl id="bijective-function" text="bijective" >}},
- $f$ is {{< knowl id="continuity-on-a-set" text="continuous" >}} on $X$, and
- $f^{-1}:Y\to X$ is continuous on $Y$.

Homeomorphisms are the isomorphisms in topology: they identify spaces that are "the same up to continuous deformation." Properties preserved by homeomorphisms are called topological invariants (e.g., {{< knowl id="compact-set" text="compactness" >}}, {{< knowl id="connected-set" text="connectedness" >}}).

**Examples:**
- $f:(0,1)\to\mathbb{R}$ given by $f(x)=\tan(\pi(x-\tfrac12))$ is a homeomorphism (continuous bijection with continuous inverse).
- Any isometry $f:X\to Y$ that is bijective is a homeomorphism.
- The map $f:[0,2\pi)\to S^1\subseteq\mathbb{R}^2$ given by $f(t)=(\cos t,\sin t)$ is continuous and surjective but not injective, hence not a homeomorphism.
