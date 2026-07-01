+++
id = "algebra-groups/image-group"
title = "Image of a group homomorphism"
kind = "knowl"
summary = "The set of values attained by a group homomorphism"
aliases = ["image-group", "Image of a group homomorphism"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/image-group.md"
+++

Let $\varphi\colon G\to H$ be a [[algebra-groups/group-homomorphism|group homomorphism]]. The **image** of $\varphi$ is the subset
$
\mathrm{im}(\varphi)=\varphi(G)=\{\varphi(g): g\in G\}\subseteq H.
$
The image is always a [[algebra-groups/subgroup|subgroup]] of $H$.

The map $\varphi$ is a [[algebra-groups/group-epimorphism|group epimorphism]] if and only if $\mathrm{im}(\varphi)=H$. Together with the kernel, the image appears in the [[algebra-groups/first-isomorphism-theorem-groups|first isomorphism theorem]], which identifies $G/\ker(\varphi)$ with $\mathrm{im}(\varphi)$ as groups.

**Examples:**
- For $\varphi\colon\mathbb{Z}\to\mathbb{Z}$ defined by $\varphi(n)=2n$, one has $\mathrm{im}(\varphi)=2\mathbb{Z}$.
- For $\mathrm{sgn}\colon S_n\to\{\pm1\}$, the image is all of $\{\pm1\}$ (for $n\ge 2$).
- If $\iota\colon H\hookrightarrow G$ is the inclusion of a subgroup, then $\mathrm{im}(\iota)=H$.
