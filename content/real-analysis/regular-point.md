---
title: "Regular point"
description: "A point where a differentiable map has maximal rank or a surjective derivative"
---

A **regular point** of a differentiable map $F:U\to \mathbb{R}^m$ (with $U\subseteq \mathbb{R}^n$ and $m\le n$) is a point $a\in U$ such that the {{< knowl id="frechet-derivative" text="Fréchet derivative" >}} $DF(a):\mathbb{R}^n\to \mathbb{R}^m$ is surjective.

Equivalently, the {{< knowl id="jacobian-matrix" text="Jacobian matrix" >}} $JF(a)$ has rank $m$ (full row rank). Regular points are the local nondegeneracy condition used in the {{< knowl id="implicit-function-theorem" text="implicit function theorem" >}} and in the definition of a {{< knowl id="regular-value" text="regular value" section="fiber-bundles">}}.

**Examples:**
- For $F(x,y)=x^2+y^2$ (a map $\mathbb{R}^2\to\mathbb{R}$), every point $(x,y)\ne(0,0)$ is regular, since the gradient $(2x,2y)$ is nonzero.
- For $F(x,y)=(x^2,y^2)$ (a map $\mathbb{R}^2\to\mathbb{R}^2$), the point $(1,1)$ is regular, while $(0,1)$ is not regular because the Jacobian has rank $1$ there.
