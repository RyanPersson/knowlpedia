---
title: "Exact functor"
description: "A functor between abelian categories that preserves all short exact sequences."
---

Let \(\mathcal A,\mathcal B\) be {{< knowl id="abelian-category" text="abelian categories" >}} and let \(F:\mathcal A\to\mathcal B\) be an additive {{< knowl id="functor" text="functor" >}}.


The functor \(F\) is **exact** if it preserves short exact sequences: whenever
\[
0 \longrightarrow A' \xrightarrow{u} A \xrightarrow{v} A'' \longrightarrow 0
\]
is exact in \(\mathcal A\), then
\[
0 \longrightarrow F(A') \xrightarrow{F(u)} F(A) \xrightarrow{F(v)} F(A'') \longrightarrow 0
\]
is exact in \(\mathcal B\).

Equivalently, $F$ is exact if and only if $F$ is both {{< knowl id="left-exact-functor" text="left exact" >}} and {{< knowl id="right-exact-functor" text="right exact" >}}.

In abelian categories, exactness can also be characterized as preservation of both {{< knowl id="kernel-categorical" text="kernels" >}} and {{< knowl id="cokernel-categorical" text="cokernels" >}} (hence images and coimages).

## Examples

1. **Restriction of scalars.** For a ring homomorphism \(\varphi:R\to S\), the forgetful/restriction functor
   \[
   \mathrm{Res}_\varphi:S\text{-}\mathbf{Mod}\to R\text{-}\mathbf{Mod}
   \]
   is exact: it does not change the underlying abelian group maps, so kernels and cokernels are preserved.

2. **Localization (commutative rings).** If \(R\) is commutative and \(S\subseteq R\) is multiplicative, then
   \[
   S^{-1}(-):R\text{-}\mathbf{Mod}\to S^{-1}R\text{-}\mathbf{Mod}
   \]
   is exact because \(S^{-1}(-)\cong -\otimes_R S^{-1}R\) and \(S^{-1}R\) is flat over \(R\).

3. **Tensor with a flat module / Hom from a projective module.**
   - The functor \(-\otimes_R M\) is exact iff \(M\) is flat.
   - The functor \(\mathrm{Hom}_R(P,-)\) is exact iff \(P\) is projective.

(These are standard sources of exact functors in module categories.)
