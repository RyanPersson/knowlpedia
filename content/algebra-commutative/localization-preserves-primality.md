---
title: "Localization preserves prime ideals"
description: "A prime ideal disjoint from the multiplicative set extends to a prime ideal in the localized ring."
---

Prime ideals behave well under {{< knowl id="localization-ring" text="localization" >}}: if a prime ideal does not meet the elements being inverted, then it stays prime after localization. This is one half of the {{< knowl id="localization-prime-correspondence" text="prime correspondence under localization" >}}.

## Theorem

Let $R$ be a {{< knowl id="commutative-ring" section="algebra-rings" text="commutative ring" >}}, let $S$ be a {{< knowl id="multiplicative-set" text="multiplicative set" >}} in $R$, and let $\mathfrak p$ be a prime ideal of $R$ such that $\mathfrak p\cap S=\varnothing$.

Then the extended ideal
\[
S^{-1}\mathfrak p \;=\; \left\{ \frac{x}{s}\in S^{-1}R : x\in\mathfrak p,\ s\in S \right\}
\]
is a prime ideal of $S^{-1}R$.

Moreover, $S^{-1}\mathfrak p$ is precisely the kernel of the canonical map
\[
S^{-1}R \longrightarrow S^{-1}(R/\mathfrak p),
\]
and contracting back recovers $\mathfrak p$:
\[
(S^{-1}\mathfrak p)\cap R=\mathfrak p.
\]

If $\mathfrak p\cap S\neq\varnothing$, then $S^{-1}\mathfrak p=S^{-1}R$ (so there is no corresponding prime in the localization), which explains the disjointness hypothesis.

## Examples

1. **Localizing $\mathbb Z$ at a prime.**  
   Let $R=\mathbb Z$ and $S=\mathbb Z\setminus(p)$, so $S^{-1}R=\mathbb Z_{(p)}$. The prime ideals of $\mathbb Z$ are $(0)$ and $(q)$ for primes $q$. One checks:
   - $(p)\cap S=\varnothing$, so $(p)$ extends to the (unique) maximal ideal $p\mathbb Z_{(p)}$, which is prime.
   - If $q\neq p$, then $(q)\cap S\neq\varnothing$ (since $q\in S$), so $(q)$ becomes the unit ideal after localization.
   - Also $(0)\cap S=\varnothing$, so $(0)$ extends to $(0)$ in $\mathbb Z_{(p)}$.

2. **Inverting a variable in a polynomial ring.**  
   Let $R=k[x,y]$ and $S=\{1,y,y^2,\dots\}$, so $S^{-1}R=k[x,y,y^{-1}]$. The ideal $\mathfrak p=(x)$ is prime and disjoint from $S$ (since no power of $y$ lies in $(x)$), hence $S^{-1}(x)$ is prime in $k[x,y,y^{-1}]$.  
   By contrast, the prime ideal $(y)$ meets $S$ (it contains $y$), so $S^{-1}(y)=S^{-1}R$.

3. **Localization at a prime and the resulting local ring.**  
   If $\mathfrak p$ is a prime ideal of $R$ and $S=R\setminus\mathfrak p$, then $S^{-1}R$ is the {{< knowl id="localization-at-prime" text="localization $R_{\mathfrak p}$" >}}, which is a {{< knowl id="local-ring" text="local ring" >}}. The extension $S^{-1}\mathfrak p$ becomes the unique maximal ideal of $R_{\mathfrak p}$, and it is prime by the theorem.

For the full bijective correspondence between primes of $S^{-1}R$ and primes of $R$ disjoint from $S$, see {{< knowl id="localization-prime-correspondence" text="the localization prime correspondence" >}}.
