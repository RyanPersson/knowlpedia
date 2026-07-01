+++
id = "algebra-rings/kernel-ring"
title = "Kernel of a ring homomorphism"
kind = "knowl"
summary = "The set of elements mapped to zero by a ring homomorphism."
aliases = ["kernel-ring", "Kernel of a ring homomorphism"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/kernel-ring.md"
+++

The **kernel** of a [[algebra-rings/ring-homomorphism|ring homomorphism]] $\varphi:R\to S$ is
\[
\ker(\varphi)=\{\,r\in R:\varphi(r)=0\,\}=\varphi^{-1}(\{0\}),
\]
i.e. the [[shared-foundations/preimage|preimage]] of the additive identity of $S$.

The kernel is always an [[algebra-rings/ideal|ideal]] of $R$ (indeed, a two-sided ideal), and it measures injectivity: $\varphi$ is a monomorphism iff $\ker(\varphi)=\{0\}$. Kernels are the basic input to forming quotient rings and proving isomorphism theorems.

**Examples:**
- For the reduction map $\mathbb Z\to \mathbb Z/n\mathbb Z$, the kernel is $n\mathbb Z$.
- For evaluation $\mathrm{ev}_c:k[x]\to k$, $\ker(\mathrm{ev}_c)=(x-c)$.
- The inclusion $\mathbb Z\hookrightarrow \mathbb Q$ has kernel $\{0\}$.
