---
title: "Exactness of localization"
description: "Localizing a sequence of modules at a multiplicative set preserves exactness."
---

Localization is not just a way to invert elements in a ring {{< knowl id="localization-ring" text="(localization of rings)" >}}; it is also a well-behaved operation on modules {{< knowl id="localization-module" text="(localization of modules)" >}}. One of its most important formal properties is that it preserves exact sequences.

## Theorem

Let $R$ be a {{< knowl id="commutative-ring" section="algebra-rings" text="commutative ring" >}}, let $S$ be a {{< knowl id="multiplicative-set" text="multiplicative set" >}} in $R$, and let
\[
0 \longrightarrow A \xrightarrow{f} B \xrightarrow{g} C \longrightarrow 0
\]
be an {{< knowl id="exact-sequence-modules" section="algebra-modules" text="exact sequence of $R$-modules" >}}. Then the localized sequence
\[
0 \longrightarrow S^{-1}A \xrightarrow{S^{-1}f} S^{-1}B \xrightarrow{S^{-1}g} S^{-1}C \longrightarrow 0
\]
is exact as a sequence of $S^{-1}R$-modules.

Equivalently, for any $R$-linear map $h\colon M\to N$,
- $S^{-1}(\ker h)=\ker(S^{-1}h)$,
- $S^{-1}(\operatorname{im} h)=\operatorname{im}(S^{-1}h)$,
so localization commutes with kernels and images.

One convenient conceptual reformulation is that localization is {{< knowl id="extension-of-scalars" text="extension of scalars" >}} along the ring map $R\to S^{-1}R$:
\[
S^{-1}M \cong M\otimes_R S^{-1}R,
\]
and this tensor description is what makes the exactness behave so cleanly.

## Examples

1. **Localizing a short exact sequence over $\mathbb Z$.**  
   Consider
   \[
   0\to \mathbb Z \xrightarrow{\times n} \mathbb Z \to \mathbb Z/n\mathbb Z \to 0.
   \]
   Localize at $S=\mathbb Z\setminus (p)$ (so $S^{-1}\mathbb Z=\mathbb Z_{(p)}$). Exactness says
   \[
   0\to \mathbb Z_{(p)} \xrightarrow{\times n} \mathbb Z_{(p)} \to (\mathbb Z/n\mathbb Z)_{(p)} \to 0
   \]
   is exact. Concretely:
   - if $p\nmid n$, then multiplication by $n$ becomes an isomorphism on $\mathbb Z_{(p)}$, so $(\mathbb Z/n\mathbb Z)_{(p)}=0$;
   - if $n=p^k m$ with $p\nmid m$, then $m$ becomes invertible in $\mathbb Z_{(p)}$, and the cokernel is “the $p$-primary part,” isomorphic to $\mathbb Z/p^k\mathbb Z$ as a $\mathbb Z_{(p)}$-module.

2. **Localization can kill torsion.**  
   Let $R=k[x]$ and consider the exact sequence
   \[
   0\to R \xrightarrow{\times x} R \to R/(x)\to 0.
   \]
   Localize at $S=\{1,x,x^2,\dots\}$, so $S^{-1}R=R_x$. Then $x$ becomes a unit in $R_x$, hence multiplication by $x$ on $R_x$ is an isomorphism. Exactness forces
   \[
   (R/(x))_x = 0,
   \]
   which reflects that $R/(x)$ is “$x$-torsion.”

3. **Exactness on kernels and images.**  
   Let $R=\mathbb Z$, $h\colon \mathbb Z\to\mathbb Z$ be multiplication by $6$, and localize at $S=\{1,2,2^2,\dots\}$. Then $\ker h=0$ and exactness implies $\ker(S^{-1}h)=0$ as well. Meanwhile $\operatorname{im} h=6\mathbb Z$ localizes to $6\mathbb Z[1/2]$, which equals the image of the localized map $\mathbb Z[1/2]\xrightarrow{\times 6}\mathbb Z[1/2]$.

Exactness is also a key input to the prime correspondence under localization; see {{< knowl id="localization-prime-correspondence" text="prime correspondence under localization" >}}.
