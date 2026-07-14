---
title: "Uniformly continuous map"
description: "A map between metric spaces with a single delta that works everywhere"
---

A **uniformly continuous map** between {{< knowl id="metric-space" text="metric spaces" >}} $(X,d_X)$ and $(Y,d_Y)$ is a {{< knowl id="function" section="shared-foundations" text="function" >}} $f:X\to Y$ such that for every $\varepsilon>0$ there exists $\delta>0$ with the property that whenever $d_X(x,y)<\delta$, one has $d_Y(f(x),f(y))<\varepsilon$ for all $x,y\in X$.

Uniform continuity implies {{< knowl id="continuous-map" section="topology-core" text="continuity" >}}. Every {{< knowl id="lipschitz-continuity" text="Lipschitz" >}} map is uniformly continuous, and every continuous map on a {{< knowl id="compact-set" section="topology-compactness" text="compact" >}} metric space is uniformly continuous.

**Examples:**
- The map $f(x)=x^2$ is not uniformly continuous on $\mathbb{R}$, but it is uniformly continuous on $[0,1]$.
- Any constant function is uniformly continuous.
- If $f(x)=3x$ on $\mathbb{R}$, then $f$ is uniformly continuous (in fact, Lipschitz).
