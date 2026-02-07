---
title: "Pushout"
description: "A universal object obtained by gluing two objects along a common source."
---

Let \(\mathcal{C}\) be a {{< knowl id="category" text="category" >}} and let
\[
X \xleftarrow{f} Z \xrightarrow{g} Y
\]
be a span of {{< knowl id="morphism" text="morphisms" >}}.

A **pushout** of \((f,g)\) is an object \(P\) together with morphisms
\[
i_X:X\to P,\qquad i_Y:Y\to P
\]
such that
\[
i_X\circ f = i_Y\circ g
\]
(using {{< knowl id="composition-category" text="composition" >}}), and satisfying the following universal property:

For any object \(W\) and morphisms \(u:X\to W\), \(v:Y\to W\) with \(u\circ f = v\circ g\), there exists a unique morphism \([u,v]:P\to W\) such that
\[
[u,v]\circ i_X = u,\qquad [u,v]\circ i_Y = v.
\]

When it exists, the pushout is unique up to unique {{< knowl id="isomorphism-category" text="isomorphism" >}} and is often denoted \(X\amalg_Z Y\).

## Relationship to other constructions
- A pushout is a special {{< knowl id="colimit" text="colimit" >}}: it is the colimit of the diagram \(X \leftarrow Z \rightarrow Y\).
- It is dual to a {{< knowl id="pullback" text="pullback" >}}.
- In many categories, it can be seen as a “coproduct with identifications,” relating it to the {{< knowl id="coproduct" text="coproduct" >}}.

## Examples
### Example (Set)
In \(\mathbf{Set}\), form the disjoint union \(X\amalg Y\) and impose the smallest {{< knowl id="equivalence-relation" section="shared-foundations" text="equivalence relation" >}} \(\sim\) such that
\[
f(z)\sim g(z)\quad\text{for all }z\in Z.
\]
Then the pushout is the {{< knowl id="quotient-set" section="shared-foundations" text="quotient set" >}}
\[
P = (X\amalg Y)/{\sim},
\]
with \(i_X,i_Y\) induced by the coproduct injections \(X\to X\amalg Y\), \(Y\to X\amalg Y\).

### Example (Top)
In \(\mathbf{Top}\), the pushout of \(X \xleftarrow{f} Z \xrightarrow{g} Y\) is the quotient space
\[
P = (X\amalg Y)/{\sim},
\]
where \(\sim\) identifies \(f(z)\) with \(g(z)\) for each \(z\in Z\), and the topology is the quotient topology. This models “gluing spaces along a common subspace.”

### Example (Grp)
In \(\mathbf{Grp}\), the pushout of \(X \xleftarrow{f} Z \xrightarrow{g} Y\) is the **amalgamated free product**
\[
X *_Z Y,
\]
characterized by the universal property that homomorphisms out of \(X\) and \(Y\) that agree on \(Z\) factor uniquely through \(X *_Z Y\).
