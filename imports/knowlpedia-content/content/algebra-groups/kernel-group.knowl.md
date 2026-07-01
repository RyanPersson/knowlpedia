+++
id = "algebra-groups/kernel-group"
title = "Kernel of a group homomorphism"
kind = "knowl"
summary = "The set of elements mapped to the identity by a group homomorphism"
aliases = ["kernel-group", "Kernel of a group homomorphism"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/kernel-group.md"
+++

Let $\varphi\colon G\to H$ be a [[algebra-groups/group-homomorphism|group homomorphism]]. The **kernel** of $\varphi$ is the subset
$
\ker(\varphi)=\{g\in G : \varphi(g)=e_H\}.
$
Equivalently, $\ker(\varphi)$ is the [[shared-foundations/preimage|preimage]] of $\{e_H\}$ under $\varphi$.

The kernel is always a [[algebra-groups/normal-subgroup|normal subgroup]] of $G$. Moreover, $\varphi$ is a [[algebra-groups/group-monomorphism|monomorphism]] if and only if $\ker(\varphi)=\{e_G\}$. The kernel controls the "collapse" of $G$ under $\varphi$; the [[algebra-groups/first-isomorphism-theorem-groups|first isomorphism theorem]] identifies the quotient [[algebra-groups/quotient-group|quotient group]] $G/\ker(\varphi)$ with the image of $\varphi$.

**Examples:**
- For the reduction map $\pi\colon\mathbb{Z}\to\mathbb{Z}/n\mathbb{Z}$, one has $\ker(\pi)=n\mathbb{Z}$.
- For $\mathrm{sgn}\colon S_n\to\{\pm1\}$, the kernel is $A_n$.
- For $\det\colon GL_m(\mathbb{R})\to\mathbb{R}^\times$, the kernel is $SL_m(\mathbb{R})$.
