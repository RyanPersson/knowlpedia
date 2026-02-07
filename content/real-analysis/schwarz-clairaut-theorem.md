---
title: "Schwarz–Clairaut theorem"
description: "Under continuity, mixed second partial derivatives agree."
---

**Schwarz–Clairaut theorem:** Let $U\subseteq\mathbb R^n$ be an {{< knowl id="open-set" section="topology" text="open set" >}} and let $f:U\to\mathbb R$. Fix indices $i,j\in\{1,\dots,n\}$. If the {{< knowl id="mixed-partial-derivative" text="mixed second partial derivatives" >}} $\frac{\partial^2 f}{\partial x_i\partial x_j}$ and $\frac{\partial^2 f}{\partial x_j\partial x_i}$ exist on a neighborhood of $a\in U$ and are continuous at $a$, then
$$
\frac{\partial^2 f}{\partial x_i\partial x_j}(a)=\frac{\partial^2 f}{\partial x_j\partial x_i}(a).
$$

This justifies treating the {{< knowl id="hessian-matrix" text="Hessian matrix" >}} of a sufficiently smooth function as symmetric, and it is a standard hypothesis in second-order local analysis such as the {{< knowl id="second-derivative-tests" text="second derivative tests" >}}.
