+++
id = "algebra-category-theory/automorphism-category"
title = "Automorphism"
kind = "knowl"
summary = "An isomorphism from an object to itself; an invertible endomorphism."
aliases = ["automorphism-category", "Automorphism"]
domains = ["algebra-category-theory"]
legacy_source_path = "algebra-category-theory/automorphism-category.md"
+++

Let \(\mathcal C\) be a [[algebra-category-theory/category|category]] and \(A\) an [[algebra-category-theory/object|object]] of \(\mathcal C\).

An **automorphism** of \(A\) is an [[algebra-category-theory/isomorphism-category|isomorphism]]
\[
f:A\longrightarrow A.
\]
Equivalently, it is an [[algebra-category-theory/endomorphism-category|endomorphism]] \(f:A\to A\) for which there exists \(g:A\to A\) such that
\[
g\circ f = \mathrm{id}_A,\qquad f\circ g = \mathrm{id}_A,
\]
where \(\mathrm{id}_A\) is the [[algebra-category-theory/identity-morphism|identity morphism]].

The set of automorphisms of \(A\) is denoted \(\mathrm{Aut}_{\mathcal C}(A)\).

## Group structure
With [[algebra-category-theory/composition-category|composition]] as the operation, \(\mathrm{Aut}_{\mathcal C}(A)\) is a group:
- identity element: \(\mathrm{id}_A\),
- inverse: \(f^{-1}\) (the inverse isomorphism).

## Examples
1. **\(\mathbf{Set}\):** Automorphisms of a set \(X\) are exactly the [[shared-foundations/bijective-function|bijections]] \(X\to X\).
   Thus \(\mathrm{Aut}_{\mathbf{Set}}(X)\) is the permutation group of \(X\).

2. **\(\mathbf{Grp}\):** Automorphisms of a group \(G\) are group isomorphisms \(G\to G\).
   Example: \(\mathrm{Aut}_{\mathbf{Grp}}(\mathbb Z)\cong\{\pm 1\}\), since any automorphism is determined by where it sends \(1\).

3. **\(R\mathbf{-Mod}\):** Automorphisms of an \(R\)-module \(M\) are the invertible \(R\)-linear maps \(M\to M\).
   For \(M=R^n\), \(\mathrm{Aut}_R(R^n)\) identifies with the group \(\mathrm{GL}_n(R)\) of invertible \(n\times n\) matrices over \(R\).
