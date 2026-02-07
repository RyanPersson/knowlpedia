---
title: "Right exact functor"
description: "An additive functor that preserves cokernels (equivalently, exactness at the right end of short exact sequences)."
---

Let \(\mathcal A,\mathcal B\) be {{< knowl id="abelian-category" text="abelian categories" >}} and let \(F:\mathcal A\to\mathcal B\) be an additive {{< knowl id="functor" text="functor" >}}.


The functor \(F\) is **right exact** if it preserves finite {{< knowl id="colimit" text="colimits" >}}; equivalently (in abelian categories), if it preserves {{< knowl id="cokernel-categorical" text="cokernels" >}}.

A standard “exact sequence” formulation is:

> For every short exact sequence in \(\mathcal A\),
> \[
> 0 \longrightarrow A' \xrightarrow{u} A \xrightarrow{v} A'' \longrightarrow 0,
> \]
> the sequence
> \[
> F(A') \xrightarrow{F(u)} F(A) \xrightarrow{F(v)} F(A'') \longrightarrow 0
> \]
> is exact in \(\mathcal B\).

Equivalently, \(F\) preserves epimorphisms and cokernels, but need not preserve kernels or monomorphisms.

## Relation to other exactness notions

- If \(F\) is both {{< knowl id="left-exact-functor" text="left exact" >}} and right exact, then \(F\) is {{< knowl id="exact-functor" text="exact" >}}.
- Any additive left adjoint functor between abelian categories is right exact (because left adjoints preserve colimits).

## Examples

1. **Tensor product is right exact.** In \(R\text{-}\mathbf{Mod}\), for a fixed right \(R\)-module \(M\) (or in the commutative case, a fixed \(R\)-module),
   \[
   -\otimes_R M : R\text{-}\mathbf{Mod}\to \mathbf{Ab}
   \]
   is right exact. It is exact iff \(M\) is flat.

2. **Quotient by an ideal (via tensor).** For a ring \(R\) and ideal \(I\), the functor
   \[
   M \longmapsto M/IM
   \]
   is right exact; in fact \(M/IM \cong M\otimes_R (R/I)\).

3. **Extension of scalars is right exact.** For a ring map \(\varphi:R\to S\), the functor
   \[
   -\otimes_R S : R\text{-}\mathbf{Mod}\to S\text{-}\mathbf{Mod}
   \]
   is left adjoint to restriction of scalars, hence right exact (and exact iff \(S\) is flat as an \(R\)-module).
