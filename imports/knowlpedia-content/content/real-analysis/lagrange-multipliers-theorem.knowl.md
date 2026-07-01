+++
id = "real-analysis/lagrange-multipliers-theorem"
title = "Lagrange multipliers theorem"
kind = "knowl"
summary = "Constrained extrema give critical points of a Lagrangian under a regularity hypothesis."
aliases = ["lagrange-multipliers-theorem", "Lagrange multipliers theorem"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/lagrange-multipliers-theorem.md"
+++

**Lagrange multipliers theorem:** Let $U\subseteq\mathbb R^n$ be an [[topology/open-set|open set]], let $f:U\to\mathbb R$ and $g:U\to\mathbb R^m$ be continuously differentiable with $m<n$, and let $S=\{x\in U: g(x)=0\}$. Assume $x^\ast\in S$ is a local extremum of $f$ on $S$ and that $Dg(x^\ast)$ has rank $m$. Define the Lagrangian
$$
L(x,\lambda)=f(x)-\sum_{i=1}^m \lambda_i g_i(x).
$$

Then there exists $\lambda^\ast\in\mathbb R^m$ such that
$$
D_xL(x^\ast,\lambda^\ast)=0
\quad\text{and}\quad
g(x^\ast)=0.
$$

Equivalently, $x^\ast$ must satisfy the [[real-analysis/lagrange-multiplier-condition|Lagrange multiplier condition]]. Solving these equations produces candidate points for constrained extrema on the given [[real-analysis/constraint-set|constraint set]].
