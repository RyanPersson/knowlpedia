+++
id = "algebra-rings/ring-homomorphism-properties"
title = "Ring homomorphisms preserve structure"
kind = "knowl"
summary = "A ring homomorphism preserves addition and multiplication and sends 0 (and 1 for unital maps) to 0 (and 1)."
aliases = ["ring-homomorphism-properties", "Ring homomorphisms preserve structure"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/ring-homomorphism-properties.md"
+++

**Ring homomorphisms preserve structure**: Let $\varphi:R\to S$ be a ring homomorphism. Then for all $a,b\in R$,
\[
\varphi(a+b)=\varphi(a)+\varphi(b),\qquad \varphi(ab)=\varphi(a)\varphi(b),\qquad \varphi(0_R)=0_S.
\]
If $\varphi$ is unital, then $\varphi(1_R)=1_S$. In particular, $\varphi(-a)=-\varphi(a)$ for all $a\in R$.

This is immediate from the definition of a [[algebra-rings/ring-homomorphism|ring homomorphism]] between [[algebra-rings/ring|rings]]; when working with [[algebra-rings/unital-ring|unital rings]] one typically requires $\varphi(1_R)=1_S$. These identities underpin the definitions of the [[algebra-rings/kernel-ring|kernel]] and [[algebra-rings/image-ring|image]] of $\varphi$.
