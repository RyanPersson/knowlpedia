---
title: "Height of a prime"
description: "The codimension of a prime ideal, measured by the maximum length of chains of primes ending at it."
---

Let $R$ be a {{< knowl id="commutative-ring" section="algebra-rings" text="commutative ring" >}} and let $\mathfrak p$ be a prime ideal (i.e., $\mathfrak p\in\operatorname{Spec}(R)$, the {{< knowl id="prime-spectrum" text="prime spectrum" >}}).

The **height** of $\mathfrak p$, denoted $\operatorname{ht}(\mathfrak p)$, is the supremum of integers $n\ge 0$ such that there exists a strictly increasing chain of prime ideals
\[
\mathfrak p_0 \subsetneq \mathfrak p_1 \subsetneq \cdots \subsetneq \mathfrak p_n=\mathfrak p
\]
in $R$.

Equivalently,
\[
\operatorname{ht}(\mathfrak p)=\dim(R_{\mathfrak p}),
\]
where $R_{\mathfrak p}$ is the {{< knowl id="localization-at-prime" text="localization at \mathfrak p" >}} and $\dim$ denotes {{< knowl id="krull-dimension" text="Krull dimension" >}}. In particular, the dimension of $R$ is the supremum of the heights of its prime ideals.

### Examples

1. **The ring of integers.**  
   In $R=\mathbb{Z}$, one has $\operatorname{ht}((0))=0$, and for any prime number $p$,
   \[
   (0)\subsetneq (p)
   \]
   is a maximal chain, so $\operatorname{ht}((p))=1$.

2. **A polynomial ring in two variables.**  
   In $k[x,y]$ (for a field $k$), the prime ideals satisfy
   \[
   (0)\subsetneq (x)\subsetneq (x,y),
   \]
   so $\operatorname{ht}((0))=0$, $\operatorname{ht}((x))=1$, and $\operatorname{ht}((x,y))=2$.

3. **Dedekind domains.**  
   If $R$ is a {{< knowl id="dedekind-domain" text="Dedekind domain" >}} (for instance, the ring of integers in a number field), then every nonzero prime ideal has height $1$. In a {{< knowl id="dvr" text="DVR" >}}, the unique nonzero prime ideal also has height $1$, reflecting that these rings are “one-dimensional.”
