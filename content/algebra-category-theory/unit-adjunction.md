---
title: "Unit of an adjunction"
description: "For F ⊣ G, the unit η: Id_C ⇒ G∘F is the natural transformation corresponding to identities under the adjunction bijection."
---

Let \(F:\mathcal C\to\mathcal D\) and \(G:\mathcal D\to\mathcal C\) be {{< knowl id="functor" text="functors" >}} with an {{< knowl id="adjoint-functors" text="adjunction" >}} \(F\dashv G\).

## Definition (Unit)
The **unit** of the adjunction is a {{< knowl id="natural-transformation" text="natural transformation" >}}
\[
\eta:\mathrm{Id}_{\mathcal C}\Rightarrow G F
\]
characterized as follows: for each object \(c\in\mathcal C\), the component
\[
\eta_c: c \longrightarrow G(Fc)
\]
is the unique morphism corresponding to the identity \(\mathrm{id}_{F c}\in\operatorname{Hom}_{\mathcal D}(F c, F c)\) under the adjunction bijection
\[
\operatorname{Hom}_{\mathcal D}(F c,\, d)\cong \operatorname{Hom}_{\mathcal C}(c,\, G d)
\quad\text{(natural in \(c,d\)).}
\]
Equivalently, \(\eta\) is the transpose of \(\mathrm{id}_F\) under the natural isomorphism of hom-bifunctors.

The unit \(\eta\) and the {{< knowl id="counit-adjunction" text="counit" >}} \(\varepsilon\) satisfy the triangle identities (see {{< knowl id="adjoint-functors" text="adjoint functors" >}}):
\[
\varepsilon_{F c}\circ F(\eta_c)=\mathrm{id}_{F c}
\quad\text{for all }c\in\mathcal C.
\]

## Examples
1. **Free/forgetful (Set–Grp).** For \(F:\mathbf{Set}\to\mathbf{Grp}\) free group and \(U:\mathbf{Grp}\to\mathbf{Set}\) forgetful with \(F\dashv U\), the unit at a set \(X\) is the function
   \[
   \eta_X: X \to U(F(X))
   \]
   sending \(x\in X\) to the corresponding generator in the underlying set of the free group.

2. **Product–exponential (Set).** For the adjunction \((-)\times X \dashv (-)^X\) in \(\mathbf{Set}\), the unit at \(A\) is the function
   \[
   \eta_A: A \to (A\times X)^X,
   \qquad
   \eta_A(a)(x)=(a,x).
   \]
   It assigns to \(a\) the constant-in-\(A\) “graph” map \(X\to A\times X\).

3. **Abelianization–inclusion (Grp–Ab).** For \(\mathrm{ab}:\mathbf{Grp}\to\mathbf{Ab}\) left adjoint to \(i:\mathbf{Ab}\hookrightarrow \mathbf{Grp}\), the unit at a group \(G\) is the canonical quotient homomorphism
   \[
   \eta_G: G \twoheadrightarrow i(\mathrm{ab}(G)) \cong G/[G,G].
   \]
