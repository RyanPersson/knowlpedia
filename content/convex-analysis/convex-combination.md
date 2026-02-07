---
title: "Convex combination"
description: "A weighted average of finitely many points with nonnegative weights summing to one"
---

Let $X$ be a real {{< knowl id="vector-space" section="linear-algebra" section="linear-algebra" text="vector space" >}}. A vector $x\in X$ is a **convex combination** of points $x_1,\dots,x_m\in X$ if there exist scalars $\lambda_1,\dots,\lambda_m\ge 0$ with
$$
\lambda_1+\cdots+\lambda_m=1
$$
such that
$$
x=\sum_{i=1}^m \lambda_i x_i.
$$

**Context.** Convex combinations describe the points obtained by repeatedly taking "weighted averages." They generate the {{< knowl id="convex-hull" text="convex hull" >}} of a set.

**Examples:**
- In $\mathbb{R}^n$, the point $\tfrac12x_1+\tfrac12x_2$ is the midpoint of $x_1$ and $x_2$.
- If $x_1,x_2,x_3\in\mathbb{R}^2$ are vertices of a triangle, then all points in the triangle are convex combinations of $x_1,x_2,x_3$.
