---
title: "Gradient"
description: "Vector of first partial derivatives of a scalar function"
---

A **gradient** of a differentiable function $f:U\to \mathbb{R}$ (with $U\subseteq \mathbb{R}^n$) at a point $a\in U$ is the vector
$$
\nabla f(a)=\left(\frac{\partial f}{\partial x_1}(a),\dots,\frac{\partial f}{\partial x_n}(a)\right),
$$

formed from the {{< knowl id="partial-derivative" text="partial derivatives" >}} of $f$.

With respect to the standard {{< knowl id="inner-product" section="linear-algebra" text="inner product" >}} on $\mathbb{R}^n$, the gradient encodes {{< knowl id="directional-derivative" text="directional derivatives" >}} via $D_v f(a)=\nabla f(a)\cdot v$ whenever $f$ is {{< knowl id="differentiable-map" text="differentiable" >}} at $a$. Points where $\nabla f(a)=0$ are {{< knowl id="critical-point" text="critical points" >}}.

**Examples:**
- If $f(x,y)=x^2+y^2$, then $\nabla f(x,y)=(2x,2y)$.
- If $f(x,y,z)=x e^{yz}$, then $\nabla f(x,y,z)=\big(e^{yz},\,xze^{yz},\,xye^{yz}\big)$.
