+++
id = "real-analysis/critical-point"
title = "Critical point"
kind = "knowl"
summary = "A point where the first derivative of a scalar function vanishes"
aliases = ["critical-point", "Critical point"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/critical-point.md"
+++

A **critical point** of a differentiable function $f:U\to \mathbb{R}$ (with $U\subseteq \mathbb{R}^n$) is a point $a\in U$ such that
$$
\nabla f(a)=0,
$$

equivalently, the [[real-analysis/frechet-derivative|Fréchet derivative]] $Df(a)$ is the zero linear map.

Critical points are candidates for [[real-analysis/local-extremum|local extrema]] but need not be extrema. Higher-order information, such as the [[real-analysis/hessian-matrix|Hessian matrix]], is used to refine classification (see [[real-analysis/second-derivative-tests|second derivative tests]]).

**Examples:**
- For $f(x)=x^3$, the point $a=0$ is a critical point, but $0$ is not a local maximum or minimum.
- For $f(x,y)=x^2+y^2$, the point $(0,0)$ is a critical point and is a (global) minimum.
