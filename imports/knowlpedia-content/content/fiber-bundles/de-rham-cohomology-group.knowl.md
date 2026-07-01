+++
id = "fiber-bundles/de-rham-cohomology-group"
title = "de Rham cohomology group"
kind = "knowl"
summary = "The quotient of closed forms by exact forms, measuring global obstructions to solving =."
aliases = ["de-rham-cohomology-group", "de Rham cohomology group"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/de-rham-cohomology-group.md"
+++

Let \(M\) be a [[fiber-bundles/smooth-manifold|smooth manifold]]. The [[fiber-bundles/exterior-derivative|exterior derivative]] makes the graded vector space of [[fiber-bundles/differential-k-form|differential forms]] into a cochain complex \((\Omega^\ast(M),d)\). Its cohomology is the **de Rham cohomology**.

Define
- \(Z^k(M)\) as the space of [[fiber-bundles/closed-differential-form|closed \\(k\\)-forms]] (those \(\omega\) with \(d\omega=0\)),
- \(B^k(M)\) as the space of [[fiber-bundles/exact-differential-form|exact \\(k\\)-forms]] (those \(\omega\) with \(\omega=d\eta\)).

Because \(d^2=0\), every exact form is closed, so \(B^k(M)\subseteq Z^k(M)\). The **\(k\)th de Rham cohomology group** is the quotient vector space
\[
H^k_{\mathrm{dR}}(M)\coloneqq Z^k(M)\,/\,B^k(M).
\]
An element \([\omega]\in H^k_{\mathrm{dR}}(M)\) is the equivalence class of a closed form \(\omega\), where \(\omega\sim\omega'\) if \(\omega-\omega'\) is exact.

## Functoriality
If \(F:M\to N\) is a [[fiber-bundles/smooth-map|smooth map]], then the [[fiber-bundles/pullback-of-differential-forms|pullback of forms]] sends closed forms to closed forms and exact forms to exact forms (since \(F^*\) commutes with \(d\)). Hence \(F\) induces a linear map on cohomology:
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
