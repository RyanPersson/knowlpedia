+++
id = "lie-groups/direct-sum-of-lie-algebras"
title = "Direct sum of Lie algebras"
kind = "knowl"
summary = "The product vector space with componentwise bracket, modeling Lie algebras of product groups."
aliases = ["direct-sum-of-lie-algebras", "Direct sum of Lie algebras"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/direct-sum-of-lie-algebras.md"
+++

Let $\mathfrak g$ and $\mathfrak h$ be [[lie-groups/lie-algebra|Lie algebras]] over the same field.

The **direct sum Lie algebra** $\mathfrak g\oplus \mathfrak h$ is the direct sum as vector spaces equipped with the bracket
\[
[(X_1,Y_1),(X_2,Y_2)] := \bigl([X_1,X_2]_{\mathfrak g},\; [Y_1,Y_2]_{\mathfrak h}\bigr).
\]
With this bracket, the inclusions $\mathfrak g\hookrightarrow \mathfrak g\oplus\mathfrak h$ and $\mathfrak h\hookrightarrow \mathfrak g\oplus\mathfrak h$ are Lie algebra homomorphisms, and $\mathfrak g$ and $\mathfrak h$ commute inside the sum.

## Universal property
Giving a Lie algebra homomorphism $\mathfrak g\oplus\mathfrak h\to\mathfrak k$ is equivalent to giving homomorphisms $\mathfrak g\to\mathfrak k$ and $\mathfrak h\to\mathfrak k$ whose images commute.

## Relation to Lie groups
If $G$ and $H$ are Lie groups, then the Lie algebra of the [[lie-groups/product-lie-group|product Lie group]] $G\times H$ is canonically
\[
\mathrm{Lie}(G\times H)\cong \mathrm{Lie}(G)\oplus \mathrm{Lie}(H),
\]
as recorded in [[lie-groups/lie-algebra-of-product|Lie algebra of a product]].

**Context.** Many decomposition results (e.g. [[lie-groups/semisimple-direct-sum-simple|semisimple as a direct sum of simples]]) are literally statements that a Lie algebra splits as a direct sum of ideals.
