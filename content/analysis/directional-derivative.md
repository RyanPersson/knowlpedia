---
title: "Directional derivative"
description: "The derivative of f at a along a direction v, defined by a one-variable limit."
---

Let $U\subseteq\mathbb{R}^k$ be open, let $f:U\to\mathbb{R}^m$, let $a\in U$, and let $v\in\mathbb{R}^k$. The **directional derivative** of $f$ at $a$ in the direction $v$ is
$$
D_v f(a) := \lim_{h\to 0}\frac{f(a+hv)-f(a)}{h},
$$
provided the limit exists in $\mathbb{R}^m$.

Directional derivatives generalize partial derivatives: taking $v=e_j$ (the $j$th standard basis vector) gives $D_{e_j}f(a)=\frac{\partial f}{\partial x_j}(a)$ (componentwise). Existence of all directional derivatives still does not, by itself, imply differentiability.

**Examples:**
- If $f(x)=\langle c,x\rangle$ is linear (with $c\in\mathbb{R}^k$), then $D_v f(a)=\langle c,v\rangle$, independent of $a$.
- If $f(x,y)=x^2+y^2$, then $D_v f(a)=2\langle a,v\rangle$ for $a\in\mathbb{R}^2$.
- For non-smooth functions, directional derivatives may exist in some directions but not others.
