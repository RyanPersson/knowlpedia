---
title: "Lagrange multiplier condition"
description: "Necessary first-order condition for constrained extrema in terms of gradients."
---

**Lagrange multiplier condition:** Let $U\subseteq\mathbb R^n$ be an {{< knowl id="open-set" section="topology" text="open set" >}}. Let $f:U\to\mathbb R$ and $g:U\to\mathbb R^m$ be continuously differentiable with $m<n$, and consider the {{< knowl id="constraint-set" text="constraint set" >}} $S=\{x\in U: g(x)=0\}$. If $x^\ast\in S$ is a local {{< knowl id="local-extremum" text="extremum" >}} of $f$ restricted to $S$ and $Dg(x^\ast)$ has rank $m$ (so $x^\ast$ is a {{< knowl id="regular-point" text="regular point" >}} of $g$), then there exists $\lambda\in\mathbb R^m$ such that
$$
Df(x^\ast)=\lambda^{\mathsf T}Dg(x^\ast).
$$

In the common case $m=1$, this says the {{< knowl id="gradient" text="gradient" >}} vectors satisfy $\nabla f(x^\ast)=\lambda\,\nabla g(x^\ast)$, so the constrained extremum occurs at a point where $f$ has a {{< knowl id="critical-point" text="critical-point-type condition" >}} compatible with the constraint.
