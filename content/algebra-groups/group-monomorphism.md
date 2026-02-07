---
title: "Group monomorphism"
description: "An injective group homomorphism"
---

A **group monomorphism** is a {{< knowl id="group-homomorphism" text="group homomorphism" >}} $\varphi\colon G\to H$ that is injective as an {{< knowl id="injective-function" section="shared-foundations" text="injective function" >}}.

Equivalently, $\varphi$ is a monomorphism if and only if its {{< knowl id="kernel-group" text="kernel" >}} is trivial: $\ker(\varphi)=\{e_G\}$. In that case $\varphi$ identifies $G$ with the {{< knowl id="image-group" text="image" >}} $\varphi(G)$, which is a {{< knowl id="subgroup" text="subgroup" >}} of $H$.

**Examples:**
- If $H\le G$, the inclusion $H\hookrightarrow G$ is a group monomorphism.
- The map $\mathbb{Z}\to\mathbb{Z}$ given by $n\mapsto 2n$ (additive groups) is a group monomorphism.
- The determinant map $\det\colon GL_m(\mathbb{R})\to\mathbb{R}^\times$ is not a monomorphism for $m\ge 2$ because it has nontrivial kernel $SL_m(\mathbb{R})$.
