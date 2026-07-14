---
title: "Metric sphere"
description: "The set of points at exactly a fixed distance from a center in a metric space"
---

A **metric sphere** in a {{< knowl id="metric-space" text="metric space" >}} $(X,d)$ is a set of the form
\[
S_d(x,r)=\{y\in X : d(x,y)=r\},
\]
where $x\in X$ and $r\ge 0$.

It is the “boundary” between the {{< knowl id="open-ball" text="open ball" >}} and {{< knowl id="closed-ball" text="closed ball" >}} of radius $r$; equivalently, it is the {{< knowl id="set-difference" section="shared-foundations" text="set difference" >}} $\overline{B}_d(x,r)\setminus B_d(x,r)$.

**Examples:**
- In $(\mathbb{R},|x-y|)$ with $r>0$, $S_d(x,r)=\{x-r,\;x+r\}$.
- In $\mathbb{R}^2$ with the Euclidean metric, $S_d(x,r)$ is a circle of radius $r$.
- In the discrete metric on $X$, $S_d(x,0)=\{x\}$ and $S_d(x,1)=X\setminus\{x\}$.
