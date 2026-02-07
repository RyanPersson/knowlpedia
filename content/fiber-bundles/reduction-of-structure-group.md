---
title: "Reduction of structure group"
description: "A way to replace the structure group G of a principal bundle by a subgroup H by choosing compatible H-frames in each fiber."
---

Let $P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} and let $H\subset G$ be a Lie subgroup of the {{< knowl id="lie-group" text="Lie group" >}} $G$.

A **reduction of structure group of $P$ from $G$ to $H$** consists of a principal $H$-bundle $\pi_H:Q\to M$ together with an injective smooth map $i:Q\hookrightarrow P$ such that:
1. $\pi\circ i=\pi_H$ (so $i$ covers $\mathrm{id}_M$),
2. $i(q\cdot h)=i(q)\cdot h$ for all $q\in Q$ and $h\in H$,
3. the induced map
   \[
   Q\times_H G \to P,\qquad [q,g]\mapsto i(q)\cdot g
   \]
   is a principal bundle isomorphism.

In this situation $Q$ is called a {{< knowl id="principal-h-subbundle" text="principal H-subbundle" >}} of $P$.

A standard equivalent characterization (useful in practice) is: a reduction to $H$ exists if and only if the associated bundle with fiber $G/H$ admits a global smooth section (here $G$ acts on $G/H$ by left multiplication).

## Examples
1. **Orientation.** The frame bundle of an $n$-manifold reduces from $GL(n)$ to $GL^+(n)$ exactly when $M$ is orientable.
2. **Riemannian metric.** A Riemannian metric determines a reduction of the frame bundle to $O(n)$, namely the orthonormal frame bundle.
3. **Almost complex structure.** An almost complex structure on a $2n$-manifold reduces the frame bundle from $GL(2n,\mathbb{R})$ to $GL(n,\mathbb{C})$ (and further to $U(n)$ when compatible with a Hermitian metric).
