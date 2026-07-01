+++
id = "algebra-category-theory/right-exact-functor"
title = "Right exact functor"
kind = "knowl"
summary = "An additive functor that preserves cokernels (equivalently, exactness at the right end of short exact sequences)."
aliases = ["right-exact-functor", "Right exact functor"]
domains = ["algebra-category-theory"]
legacy_source_path = "algebra-category-theory/right-exact-functor.md"
+++

Let \(\mathcal A,\mathcal B\) be [[algebra-category-theory/abelian-category|abelian categories]] and let \(F:\mathcal A\to\mathcal B\) be an additive [[algebra-category-theory/functor|functor]].


The functor \(F\) is **right exact** if it preserves finite [[algebra-category-theory/colimit|colimits]]; equivalently (in abelian categories), if it preserves [[algebra-category-theory/cokernel-categorical|cokernels]].

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

- If \(F\) is both [[algebra-category-theory/left-exact-functor|left exact]] and right exact, then \(F\) is [[algebra-category-theory/exact-functor|exact]].
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
