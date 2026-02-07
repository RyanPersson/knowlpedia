---
title: "Critical point"
description: "A point where the first derivative of a scalar function vanishes"
---

A **critical point** of a differentiable function $f:U\to \mathbb{R}$ (with $U\subseteq \mathbb{R}^n$) is a point $a\in U$ such that
$$
\nabla f(a)=0,
$$

equivalently, the {{< knowl id="frechet-derivative" text="Fréchet derivative" >}} $Df(a)$ is the zero linear map.

Critical points are candidates for {{< knowl id="local-extremum" text="local extrema" >}} but need not be extrema. Higher-order information, such as the {{< knowl id="hessian-matrix" text="Hessian matrix" >}}, is used to refine classification (see {{< knowl id="second-derivative-tests" text="second derivative tests" >}}).

**Examples:**
- For $f(x)=x^3$, the point $a=0$ is a critical point, but $0$ is not a local maximum or minimum.
- For $f(x,y)=x^2+y^2$, the point $(0,0)$ is a critical point and is a (global) minimum.
