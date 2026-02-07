---
title: "Krull dimension"
description: "The supremum of lengths of chains of prime ideals in a ring (equivalently, the dimension of its prime spectrum)."
---

Let $R$ be a {{< knowl id="commutative-ring" section="algebra-rings" text="commutative ring" >}}. The **Krull dimension** of $R$, denoted $\dim R$, is the supremum of integers $n\ge 0$ for which there exists a strictly increasing chain of prime ideals
\[
\mathfrak p_0 \subsetneq \mathfrak p_1 \subsetneq \cdots \subsetneq \mathfrak p_n
\]
in $R$. If no such finite supremum exists, one writes $\dim R = \infty$.

Equivalently, $\dim R$ is the Krull dimension of the topological space {{< knowl id="prime-spectrum" text="\operatorname{Spec}(R)" >}} with its {{< knowl id="zariski-topology" text="Zariski topology" >}}.

The Krull dimension can also be expressed in terms of heights: for each prime $\mathfrak p$, its {{< knowl id="height-of-prime" text="height" >}} $\operatorname{ht}(\mathfrak p)$ is the supremum of lengths of prime chains ending at $\mathfrak p$, and one has
\[
\dim R = \sup_{\mathfrak p\in \operatorname{Spec}(R)} \operatorname{ht}(\mathfrak p).
\]
Moreover, $\operatorname{ht}(\mathfrak p)$ agrees with the dimension of the {{< knowl id="localization-at-prime" text="localization $R_{\mathfrak p}$" >}}.

### Examples

1. **Fields and Artinian rings have dimension $0$.**  
   If $k$ is a {{< knowl id="field" section="algebra-rings" text="field" >}}, the only prime ideal is $(0)$, so $\dim k=0$. More generally, if $R$ is an {{< knowl id="artinian-ring" text="Artinian ring" >}}, then every prime ideal is maximal and there are no nontrivial chains of primes, so $\dim R=0$.

2. **Dimension $1$: $\mathbb{Z}$ and $k[x]$.**  
   In $\mathbb{Z}$ there are chains $(0)\subsetneq (p)$, but no longer chains, so $\dim \mathbb{Z}=1$. Similarly, for a field $k$, the ring $k[x]$ has chains $(0)\subsetneq (f)$ (with $f$ irreducible), but no longer ones, hence $\dim k[x]=1$.

3. **Polynomial rings.**  
   For a field $k$, the polynomial ring $k[x_1,\dots,x_n]$ has Krull dimension $n$. For instance, in $k[x,y]$ one has the chain
   \[
   (0)\subsetneq (x)\subsetneq (x,y),
   \]
   showing $\dim k[x,y]\ge 2$, and in fact equality holds.
