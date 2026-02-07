---
title: "Regular point and critical point"
description: "Points where the derivative of a map has maximal rank, versus points where it fails to"
---

Let $U\subseteq \mathbb{R}^n$ be open and let $f:U\to \mathbb{R}^m$ be {{< knowl id="differentiable-map" text="differentiable" >}}.

A point $a\in U$ is a **regular point** of $f$ if the derivative ({{< knowl id="jacobian-matrix" text="Jacobian" >}}) $Df(a):\mathbb{R}^n\to\mathbb{R}^m$ has rank $m$ (equivalently, $Df(a)$ is surjective).
A point $a\in U$ is a **critical point** of $f$ if $\operatorname{rank} Df(a) < m$.

Regular points are where $f$ behaves locally like a projection (after smooth changes of coordinates). Critical points are where local geometry can "pinch" or change dimension; they govern where the implicit function theorem can fail.

**Examples:**
- If $f:\mathbb{R}^2\to\mathbb{R}$ is given by $f(x,y)=x^2+y^2$, then $(0,0)$ is a critical point since $\nabla f(0,0)=(0,0)$, while any $(x,y)\neq (0,0)$ is regular.
- If $f:\mathbb{R}^2\to\mathbb{R}^2$ is $f(x,y)=(x,y)$, then every point is regular since $Df(a)=I$ has rank $2$.
- For $f:\mathbb{R}\to\mathbb{R}$, a point $a$ is critical exactly when $f'(a)=0$.
