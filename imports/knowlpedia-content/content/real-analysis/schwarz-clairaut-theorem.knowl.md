+++
id = "real-analysis/schwarz-clairaut-theorem"
title = "Schwarz–Clairaut theorem"
kind = "knowl"
summary = "Under continuity, mixed second partial derivatives agree."
aliases = ["schwarz-clairaut-theorem", "Schwarz–Clairaut theorem"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/schwarz-clairaut-theorem.md"
+++

**Schwarz–Clairaut theorem:** Let $U\subseteq\mathbb R^n$ be an [[topology/open-set|open set]] and let $f:U\to\mathbb R$. Fix indices $i,j\in\{1,\dots,n\}$. If the [[real-analysis/mixed-partial-derivative|mixed second partial derivatives]] $\frac{\partial^2 f}{\partial x_i\partial x_j}$ and $\frac{\partial^2 f}{\partial x_j\partial x_i}$ exist on a neighborhood of $a\in U$ and are continuous at $a$, then
$$
\frac{\partial^2 f}{\partial x_i\partial x_j}(a)=\frac{\partial^2 f}{\partial x_j\partial x_i}(a).
$$

This justifies treating the [[real-analysis/hessian-matrix|Hessian matrix]] of a sufficiently smooth function as symmetric, and it is a standard hypothesis in second-order local analysis such as the [[real-analysis/second-derivative-tests|second derivative tests]].
