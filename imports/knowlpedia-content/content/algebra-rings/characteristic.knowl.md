+++
id = "algebra-rings/characteristic"
title = "Characteristic"
kind = "knowl"
summary = "The additive order of 1 in a unital ring; either 0 or a positive integer."
aliases = ["characteristic"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/characteristic.md"
+++

Let $R$ be a [[algebra-rings/unital-ring|unital ring]] with identity $1_R$. The **characteristic** of $R$, denoted $\mathrm{char}(R)$, is the least positive integer $n$ such that $n\cdot 1_R=0$, if such an $n$ exists; otherwise $\mathrm{char}(R)=0$.

Characteristic controls the arithmetic inside $R$: the prime field (or prime subring) embeds via $\mathbb{Z}\to R$ with kernel $n\mathbb{Z}$. If $R$ is an [[algebra-rings/integral-domain|integral domain]] (in particular, a [[algebra-rings/field|field]]), then $\mathrm{char}(R)$ is either $0$ or a prime number (see [[algebra-rings/characteristic-zero-or-prime|characteristic is zero or prime]]).

**Examples:**
- $\mathrm{char}(\mathbb{Z})=0$.
- For a prime $p$, $\mathrm{char}(\mathbb{F}_p)=p$.
- $\mathrm{char}(\mathbb{Z}/6\mathbb{Z})=6$, and $\mathrm{char}(M_n(\mathbb{F}_p))=p$.
