---
title: "Diameter"
description: "The supremum of all distances between pairs of points in a set within a metric space."
---

The **diameter** of a subset $A$ of a metric space $(X,d)$ is
\[
\operatorname{diam}(A)=\sup\{d(x,y): x\in A,\ y\in A\}\in[0,\infty],
\]
where $\sup$ denotes the {{< knowl id="supremum" section="real-analysis" text="supremum" >}} (and the value may be $+\infty$). By convention, $\operatorname{diam}(\varnothing)=0$.

Diameter measures the “size” of a set in a way that is tailored to the {{< knowl id="metric" text="metric" >}}; it is directly tied to the notion of a {{< knowl id="bounded-set" text="bounded set" >}}.

**Examples:**
- In $(\mathbb{R},|\cdot|)$, $\operatorname{diam}([a,b])=b-a$ for $a\le b$.
- In $\mathbb{R}^2$ with the Euclidean metric, the unit circle has diameter $2$.
