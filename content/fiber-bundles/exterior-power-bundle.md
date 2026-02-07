---
title: "Exterior power bundle"
description: "The vector bundle whose fiber at each point is the k-th exterior power of the original fiber."
---

Let $\pi:E\to M$ be a smooth vector bundle of rank $r$ over a {{< knowl id="smooth-manifold" text="smooth manifold" >}}. For an integer $k$ with $0\le k\le r$, the **k-th exterior power bundle** of $E$ is the vector bundle
\[
\Lambda^k E \to M
\]
defined fiberwise by
\[
(\Lambda^k E)_x := \Lambda^k(E_x).
\]

If $(e_1,\dots,e_r)$ is a local frame of $E|_U$, then the wedge products
\[
e_{i_1}\wedge \cdots \wedge e_{i_k}\qquad (1\le i_1<\cdots<i_k\le r)
\]
form a local frame of $(\Lambda^k E)|_U$. Under a change of local frame with transition matrix $g:U\cap V\to \mathrm{GL}(r,\mathbb F)$, the induced transition matrix on $\Lambda^kE$ is the $k$-th exterior power representation $\Lambda^k g$.

The construction is functorial: a {{< knowl id="vector-bundle-morphism" text="vector bundle morphism" >}} $\Phi:E\to F$ over $\mathrm{id}_M$ induces $\Lambda^k\Phi:\Lambda^kE\to \Lambda^kF$ fiberwise.

This exterior-power construction is compatible with the {{< knowl id="tensor-product-vector-bundle" text="tensor product bundle" >}} viewpoint via universal properties.

## Examples
1. **Forms as sections.** Taking $E=T^*M$, the sections of $\Lambda^k T^*M$ are precisely smooth {{< knowl id="differential-k-form" text="differential k-forms" >}} on $M$.

2. **Determinant line bundle.** For a rank $r$ bundle $E$, the top exterior power $\Lambda^r E$ is a line bundle, often denoted $\det(E)$. An {{< knowl id="orientation-of-a-real-vector-bundle" text="orientation" >}} of a real bundle can be encoded as a choice of “positive” component in $\det(E)\setminus\{0\}$.

3. **Low-degree cases.** $\Lambda^0E$ is canonically the trivial line bundle $M\times \mathbb F$, and $\Lambda^1E\cong E$ canonically.
