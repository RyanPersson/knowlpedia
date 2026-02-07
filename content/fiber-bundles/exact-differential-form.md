---
title: "Exact differential form"
description: "A differential form that is the exterior derivative of another form: =d."
---

Let \(M\) be a {{< knowl id="smooth-manifold" text="smooth manifold" >}}. Exactness is defined using the {{< knowl id="exterior-derivative" text="exterior derivative" >}} on {{< knowl id="differential-k-form" text="differential forms" >}}.

A form \(\omega\in\Omega^k(M)\) is **exact** if there exists \(\eta\in\Omega^{k-1}(M)\) such that
\[
\omega = d\eta.
\]
The vector space of exact \(k\)-forms is
\[
B^k(M) \coloneqq \operatorname{im}\!\bigl(d:\Omega^{k-1}(M)\to\Omega^k(M)\bigr).
\]

Exact forms are automatically {{< knowl id="closed-differential-form" text="closed" >}} because \(d^2=0\). In the {{< knowl id="de-rham-cohomology-group" text="de Rham cohomology group" >}} \(H^k_{\mathrm{dR}}(M)\), exact forms represent the zero class.

## Examples
1. **Differentials of functions are exact 1-forms.**  
   For any smooth function \(f\in C^\infty(M)\), the 1-form \(df\) is exact by definition, with \(\eta=f\) viewed as a 0-form.

2. **A basic exact 2-form on \(\mathbb{R}^3\).**  
   On \(\mathbb{R}^3\) with coordinates \((x,y,z)\),
   \[
   dx\wedge dy = d(x\,dy),
   \]
   so \(dx\wedge dy\) is exact.

3. **A closed non-example (not exact globally).**  
   On \(U=\mathbb{R}^2\setminus\{0\}\), the 1-form
   \[
   \omega=\frac{-y\,dx + x\,dy}{x^2+y^2}
   \]
   is {{< knowl id="closed-differential-form" text="closed" >}} but not exact; equivalently, it defines a nonzero class in the {{< knowl id="de-rham-cohomology-group" text="de Rham cohomology" >}} of \(U\).
