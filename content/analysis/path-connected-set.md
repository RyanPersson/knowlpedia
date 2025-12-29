---
title: "Path-connected set"
description: "A set in which any two points can be joined by a continuous path."
---

Let $(X,d)$ be a metric space and let $E\subseteq X$. The set $E$ is **path-connected** if for every $x,y\in E$ there exists a path $\gamma:[0,1]\to E$ such that
$$\gamma(0)=x\quad\text{and}\quad \gamma(1)=y.$$

Path-connectedness implies connectedness in metric spaces (and more generally in topological spaces). In Euclidean spaces, many natural sets are path-connected by explicit paths.

**Examples:**
- Any interval in $\mathbb{R}$ is path-connected via linear interpolation.
- Any convex subset $C\subseteq\mathbb{R}^k$ is path-connected: use $\gamma(t)=(1-t)x+ty$.
- The set $\mathbb{R}^2\setminus\{0\}$ is path-connected (e.g., connect points by polygonal paths avoiding $0$).
