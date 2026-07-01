+++
id = "lie-groups/abelian-lie-group"
title = "Abelian Lie group"
kind = "knowl"
summary = "A Lie group with commutative multiplication."
aliases = ["abelian-lie-group", "Abelian Lie group"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/abelian-lie-group.md"
+++

Let $G$ be a [[fiber-bundles/lie-group|Lie group]].

**Definition.** $G$ is **abelian** if its multiplication is commutative:
$$
gh=hg \quad \text{for all } g,h\in G.
$$

Equivalently, the [[lie-groups/commutator-subgroup-of-a-lie-group|commutator subgroup]] $[G,G]$ is trivial, or (for connected $G$) its Lie algebra [[lie-groups/lie-algebra-of-a-lie-group|$\mathfrak{g}=\mathrm{Lie}(G)$]] is an [[lie-groups/abelian-lie-algebra|abelian Lie algebra]].

**Motivation.** For abelian $G$, the [[lie-groups/baker-campbell-hausdorff-formula|Baker–Campbell–Hausdorff formula]] collapses to ordinary addition in the Lie algebra: in exponential coordinates, local multiplication is just $X+Y$. This is one reason connected abelian Lie groups admit an explicit classification (see [[lie-groups/connected-abelian-lie-group-structure|structure of connected abelian Lie groups]]).

**Remark.** Any [[lie-groups/coset-space|quotient]] of an abelian Lie group by a closed subgroup is again abelian, and its Lie algebra is a [[lie-groups/quotient-lie-algebra|quotient Lie algebra]] of $\mathfrak{g}$.
