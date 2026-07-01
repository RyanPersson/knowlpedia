+++
id = "real-analysis/gradient"
title = "Gradient"
kind = "knowl"
summary = "Vector of first partial derivatives of a scalar function"
aliases = ["gradient"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/gradient.md"
+++

A **gradient** of a differentiable function $f:U\to \mathbb{R}$ (with $U\subseteq \mathbb{R}^n$) at a point $a\in U$ is the vector
$$
\nabla f(a)=\left(\frac{\partial f}{\partial x_1}(a),\dots,\frac{\partial f}{\partial x_n}(a)\right),
$$

formed from the [[real-analysis/partial-derivative|partial derivatives]] of $f$.

With respect to the standard [[linear-algebra/inner-product|inner product]] on $\mathbb{R}^n$, the gradient encodes [[real-analysis/directional-derivative|directional derivatives]] via $D_v f(a)=\nabla f(a)\cdot v$ whenever $f$ is [[real-analysis/differentiable-map|differentiable]] at $a$. Points where $\nabla f(a)=0$ are [[real-analysis/critical-point|critical points]].

**Examples:**
- If $f(x,y)=x^2+y^2$, then $\nabla f(x,y)=(2x,2y)$.
- If $f(x,y,z)=x e^{yz}$, then $\nabla f(x,y,z)=\big(e^{yz},\,xze^{yz},\,xye^{yz}\big)$.
