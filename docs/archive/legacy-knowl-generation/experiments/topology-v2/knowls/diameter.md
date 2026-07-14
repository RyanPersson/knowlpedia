---
title: "Diameter"
description: "The supremum of distances between pairs of points in a subset"
---

The **diameter** of a subset $A$ of a {{< knowl id="metric-space" text="metric space" >}} $(X,d)$ is
\[
\operatorname{diam}(A)=\sup\{d(x,y): x,y\in A\}\in[0,\infty],
\]
with the convention $\operatorname{diam}(\varnothing)=0$.

A set is {{< knowl id="bounded-set" text="bounded" >}} if and only if it has finite diameter (for nonempty sets).

**Examples:**
- In $\mathbb{R}$ with $d(x,y)=|x-y|$, $\operatorname{diam}([0,1])=1$.
- Any singleton set has diameter $0$.
- In any metric space, $\operatorname{diam}(B_d(x,r))\le 2r$ for an {{< knowl id="open-ball" text="open ball" >}}.
