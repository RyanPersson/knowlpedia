---
title: "Gauge transform of a local connection form"
description: "How a local connection 1-form changes under a change of local section by a G-valued gauge function."
---

Let \(\pi:P\to M\) be a principal \(G\)-bundle with connection form \(\omega\in \Omega^1(P;\mathfrak{g})\) as in {{< knowl id="connection-1-form-on-a-principal-bundle" text="a connection 1-form on a principal bundle" >}}.

Fix an open set \(U\subset M\) and a local section \(s:U\to P\). The **local connection form** on \(U\) is
\[
A \coloneqq s^*\omega \in \Omega^1(U;\mathfrak{g}).
\]

A **gauge transformation** on \(U\) is a {{< knowl id="smooth-map" text="smooth map" >}} \(g:U\to  G\). It determines a new local section \(s':U\to P\) by
\[
s'(x)\coloneqq s(x)\cdot g(x).
\]
The corresponding local connection form \(A'=(s')^*\omega\) is related to \(A\) by the **gauge transformation rule**
\[
A' \;=\; \mathrm{Ad}(g^{-1})A \;+\; g^{-1}dg,
\]
where \(g^{-1}dg\in \Omega^1(U;\mathfrak{g})\) is the pullback of the left Maurer–Cartan form on \(G\) along \(g\), and \(\mathrm{Ad}(g^{-1})\) acts pointwise on \(\mathfrak{g}\).

This formula is the local manifestation of the global equivariance condition \(R_h^*\omega=\mathrm{Ad}(h^{-1})\omega.

## Examples
1. **Abelian case \(U(1)\).** For \(G=U(1)\), \(\mathrm{Ad}\) is trivial, so \(A'=A+g^{-1}dg\). Writing \(g=e^{if}\) locally gives \(g^{-1}dg=i\,df\), hence \(A'=A+i\,df\).

2. **Matrix group \(GL(n)\).** For \(G=GL(n)\subset \mathrm{End}(\mathbb{R}^n)\), the adjoint action is conjugation, and the rule becomes
   \[
   A' = g^{-1}Ag + g^{-1}dg,
   \]
   where \(A\) is a matrix-valued 1-form.

3. **Constant gauge transformations.** If \(g\) is constant on \(U\), then \(dg=0\) and \(A'=\mathrm{Ad}(g^{-1})A\); i.e. only the \(\mathfrak{g}\)-basis changes.
