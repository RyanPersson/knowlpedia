---
title: "Gradient"
description: "The vector of first partial derivatives ∇f of a scalar-valued function."
---

Let $U\subseteq\mathbb{R}^k$ be open and let $f:U\to\mathbb{R}$ be differentiable (at least with existing partial derivatives) at $a\in U$. The **gradient** of $f$ at $a$ is the vector
$$
\nabla f(a) := \left(\frac{\partial f}{\partial x_1}(a),\dots,\frac{\partial f}{\partial x_k}(a)\right)\in\mathbb{R}^k.
$$

When $f$ is differentiable at $a$, $\nabla f(a)$ represents the linear functional "best approximating" changes in $f$ near $a$, via
$$f(a+h)\approx f(a)+\langle \nabla f(a),h\rangle.$$
The gradient points in the direction of steepest increase.

**Examples:**
- If $f(x,y)=x^2+y^2$, then $\nabla f(x,y)=(2x,2y)$.
- If $f(x)=\langle c,x\rangle$, then $\nabla f(x)=c$ (constant).
- If $f$ has a local extremum at an interior point and is differentiable there, then $\nabla f(a)=0$ (a necessary condition).
