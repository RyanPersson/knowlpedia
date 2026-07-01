+++
id = "lie-groups/universal-covering-group"
title = "Universal covering group"
kind = "knowl"
summary = "A simply connected covering Lie group of a connected Lie group , unique up to isomorphism."
aliases = ["universal-covering-group", "Universal covering group"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/universal-covering-group.md"
+++

### Definition
Let $G$ be a connected Lie group. A **universal covering group** of $G$ is a pair $(\widetilde G,p)$ where:
- $\widetilde G$ is a [[lie-groups/simply-connected-lie-group|simply connected Lie group]],
- $p:\widetilde G\to G$ is a smooth covering map that is also a [[lie-groups/lie-group-homomorphism|Lie group homomorphism]],
- and $p$ is universal among covering Lie groups of $G$ in the sense that any [[lie-groups/covering-lie-group|covering Lie group]] $q:H\to G$ factors uniquely through $p$ by a Lie group homomorphism $H\to \widetilde G$ commuting with the projections to $G$.

The existence of such a pair is guaranteed by [[lie-groups/universal-covering-group-existence|the existence theorem for universal covering groups]].

### Kernel and fundamental group
The kernel $\ker(p)$ is a discrete normal subgroup of $\widetilde G$ (see [[lie-groups/discrete-subgroup|discrete subgroups]]) and in fact lies in the [[lie-groups/center-of-a-lie-group|center of $\\widetilde G$]]. Topologically, $\ker(p)$ is naturally isomorphic to the fundamental group $\pi_1(G)$ once basepoints are chosen. Consequently,
$$
G \cong \widetilde G / \ker(p)
$$
as a [[lie-groups/quotient-lie-group|quotient Lie group]].

### Lie algebra
The differential $dp_e:\mathrm{Lie}(\widetilde G)\to \mathrm{Lie}(G)$ is an isomorphism of Lie algebras (compare [[lie-groups/differential-is-lie-algebra-homomorphism|differentials of Lie group homomorphisms]]). Thus covering changes global topology but not the infinitesimal structure.
