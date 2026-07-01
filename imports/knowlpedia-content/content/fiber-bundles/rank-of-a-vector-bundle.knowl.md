+++
id = "fiber-bundles/rank-of-a-vector-bundle"
title = "Rank of a vector bundle"
kind = "knowl"
summary = "The (constant) dimension of the fibers of a vector bundle, viewed as real or complex vector spaces."
aliases = ["rank-of-a-vector-bundle", "Rank of a vector bundle"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/rank-of-a-vector-bundle.md"
+++

Let $\pi:E\to M$ be a smooth real or complex vector bundle over a [[fiber-bundles/smooth-manifold|smooth manifold]] $M$. The **rank** of $E$ at a point $x\in M$ is
\[
\mathrm{rank}_x(E):=\dim_{\mathbb F}(E_x),
\]
where $\mathbb F=\mathbb R$ for real bundles and $\mathbb F=\mathbb C$ for complex bundles (for example, a [[fiber-bundles/complex-vector-bundle|complex vector bundle]]).

A smooth vector bundle is, by definition, *locally trivial*, so $\mathrm{rank}_x(E)$ is locally constant as a function of $x$. If $M$ is connected, then $\mathrm{rank}_x(E)$ is constant, and this common value is called **the rank of $E$**, denoted $\mathrm{rank}(E)$.

## Examples
1. If $\dim M = n$, then $\mathrm{rank}(TM)=n$ and $\mathrm{rank}(T^*M)=n$ for the [[fiber-bundles/tangent-bundle|tangent bundle]] and cotangent bundle.

2. The trivial bundle $M\times \mathbb F^r\to M$ has rank $r$.

3. If $E$ and $F$ are bundles over the same base, then
   \[
   \mathrm{rank}(E\oplus F)=\mathrm{rank}(E)+\mathrm{rank}(F),\qquad
   \mathrm{rank}(E\otimes F)=\mathrm{rank}(E)\,\mathrm{rank}(F),
   \]
   where $\oplus$ and $\otimes$ denote the fiberwise direct sum and tensor product bundles.
