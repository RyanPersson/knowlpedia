---
title: "Product Lie group"
description: "The Cartesian product of Lie groups, with componentwise multiplication, is again a Lie group."
---

Given Lie groups $G$ and $H$ (see {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}}), their **product Lie group** is the manifold $G\times H$ with group structure
\[
(g,h)\cdot(g',h')=(gg',hh'),\qquad (g,h)^{-1}=(g^{-1},h^{-1}).
\]
With the product smooth structure, the multiplication and inversion maps are smooth, so $G\times H$ is a Lie group. The coordinate projections
\[
\mathrm{pr}_G:G\times H\to G,\qquad \mathrm{pr}_H:G\times H\to H
\]
are smooth group homomorphisms (see {{< knowl id="lie-group-homomorphism" text="Lie group homomorphism" >}}).

On the infinitesimal level, the Lie algebra satisfies
\[
\mathrm{Lie}(G\times H)\;\cong\;\mathrm{Lie}(G)\oplus \mathrm{Lie}(H),
\]
compatibly with brackets (see {{< knowl id="lie-algebra-of-product" text="Lie algebra of a product" >}} and {{< knowl id="direct-sum-of-lie-algebras" text="direct sum of Lie algebras" >}}). Under this identification, the exponential map (see {{< knowl id="exponential-map-lie-group" text="exponential map" >}}) splits:
\[
\exp_{G\times H}(X,Y)=\big(\exp_G(X),\exp_H(Y)\big).
\]

This construction is ubiquitous: representation theory often reduces statements about a product to separate statements about factors (compare with {{< knowl id="tensor-product-of-representations-lie" text="tensor products of representations" >}} and {{< knowl id="irreducible-representation-lie-group" text="irreducibles" >}}).
