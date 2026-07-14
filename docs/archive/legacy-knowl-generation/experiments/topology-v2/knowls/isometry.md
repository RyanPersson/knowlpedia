---
title: "Isometry"
description: "A distance-preserving map between metric spaces"
---

An **isometry** between {{< knowl id="metric-space" text="metric spaces" >}} $(X,d_X)$ and $(Y,d_Y)$ is a {{< knowl id="function" section="shared-foundations" text="function" >}} $f:X\to Y$ such that
\[
d_Y\bigl(f(x),f(y)\bigr)=d_X(x,y)\quad\text{for all }x,y\in X.
\]

An isometry is automatically {{< knowl id="uniformly-continuous-map" text="uniformly continuous" >}}. If an isometry is {{< knowl id="bijective-function" section="shared-foundations" text="bijective" >}}, then it is a {{< knowl id="homeomorphism" section="topology-core" text="homeomorphism" >}} between the metric-induced topologies.

**Examples:**
- The translation $f(x)=x+a$ and reflection $f(x)=-x$ are isometries of $(\mathbb{R},|x-y|)$.
- Rotations of $\mathbb{R}^n$ about the origin are isometries for the Euclidean metric.
- If $A\subseteq X$ is given the restricted metric, then the inclusion map $A\hookrightarrow X$ is an isometry onto its image.
