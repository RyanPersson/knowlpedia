---
title: "Characteristic class"
description: "A de Rham cohomology class of a principal bundle defined from curvature via the Chern–Weil construction."
---

Let \(\pi:P\to M\) be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} over a smooth manifold \(M\). Fix an Ad-invariant polynomial \(P\) on the Lie algebra \(\mathfrak{g}\) of \(G\).

Choose any principal connection on \(P\), form its Chern–Weil form \(\mathrm{CW}_P(\omega)\in \Omega^{2k}(M)\) as in {{< knowl id="chernweil-form" text="the Chern–Weil form construction" >}}, and take its de Rham class:
\[
c_P(P) \;\coloneqq\; [\,\mathrm{CW}_P(\omega)\,]\in H^{2k}_{\mathrm{dR}}(M).
\]

This cohomology class is called the **characteristic class** associated to the invariant polynomial \(P\) (and the bundle \(P\)). It is well-defined because:
- \(\mathrm{CW}_P(\omega)\) is closed, and
- the cohomology class \([\,\mathrm{CW}_P(\omega)\,]\) is independent of the choice of connection \(\omega\).

Characteristic classes are natural under pullback of bundles: if \(f:N\to M\) is smooth and \(f^*P\to N\) is the pulled-back bundle, then the characteristic class of \(f^*P\) is \(f^*c_P(P)\).

## Examples
1. **First Chern class of a circle bundle.** For a principal \(U(1)\)-bundle, the de Rham class of the curvature form (with conventional normalization) gives the first Chern class \(c_1\in H^2_{\mathrm{dR}}(M)\).

2. **Pontryagin classes.** For an \(SO(n)\)-bundle, Ad-invariant polynomials built from traces of even powers (e.g. \(\mathrm{tr}(X^2)\), \(\mathrm{tr}(X^4)\), etc.) produce the Pontryagin classes \(p_i\in H^{4i}_{\mathrm{dR}}(M)\) via Chern–Weil theory.

3. **Euler class.** For an oriented \(SO(2m)\)-bundle, the Pfaffian polynomial yields a top-degree class in \(H^{2m}_{\mathrm{dR}}(M)\), the Euler class; integrating a representative over a closed base manifold recovers the Euler number.
