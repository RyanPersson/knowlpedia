+++
id = "real-analysis/local-implicit-function-parameterization"
title = "Local implicit-function parameterization"
kind = "knowl"
summary = "Near a regular point, a level set is locally the graph of a differentiable map."
aliases = ["local-implicit-function-parameterization", "Local implicit-function parameterization"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/local-implicit-function-parameterization.md"
+++

**Local implicit-function parameterization:** Let $U\subseteq\mathbb R^n$ be an [[topology/open-set|open set]], let $F:U\to\mathbb R^m$ be continuously differentiable with $m<n$, and let $p\in U$ satisfy $F(p)=0$. If the derivative $DF(p):\mathbb R^n\to\mathbb R^m$ has rank $m$ (equivalently, $p$ is a [[real-analysis/regular-point|regular point]] of $F$), then after reordering coordinates in $\mathbb R^n$ there exist neighborhoods $W$ of $p$ and $V$ of some $u_0\in\mathbb R^{n-m}$ and a continuously differentiable map $\varphi:V\to\mathbb R^m$ such that, in these coordinates,
$$
\{x\in W: F(x)=0\}=\{(u,\varphi(u)): u\in V\}.
$$

Equivalently, near a regular point, the constraint set $F^{-1}(0)$ is locally a graph, as guaranteed by the [[real-analysis/implicit-function-theorem|implicit function theorem]].
