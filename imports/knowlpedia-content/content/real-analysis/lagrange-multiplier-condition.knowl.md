+++
id = "real-analysis/lagrange-multiplier-condition"
title = "Lagrange multiplier condition"
kind = "knowl"
summary = "Necessary first-order condition for constrained extrema in terms of gradients."
aliases = ["lagrange-multiplier-condition", "Lagrange multiplier condition"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/lagrange-multiplier-condition.md"
+++

**Lagrange multiplier condition:** Let $U\subseteq\mathbb R^n$ be an [[topology/open-set|open set]]. Let $f:U\to\mathbb R$ and $g:U\to\mathbb R^m$ be continuously differentiable with $m<n$, and consider the [[real-analysis/constraint-set|constraint set]] $S=\{x\in U: g(x)=0\}$. If $x^\ast\in S$ is a local [[real-analysis/local-extremum|extremum]] of $f$ restricted to $S$ and $Dg(x^\ast)$ has rank $m$ (so $x^\ast$ is a [[real-analysis/regular-point|regular point]] of $g$), then there exists $\lambda\in\mathbb R^m$ such that
$$
Df(x^\ast)=\lambda^{\mathsf T}Dg(x^\ast).
$$

In the common case $m=1$, this says the [[real-analysis/gradient|gradient]] vectors satisfy $\nabla f(x^\ast)=\lambda\,\nabla g(x^\ast)$, so the constrained extremum occurs at a point where $f$ has a [[real-analysis/critical-point|critical-point-type condition]] compatible with the constraint.
