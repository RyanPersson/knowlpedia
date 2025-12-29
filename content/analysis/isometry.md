---
title: "Isometry"
description: "A distance-preserving map between metric spaces."
---

Let $(X,d_X)$ and $(Y,d_Y)$ be {{< knowl id="metric-space" text="metric spaces" >}}. A function $f:X\to Y$ is an **isometry** if
$$\forall x_1,x_2\in X,\quad d_Y\bigl(f(x_1),f(x_2)\bigr)=d_X(x_1,x_2).$$

Isometries preserve all metric structure: {{< knowl id="convergent-sequence" text="convergence" >}}, {{< knowl id="cauchy-sequence" text="Cauchy sequences" >}}, {{< knowl id="complete-metric-space" text="completeness" >}}, and (when $f$ is {{< knowl id="bijective-function" text="bijective" >}} onto its image) the induced topology. They are the natural notion of "rigid motion" in metric spaces.

**Examples:**
- The translation $T_a:\mathbb{R}\to\mathbb{R}$ given by $T_a(x)=x+a$ is an isometry for the metric $|x-y|$.
- The rotation $R:\mathbb{R}^2\to\mathbb{R}^2$ about the origin is an isometry for Euclidean distance.
- The map $f:\mathbb{R}\to\mathbb{R}$, $f(x)=2x$, is not an isometry (it scales distances by $2$).
