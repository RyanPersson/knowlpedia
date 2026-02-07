---
title: "Wedge product of differential forms"
description: "An alternating product that combines a -form and an -form into a (k+)-form."
---

Let \(M\) be a {{< knowl id="smooth-manifold" text="smooth manifold" >}}. The **wedge product** is the canonical bilinear product on the graded algebra of {{< knowl id="differential-k-form" text="differential forms" >}}.

For \(\alpha \in \Omega^k(M)\) and \(\beta \in \Omega^\ell(M)\), their **wedge product** \(\alpha\wedge\beta \in \Omega^{k+\ell}(M)\) is defined pointwise by the alternating product of multilinear forms on each {{< knowl id="tangent-space-at-a-point" text="tangent space" >}}:
\[
(\alpha\wedge\beta)_p(v_1,\dots,v_{k+\ell})
=\frac{1}{k!\,\ell!}\sum_{\sigma\in S_{k+\ell}}\operatorname{sgn}(\sigma)\,
\alpha_p\!\bigl(v_{\sigma(1)},\dots,v_{\sigma(k)}\bigr)\,
\beta_p\!\bigl(v_{\sigma(k+1)},\dots,v_{\sigma(k+\ell)}\bigr),
\]
for all \(p\in M\) and \(v_1,\dots,v_{k+\ell}\in T_pM\).

Equivalently, \((\alpha\wedge\beta)_p\) is the alternation of the tensor product \(\alpha_p\otimes \beta_p\).

## Key properties
If \(\alpha\in\Omega^k(M)\), \(\beta\in\Omega^\ell(M)\), and \(\gamma\in\Omega^m(M)\), then:

- **Bilinearity:** \(\wedge\) is \(\mathbb{R}\)-bilinear in each argument.
- **Associativity:** \((\alpha\wedge\beta)\wedge\gamma=\alpha\wedge(\beta\wedge\gamma)\).
- **Graded-commutativity:**
  \[
  \alpha\wedge\beta = (-1)^{k\ell}\,\beta\wedge\alpha.
  \]
  In particular, if \(k\) is odd then \(\alpha\wedge\alpha=0\).
- **Compatibility with pullback:** for any {{< knowl id="smooth-map" text="smooth map" >}} \(F:M\to N\),
  the {{< knowl id="pullback-of-differential-forms" text="pullback of forms" >}} satisfies
  \(F^*(\alpha\wedge\beta)=F^*\alpha\wedge F^*\beta\).
- The wedge product is the product appearing in the graded Leibniz rule for the {{< knowl id="exterior-derivative" text="exterior derivative" >}}.

## Examples
1. **Coordinate 1-forms on \(\mathbb{R}^3\).**  
   With standard coordinates \((x,y,z)\), the 2-form \(dx\wedge dy\) satisfies
   \((dx\wedge dy)(\partial_x,\partial_y)=1\) and changes sign when the vectors are swapped:
   \((dx\wedge dy)(\partial_y,\partial_x)=-1\).

2. **A wedge computation with functions.**  
   Let \(\alpha = f\,dx + g\,dy\) and \(\beta = h\,dz\) on \(\mathbb{R}^3\), where \(f,g,h\) are smooth functions. Then
   \[
   \alpha\wedge\beta = fh\,dx\wedge dz + gh\,dy\wedge dz.
   \]

3. **Wedge of a 1-form with itself is zero (odd degree).**  
   On any manifold, \(dx\wedge dx=0\). More generally, if \(\eta\) is any 1-form then \(\eta\wedge\eta=0\) by graded-commutativity with \(k=\ell=1\).
