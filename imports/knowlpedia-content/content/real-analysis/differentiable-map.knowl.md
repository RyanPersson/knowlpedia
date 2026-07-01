+++
id = "real-analysis/differentiable-map"
title = "Differentiable map"
kind = "knowl"
summary = "Differentiability for maps between Euclidean spaces via a best linear approximation"
aliases = ["differentiable-map", "Differentiable map"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/differentiable-map.md"
+++

A **differentiable map** at a point $a$ is a map $f:U\to \mathbb{R}^m$ (with $U\subseteq \mathbb{R}^n$) for which there exists a linear map $L:\mathbb{R}^n\to \mathbb{R}^m$ such that
$$
\lim_{h\to 0}\frac{\|f(a+h)-f(a)-Lh\|}{\|h\|}=0,
$$

where $\|\cdot\|$ is the [[linear-algebra/euclidean-norm|Euclidean norm]].

In this case $L$ is the [[real-analysis/frechet-derivative|Fréchet derivative]] of $f$ at $a$, and (when it exists) it is represented in coordinates by the [[real-analysis/jacobian-matrix|Jacobian matrix]]. Maps that are differentiable at every point of their domain are the basic objects of multivariable [[real-analysis/differentiability-1d|differentiability]] in higher dimensions, and higher smoothness is recorded by [[real-analysis/class-ck-map|C^k maps]].

**Examples:**
- Any affine map $f(x)=Ax+b$ (with $A$ an $m\times n$ matrix) is differentiable everywhere, with derivative $L(h)=Ah$.
- The map $f:\mathbb{R}^2\to \mathbb{R}^3$ given by $f(x,y)=(x^2,xy,\sin y)$ is differentiable everywhere.
