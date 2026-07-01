+++
id = "lie-groups/product-lie-group"
title = "Product Lie group"
kind = "knowl"
summary = "The Cartesian product of Lie groups, with componentwise multiplication, is again a Lie group."
aliases = ["product-lie-group", "Product Lie group"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/product-lie-group.md"
+++

Given Lie groups $G$ and $H$ (see [[fiber-bundles/lie-group|Lie group]]), their **product Lie group** is the manifold $G\times H$ with group structure
\[
(g,h)\cdot(g',h')=(gg',hh'),\qquad (g,h)^{-1}=(g^{-1},h^{-1}).
\]
With the product smooth structure, the multiplication and inversion maps are smooth, so $G\times H$ is a Lie group. The coordinate projections
\[
\mathrm{pr}_G:G\times H\to G,\qquad \mathrm{pr}_H:G\times H\to H
\]
are smooth group homomorphisms (see [[lie-groups/lie-group-homomorphism|Lie group homomorphism]]).

On the infinitesimal level, the Lie algebra satisfies
\[
\mathrm{Lie}(G\times H)\;\cong\;\mathrm{Lie}(G)\oplus \mathrm{Lie}(H),
\]
compatibly with brackets (see [[lie-groups/lie-algebra-of-product|Lie algebra of a product]] and [[lie-groups/direct-sum-of-lie-algebras|direct sum of Lie algebras]]). Under this identification, the exponential map (see [[lie-groups/exponential-map-lie-group|exponential map]]) splits:
\[
\exp_{G\times H}(X,Y)=\big(\exp_G(X),\exp_H(Y)\big).
\]

This construction is ubiquitous: representation theory often reduces statements about a product to separate statements about factors (compare with [[lie-groups/tensor-product-of-representations-lie|tensor products of representations]] and [[lie-groups/irreducible-representation-lie-group|irreducibles]]).
