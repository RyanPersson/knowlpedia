---
title: "Diameter"
description: "The supremum of distances between pairs of points in a set."
---

Let $(X,d)$ be a {{< knowl id="metric-space" text="metric space" >}} and let $A\subseteq X$. The **diameter** of $A$ is
$$
\operatorname{diam}(A)=\sup\{d(x,y): x,y\in A\}.
$$
(One common convention is $\operatorname{diam}(\varnothing)=0$.)

A set has finite diameter exactly when it is {{< knowl id="bounded-set" text="bounded" >}}. Diameters also play a key role in the {{< knowl id="cantor-intersection-theorem" text="Cantor intersection theorem" >}}.

**Examples:**
- In $\mathbb{R}$ with the usual metric, the diameter of $[0,1]$ is $1$.
- In the discrete metric on a nonempty set, any subset with at least two points has diameter $1$.
