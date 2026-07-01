+++
id = "algebra-groups/semidirect-product-splitting"
title = "Semidirect product from a splitting exact sequence"
kind = "knowl"
summary = "A split extension yields a semidirect product decomposition"
aliases = ["semidirect-product-splitting", "Semidirect product from a splitting exact sequence"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/semidirect-product-splitting.md"
+++

**Proposition (Semidirect product from splitting).**
Let
$$
1 \longrightarrow N \xrightarrow{\ \iota\ } G \xrightarrow{\ \pi\ } Q \longrightarrow 1
$$

be an [[algebra-groups/exact-sequence-groups|exact sequence of groups]]. Suppose the sequence **splits**, meaning there exists a homomorphism $s:Q\to G$ (a section) such that $\pi\circ s=\mathrm{id}_Q$; equivalently, $G$ is a [[algebra-groups/split-extension|split extension]] of $Q$ by $N$.

Then:
1. $\iota(N)$ is a normal subgroup of $G$ and we may identify $N$ with $\iota(N)\lhd G$.
2. Let $\varphi:Q\to \mathrm{Aut}(N)$ be the homomorphism defined by
   $$
   \varphi(q)(n) := s(q)\,n\,s(q)^{-1}\qquad (q\in Q,\ n\in N).
   $$

   Then $G$ is isomorphic to the [[algebra-groups/semidirect-product|semidirect product]] $N\rtimes_{\varphi} Q$.
3. Under this isomorphism, every $g\in G$ can be written uniquely as $g = n\,s(q)$ with $n\in N$ and $q\in Q$.

**Context.**
This proposition is the standard bridge between abstract extensions and concrete constructions: split exact sequences are exactly semidirect products. The "internal" version is phrased via the [[algebra-groups/internal-semidirect-product|internal semidirect product]] inside $G$.
