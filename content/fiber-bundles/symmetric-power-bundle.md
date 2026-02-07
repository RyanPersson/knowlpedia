---
title: "Symmetric power bundle"
description: "The vector bundle whose fiber at each point is the k-th symmetric power of the original fiber."
---

Let $\pi:E\to M$ be a smooth vector bundle of rank $r$ over a {{< knowl id="smooth-manifold" text="smooth manifold" >}}. For an integer $k\ge 0$, the **k-th symmetric power bundle** of $E$ is the vector bundle
\[
S^k E \to M
\]
defined fiberwise by
\[
(S^k E)_x := S^k(E_x),
\]
the $k$-th symmetric power of the vector space $E_x$ (i.e. the quotient of $E_x^{\otimes k}$ by the action of the symmetric group permuting factors).

In local frames, if $(e_1,\dots,e_r)$ is a local frame of $E|_U$, then the symmetrized tensors built from the $e_i$ give a local frame of $(S^kE)|_U$. Under a change of frame with transition matrix $g$, the induced transition on $S^kE$ is the symmetric power representation $S^k g$. This can be constructed systematically from the local description of the {{< knowl id="tensor-product-vector-bundle" text="tensor product bundle" >}} $E^{\otimes k}$.

Functoriality holds: a bundle map $\Phi:E\to F$ over $\mathrm{id}_M$ induces $S^k\Phi:S^kE\to S^kF$ fiberwise.

## Examples
1. **Symmetric 2-tensors.** For $E=T^*M$, the bundle $S^2T^*M$ has sections given by symmetric covariant 2-tensor fields; a Riemannian metric is an everywhere positive-definite section of this bundle.

2. **Line bundles.** If $L\to M$ is a line bundle, then $S^k L \cong L^{\otimes k}$ canonically (since there is no nontrivial symmetrization in rank 1).

3. **Trivial bundle case.** If $E\cong M\times \mathbb F^r$, then $S^kE\cong M\times S^k(\mathbb F^r)$.
