---
title: "Metric sphere"
description: "The set of points at exactly a fixed distance from a given center point in a metric space."
---

A **metric sphere** in a metric space $(X,d)$ is a set of the form
\[
S_d(x,r)=\{y\in X : d(x,y)=r\},
\]
where $x\in X$ and $r\ge 0$.

A sphere can be written as $\overline{B}_d(x,r)\setminus B_d(x,r)$, so it sits between the {{< knowl id="open-ball" text="open ball" >}} and {{< knowl id="closed-ball" text="closed ball" >}} of the same radius.

**Examples:**
- In $\mathbb{R}^n$ with the Euclidean metric, $S(x,r)$ is the usual sphere of radius $r$ centered at $x$.
- In $(\mathbb{R},|\cdot|)$, $S(x,r)=\{x-r,x+r\}$ for $r>0$, and $S(x,0)=\{x\}$.
