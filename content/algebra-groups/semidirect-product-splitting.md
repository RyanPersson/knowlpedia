---
title: "Semidirect product from a splitting exact sequence"
description: "A split extension yields a semidirect product decomposition"
---

**Proposition (Semidirect product from splitting).**
Let
$$
1 \longrightarrow N \xrightarrow{\ \iota\ } G \xrightarrow{\ \pi\ } Q \longrightarrow 1
$$
be an {{< knowl id="exact-sequence-groups" text="exact sequence of groups" >}}. Suppose the sequence **splits**, meaning there exists a homomorphism $s:Q\to G$ (a section) such that $\pi\circ s=\mathrm{id}_Q$; equivalently, $G$ is a {{< knowl id="split-extension" text="split extension" >}} of $Q$ by $N$.

Then:
1. $\iota(N)$ is a normal subgroup of $G$ and we may identify $N$ with $\iota(N)\lhd G$.
2. Let $\varphi:Q\to \mathrm{Aut}(N)$ be the homomorphism defined by
   $$
   \varphi(q)(n) := s(q)\,n\,s(q)^{-1}\qquad (q\in Q,\ n\in N).
   $$
   Then $G$ is isomorphic to the {{< knowl id="semidirect-product" text="semidirect product" >}} $N\rtimes_{\varphi} Q$.
3. Under this isomorphism, every $g\in G$ can be written uniquely as $g = n\,s(q)$ with $n\in N$ and $q\in Q$.

**Context.**
This proposition is the standard bridge between abstract extensions and concrete constructions: split exact sequences are exactly semidirect products. The "internal" version is phrased via the {{< knowl id="internal-semidirect-product" text="internal semidirect product" >}} inside $G$.

**Proof sketch.**
Exactness implies $N=\ker(\pi)$, hence $N\lhd G$ by {{< knowl id="kernel-is-normal" text="kernel is normal" >}}. Define a map
$$
\Phi: N\rtimes_{\varphi} Q \to G,\qquad \Phi(n,q)=n\,s(q).
$$
Using the definition of the semidirect product multiplication (twisted by $\varphi$) and the fact that $s$ is a homomorphism, check $\Phi$ is a homomorphism. Surjectivity follows because $\pi(g)\in Q$ and $g\,s(\pi(g))^{-1}\in \ker(\pi)=N$. Injectivity and uniqueness come from $N\cap s(Q)=\{e\}$ (a consequence of $\pi\circ s=\mathrm{id}_Q$) and the factorization argument.
