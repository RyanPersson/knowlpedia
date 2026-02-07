---
title: "Image is a subring"
description: "The image of a ring homomorphism is closed under the ring operations."
---

**Image is a subring**: Let $\varphi:R\to S$ be a ring homomorphism. Then
\[
\operatorname{im}(\varphi)=\{\varphi(r):r\in R\}
\]
is a subring of $S$. If $\varphi$ is unital, then $\operatorname{im}(\varphi)$ contains $1_S$.

Thus the {{< knowl id="image-ring" text="image" >}} of a {{< knowl id="ring-homomorphism" text="ring homomorphism" >}} naturally inherits the structure of a {{< knowl id="subring" text="subring" >}} of the codomain, and in the {{< knowl id="unital-ring" text="unital" >}} setting it is a unital subring. Combined with {{< knowl id="kernel-is-ideal" text="the kernel–ideal property" >}}, this yields {{< knowl id="first-isomorphism-theorem-rings" text="the First Isomorphism Theorem" >}} identifying $R/\ker\varphi$ with $\operatorname{im}\varphi$.