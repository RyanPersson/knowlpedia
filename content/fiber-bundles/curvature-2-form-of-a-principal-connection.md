---
title: "Curvature 2-form of a principal connection"
description: "A Lie-algebra-valued 2-form measuring the non-integrability of the horizontal distribution of a principal connection."
---

Let \(\pi:P\to M\) be a principal \(G\)-bundle with connection 1-form \(\omega\in \Omega^1(P;\mathfrak{g})\) (see {{< knowl id="connection-1-form-on-a-principal-bundle" text="connection 1-form" >}}). The **curvature 2-form** is the \(\mathfrak{g}\)-valued 2-form
\[
\Omega \;\coloneqq\; d\omega \;+\; \tfrac12[\omega\wedge \omega] \;\in\; \Omega^2(P;\mathfrak{g}),
\]
where \(d\) is the {{< knowl id="exterior-derivative" text="exterior derivative" >}} and \([\omega\wedge\omega]\) is formed using the {{< knowl id="lie-bracket" text="Lie bracket" >}} on \(\mathfrak{g}\) together with the wedge product of 1-forms.

Key properties:
- \(\Omega\) is **horizontal**: \(\Omega(X,\cdot)=0\) whenever \(X\) is vertical.
- \(\Omega\) is **equivariant**: \(R_g^*\Omega=\mathrm{Ad}(g^{-1})\Omega\).

Consequently, \(\Omega\) represents the {{< knowl id="curvature" text="curvature" >}} of the underlying {{< knowl id="principal-connection" text="principal connection" >}} and can be viewed as an \(\mathrm{ad}(P)\)-valued 2-form on \(M\) after descending from \(P\).

One conceptual characterization: if \(X,Y\) are vector fields on \(M\) and \(X^H,Y^H\) are their horizontal lifts to \(P\), then
\[
\Omega(X^H,Y^H) = -\,\omega([X^H,Y^H]),
\]
so \(\Omega\) measures the failure of horizontal lifts to close under brackets.

## Examples
1. **Maurer–Cartan form is flat.** On \(P=G\to\{\ast\}\) with \(\omega=\theta=g^{-1}dg\), the Maurer–Cartan equation says \(d\theta+\tfrac12[\theta\wedge\theta]=0\). Hence \(\Omega=0\).

2. **Curvature in a trivialization.** On \(U\times G\to U\) with \(\omega=\mathrm{Ad}(g^{-1})A+g^{-1}dg\), one computes
   \[
   \Omega = \mathrm{Ad}(g^{-1})\,\pi_U^*\!\left(dA+\tfrac12[A\wedge A]\right),
   \]
   so the entire curvature is pulled back from the base.

3. **Abelian structure group.** If \(G\) is abelian, then \([\omega\wedge\omega]=0\) and \(\Omega=d\omega\). In particular for principal \(U(1)\)-bundles the curvature is just the exterior derivative of the connection form.
