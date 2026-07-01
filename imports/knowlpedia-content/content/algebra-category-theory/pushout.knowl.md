+++
id = "algebra-category-theory/pushout"
title = "Pushout"
kind = "knowl"
summary = "A universal object obtained by gluing two objects along a common source."
aliases = ["pushout"]
domains = ["algebra-category-theory"]
legacy_source_path = "algebra-category-theory/pushout.md"
+++

Let \(\mathcal{C}\) be a [[algebra-category-theory/category|category]] and let
\[
X \xleftarrow{f} Z \xrightarrow{g} Y
\]
be a span of [[algebra-category-theory/morphism|morphisms]].

A **pushout** of \((f,g)\) is an object \(P\) together with morphisms
\[
i_X:X\to P,\qquad i_Y:Y\to P
\]
such that
\[
i_X\circ f = i_Y\circ g
\]
(using [[algebra-category-theory/composition-category|composition]]), and satisfying the following universal property:

For any object \(W\) and morphisms \(u:X\to W\), \(v:Y\to W\) with \(u\circ f = v\circ g\), there exists a unique morphism \([u,v]:P\to W\) such that
\[
[u,v]\circ i_X = u,\qquad [u,v]\circ i_Y = v.
\]

When it exists, the pushout is unique up to unique [[algebra-category-theory/isomorphism-category|isomorphism]] and is often denoted \(X\amalg_Z Y\).

## Relationship to other constructions
- A pushout is a special [[algebra-category-theory/colimit|colimit]]: it is the colimit of the diagram \(X \leftarrow Z \rightarrow Y\).
- It is dual to a [[algebra-category-theory/pullback|pullback]].
- In many categories, it can be seen as a “coproduct with identifications,” relating it to the [[algebra-category-theory/coproduct|coproduct]].

## Examples
### Example (Set)
In \(\mathbf{Set}\), form the disjoint union \(X\amalg Y\) and impose the smallest [[shared-foundations/equivalence-relation|equivalence relation]] \(\sim\) such that
\[
f(z)\sim g(z)\quad\text{for all }z\in Z.
\]
Then the pushout is the [[shared-foundations/quotient-set|quotient set]]
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
