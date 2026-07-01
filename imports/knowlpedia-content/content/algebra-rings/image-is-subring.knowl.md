+++
id = "algebra-rings/image-is-subring"
title = "Image is a subring"
kind = "knowl"
summary = "The image of a ring homomorphism is closed under the ring operations."
aliases = ["image-is-subring", "Image is a subring"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/image-is-subring.md"
+++

**Image is a subring**: Let $\varphi:R\to S$ be a ring homomorphism. Then
\[
\operatorname{im}(\varphi)=\{\varphi(r):r\in R\}
\]
is a subring of $S$. If $\varphi$ is unital, then $\operatorname{im}(\varphi)$ contains $1_S$.

Thus the [[algebra-rings/image-ring|image]] of a [[algebra-rings/ring-homomorphism|ring homomorphism]] naturally inherits the structure of a [[algebra-rings/subring|subring]] of the codomain, and in the [[algebra-rings/unital-ring|unital]] setting it is a unital subring. Combined with [[algebra-rings/kernel-is-ideal|the kernel–ideal property]], this yields [[algebra-rings/first-isomorphism-theorem-rings|the First Isomorphism Theorem]] identifying $R/\ker\varphi$ with $\operatorname{im}\varphi$.
