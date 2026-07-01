+++
id = "real-analysis/chain-rule"
title = "Chain rule"
kind = "knowl"
summary = "Derivative of a composition equals the composition of derivatives."
aliases = ["chain-rule", "Chain rule"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/chain-rule.md"
+++

**Chain rule:** Let $U\subseteq\mathbb R^k$ and $V\subseteq\mathbb R^m$ be [[topology/open-set|open sets]]. Let $f:U\to V$ be [[real-analysis/differentiable-map|differentiable]] at $a\in U$, and let $g:V\to\mathbb R^p$ be differentiable at $f(a)$. Then the [[shared-foundations/composition|composition]] $g\circ f$ is differentiable at $a$, and
$$
D(g\circ f)(a)=Dg(f(a))\circ Df(a).
$$

In terms of the [[real-analysis/jacobian-matrix|Jacobian matrix]], this becomes the matrix identity $J_{g\circ f}(a)=J_g(f(a))\,J_f(a)$, which is the standard “multiply Jacobians” rule.
