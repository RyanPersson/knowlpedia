---
title: "Chain rule"
description: "Derivative of a composition equals the composition of derivatives."
---

**Chain rule:** Let $U\subseteq\mathbb R^k$ and $V\subseteq\mathbb R^m$ be {{< knowl id="open-set" section="topology" text="open sets" >}}. Let $f:U\to V$ be {{< knowl id="differentiable-map" text="differentiable" >}} at $a\in U$, and let $g:V\to\mathbb R^p$ be differentiable at $f(a)$. Then the {{< knowl id="composition" section="shared-foundations" text="composition" >}} $g\circ f$ is differentiable at $a$, and
$$
D(g\circ f)(a)=Dg(f(a))\circ Df(a).
$$

In terms of the {{< knowl id="jacobian-matrix" text="Jacobian matrix" >}}, this becomes the matrix identity $J_{g\circ f}(a)=J_g(f(a))\,J_f(a)$, which is the standard “multiply Jacobians” rule.
