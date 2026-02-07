---
title: "Extension of scalars"
description: "Given a ring map R→S, the S-module S⊗_R M obtained from an R-module M by base change."
---

Let $f:R\to S$ be a homomorphism of {{< knowl id="commutative-ring" section="algebra-rings" text="commutative rings" >}}, and let $M$ be an $R$-module. The **extension of scalars** (or **base change**) of $M$ along $f$ is the $S$-module
\[
S\otimes_R M,
\]
where $S$ acts on the left tensor factor: $s\cdot(s'\otimes m)=(ss')\otimes m$.

There is a canonical $R$-linear map
\[
\eta_M: M \longrightarrow S\otimes_R M,\qquad m\longmapsto 1\otimes m,
\]
where $S\otimes_R M$ is viewed as an $R$-module via $f$.

### Universal property and adjunction
For every $S$-module $N$, restriction of scalars along $f$ produces an $R$-module; this is {{< knowl id="restriction-of-scalars" text="restriction of scalars" >}}. Extension of scalars is left adjoint to restriction of scalars, meaning there is a natural bijection
\[
\mathrm{Hom}_S(S\otimes_R M,\;N)\ \cong\ \mathrm{Hom}_R(M,\;\mathrm{Res}_f N),
\]
where $\mathrm{Res}_f N$ denotes $N$ viewed as an $R$-module via $f$.

A particularly important special case is localization: if $S^{-1}R$ is the {{< knowl id="localization-ring" text="localization of R" >}} at a {{< knowl id="multiplicative-set" text="multiplicative set" >}} $S\subseteq R$, then extension of scalars along $R\to S^{-1}R$ recovers {{< knowl id="localization-module" text="localization of modules" >}}:
\[
(S^{-1}R)\otimes_R M \cong S^{-1}M.
\]

### Examples

1. **Quotient base change.** Let $S=R/I$ and $f:R\to R/I$ be the quotient map. Then for any $R$-module $M$,
   \[
   (R/I)\otimes_R M \cong M/IM.
   \]
   For example, with $R=\mathbb Z$, $S=\mathbb Z/n\mathbb Z$, one gets $(\mathbb Z/n)\otimes_{\mathbb Z} M \cong M/nM$.

2. **Field extension.** If $k\subseteq K$ is a field extension and $V$ is a $k$-vector space, then $K\otimes_k V$ is the $K$-vector space obtained by extending scalars. If $V\cong k^d$ is finite-dimensional, then $K\otimes_k V\cong K^d$.

3. **Localization as extension of scalars.** Let $R=k[x]$, let $S=\{1,x,x^2,\dots\}$, and set $R'=S^{-1}R\cong k[x,x^{-1}]$. For $M=R/(x)$, extension of scalars gives
   \[
   R'\otimes_R M \cong S^{-1}M = 0,
   \]
   since $x$ becomes invertible after localization but kills $M$.
