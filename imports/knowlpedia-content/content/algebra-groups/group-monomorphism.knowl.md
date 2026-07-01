+++
id = "algebra-groups/group-monomorphism"
title = "Group monomorphism"
kind = "knowl"
summary = "An injective group homomorphism"
aliases = ["group-monomorphism", "Group monomorphism"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/group-monomorphism.md"
+++

A **group monomorphism** is a [[algebra-groups/group-homomorphism|group homomorphism]] $\varphi\colon G\to H$ that is injective as an [[shared-foundations/injective-function|injective function]].

Equivalently, $\varphi$ is a monomorphism if and only if its [[algebra-groups/kernel-group|kernel]] is trivial: $\ker(\varphi)=\{e_G\}$. In that case $\varphi$ identifies $G$ with the [[algebra-groups/image-group|image]] $\varphi(G)$, which is a [[algebra-groups/subgroup|subgroup]] of $H$.

**Examples:**
- If $H\le G$, the inclusion $H\hookrightarrow G$ is a group monomorphism.
- The map $\mathbb{Z}\to\mathbb{Z}$ given by $n\mapsto 2n$ (additive groups) is a group monomorphism.
- The determinant map $\det\colon GL_m(\mathbb{R})\to\mathbb{R}^\times$ is not a monomorphism for $m\ge 2$ because it has nontrivial kernel $SL_m(\mathbb{R})$.
