---
title: "Path"
description: "A continuous map from the unit interval into a topological space connecting two points"
---

A **path** in a {{< knowl id="topological-space" section="topology-core" text="topological space" >}} $X$ is a {{< knowl id="continuous-map" section="topology-core" text="continuous map" >}} $\gamma:[0,1]\to X$. If $\gamma(0)=x$ and $\gamma(1)=y$, then $\gamma$ is a path from $x$ to $y$.

Paths are the basic objects used to define {{< knowl id="path-connected-set" text="path-connected sets" >}}. Any {{< knowl id="curve" text="curve" >}} defined on a closed interval $[a,b]$ can be reparameterized to a path by composing with an affine homeomorphism $[0,1]\to[a,b]$.

**Examples:**
- In $\mathbb{R}^n$, the line segment $\gamma(t)=(1-t)x+ty$ is a path from $x$ to $y$.
- The constant map $\gamma(t)=x_0$ is a path from $x_0$ to $x_0$.
- A loop in the circle can be given by $\gamma(t)=(\cos(2\pi t),\sin(2\pi t))$ as a path in $S^1\subseteq \mathbb{R}^2$.
