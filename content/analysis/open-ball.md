---
title: "Open ball"
description: "The set of points within distance < r of a center point in a metric space."
---

Let $(X,d)$ be a metric space, let $x\in X$, and let $r>0$. The **open ball** of radius $r$ centered at $x$ is
$$B(x,r):=\{y\in X : d(x,y)<r\}.$$

Open balls are the basic building blocks of the topology induced by a metric: open sets are exactly those that contain an open ball around each of their points.

**Examples:**
- In $\mathbb{R}$ with $d(x,y)=|x-y|$, $B(a,r)=(a-r,a+r)$.
- In $\mathbb{R}^2$ with Euclidean distance, $B(0,1)$ is the open unit disk.
- In a discrete metric space, $B(x,1)=\{x\}$ for every $x$.
