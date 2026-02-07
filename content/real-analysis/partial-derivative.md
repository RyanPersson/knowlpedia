---
title: "Partial derivative"
description: "Derivative of a multivariable function with respect to one coordinate"
---

A **partial derivative** of a map $f:U\to \mathbb{R}^m$ (with $U\subseteq \mathbb{R}^n$) at $a=(a_1,\dots,a_n)\in U$ with respect to the $j$th coordinate is the limit
$$
\frac{\partial f}{\partial x_j}(a)
=\lim_{t\to 0}\frac{f(a_1,\dots,a_j+t,\dots,a_n)-f(a_1,\dots,a_n)}{t},
$$

when it exists (for vector-valued $f$, this limit is taken in $\mathbb{R}^m$).

Partial derivatives are one-coordinate versions of the {{< knowl id="limit-at-a-point" text="limit at a point" >}} and are the entries used to build the {{< knowl id="jacobian-matrix" text="Jacobian matrix" >}}. Existence of all partial derivatives at $a$ does not by itself guarantee that $f$ is a {{< knowl id="differentiable-map" text="differentiable map" >}} at $a$.

**Examples:**
- For $f(x,y)=x^2y$, one has $\frac{\partial f}{\partial x}(x,y)=2xy$ and $\frac{\partial f}{\partial y}(x,y)=x^2$.
- For $f(x,y)=|x|$, the partial derivative $\frac{\partial f}{\partial x}(0,y)$ does not exist (for any $y$), since the corresponding one-variable derivative at $0$ fails to exist.
