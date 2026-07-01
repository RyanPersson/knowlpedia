+++
id = "algebra-category-theory/endomorphism-category"
title = "Endomorphism"
kind = "knowl"
summary = "A morphism whose domain and codomain are the same object."
aliases = ["endomorphism-category", "Endomorphism"]
domains = ["algebra-category-theory"]
legacy_source_path = "algebra-category-theory/endomorphism-category.md"
+++

Let \(\mathcal C\) be a [[algebra-category-theory/category|category]] and let \(A\) be an [[algebra-category-theory/object|object]] of \(\mathcal C\).

An **endomorphism** of \(A\) is a [[algebra-category-theory/morphism|morphism]]
\[
f:A\longrightarrow A.
\]
The set of endomorphisms of \(A\) is denoted
\[
\mathrm{End}_{\mathcal C}(A)\;:=\;\mathrm{Hom}_{\mathcal C}(A,A).
\]

## Algebraic structure
With [[algebra-category-theory/composition-category|composition]] as multiplication,
\[
(f,g)\mapsto f\circ g,
\]
the set \(\mathrm{End}_{\mathcal C}(A)\) is a monoid with identity element the [[algebra-category-theory/identity-morphism|identity morphism]] \(\mathrm{id}_A\).

An endomorphism is an [[algebra-category-theory/automorphism-category|automorphism]] precisely when it is invertible (i.e., an [[algebra-category-theory/isomorphism-category|isomorphism]] \(A\to A\)).

## Examples
1. **\(\mathbf{Set}\):** Endomorphisms of a set \(X\) are just [[shared-foundations/function|functions]] \(X\to X\).

2. **\(\mathbf{Grp}\) / \(\mathbf{Ab}\):** Endomorphisms of a group (or abelian group) \(G\) are group homomorphisms \(G\to G\).
   For example, \(n\mapsto kn\) defines an endomorphism of \(\mathbb Z\) for each integer \(k\).

3. **\(R\mathbf{-Mod}\):** Endomorphisms of an \(R\)-module \(M\) are \(R\)-linear maps \(M\to M\).
   For a free module \(R^n\), \(\mathrm{End}_R(R^n)\) can be identified with the ring of \(n\times n\) matrices over \(R\) (via the action on the standard basis).
