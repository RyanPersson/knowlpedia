+++
id = "lie-groups/general-linear-group"
title = "General linear group"
kind = "knowl"
summary = "The Lie group GL(V) of invertible linear maps on a finite-dimensional vector space."
aliases = ["general-linear-group", "General linear group"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/general-linear-group.md"
+++

Let $V$ be a finite-dimensional real or complex vector space.

**Definition (General linear group).**
The **general linear group** of $V$ is
\[
\mathrm{GL}(V)=\{A:V\to V \text{ linear and invertible}\},
\]
with group operation given by composition. After choosing a basis, $\mathrm{GL}(V)\cong \mathrm{GL}_n(\mathbb F)$ where $\mathbb F=\mathbb R$ or $\mathbb C$ and
\[
\mathrm{GL}_n(\mathbb F)=\{A\in M_n(\mathbb F):\det(A)\ne 0\}.
\]

**Lie group structure.**
Viewed as a subset of the affine space $M_n(\mathbb F)$, $\mathrm{GL}_n(\mathbb F)$ is open (since $\det$ is continuous and $\mathbb F^\times$ is open), hence it is a smooth manifold and a [[fiber-bundles/lie-group|Lie group]]. Its Lie algebra is the [[lie-groups/general-linear-lie-algebra|general linear Lie algebra]] $\mathfrak{gl}_n(\mathbb F)$, identified with $T_I\mathrm{GL}_n(\mathbb F)$ (compare [[lie-groups/lie-algebra-of-a-lie-group|Lie algebra of a Lie group]]).

**Basic structure.**
Over $\mathbb C$, $\mathrm{GL}_n(\mathbb C)$ is connected. Over $\mathbb R$, $\mathrm{GL}_n(\mathbb R)$ has two connected components distinguished by the sign of $\det$. The [[lie-groups/exponential-map-lie-group|exponential map]] is the matrix exponential $\exp:\mathfrak{gl}_n(\mathbb F)\to \mathrm{GL}_n(\mathbb F)$.

**Context.**
Many linear representations of Lie groups are concretely [[lie-groups/lie-group-homomorphism|homomorphisms]] into some $\mathrm{GL}(V)$; special subgroups such as [[lie-groups/special-linear-group|SL_n]], [[lie-groups/orthogonal-group|O(n)]], and [[lie-groups/unitary-group|U(n)]] are defined by additional algebraic constraints.
