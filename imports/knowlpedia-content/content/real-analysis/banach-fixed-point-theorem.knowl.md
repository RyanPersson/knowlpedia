+++
id = "real-analysis/banach-fixed-point-theorem"
title = "Banach Fixed Point Theorem"
kind = "knowl"
summary = "A contraction on a complete metric space has a unique fixed point, found by iteration"
aliases = ["banach-fixed-point-theorem", "Banach Fixed Point Theorem"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/banach-fixed-point-theorem.md"
+++

**Banach Fixed Point Theorem (contraction mapping principle)**: Let $(X,d)$ be a [[topology/complete-metric-space|complete metric space]] and let $T:X\to X$ be a [[shared-foundations/contraction-mapping|contraction]] with contraction constant $c\in[0,1)$. Then:

- There exists a unique [[real-analysis/fixed-point|fixed point]] $x^\ast\in X$ such that $T(x^\ast)=x^\ast$.
- For any starting point $x_0\in X$, the iterates defined by
  $
  x_{n+1}=T(x_n)\quad(n\ge 0)
  $
  [[topology/convergent-sequence|converge]] to $x^\ast$.
- Quantitative error bounds hold: for all $n\ge 0$,
  $
  d(x_{n},x^\ast)\le \frac{c^{n}}{1-c}\,d(x_1,x_0),
  \qquad
  d(x_n,x^\ast)\le c^n\,d(x_0,x^\ast).
  $

This theorem is one of the main uses of completeness: it turns a global "shrinking" hypothesis into existence and uniqueness of solutions of $T(x)=x$.
