---
title: "Isometry"
description: "A distance-preserving map between metric spaces."
---

Let $(X,d_X)$ and $(Y,d_Y)$ be metric spaces. An **isometry** is a {{< knowl id="function" text="function" >}} $f:X\to Y$ such that for all $x,x'\in X$,
$$
d_Y(f(x),f(x')) = d_X(x,x').
$$

An isometry between {{< knowl id="metric-space" text="metric spaces" >}} is automatically {{< knowl id="injective-function" text="injective" >}} and {{< knowl id="uniformly-continuous-map" text="uniformly continuous" >}}.

**Examples:**
- In Euclidean space, translations and rotations are isometries.
- The inclusion of a subset $A\subseteq X$ into $X$ is an isometry when $A$ is given the restricted metric.
