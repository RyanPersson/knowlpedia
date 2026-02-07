---
title: "Adjoint functors"
description: "A pair of functors F ⊣ G equipped with a natural hom-set bijection (equivalently, a unit and counit satisfying the triangle identities)."
---

Let \(\mathcal C,\mathcal D\) be a {{< knowl id="category" text="category" >}} and let
\(F:\mathcal C\to\mathcal D\) and \(G:\mathcal D\to\mathcal C\) be {{< knowl id="functor" text="functors" >}}.

## Definition (Adjunction)
We say **\(F\) is left adjoint to \(G\)**, and write \(F \dashv G\), if for every object \(c\in\mathcal C\) and \(d\in\mathcal D\) there is a bijection of sets
\[
\Phi_{c,d}:\operatorname{Hom}_{\mathcal D}(F c,\, d)\;\xrightarrow{\;\cong\;}\;\operatorname{Hom}_{\mathcal C}(c,\, G d),
\]
which is **natural in \(c\) and \(d\)** (i.e. it is a natural isomorphism of bifunctors
\(\operatorname{Hom}_{\mathcal D}(F-, -)\cong \operatorname{Hom}_{\mathcal C}(-, G-)\)).

Elements of \(\operatorname{Hom}\) are {{< knowl id="morphism" text="morphisms" >}}; the naturality condition says that \(\Phi\) commutes with pre- and post-composition in the two variables (using {{< knowl id="composition-category" text="composition" >}} in \(\mathcal C,\mathcal D\)).

## Equivalent data: unit and counit
An adjunction \(F\dashv G\) is equivalently specified by:
- a **unit** \(\eta:\mathrm{Id}_{\mathcal C}\Rightarrow G F\), a {{< knowl id="natural-transformation" text="natural transformation" >}} (see {{< knowl id="unit-adjunction" text="unit" >}}),
- a **counit** \(\varepsilon:F G\Rightarrow \mathrm{Id}_{\mathcal D}\), a {{< knowl id="natural-transformation" text="natural transformation" >}} (see {{< knowl id="counit-adjunction" text="counit" >}}),

such that the **triangle identities** hold for all \(c\in\mathcal C\), \(d\in\mathcal D\):
\[
\varepsilon_{F c}\circ F(\eta_c)=\mathrm{id}_{F c},
\qquad
G(\varepsilon_d)\circ \eta_{G d}=\mathrm{id}_{G d}.
\]
(Here \(\mathrm{id}\) is the {{< knowl id="identity-morphism" text="identity morphism" >}}.)

If moreover \(\eta\) and \(\varepsilon\) are {{< knowl id="natural-isomorphism" text="natural isomorphisms" >}}, then \(F\) and \(G\) form an {{< knowl id="equivalence-of-categories" text="equivalence of categories" >}}.

## Examples
1. **Free/forgetful (Set–Grp).** The free group functor \(F:\mathbf{Set}\to\mathbf{Grp}\) is left adjoint to the forgetful functor \(U:\mathbf{Grp}\to\mathbf{Set}\). Concretely,
   \[
   \operatorname{Hom}_{\mathbf{Grp}}(F(X),\,H)\cong \operatorname{Hom}_{\mathbf{Set}}(X,\,U(H)),
   \]
   naturally in a {{< knowl id="set" section="shared-foundations" text="set" >}} \(X\) and a group \(H\).

2. **Product–exponential (Set).** Fix a set \(X\). In \(\mathbf{Set}\), the functor \((-)\times X\) is left adjoint to the exponential functor \((-)^X=\operatorname{Hom}(X,-)\):
   \[
   \operatorname{Hom}(A\times X,\,B)\cong \operatorname{Hom}(A,\,B^X),
   \]
   naturally in \(A,B\in\mathbf{Set}\). (This is the usual currying bijection.)

3. **Abelianization–inclusion (Grp–Ab).** Let \(i:\mathbf{Ab}\hookrightarrow \mathbf{Grp}\) be the inclusion. The abelianization functor \(\mathrm{ab}:\mathbf{Grp}\to\mathbf{Ab}\), \(G\mapsto G/[G,G]\), is left adjoint to \(i\):
   \[
   \operatorname{Hom}_{\mathbf{Ab}}(\mathrm{ab}(G),\,A)\cong \operatorname{Hom}_{\mathbf{Grp}}(G,\,i(A)).
   \]
