---
title: "de Rham cohomology group"
description: "The quotient of closed forms by exact forms, measuring global obstructions to solving =."
---

Let \(M\) be a {{< knowl id="smooth-manifold" text="smooth manifold" >}}. The {{< knowl id="exterior-derivative" text="exterior derivative" >}} makes the graded vector space of {{< knowl id="differential-k-form" text="differential forms" >}} into a cochain complex \((\Omega^\ast(M),d)\). Its cohomology is the **de Rham cohomology**.

Define
- \(Z^k(M)\) as the space of {{< knowl id="closed-differential-form" text="closed \\(k\\)-forms" >}} (those \(\omega\) with \(d\omega=0\)),
- \(B^k(M)\) as the space of {{< knowl id="exact-differential-form" text="exact \\(k\\)-forms" >}} (those \(\omega\) with \(\omega=d\eta\)).

Because \(d^2=0\), every exact form is closed, so \(B^k(M)\subseteq Z^k(M)\). The **\(k\)th de Rham cohomology group** is the quotient vector space
\[
H^k_{\mathrm{dR}}(M)\coloneqq Z^k(M)\,/\,B^k(M).
\]
An element \([\omega]\in H^k_{\mathrm{dR}}(M)\) is the equivalence class of a closed form \(\omega\), where \(\omega\sim\omega'\) if \(\omega-\omega'\) is exact.

## Functoriality
If \(F:M\to N\) is a {{< knowl id="smooth-map" text="smooth map" >}}, then the {{< knowl id="pullback-of-differential-forms" text="pullback of forms" >}} sends closed forms to closed forms and exact forms to exact forms (since \(F^*\) commutes with \(d\)). Hence \(F\) induces a linear map on cohomology:
\[
F^*:H^k_{\mathrm{dR}}(N)\to H^k_{\mathrm{dR}}(M),\qquad [\omega]\mapsto [F^*\omega].
\]

## Examples
1. **Euclidean space.**  
   For \(M=\mathbb{R}^n\), one has \(H^0_{\mathrm{dR}}(\mathbb{R}^n)\cong \mathbb{R}\) and \(H^k_{\mathrm{dR}}(\mathbb{R}^n)=0\) for all \(k>0\).

2. **The circle.**  
   For \(M=S^1\), one has \(H^0_{\mathrm{dR}}(S^1)\cong \mathbb{R}\) and \(H^1_{\mathrm{dR}}(S^1)\cong \mathbb{R}\). A generator of \(H^1_{\mathrm{dR}}(S^1)\) can be represented by a closed 1-form whose integral around the circle is nonzero.

3. **The sphere \(S^n\).**  
   For \(M=S^n\) with \(n\ge 1\), one has \(H^0_{\mathrm{dR}}(S^n)\cong \mathbb{R}\), \(H^n_{\mathrm{dR}}(S^n)\cong \mathbb{R}\), and \(H^k_{\mathrm{dR}}(S^n)=0\) for \(0<k<n\).
