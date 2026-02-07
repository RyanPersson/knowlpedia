---
title: "Local trivialization"
description: "A local trivialization identifies a bundle over an open set with a product of that open set and the fiber."
---

Let $\pi:E\to M$ be a {{< knowl id="smooth-fiber-bundle" text="smooth fiber bundle" >}} with typical fiber $F$ (see {{< knowl id="typical-fiber" text="typical fiber" >}}). Let $U\subset M$ be open.

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

A collection of local trivializations over an open cover that satisfy the compatibility condition defines a {{< knowl id="bundle-atlas" text="bundle atlas" >}}. On overlaps $U_i\cap U_j$, comparing trivializations produces the usual {{< knowl id="transition-function" text="transition functions" >}} (or transition maps), and these satisfy the {{< knowl id="cocycle-condition-for-transition-functions" text="cocycle condition" >}}.

For principal bundles, one often uses the equivariant version (compare {{< knowl id="equivariant-local-trivialization" text="equivariant local trivialization" >}}), and local trivializations can be built from local sections as in {{< knowl id="construction-local-trivialization-from-a-local-section" text="constructing a trivialization from a local section" >}}.

## Examples
1. **Trivial bundle.**  
   For the product bundle $E=M\times F$ (see {{< knowl id="trivial-fiber-bundle" text="trivial fiber bundle" >}}), the global map
   \[
   \Phi:M\times F\to M\times F,\quad \Phi(x,f)=(x,f),
   \]
   is a local trivialization over every open $U\subset M$ (in fact a global trivialization).

2. **Tangent bundle in a coordinate chart.**  
   Let $M$ be a smooth manifold and let $(U,\varphi)$ be a smooth chart (see {{< knowl id="smooth-chart" text="smooth chart" >}}). The differential $d\varphi$ identifies $T_xM$ with $\mathbb R^n$ for $x\in U$. This yields a local trivialization of the {{< knowl id="tangent-bundle" text="tangent bundle" >}} over $U$,
   \[
   \Phi:TU\to U\times \mathbb R^n,\quad v_x\mapsto (x, d\varphi_x(v_x)).
   \]

3. **Vector bundle via a local frame.**  
   If $E\to M$ is a rank-$n$ vector bundle and $(e_1,\dots,e_n)$ is a {{< knowl id="local-frame-of-a-vector-bundle" text="local frame" >}} on $U$, then every $v\in E_x$ can be written uniquely as $v=\sum_i a^i e_i(x)$. This gives a local trivialization
   \[
   \Phi:\pi^{-1}(U)\to U\times \mathbb R^n,\quad v\mapsto \big(\pi(v),(a^1,\dots,a^n)\big),
   \]
   and on overlaps the change of frame is encoded by the {{< knowl id="transition-matrix-of-a-local-frame" text="transition matrix" >}}.
