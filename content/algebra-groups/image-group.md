---
title: "Image of a group homomorphism"
description: "The set of values attained by a group homomorphism"
---

Let $\varphi\colon G\to H$ be a {{< knowl id="group-homomorphism" text="group homomorphism" >}}. The **image** of $\varphi$ is the subset
$
\mathrm{im}(\varphi)=\varphi(G)=\{\varphi(g): g\in G\}\subseteq H.
$
The image is always a {{< knowl id="subgroup" text="subgroup" >}} of $H$.

The map $\varphi$ is a {{< knowl id="group-epimorphism" text="group epimorphism" >}} if and only if $\mathrm{im}(\varphi)=H$. Together with the kernel, the image appears in the {{< knowl id="first-isomorphism-theorem-groups" text="first isomorphism theorem" >}}, which identifies $G/\ker(\varphi)$ with $\mathrm{im}(\varphi)$ as groups.

**Examples:**
- For $\varphi\colon\mathbb{Z}\to\mathbb{Z}$ defined by $\varphi(n)=2n$, one has $\mathrm{im}(\varphi)=2\mathbb{Z}$.
- For $\mathrm{sgn}\colon S_n\to\{\pm1\}$, the image is all of $\{\pm1\}$ (for $n\ge 2$).
- If $\iota\colon H\hookrightarrow G$ is the inclusion of a subgroup, then $\mathrm{im}(\iota)=H$.
