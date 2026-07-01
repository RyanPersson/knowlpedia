+++
id = "real-analysis/mixed-partial-derivative"
title = "Mixed partial derivative"
kind = "knowl"
summary = "A second partial derivative taken with respect to two different coordinates"
aliases = ["mixed-partial-derivative", "Mixed partial derivative"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/mixed-partial-derivative.md"
+++

A **mixed partial derivative** of a scalar function $f:U\to \mathbb{R}$ (with $U\subseteq \mathbb{R}^n$) at $a\in U$ is a second-order partial derivative of the form
$$
\frac{\partial^2 f}{\partial x_i\,\partial x_j}(a)
=\frac{\partial}{\partial x_i}\left(\frac{\partial f}{\partial x_j}\right)(a),
$$
provided the relevant partial derivatives exist.

Mixed partial derivatives form the off-diagonal entries of the [[real-analysis/hessian-matrix|Hessian matrix]]. Under appropriate regularity hypotheses (for example, continuity of the second partials near $a$), the [[real-analysis/schwarz-clairaut-theorem|Schwarz–Clairaut theorem]] guarantees equality of the two orders of differentiation.

**Examples:**
- For $f(x,y)=x^2y$, one has $\frac{\partial^2 f}{\partial x\,\partial y}(x,y)=2x$ and $\frac{\partial^2 f}{\partial y\,\partial x}(x,y)=2x$.
- For $f(x,y)=e^{x+y}$, every mixed partial derivative exists and equals $e^{x+y}$.
