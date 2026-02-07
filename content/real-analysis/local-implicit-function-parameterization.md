---
title: "Local implicit-function parameterization"
description: "Near a regular point, a level set is locally the graph of a differentiable map."
---

**Local implicit-function parameterization:** Let $U\subseteq\mathbb R^n$ be an {{< knowl id="open-set" section="topology" text="open set" >}}, let $F:U\to\mathbb R^m$ be continuously differentiable with $m<n$, and let $p\in U$ satisfy $F(p)=0$. If the derivative $DF(p):\mathbb R^n\to\mathbb R^m$ has rank $m$ (equivalently, $p$ is a {{< knowl id="regular-point" text="regular point" >}} of $F$), then after reordering coordinates in $\mathbb R^n$ there exist neighborhoods $W$ of $p$ and $V$ of some $u_0\in\mathbb R^{n-m}$ and a continuously differentiable map $\varphi:V\to\mathbb R^m$ such that, in these coordinates,
$$
\{x\in W: F(x)=0\}=\{(u,\varphi(u)): u\in V\}.
$$

Equivalently, near a regular point, the constraint set $F^{-1}(0)$ is locally a graph, as guaranteed by the {{< knowl id="implicit-function-theorem" text="implicit function theorem" >}}.
