---
title: "Lipschitz continuity"
description: "A strong form of continuity where distances in the image are bounded by a constant times distances in the domain."
---

A **Lipschitz continuous map** between metric spaces $(X,d_X)$ and $(Y,d_Y)$ is a map $f\colon X\to Y$ for which there exists a constant $L\ge 0$ such that for all $x,y\in X$,
\[
d_Y\bigl(f(x),f(y)\bigr)\le L\,d_X(x,y).
\]

Lipschitz continuity is a quantitative strengthening of {{< knowl id="uniformly-continuous-map" text="uniform continuity" >}}: every Lipschitz map is uniformly continuous. It also gives direct control of the size of images of sets via {{< knowl id="diameter" text="diameter" >}}.

**Examples:**
- On $\mathbb{R}$ with the usual metric, $f(x)=ax+b$ is Lipschitz with constant $L=|a|$.
- On any metric space $(X,d)$, the function $x\mapsto d(x,x_0)$ (distance to a fixed point $x_0$) is Lipschitz with constant $1$.
