---
title: "Isometry"
description: "A map between metric spaces that preserves all distances."
---

An **isometry** between metric spaces $(X,d_X)$ and $(Y,d_Y)$ is a map $f:X\to Y$ such that for all $x,x'\in X$,
\[
d_Y(f(x),f(x'))=d_X(x,x').
\]

An isometry preserves {{{< knowl id="open-ball" text="open balls" >}}} (hence is continuous for the {{{< knowl id="metric-induced-topology" text="metric-induced topology" >}}}), and is automatically {{{< knowl id="uniformly-continuous-map" text="uniformly continuous" >}}}. If an isometry is bijective, it is a {{{< knowl id="homeomorphism" section="topology-core" text="homeomorphism" >}}}.

**Examples:**
- For any fixed $a\in\mathbb{R}^n$, the translation $x\mapsto x+a$ is an isometry of $\mathbb{R}^n$ with the Euclidean metric.
