---
title: "Differentiable map"
description: "Differentiability for maps between Euclidean spaces via a best linear approximation"
---

A **differentiable map** at a point $a$ is a map $f:U\to \mathbb{R}^m$ (with $U\subseteq \mathbb{R}^n$) for which there exists a linear map $L:\mathbb{R}^n\to \mathbb{R}^m$ such that
$$
\lim_{h\to 0}\frac{\|f(a+h)-f(a)-Lh\|}{\|h\|}=0,
$$

where $\|\cdot\|$ is the {{< knowl id="euclidean-norm" section="linear-algebra" text="Euclidean norm" >}}.

In this case $L$ is the {{< knowl id="frechet-derivative" text="Fréchet derivative" >}} of $f$ at $a$, and (when it exists) it is represented in coordinates by the {{< knowl id="jacobian-matrix" text="Jacobian matrix" >}}. Maps that are differentiable at every point of their domain are the basic objects of multivariable {{< knowl id="differentiability-1d" text="differentiability" >}} in higher dimensions, and higher smoothness is recorded by {{< knowl id="class-ck-map" text="C^k maps" >}}.

**Examples:**
- Any affine map $f(x)=Ax+b$ (with $A$ an $m\times n$ matrix) is differentiable everywhere, with derivative $L(h)=Ah$.
- The map $f:\mathbb{R}^2\to \mathbb{R}^3$ given by $f(x,y)=(x^2,xy,\sin y)$ is differentiable everywhere.
