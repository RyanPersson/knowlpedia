---
title: "Banach Fixed Point Theorem"
description: "A contraction on a complete metric space has a unique fixed point, found by iteration"
---

**Banach Fixed Point Theorem (contraction mapping principle)**: Let $(X,d)$ be a {{< knowl id="complete-metric-space" text="complete metric space" >}} and let $T:X\to X$ be a {{< knowl id="contraction-mapping" text="contraction" >}} with contraction constant $c\in[0,1)$. Then:

- There exists a unique {{< knowl id="fixed-point" text="fixed point" >}} $x^\ast\in X$ such that $T(x^\ast)=x^\ast$.
- For any starting point $x_0\in X$, the iterates defined by
  $
  x_{n+1}=T(x_n)\quad(n\ge 0)
  $
  {{< knowl id="convergent-sequence" text="converge" >}} to $x^\ast$.
- Quantitative error bounds hold: for all $n\ge 0$,
  $
  d(x_{n},x^\ast)\le \frac{c^{n}}{1-c}\,d(x_1,x_0),
  \qquad
  d(x_n,x^\ast)\le c^n\,d(x_0,x^\ast).
  $

This theorem is one of the main uses of completeness: it turns a global "shrinking" hypothesis into existence and uniqueness of solutions of $T(x)=x$.

**Proof sketch**:
From the contraction inequality,
$
d(x_{n+1},x_n)=d(Tx_n,Tx_{n-1})\le c\,d(x_n,x_{n-1})\le \cdots \le c^n d(x_1,x_0).
$
Then for $m>n$,
$
d(x_m,x_n)\le \sum_{k=n}^{m-1} d(x_{k+1},x_k)
\le d(x_1,x_0)\sum_{k=n}^{\infty} c^k
=\frac{c^n}{1-c}d(x_1,x_0),
$
so $(x_n)$ is {{< knowl id="cauchy-sequence" text="Cauchy" >}} and hence converges (completeness) to some $x^\ast\in X$. {{< knowl id="continuity-at-a-point" text="Continuity" >}} of $T$ (it is {{< knowl id="lipschitz-function" text="Lipschitz" >}}) gives $T(x^\ast)=x^\ast$. Uniqueness follows since if $Tx=x$ and $Ty=y$, then
$
d(x,y)=d(Tx,Ty)\le c\,d(x,y),
$
forcing $d(x,y)=0$ and hence $x=y$.
