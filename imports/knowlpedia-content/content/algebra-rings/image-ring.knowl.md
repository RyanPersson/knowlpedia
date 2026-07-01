+++
id = "algebra-rings/image-ring"
title = "Image of a ring homomorphism"
kind = "knowl"
summary = "The subset of the codomain attained by a ring homomorphism."
aliases = ["image-ring", "Image of a ring homomorphism"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/image-ring.md"
+++

The **image** of a [[algebra-rings/ring-homomorphism|ring homomorphism]] $\varphi:R\to S$ is
\[
\operatorname{im}(\varphi)=\{\varphi(r):r\in R\}\subseteq S,
\]
i.e. the [[shared-foundations/image|image]] of $R$ under $\varphi$.

The image is a [[algebra-rings/subring|subring]] of $S$ (and a unital subring if $\varphi$ is unital and $S$ is unital). Together with the kernel, the image governs the structure of $\varphi$ via isomorphism theorems.

**Examples:**
- For the inclusion $\mathbb Z\hookrightarrow \mathbb Q$, the image is $\mathbb Z\subseteq \mathbb Q$.
- For the reduction map $\mathbb Z\to \mathbb Z/n\mathbb Z$, the image is all of $\mathbb Z/n\mathbb Z$.
- For evaluation $k[x,y]\to k[x]$ at $y=0$, the image is $k[x]$.
