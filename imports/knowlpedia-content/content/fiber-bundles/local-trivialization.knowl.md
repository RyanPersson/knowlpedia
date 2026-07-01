+++
id = "fiber-bundles/local-trivialization"
title = "Local trivialization"
kind = "knowl"
summary = "A local trivialization identifies a bundle over an open set with a product of that open set and the fiber."
aliases = ["local-trivialization", "Local trivialization"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/local-trivialization.md"
+++

Let $\pi:E\to M$ be a [[fiber-bundles/smooth-fiber-bundle|smooth fiber bundle]] with typical fiber $F$ (see [[fiber-bundles/typical-fiber|typical fiber]]). Let $U\subset M$ be open.

A **local trivialization** of $E$ over $U$ is a diffeomorphism
\[
\Phi:\pi^{-1}(U)\longrightarrow U\times F
\]
such that the projection to $U$ agrees with $\pi$, i.e.
\[
\mathrm{pr}_1\circ \Phi = \pi|_{\pi^{-1}(U)}.
\]

Equivalently, for each $x\in U$ the map $\Phi$ restricts to a diffeomorphism of fibers
\[
\Phi_x:E_x\stackrel{\cong}{\longrightarrow} \{x\}\times F \cong F.
\]

A collection of local trivializations over an open cover that satisfy the compatibility condition defines a [[fiber-bundles/bundle-atlas|bundle atlas]]. On overlaps $U_i\cap U_j$, comparing trivializations produces the usual [[fiber-bundles/transition-function|transition functions]] (or transition maps), and these satisfy the [[fiber-bundles/cocycle-condition-for-transition-functions|cocycle condition]].

For principal bundles, one often uses the equivariant version (compare [[fiber-bundles/equivariant-local-trivialization|equivariant local trivialization]]), and local trivializations can be built from local sections as in [[fiber-bundles/construction-local-trivialization-from-a-local-section|constructing a trivialization from a local section]].

## Examples
1. **Trivial bundle.**
   For the product bundle $E=M\times F$ (see [[fiber-bundles/trivial-fiber-bundle|trivial fiber bundle]]), the global map
   \[
   \Phi:M\times F\to M\times F,\quad \Phi(x,f)=(x,f),
   \]
   is a local trivialization over every open $U\subset M$ (in fact a global trivialization).

2. **Tangent bundle in a coordinate chart.**
   Let $M$ be a smooth manifold and let $(U,\varphi)$ be a smooth chart (see [[fiber-bundles/smooth-chart|smooth chart]]). The differential $d\varphi$ identifies $T_xM$ with $\mathbb R^n$ for $x\in U$. This yields a local trivialization of the [[fiber-bundles/tangent-bundle|tangent bundle]] over $U$,
   \[
   \Phi:TU\to U\times \mathbb R^n,\quad v_x\mapsto (x, d\varphi_x(v_x)).
   \]

3. **Vector bundle via a local frame.**
   If $E\to M$ is a rank-$n$ vector bundle and $(e_1,\dots,e_n)$ is a [[fiber-bundles/local-frame-of-a-vector-bundle|local frame]] on $U$, then every $v\in E_x$ can be written uniquely as $v=\sum_i a^i e_i(x)$. This gives a local trivialization
   \[
   \Phi:\pi^{-1}(U)\to U\times \mathbb R^n,\quad v\mapsto \big(\pi(v),(a^1,\dots,a^n)\big),
   \]
   and on overlaps the change of frame is encoded by the [[fiber-bundles/transition-matrix-of-a-local-frame|transition matrix]].
