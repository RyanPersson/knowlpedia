+++
id = "algebra-groups/group-epimorphism"
title = "Group epimorphism"
kind = "knowl"
summary = "A surjective group homomorphism"
aliases = ["group-epimorphism", "Group epimorphism"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/group-epimorphism.md"
+++

A **group epimorphism** is a [[algebra-groups/group-homomorphism|group homomorphism]] $\varphi\colon G\to H$ that is surjective as a [[shared-foundations/surjective-function|surjective function]].

Equivalently, $\varphi$ is an epimorphism if and only if its [[algebra-groups/image-group|image]] equals all of $H$, i.e. $\varphi(G)=H$. Many natural epimorphisms arise as quotient maps: if $N\lhd G$ then the canonical projection $G\to$ [[algebra-groups/quotient-group|quotient group]] $G/N$ is surjective.

**Examples:**
- The reduction map $\mathbb{Z}\to\mathbb{Z}/n\mathbb{Z}$ is an epimorphism of additive groups.
- The projection $G\times H\to G$ is a group epimorphism.
- The sign map $\mathrm{sgn}\colon S_n\to\{\pm 1\}$ is a group epimorphism for $n\ge 2$.
