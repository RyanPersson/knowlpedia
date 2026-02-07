---
title: "Exterior derivative"
description: "The differential operator on differential forms satisfying ^2=0 and the graded Leibniz rule."
---

On a {{< knowl id="smooth-manifold" text="smooth manifold" >}} \(M\), the **exterior derivative** is the fundamental operator on {{< knowl id="differential-k-form" text="differential forms" >}} that generalizes the differential of a function and is compatible with the {{< knowl id="wedge-product-of-differential-forms" text="wedge product" >}}.

## Characterization and definition
There is a unique family of \(\mathbb{R}\)-linear maps
\[
d:\Omega^k(M)\to \Omega^{k+1}(M)\qquad (k\ge 0)
\]
such that:

1. (**On functions**) If \(f\in\Omega^0(M)=C^\infty(M)\), then \(df\) is the usual differential (a 1-form) given by \(df_p(v)=v(f)\).
2. (**Graded Leibniz rule**) For \(\alpha\in\Omega^k(M)\) and \(\beta\in\Omega^\ell(M)\),
   \[
   d(\alpha\wedge\beta)=d\alpha\wedge\beta + (-1)^k\,\alpha\wedge d\beta.
   \]
3. (**Nilpotence**) \(d\circ d = 0\).

A key naturality property is that for any {{< knowl id="smooth-map" text="smooth map" >}} \(F:M\to N\), the {{< knowl id="pullback-of-differential-forms" text="pullback of differential forms" >}} satisfies
\[
F^*(d\omega)=d(F^*\omega)
\]
for every \(\omega\in\Omega^k(N)\).

The notions of {{< knowl id="closed-differential-form" text="closed" >}} and {{< knowl id="exact-differential-form" text="exact" >}} forms are defined using \(d\), and their quotient defines the {{< knowl id="de-rham-cohomology-group" text="de Rham cohomology groups" >}}.

## Local coordinate formula
In a coordinate chart \((x^1,\dots,x^n)\), write a \(k\)-form as
\[
\alpha=\sum_{I} a_I\, dx^{i_1}\wedge\cdots\wedge dx^{i_k},
\]
where \(I=(i_1<\cdots<i_k)\) and \(a_I\) are smooth functions. Then
\[
d\alpha=\sum_I \sum_{j=1}^n \frac{\partial a_I}{\partial x^j}\, dx^j \wedge dx^{i_1}\wedge\cdots\wedge dx^{i_k}.
\]

## Examples
1. **A function on \(\mathbb{R}^2\).**  
   For \(f(x,y)\), the exterior derivative is
   \[
   df = \frac{\partial f}{\partial x}\,dx + \frac{\partial f}{\partial y}\,dy.
   \]

2. **A 1-form on \(\mathbb{R}^2\).**  
   Let \(\alpha = P(x,y)\,dx + Q(x,y)\,dy\). Then
   \[
   d\alpha = \left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)\,dx\wedge dy.
   \]

3. **A 2-form on \(\mathbb{R}^3\).**  
   If \(\omega = f(x,y,z)\,dx\wedge dy\), then
   \[
   d\omega = df\wedge dx\wedge dy = \frac{\partial f}{\partial z}\,dz\wedge dx\wedge dy,
   \]
   since the terms involving \(dx\wedge dx\) and \(dy\wedge dy\) vanish by alternation.
