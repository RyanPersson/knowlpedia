---
title: "Universal covering group"
description: "A simply connected covering Lie group of a connected Lie group , unique up to isomorphism."
---

### Definition
Let $G$ be a connected Lie group. A **universal covering group** of $G$ is a pair $(\widetilde G,p)$ where:
- $\widetilde G$ is a {{< knowl id="simply-connected-lie-group" text="simply connected Lie group" >}},
- $p:\widetilde G\to G$ is a smooth covering map that is also a {{< knowl id="lie-group-homomorphism" text="Lie group homomorphism" >}},
- and $p$ is universal among covering Lie groups of $G$ in the sense that any {{< knowl id="covering-lie-group" text="covering Lie group" >}} $q:H\to G$ factors uniquely through $p$ by a Lie group homomorphism $H\to \widetilde G$ commuting with the projections to $G$.

The existence of such a pair is guaranteed by {{< knowl id="universal-covering-group-existence" text="the existence theorem for universal covering groups" >}}.

### Kernel and fundamental group
The kernel $\ker(p)$ is a discrete normal subgroup of $\widetilde G$ (see {{< knowl id="discrete-subgroup" text="discrete subgroups" >}}) and in fact lies in the {{< knowl id="center-of-a-lie-group" text="center of $\\widetilde G$" >}}. Topologically, $\ker(p)$ is naturally isomorphic to the fundamental group $\pi_1(G)$ once basepoints are chosen. Consequently,
$$
G \cong \widetilde G / \ker(p)
$$
as a {{< knowl id="quotient-lie-group" text="quotient Lie group" >}}.

### Lie algebra
The differential $dp_e:\mathrm{Lie}(\widetilde G)\to \mathrm{Lie}(G)$ is an isomorphism of Lie algebras (compare {{< knowl id="differential-is-lie-algebra-homomorphism" text="differentials of Lie group homomorphisms" >}}). Thus covering changes global topology but not the infinitesimal structure.
