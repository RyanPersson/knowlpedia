---
title: "Local curvature 2-form"
description: "The curvature 2-form expressed on the base via pullback along a local section."
---

Let \(\pi:P\to M\) be a principal \(G\)-bundle with connection form \(\omega\) and curvature \(\Omega\) as in {{< knowl id="curvature-2-form-of-a-principal-connection" text="the curvature 2-form of a principal connection" >}}.

On an open set \(U\subset M\) with local section \(s:U\to P\), define the local connection 1-form \(A=s^*\omega\in \Omega^1(U;\mathfrak{g})\). The **local curvature 2-form** on \(U\) is
\[
F \;\coloneqq\; s^*\Omega \in \Omega^2(U;\mathfrak{g}).
\]

Then \(F\) is given by the structure equation
\[
F \;=\; dA \;+\; \tfrac12[A\wedge A],
\]
where \(d\) is the {{< knowl id="exterior-derivative" text="exterior derivative" >}} and the bracket uses the {{< knowl id="lie-bracket" text="Lie bracket" >}} on \(\mathfrak{g}\).

If \(s' = s\cdot g\) is another local section related by a gauge function \(g:U\to G\), then the associated local curvature forms satisfy the gauge transformation rule
\[
F' = \mathrm{Ad}(g^{-1})F,
\]
compatible with the {{< knowl id="gauge-transform-of-a-local-connection-form" text="gauge transformation of the local connection form" >}}.

## Examples
1. **Abelian case.** If \(G\) is abelian (e.g. \(U(1)\)), then \([A\wedge A]=0\), hence \(F=dA\), and the gauge rule reduces to \(F'=F\).

2. **Matrix-valued form convention.** For \(G\subset GL(n)\), one often writes \(F=dA + A\wedge A\). This matches the formula above because for matrix-valued 1-forms, \([A\wedge A]=A\wedge A - (A\wedge A)^{\mathrm{op}} = 2A\wedge A\).

3. **Trivial (flat) local connection.** If \(A=0\) on \(U\), then \(F=0\) on \(U\), so the connection is locally flat there.
