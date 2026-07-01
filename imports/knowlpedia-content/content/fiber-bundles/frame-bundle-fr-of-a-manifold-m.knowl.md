+++
id = "fiber-bundles/frame-bundle-fr-of-a-manifold-m"
title = "Frame bundle of a manifold"
kind = "knowl"
summary = "Principal GL(n) bundle of ordered tangent frames on a smooth n-manifold."
aliases = ["frame-bundle-fr-of-a-manifold-m", "Frame bundle of a manifold"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/frame-bundle-fr-of-a-manifold-m.md"
+++

Let $M$ be an $n$-dimensional [[fiber-bundles/smooth-manifold|smooth manifold]] with [[fiber-bundles/tangent-bundle|tangent bundle]] $\pi:TM\to M$.

The **frame bundle** of $M$, denoted $\mathrm{Fr}(TM)$, is the set of all ordered bases (frames) of tangent spaces:
\[
\mathrm{Fr}(TM)=\{(x,(e_1,\dots,e_n)):\ x\in M,\ (e_1,\dots,e_n)\text{ is a basis of }T_xM\}.
\]
Equivalently, a point of $\mathrm{Fr}(TM)$ can be viewed as a linear isomorphism $u:\mathbb R^n\to T_xM$.

The projection $\mathrm{Fr}(TM)\to M$ sends a frame to its basepoint. There is a right action of $\mathrm{GL}(n,\mathbb R)$ by change of basis:
\[
(x,(e_1,\dots,e_n))\cdot A := (x,(\sum_j e_j A_{j1},\dots,\sum_j e_j A_{jn})).
\]
With this structure, $\mathrm{Fr}(TM)\to M$ is a [[fiber-bundles/principal-g-bundle|principal G-bundle]] with structure group $\mathrm{GL}(n,\mathbb R)$.

Connections on $TM$ can be equivalently encoded as principal connections on $\mathrm{Fr}(TM)$ (see [[fiber-bundles/tfae-vector-bundle-connections-via-frame-bundles-rank-n-vector-bundle-em|connections via frame bundles]]).

## Examples
1. **Euclidean space.**
   For $M=\mathbb R^n$, choosing the standard coordinate frame identifies $\mathrm{Fr}(T\mathbb R^n)\cong \mathbb R^n\times \mathrm{GL}(n,\mathbb R)$.

2. **Parallelizable manifolds.**
   If $M$ admits a global frame of vector fields (a global trivialization of $TM$), then $\mathrm{Fr}(TM)$ is globally a product $M\times \mathrm{GL}(n,\mathbb R)$.

3. **The 2-sphere.**
   For $M=S^2$, the tangent bundle is nontrivial, so $\mathrm{Fr}(TS^2)$ is not isomorphic to $S^2\times \mathrm{GL}(2,\mathbb R)$. This is a bundle-level reflection of the fact that $TS^2$ has no global frame.
