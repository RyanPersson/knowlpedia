+++
id = "algebra-category-theory/pullback"
title = "Pullback"
kind = "knowl"
summary = "A universal object representing compatible pairs over a cospan."
aliases = ["pullback"]
domains = ["algebra-category-theory"]
legacy_source_path = "algebra-category-theory/pullback.md"
+++

Let \(\mathcal{C}\) be a [[algebra-category-theory/category|category]] and let
\[
X \xrightarrow{f} Z \xleftarrow{g} Y
\]
be a cospan of [[algebra-category-theory/morphism|morphisms]].

A **pullback** (or **fiber product**) of \((f,g)\) is an object \(P\) together with morphisms
\[
p_X:P\to X,\qquad p_Y:P\to Y
\]
such that
\[
f\circ p_X = g\circ p_Y
\]
(using [[algebra-category-theory/composition-category|composition]]), and satisfying the following universal property:

For any object \(W\) and morphisms \(u:W\to X\), \(v:W\to Y\) with \(f\circ u = g\circ v\), there exists a unique morphism \(\langle u,v\rangle:W\to P\) such that
\[
p_X\circ \langle u,v\rangle = u,\qquad p_Y\circ \langle u,v\rangle = v.
\]

When it exists, the pullback is unique up to unique [[algebra-category-theory/isomorphism-category|isomorphism]] and is often denoted \(X\times_Z Y\).

## Relationship to other constructions
- A pullback is a special [[algebra-category-theory/limit|limit]]: it is the limit of the diagram \(X\to Z \leftarrow Y\).
- In categories with [[algebra-category-theory/categorical-product|products]] and [[algebra-category-theory/equalizer|equalizers]], one can realize a pullback as an equalizer of the two maps
  \[
  X\times Y \rightrightarrows Z,\quad (x,y)\mapsto f(x),\ (x,y)\mapsto g(y).
  \]

## Examples
### Example (Set)
In \(\mathbf{Set}\), the pullback is the subset of the [[shared-foundations/cartesian-product|cartesian product]]
\[
X\times Y=\{(x,y)\}
\]
(consisting of [[shared-foundations/ordered-pair|ordered pairs]]) given by
\[
X\times_Z Y \;=\; \{(x,y)\in X\times Y \mid f(x)=g(y)\}.
\]
The maps \(p_X,p_Y\) are the coordinate projections.

### Example (Grp)
In \(\mathbf{Grp}\), the pullback of \(f:X\to Z\) and \(g:Y\to Z\) is the subgroup
\[
X\times_Z Y \;=\; \{(x,y)\in X\times Y \mid f(x)=g(y)\},
\]
with group operation defined componentwise and projections \(p_X,p_Y\).

### Example (Top)
In \(\mathbf{Top}\), the pullback is the same set-theoretic fiber product as in \(\mathbf{Set}\), equipped with the subspace topology inherited from \(X\times Y\) (with the product topology). The projections are continuous and satisfy the universal property in \(\mathbf{Top}\).
