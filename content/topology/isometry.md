---
title: "Isometry"
description: "A distance-preserving map between metric spaces."
---

An **isometry** between metric spaces $(X,d_X)$ and $(Y,d_Y)$ is a map $f\colon X\to Y$ such that for all $x,x'\in X$,
\[
d_Y\bigl(f(x),f(x')\bigr)=d_X(x,x').
\]

An isometry preserves all metric structure (in particular, it is {{< knowl id="uniformly-continuous-map" text="uniformly continuous" >}} and even {{< knowl id="lipschitz-continuity" text="Lipschitz" >}} with constant $1$). A bijective isometry is a {{< knowl id="homeomorphism" text="homeomorphism" >}} whose inverse is also an isometry.

**Examples:**
- In $\mathbb{R}^n$ with the Euclidean metric, translations $x\mapsto x+a$ and orthogonal transformations are isometries.
- If $A\subseteq X$ is given the restricted metric, the inclusion map $A\hookrightarrow X$ is an isometry onto its image.
