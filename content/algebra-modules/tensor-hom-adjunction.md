---
title: "Tensor–Hom adjunction"
description: "The natural identification Hom(M⊗N,P) ≅ Hom(M,Hom(N,P))."
---

The **tensor–Hom adjunction** (over a commutative ring \(R\)) is the natural isomorphism of abelian groups (indeed \(R\)-modules)
\[
\mathrm{Hom}_R(M\otimes_R N,\,P)\;\cong\;\mathrm{Hom}_R\!\bigl(M,\,\mathrm{Hom}_R(N,P)\bigr),
\]
natural in \(M,N,P\), where \(\otimes_R\) is the {{</* knowl id="tensor-product" text="tensor product" */>}} and \(\mathrm{Hom}_R(N,P)\) is the {{</* knowl id="hom-module" text="Hom module" */>}}. Concretely, a map \(f\colon M\otimes_R N\to P\) corresponds to the map \(\Phi(f)\colon M\to \mathrm{Hom}_R(N,P)\) defined by \(\Phi(f)(m)(n)=f(m\otimes n)\), with inverse \(\Psi(g)(m\otimes n)=g(m)(n)\).

This adjunction is a formal consequence of the {{</* knowl id="tensor-product-universal-property" text="universal property of the tensor product" */>}}: it linearizes {{</* knowl id="bilinear-map" text="bilinear maps" */>}}, and it specializes to duality when \(P=R\), giving \(\mathrm{Hom}_R(M\otimes_R N,R)\cong \mathrm{Hom}_R(M,N^\vee)\) with \(N^\vee\) the {{</* knowl id="dual-module" text="dual module" */>}}

**Examples:**
- Bilinear pairings \(M\times N\to P\) correspond to linear maps \(M\to \mathrm{Hom}_R(N,P)\).
- Taking \(P=R\) identifies bilinear forms \(M\times N\to R\) with linear maps \(M\to N^\vee\).
