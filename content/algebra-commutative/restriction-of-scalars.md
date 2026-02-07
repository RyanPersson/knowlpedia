---
title: "Restriction of scalars"
description: "Given a ring map R→S, any S-module can be regarded as an R-module by forgetting part of the scalar action."
---

Let $R$ and $S$ be {{< knowl id="commutative-ring" section="algebra-rings" text="commutative rings" >}}, and let $\varphi: R \to S$ be a ring homomorphism. If $M$ is an $S$-module, the **restriction of scalars** of $M$ along $\varphi$ is the $R$-module
\[
\operatorname{Res}_\varphi(M),
\]
defined as follows:

- As an abelian group, $\operatorname{Res}_\varphi(M)$ is the same underlying abelian group as $M$.
- The $R$-action is given by
  \[
  r\cdot m := \varphi(r)m \quad \text{for } r\in R,\ m\in M,
  \]
  where the multiplication on the right is the original $S$-module structure on $M$.

This construction is functorial in $M$ and defines a forgetful functor
\[
\operatorname{Res}_\varphi : \mathrm{Mod}_S \longrightarrow \mathrm{Mod}_R.
\]
It is faithful and exact (it does not change the underlying abelian groups or group homomorphisms).

Restriction of scalars is the natural companion to {{< knowl id="extension-of-scalars" text="extension of scalars" >}}, and in many settings these form an adjoint pair (extension is left adjoint to restriction).

### Examples

1. **From a polynomial algebra to the base field.**  
   Let $k$ be a {{< knowl id="field" section="algebra-rings" text="field" >}} and $\varphi: k \hookrightarrow k[x]$ the usual inclusion. If $M = k[x]$ is viewed as a $k[x]$-module over itself, then $\operatorname{Res}_\varphi(M)$ is just the underlying $k$-{{< knowl id="vector-space" section="linear-algebra" text="vector space" >}} of polynomials, which is infinite-dimensional over $k$.

2. **Forgetting an $S$-module to a $\mathbb{Z}$-module.**  
   For the canonical surjection $\varphi: \mathbb{Z}\to \mathbb{Z}/n\mathbb{Z}$, any $\mathbb{Z}/n\mathbb{Z}$-module $M$ becomes a $\mathbb{Z}$-module by restriction. Concretely, $\operatorname{Res}_\varphi(M)$ is the underlying abelian group of $M$, and it satisfies $nM=0$, i.e. $n$ lies in the {{< knowl id="annihilator-module" section="algebra-modules" text="annihilator" >}} of $\operatorname{Res}_\varphi(M)$.

3. **Restriction along localization.**  
   If $S=R_f$ is the {{< knowl id="localization-ring" text="localization" >}} of $R$ at a single element $f\in R$, then every $R_f$-module restricts to an $R$-module along $R\to R_f$. For instance, $R_f$ itself (as an $R_f$-module) becomes an $R$-module in which multiplication by $f$ is invertible; compare this with {{< knowl id="localization-module" text="localization of modules" >}}.
