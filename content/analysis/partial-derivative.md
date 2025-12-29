---
title: "Partial derivative"
description: "The derivative with respect to one coordinate of a function f:ℝ^k→ℝ^m."
---

Let $U\subseteq\mathbb{R}^k$ be {{< knowl id="open-set" text="open" >}}, let $f:U\to\mathbb{R}$ be a scalar-valued function, and let $a=(a_1,\dots,a_k)\in U$. The **partial derivative of $f$ with respect to the $j$th variable at $a$** is
$$
\frac{\partial f}{\partial x_j}(a)
:=\lim_{h\to 0}\frac{f(a_1,\dots,a_j+h,\dots,a_k)-f(a_1,\dots,a_j,\dots,a_k)}{h},
$$
provided the {{< knowl id="limit-of-a-function-at-a-point" text="limit" >}} exists.

Partial derivatives measure the sensitivity of $f$ to changes in a single coordinate direction while holding all other coordinates fixed. Existence of partial derivatives alone does not imply {{< knowl id="differentiable-map" text="differentiability" >}} of $f$ as a multivariable map.

**Examples:**
- If $f(x,y)=x^2y$, then $\frac{\partial f}{\partial x}(x,y)=2xy$ and $\frac{\partial f}{\partial y}(x,y)=x^2$.
- If $f(x,y)=x+y$, then both partial derivatives are constantly $1$.
- There exist functions with all partial derivatives at a point but not continuous or not differentiable there (standard pathology examples).
