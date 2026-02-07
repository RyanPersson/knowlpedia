---
title: "Automorphisms of a cyclic group"
description: "Aut(C_n) is naturally isomorphic to (ℤ/nℤ)×"
---

**Proposition (Automorphism group of a finite cyclic group).**
Let $G$ be a cyclic group of order $n$, and identify $G\cong \mathbb Z/n\mathbb Z$ via {{< knowl id="finite-cyclic-isomorphic-zn" text="the standard isomorphism" >}}. Then
$$
\mathrm{Aut}(G)\ \cong\ (\mathbb Z/n\mathbb Z)^\times,
$$

where $(\mathbb Z/n\mathbb Z)^\times$ denotes the {{< knowl id="group-of-units" section="algebra-rings" text="group of units" >}} of the ring $\mathbb Z/n\mathbb Z$.

Equivalently: if $G=\langle g\rangle$, then every automorphism $\alpha\in \mathrm{Aut}(G)$ is uniquely determined by $\alpha(g)=g^k$ with $\gcd(k,n)=1$, and composition corresponds to multiplication of $k$ modulo $n$.

**Context.**
This makes automorphisms of cyclic groups completely explicit: an automorphism is exactly the choice of a generator-image. The group $\mathrm{Aut}(G)$ itself is a central object in extension theory and semidirect products.
