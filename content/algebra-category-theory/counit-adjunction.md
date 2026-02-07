---
title: "Counit of an adjunction"
description: "For F ⊣ G, the counit ε: F∘G ⇒ Id_D is the natural transformation corresponding to identities under the adjunction bijection."
---

Let \(F:\mathcal C\to\mathcal D\) and \(G:\mathcal D\to\mathcal C\) be {{< knowl id="functor" text="functors" >}} with an {{< knowl id="adjoint-functors" text="adjunction" >}} \(F\dashv G\).

## Definition (Counit)
The **counit** of the adjunction is a {{< knowl id="natural-transformation" text="natural transformation" >}}
\[
\varepsilon: F G \Rightarrow \mathrm{Id}_{\mathcal D}
\]
characterized as follows: for each object \(d\in\mathcal D\), the component
\[
\varepsilon_d: F(Gd) \longrightarrow d
\]
is the unique morphism corresponding to the identity \(\mathrm{id}_{G d}\in\operatorname{Hom}_{\mathcal C}(G d, G d)\) under the adjunction bijection
\[
\operatorname{Hom}_{\mathcal D}(F c,\, d)\cong \operatorname{Hom}_{\mathcal C}(c,\, G d).
\]
Equivalently, \(\varepsilon\) is the transpose of \(\mathrm{id}_G\).

The counit \(\varepsilon\) and the {{< knowl id="unit-adjunction" text="unit" >}} \(\eta\) satisfy the triangle identities:
\[
G(\varepsilon_d)\circ \eta_{G d}=\mathrm{id}_{G d}
\quad\text{for all }d\in\mathcal D.
\]

## Examples
1. **Free/forgetful (Set–Grp).** For \(F\dashv U\) (free group and forgetful), the counit at a group \(H\) is the homomorphism
   \[
   \varepsilon_H: F(U(H)) \to H
   \]
   sending a formal word in the underlying set \(U(H)\) to its evaluation in \(H\).

2. **Product–exponential (Set).** For \((-)\times X \dashv (-)^X\) in \(\mathbf{Set}\), the counit at \(B\) is the evaluation map
   \[
   \varepsilon_B: B^X \times X \to B,
   \qquad
   \varepsilon_B(f,x)=f(x).
   \]

3. **Abelianization–inclusion (Grp–Ab).** For \(\mathrm{ab}\dashv i\), the counit at an abelian group \(A\) is (canonically) the identity isomorphism
   \[
   \varepsilon_A: \mathrm{ab}(i(A)) \xrightarrow{\ \cong\ } A,
   \]
   since the abelianization of an already abelian group is itself.
