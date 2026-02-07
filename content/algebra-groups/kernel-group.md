---
title: "Kernel of a group homomorphism"
description: "The set of elements mapped to the identity by a group homomorphism"
---

Let $\varphi\colon G\to H$ be a {{< knowl id="group-homomorphism" text="group homomorphism" >}}. The **kernel** of $\varphi$ is the subset
$
\ker(\varphi)=\{g\in G : \varphi(g)=e_H\}.
$
Equivalently, $\ker(\varphi)$ is the {{< knowl id="preimage" section="shared-foundations" text="preimage" >}} of $\{e_H\}$ under $\varphi$.

The kernel is always a {{< knowl id="normal-subgroup" text="normal subgroup" >}} of $G$. Moreover, $\varphi$ is a {{< knowl id="group-monomorphism" text="monomorphism" >}} if and only if $\ker(\varphi)=\{e_G\}$. The kernel controls the "collapse" of $G$ under $\varphi$; the {{< knowl id="first-isomorphism-theorem-groups" text="first isomorphism theorem" >}} identifies the quotient {{< knowl id="quotient-group" text="quotient group" >}} $G/\ker(\varphi)$ with the image of $\varphi$.

**Examples:**
- For the reduction map $\pi\colon\mathbb{Z}\to\mathbb{Z}/n\mathbb{Z}$, one has $\ker(\pi)=n\mathbb{Z}$.
- For $\mathrm{sgn}\colon S_n\to\{\pm1\}$, the kernel is $A_n$.
- For $\det\colon GL_m(\mathbb{R})\to\mathbb{R}^\times$, the kernel is $SL_m(\mathbb{R})$.
