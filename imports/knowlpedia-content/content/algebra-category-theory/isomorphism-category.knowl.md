+++
id = "algebra-category-theory/isomorphism-category"
title = "Isomorphism"
kind = "knowl"
summary = "A morphism that has a two-sided inverse in a category."
aliases = ["isomorphism-category", "Isomorphism"]
domains = ["algebra-category-theory"]
legacy_source_path = "algebra-category-theory/isomorphism-category.md"
+++

Let \(\mathcal C\) be a [[algebra-category-theory/category|category]]. A morphism \(f : X \to Y\) is an **isomorphism** if there exists a morphism \(g : Y \to X\) such that
\[
g\circ f = 1_X
\quad\text{and}\quad
f\circ g = 1_Y,
\]
where \(1_X\) and \(1_Y\) are the [[algebra-category-theory/identity-morphism|identity morphisms]] and \(\circ\) is [[algebra-category-theory/composition-category|composition]].

The morphism \(g\) is unique if it exists, and is denoted \(f^{-1}\). In this case, \(X\) and \(Y\) are said to be **isomorphic** (in \(\mathcal C\)).

Related notions:
- An isomorphism \(X\to X\) is an [[algebra-category-theory/automorphism-category|automorphism]].
- Every isomorphism is both a [[algebra-category-theory/monomorphism-category|monomorphism]] and an [[algebra-category-theory/epimorphism-category|epimorphism]].

## Examples
1. In \(\mathbf{Set}\), the isomorphisms are exactly the [[shared-foundations/bijective-function|bijective functions]].
2. In \(\mathbf{Grp}\), the isomorphisms are exactly group isomorphisms (bijective homomorphisms).
3. In \(R\text{-}\mathbf{Mod}\), the isomorphisms are exactly \(R\)-linear maps with \(R\)-linear inverses (invertible module homomorphisms).
