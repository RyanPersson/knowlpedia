---
title: "Equivalent metrics"
description: "Two metrics that determine the same notion of openness."
---

Two metrics $d$ and $d'$ on the same set $X$ are **equivalent** if they induce the same collection of open sets, i.e. if they define the same {{< knowl id="metric-induced-topology" text="metric-induced topology" >}} on $X$.

Equivalently, the {{< knowl id="identity-function" text="identity map" >}} $\mathrm{id}_X$ is a {{< knowl id="homeomorphism" text="homeomorphism" >}} from $(X,d)$ to $(X,d')$.

**Examples:**
- If $d$ is any metric, then $d'(x,y)=\min\{1,d(x,y)\}$ is equivalent to $d$.
- If $d$ is any metric, then $d''(x,y)=\dfrac{d(x,y)}{1+d(x,y)}$ is equivalent to $d$.
