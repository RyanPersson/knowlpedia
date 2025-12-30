---
title: "Characteristic"
description: "The additive order of 1 in a unital ring; either 0 or a positive integer."
---

Let $R$ be a {{< knowl id="unital-ring" text="unital ring" >}} with identity $1_R$. The **characteristic** of $R$, denoted $\mathrm{char}(R)$, is the least positive integer $n$ such that $n\cdot 1_R=0$, if such an $n$ exists; otherwise $\mathrm{char}(R)=0$.

Characteristic controls the arithmetic inside $R$: the prime field (or prime subring) embeds via $\mathbb{Z}\to R$ with kernel $n\mathbb{Z}$. If $R$ is an {{< knowl id="integral-domain" text="integral domain" >}} (in particular, a {{< knowl id="field" text="field" >}}), then $\mathrm{char}(R)$ is either $0$ or a prime number (see {{< knowl id="characteristic-zero-or-prime" text="characteristic is zero or prime" >}}).

**Examples:**
- $\mathrm{char}(\mathbb{Z})=0$.
- For a prime $p$, $\mathrm{char}(\mathbb{F}_p)=p$.
- $\mathrm{char}(\mathbb{Z}/6\mathbb{Z})=6$, and $\mathrm{char}(M_n(\mathbb{F}_p))=p$.