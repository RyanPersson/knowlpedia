---
title: "Ring homomorphisms preserve structure"
description: "A ring homomorphism preserves addition and multiplication and sends 0 (and 1 for unital maps) to 0 (and 1)."
---

**Ring homomorphisms preserve structure**: Let $\varphi:R\to S$ be a ring homomorphism. Then for all $a,b\in R$,
\[
\varphi(a+b)=\varphi(a)+\varphi(b),\qquad \varphi(ab)=\varphi(a)\varphi(b),\qquad \varphi(0_R)=0_S.
\]
If $\varphi$ is unital, then $\varphi(1_R)=1_S$. In particular, $\varphi(-a)=-\varphi(a)$ for all $a\in R$.

This is immediate from the definition of a {{< knowl id="ring-homomorphism" text="ring homomorphism" >}} between {{< knowl id="ring" text="rings" >}}; when working with {{< knowl id="unital-ring" text="unital rings" >}} one typically requires $\varphi(1_R)=1_S$. These identities underpin the definitions of the {{< knowl id="kernel-ring" text="kernel" >}} and {{< knowl id="image-ring" text="image" >}} of $\varphi$.