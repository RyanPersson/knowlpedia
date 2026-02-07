---
title: "Left exact functor"
description: "An additive functor that preserves kernels (equivalently, exactness at the left end of short exact sequences)."
---

Let \(\mathcal A,\mathcal B\) be {{< knowl id="abelian-category" text="abelian categories" >}} and let \(F:\mathcal A\to\mathcal B\) be an additive {{< knowl id="functor" text="functor" >}}.


The functor \(F\) is **left exact** if it preserves finite {{< knowl id="limit" text="limits" >}}; equivalently (in abelian categories), if it preserves {{< knowl id="kernel-categorical" text="kernels" >}}.

A standard “exact sequence” formulation is:

> For every short exact sequence in \(\mathcal A\),
> \[
> 0 \longrightarrow A' \xrightarrow{u} A \xrightarrow{v} A'' \longrightarrow 0,
> \]
> the sequence
> \[
> 0 \longrightarrow F(A') \xrightarrow{F(u)} F(A) \xrightarrow{F(v)} F(A'')
> \]
> is exact in \(\mathcal B\).

Equivalently, \(F\) preserves monomorphisms and kernels, but need not preserve cokernels or epimorphisms.

## Relation to other exactness notions

- If \(F\) is both left exact and {{< knowl id="right-exact-functor" text="right exact" >}}, then \(F\) is {{< knowl id="exact-functor" text="exact" >}}.
- Any additive right adjoint functor between abelian categories is left exact (because right adjoints preserve limits).

## Examples

1. **\(\mathrm{Hom}\) is left exact.** In \(R\text{-}\mathbf{Mod}\), for a fixed \(R\)-module \(M\), the functor
   \[
   \mathrm{Hom}_R(M,-):R\text{-}\mathbf{Mod}\to \mathbf{Ab}
   \]
   is left exact: applying \(\mathrm{Hom}_R(M,-)\) to a short exact sequence yields an exact sequence starting with \(0\).
   It is not generally right exact (failure of surjectivity at the right is measured by \(\mathrm{Ext}^1_R(M,-)\)).

2. **Global sections of sheaves.** For a topological space \(X\), the global sections functor
   \[
   \Gamma(X,-):\mathrm{Sh}_{\mathbf{Ab}}(X)\to \mathbf{Ab}
   \]
   is left exact, but not right exact in general.

3. **Restriction of scalars (actually exact).** If \(\varphi:R\to S\) is a ring homomorphism, the restriction-of-scalars functor
   \[
   \mathrm{Res}_\varphi:S\text{-}\mathbf{Mod}\to R\text{-}\mathbf{Mod}
   \]
   is exact, hence left exact.
