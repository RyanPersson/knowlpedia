---
title: "Banach Fixed Point Theorem"
description: "A contraction on a complete metric space has a unique fixed point, found by iteration"
---

**Banach Fixed Point Theorem (contraction mapping principle)**: Let $(X,d)$ be a {{< knowl id="complete-metric-space" section="topology" text="complete metric space" >}} and let $T:X\to X$ be a {{< knowl id="contraction-mapping" section="shared-foundations" text="contraction" >}} with contraction constant $c\in[0,1)$. Then:

- There exists a unique {{< knowl id="fixed-point" text="fixed point" >}} $x^\ast\in X$ such that $T(x^\ast)=x^\ast$.
- For any starting point $x_0\in X$, the iterates defined by
  $
  x_{n+1}=T(x_n)\quad(n\ge 0)
  $
  {{< knowl id="convergent-sequence" section="topology" text="converge" >}} to $x^\ast$.
- Quantitative error bounds hold: for all $n\ge 0$,
  $
  d(x_{n},x^\ast)\le \frac{c^{n}}{1-c}\,d(x_1,x_0),
  \qquad
  d(x_n,x^\ast)\le c^n\,d(x_0,x^\ast).
  $

This theorem is one of the main uses of completeness: it turns a global "shrinking" hypothesis into existence and uniqueness of solutions of $T(x)=x$.
