---
title: "Isomorphic principal bundles have the same Chern–Weil classes"
description: "Chern–Weil characteristic classes agree for isomorphic principal bundles."
---

Let \(P\to M\) and \(P'\to M\) be principal \(G\)-bundles, and let \(\Phi:P\to P'\) be an isomorphism of principal bundles over \(M\) (a \(G\)-equivariant {{< knowl id="diffeomorphism" text="diffeomorphism" >}} with \(\pi'\circ\Phi=\pi\)).

## Corollary (invariance under bundle isomorphism)
For every invariant polynomial \(p\), the corresponding {{< knowl id="corollary-chernweil-characteristic-classes-are-invariants-of-the-principal-bundle" text="Chern–Weil characteristic class" >}} satisfies
\[
\mathrm{cw}_p(P)=\mathrm{cw}_p(P') \in H^{*}_{\mathrm{dR}}(M).
\]

Equivalently: choosing any connection \(\omega\) on \(P\), the pullback connection \((\Phi^{-1})^*\omega\) on \(P'\) has the property that the Chern–Weil forms produced from \(\omega\) and \((\Phi^{-1})^*\omega\) represent the same de Rham class, so the classes coincide.

## Examples
1. **Same bundle via different constructions.** If a principal bundle is presented using two different atlases or two different cocycles related by a coboundary, the resulting bundles are isomorphic; their Chern–Weil classes coincide.
2. **Vector bundle isomorphism.** If two rank-\(n\) real vector bundles are isomorphic, their frame bundles are isomorphic as principal \(GL(n,\mathbb R)\)-bundles, so all Chern–Weil classes defined from the frame bundle agree (e.g. Pontryagin classes).
3. **Pullback by a diffeomorphism.** If \(f:N\to M\) is a diffeomorphism and \(P\to M\) is a principal bundle, then \(f^*P\to N\) is isomorphic to \(P\) transported along \(f\), and the Chern–Weil classes transform by pullback in cohomology.
