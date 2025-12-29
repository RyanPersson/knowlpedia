---
title: "Mixed partial derivative"
description: "An iterated partial derivative such as ∂^2f/(∂x_i∂x_j)."
---

Let $U\subseteq\mathbb{R}^k$ be open and let $f:U\to\mathbb{R}$ be a scalar-valued function. If the partial derivative $\frac{\partial f}{\partial x_j}$ exists on a neighborhood of a point $a\in U$, and if $\frac{\partial f}{\partial x_j}$ is partially differentiable with respect to $x_i$ at $a$, then the **mixed partial derivative** is
$$
\frac{\partial^2 f}{\partial x_i\,\partial x_j}(a)
:= \frac{\partial}{\partial x_i}\left(\frac{\partial f}{\partial x_j}\right)(a).
$$

Mixed partial derivatives appear in second-order Taylor expansions and in the Hessian. Under suitable continuity assumptions (e.g., $C^2$), mixed partials commute: $\partial_{x_i}\partial_{x_j}f=\partial_{x_j}\partial_{x_i}f$ (Schwarz/Clairaut theorem).

**Examples:**
- If $f(x,y)=x^2y$, then $\frac{\partial^2 f}{\partial y\,\partial x}(x,y)=\frac{\partial}{\partial y}(2xy)=2x$, and $\frac{\partial^2 f}{\partial x\,\partial y}(x,y)=\frac{\partial}{\partial x}(x^2)=2x$ (they agree).
- For a polynomial, all mixed partial derivatives exist and are continuous, so they commute.
- There are functions where mixed partials exist but are not equal at a point if continuity hypotheses fail.
