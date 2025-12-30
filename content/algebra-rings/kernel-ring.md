---
title: "Kernel of a ring homomorphism"
description: "The set of elements mapped to zero by a ring homomorphism."
---

The **kernel** of a {{< knowl id="ring-homomorphism" text="ring homomorphism" >}} $\varphi:R\to S$ is
\[
\ker(\varphi)=\{\,r\in R:\varphi(r)=0\,\}=\varphi^{-1}(\{0\}),
\]
i.e. the {{< knowl id="preimage" text="preimage" >}} of the additive identity of $S$.

The kernel is always an {{< knowl id="ideal" text="ideal" >}} of $R$ (indeed, a two-sided ideal), and it measures injectivity: $\varphi$ is a monomorphism iff $\ker(\varphi)=\{0\}$. Kernels are the basic input to forming quotient rings and proving isomorphism theorems.

**Examples:**
- For the reduction map $\mathbb Z\to \mathbb Z/n\mathbb Z$, the kernel is $n\mathbb Z$.
- For evaluation $\mathrm{ev}_c:k[x]\to k$, $\ker(\mathrm{ev}_c)=(x-c)$.
- The inclusion $\mathbb Z\hookrightarrow \mathbb Q$ has kernel $\{0\}$.