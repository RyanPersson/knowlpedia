---
title: "Open balls are open"
description: "In any metric space, every open ball is an open set"
---

**Proposition.**
In any {{< knowl id="metric-metric-space" text="metric space" >}}, every open ball $B(x_0;r)$ is an {{< knowl id="open-subset" text="open set" >}}.

**Proof sketch.** Fix $a\in B(x_0;r)$. Let $\delta:=r-d(a,x_0)>0$. If $d(x,a)<\delta$, then by the triangle inequality
$$
d(x,x_0)\le d(x,a)+d(a,x_0)<\delta+d(a,x_0)=r,
$$

so $x\in B(x_0;r)$. Hence $B(a;\delta)\subset B(x_0;r)$, which is exactly openness.
