+++
id = "algebra-groups/group-isomorphism"
title = "Group isomorphism"
kind = "knowl"
summary = "A bijective group homomorphism"
aliases = ["group-isomorphism", "Group isomorphism"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/group-isomorphism.md"
+++

Let $G,H$ be groups. A **group isomorphism** is a [[algebra-groups/group-homomorphism|group homomorphism]] $\varphi\colon G\to H$ that is bijective as a [[shared-foundations/bijective-function|bijective function]].

If $\varphi$ is an isomorphism, then its [[shared-foundations/inverse-function|inverse function]] $\varphi^{-1}\colon H\to G$ is also a group homomorphism, so $\varphi$ gives a structure-preserving identification between $G$ and $H$. One writes $G\cong H$ to denote that there exists a group isomorphism between them.

**Examples:**
- The map $\mathbb{Z}\to 2\mathbb{Z}$ given by $n\mapsto 2n$ is a group isomorphism (additive groups).
- For each $n\ge 1$, any cyclic group of order $n$ is isomorphic to $\mathbb{Z}/n\mathbb{Z}$.
- The map $G\to G$ given by $g\mapsto xgx^{-1}$ (for fixed $x\in G$) is an isomorphism (an inner automorphism).
