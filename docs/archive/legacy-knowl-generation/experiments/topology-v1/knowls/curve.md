---
title: "Curve"
description: "A continuous map from an interval of the real line into a space"
---

A **curve** in a space $X$ is a {{< knowl id="continuous-map" text="continuous map" >}} $\gamma:I\to X$ where $I\subseteq\mathbb{R}$ is an interval (commonly $[a,b]$, $(a,b)$, or $[0,\infty)$). A curve generalizes a {{< knowl id="path" text="path" >}} by allowing the domain interval to be something other than $[0,1]$.

Because an interval is connected, the image of a curve is connected by {{< knowl id="continuous-image-of-connected-set-is-connected" text="continuous images of connected sets are connected" >}}. In many settings one also studies additional regularity (e.g., differentiability), but “curve” in topology typically only means continuity.

**Examples:**
- In {{< knowl id="euclidean-space" text="Euclidean space" >}} $\mathbb{R}^2$, $\gamma(t)=(\cos t,\sin t)$ defines a curve tracing the unit circle.
- The map $\gamma(t)=(t,t^2)$ for $t\in[-1,1]$ is a curve whose image is a parabola segment in $\mathbb{R}^2$.
