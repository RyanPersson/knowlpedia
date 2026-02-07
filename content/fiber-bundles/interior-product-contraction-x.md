---
title: "Interior product (contraction) ι_X"
description: "Insertion of a vector field into a differential form, producing a form of one lower degree."
---

Let $M$ be a {{< knowl id="smooth-manifold" text="smooth manifold" >}} and let $X$ be a {{< knowl id="vector-field" text="vector field" >}} on $M$. For a {{< knowl id="differential-k-form" text="differential form" >}} $\omega\in\Omega^k(M)$, the **interior product** (or **contraction**) of $\omega$ by $X$ is the $(k-1)$-form $\iota_X\omega\in\Omega^{k-1}(M)$ defined by
\[
(\iota_X\omega)_p(v_1,\dots,v_{k-1})
\;:=\;
\omega_p(X_p,v_1,\dots,v_{k-1}),
\qquad
p\in M,\; v_i\in T_pM.
\]
By convention, if $k=0$ then $\iota_X\omega:=0$.

The contraction satisfies the following standard identities.

- **$C^\infty(M)$-linearity in the vector field:** for $f\in C^\infty(M)$,
  \[
  \iota_{fX}\omega = f\,\iota_X\omega.
  \]

- **Graded derivation rule for the** {{< knowl id="wedge-product-of-differential-forms" text="wedge product" >}}: if $\alpha\in\Omega^p(M)$ and $\beta\in\Omega^q(M)$, then
  \[
  \iota_X(\alpha\wedge\beta) = (\iota_X\alpha)\wedge\beta + (-1)^p\,\alpha\wedge(\iota_X\beta).
  \]

- **Cartan’s formula (interaction with differentiation):** the {{< knowl id="lie-derivative-of-a-differential-form" text="Lie derivative" >}} of forms along $X$ is given by
  \[
  \mathcal{L}_X\omega = d(\iota_X\omega)+\iota_X(d\omega),
  \]
  where $d$ is the {{< knowl id="exterior-derivative" text="exterior derivative" >}}.

## Examples

1. If $\alpha\in\Omega^1(M)$ is a $1$-form, then $\iota_X\alpha$ is the smooth function $\alpha(X)\in C^\infty(M)$ obtained by evaluating $\alpha$ on the vector field $X$.

2. On $M=\mathbb{R}^2$ with coordinates $(x,y)$, let $\omega=dx\wedge dy$ and $X=\frac{\partial}{\partial x}$. Then
   \[
   \iota_X\omega = dy.
   \]

3. On $M=\mathbb{R}^3$ with coordinates $(x,y,z)$, let $\omega=dx\wedge dy\wedge dz$ and $X=\frac{\partial}{\partial x}+2\frac{\partial}{\partial y}$. Then
   \[
   \iota_X\omega = dy\wedge dz - 2\,dx\wedge dz.
   \]
