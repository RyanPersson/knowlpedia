+++
id = "algebra-groups/direct-product-groups"
title = "Direct Product of Groups"
kind = "knowl"
summary = "The product group with componentwise multiplication"
aliases = ["direct-product-groups", "Direct Product of Groups"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/direct-product-groups.md"
+++

Given [[algebra-groups/group|groups]] $G$ and $H$, their (external) **direct product** is the set [[shared-foundations/cartesian-product|Cartesian product]] $G\times H$ equipped with componentwise multiplication:
$$
(g_1,h_1)\cdot(g_2,h_2) := (g_1g_2,\;h_1h_2).
$$

With this operation, $G\times H$ is a group, with identity $(e_G,e_H)$ and inverse $(g,h)^{-1}=(g^{-1},h^{-1})$.

The maps $\pi_G:G\times H\to G$ and $\pi_H:G\times H\to H$ given by projection onto components are [[algebra-groups/group-homomorphism|group homomorphisms]]. Conversely, to give a homomorphism $K\to G\times H$ is equivalent to giving a pair of homomorphisms $K\to G$ and $K\to H$.

**Examples:**
- $\mathbb{Z}\times\mathbb{Z}$ is the free abelian group of rank $2$ under addition.
- $C_2\times C_2$ is the Klein four-group (an abelian group of order $4$).
- If $G$ and $H$ are finite, then $|G\times H| = |G|\cdot |H|$.
