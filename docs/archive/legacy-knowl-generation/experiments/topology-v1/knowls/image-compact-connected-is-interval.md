---
title: "Image of a compact connected set in the real line is an interval"
description: "A continuous real-valued function on a compact connected space has an interval as its range"
---

**Image of a compact connected set in the real line is an interval**: Let $X$ be a {{< knowl id="compact-set" text="compact set" >}} that is also {{< knowl id="connected-set" text="connected" >}}, and let $f:X\to\mathbb{R}$ be a {{< knowl id="continuous-map" text="continuous map" >}}. Then the {{< knowl id="image" text="image" >}} $f(X)$ is a compact interval in $\mathbb{R}$; in particular, there exist real numbers $m\le M$ such that
$$
f(X)=[m,M],
$$
where $m=\min f$ and $M=\max f$.

This follows by combining: {{< knowl id="continuous-image-of-compact-set-is-compact" text="continuous images of compact sets are compact" >}}, {{< knowl id="continuous-image-of-connected-set-is-connected" text="continuous images of connected sets are connected" >}}, and {{< knowl id="connected-subsets-of-r-are-intervals" text="connected subsets of the real line are intervals" >}}. Compactness also guarantees endpoints exist via {{< knowl id="continuous-attains-max-min-compact" text="attainment of maxima and minima on compact sets" >}}.

**Proof sketch** *(optional)*: Since $X$ is compact and $f$ is continuous, $f(X)$ is compact. Since $X$ is connected, $f(X)$ is connected. A compact connected subset of $\mathbb{R}$ must be a closed interval, and compactness ensures the endpoints are achieved values of $f$.

**Examples:**
- For $X=[0,1]$ and $f(x)=x^2$, the image is $[0,1]$.
- Let $X$ be the unit circle in $\mathbb{R}^2$ and $f(x,y)=x$. Then $f(X)=[-1,1]$.
