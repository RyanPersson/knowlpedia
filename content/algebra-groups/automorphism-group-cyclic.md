---
title: "Automorphisms of a cyclic group"
description: "Aut(C_n) is naturally isomorphic to (ℤ/nℤ)×"
---

**Proposition (Automorphism group of a finite cyclic group).**
Let $G$ be a cyclic group of order $n$, and identify $G\cong \mathbb Z/n\mathbb Z$ via {{</* knowl id="finite-cyclic-isomorphic-zn" text="the standard isomorphism" */>}}. Then
$$
\mathrm{Aut}(G)\ \cong\ (\mathbb Z/n\mathbb Z)^\times,
$$
where $(\mathbb Z/n\mathbb Z)^\times$ denotes the {{</* knowl id="group-of-units" text="group of units" */>}} of the ring $\mathbb Z/n\mathbb Z$.

Equivalently: if $G=\langle g\rangle$, then every automorphism $\alpha\in \mathrm{Aut}(G)$ is uniquely determined by $\alpha(g)=g^k$ with $\gcd(k,n)=1$, and composition corresponds to multiplication of $k$ modulo $n$.

**Context.**
This makes automorphisms of cyclic groups completely explicit: an automorphism is exactly the choice of a generator-image. The group $\mathrm{Aut}(G)$ itself is a central object in extension theory and semidirect products.

**Proof sketch.**
Define a map $(\mathbb Z/n\mathbb Z)^\times\to \mathrm{Aut}(\mathbb Z/n\mathbb Z)$ by sending $\overline{k}$ to multiplication-by-$\overline{k}$. This is a homomorphism. It is injective because multiplication-by-$\overline{k}$ is the identity only when $\overline{k}=\overline{1}$. It is surjective because any group endomorphism of a cyclic group is determined by the image of $1$, and it is invertible exactly when that image is a generator, i.e. a unit modulo $n$.
