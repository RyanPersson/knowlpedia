+++
id = "algebra-groups/group-homomorphism"
title = "Group homomorphism"
kind = "knowl"
summary = "A map between groups that preserves the group operation"
aliases = ["group-homomorphism", "Group homomorphism"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/group-homomorphism.md"
+++

Let $G,H$ be [[algebra-groups/group|groups]]. A **group homomorphism** is a [[shared-foundations/function|function]] $\varphi\colon G\to H$ such that for all $x,y\in G$,
$
\varphi(xy)=\varphi(x)\varphi(y).
$
(Here $xy$ denotes the product in $G$ and $\varphi(x)\varphi(y)$ the product in $H$.)

Basic consequences of the defining identity include: $\varphi(e_G)=e_H$ and $\varphi(x^{-1})=\varphi(x)^{-1}$ for all $x\in G$. Two fundamental associated subgroups are the [[algebra-groups/kernel-group|kernel]] and the [[algebra-groups/image-group|image]] of $\varphi$. These are tied together by the [[algebra-groups/first-isomorphism-theorem-groups|first isomorphism theorem]].

**Examples:**
- For $n\ge 1$, the reduction map $\pi\colon \mathbb{Z}\to \mathbb{Z}/n\mathbb{Z}$ given by $\pi(k)=k\bmod n$ is a homomorphism of additive groups.
- The determinant $\det\colon GL_m(\mathbb{R})\to \mathbb{R}^\times$ is a group homomorphism under multiplication.
- If $H\le G$, the inclusion map $H\hookrightarrow G$ is a group homomorphism.
