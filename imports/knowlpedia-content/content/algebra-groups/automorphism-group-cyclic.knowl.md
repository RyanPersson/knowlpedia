+++
id = "algebra-groups/automorphism-group-cyclic"
title = "Automorphisms of a cyclic group"
kind = "knowl"
summary = "Aut(C_n) is naturally isomorphic to (ℤ/nℤ)×"
aliases = ["automorphism-group-cyclic", "Automorphisms of a cyclic group"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/automorphism-group-cyclic.md"
+++

**Proposition (Automorphism group of a finite cyclic group).**
Let $G$ be a cyclic group of order $n$, and identify $G\cong \mathbb Z/n\mathbb Z$ via [[algebra-groups/finite-cyclic-isomorphic-zn|the standard isomorphism]]. Then
$$
\mathrm{Aut}(G)\ \cong\ (\mathbb Z/n\mathbb Z)^\times,
$$

where $(\mathbb Z/n\mathbb Z)^\times$ denotes the [[algebra-rings/group-of-units|group of units]] of the ring $\mathbb Z/n\mathbb Z$.

Equivalently: if $G=\langle g\rangle$, then every automorphism $\alpha\in \mathrm{Aut}(G)$ is uniquely determined by $\alpha(g)=g^k$ with $\gcd(k,n)=1$, and composition corresponds to multiplication of $k$ modulo $n$.

**Context.**
This makes automorphisms of cyclic groups completely explicit: an automorphism is exactly the choice of a generator-image. The group $\mathrm{Aut}(G)$ itself is a central object in extension theory and semidirect products.
