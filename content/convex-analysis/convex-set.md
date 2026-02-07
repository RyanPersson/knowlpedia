---
title: "Convex set"
description: "A set is convex if it contains the line segment between any two of its points"
---

Let $X$ be a {{< knowl id="vector-space" section="linear-algebra" section="linear-algebra" text="vector space" >}} (typically over $\mathbb{R}$). A set $\Omega\subset X$ is **convex** if for all $x,y\in\Omega$ and all $\lambda\in[0,1]$ we have
$$
\lambda x+(1-\lambda)y\in \Omega.
$$

**Context.** Equivalently, $\Omega$ is convex iff it contains every {{< knowl id="line-segments-in-a-vector-space" text="line segment" >}} joining any two of its points. Convexity is the core geometric notion underlying convex analysis and optimization.

**Examples:**
- Any affine subspace of $\mathbb{R}^n$ (e.g., a line or plane) is convex.
- Any ball $\{x:\|x-x_0\|\le r\}$ in a normed space is convex.
- A halfspace $\{x\in\mathbb{R}^n:\langle a,x\rangle\le b\}$ is convex.

**Non-example.**
- The annulus $\{x\in\mathbb{R}^2:1<\|x\|<2\}$ is not convex: a segment between two points may pass through the "hole."
