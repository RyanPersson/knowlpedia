---
title: "Reducing a GL(n)-structure to O(n) using a bundle metric"
description: "A fiberwise inner product reduces the structure group of a frame bundle from GL(n) to O(n)."
---

Let $E\to M$ be a smooth real rank-$n$ vector bundle over a smooth manifold $M$. Its frame bundle $\mathrm{Fr}(E)\to M$ is a principal $\mathrm{GL}(n,\mathbb R)$-bundle.

A **reduction of structure group** from $\mathrm{GL}(n,\mathbb R)$ to a subgroup $H\subset \mathrm{GL}(n,\mathbb R)$ is, by definition, a principal $H$-subbundle $Q\subset \mathrm{Fr}(E)$ such that
\[
Q\times_H \mathbb R^n \cong E
\]
as associated bundles.

## Example (bundle metric gives an O(n)-reduction)
A **bundle metric** on $E$ is a smooth choice of inner product $\langle\cdot,\cdot\rangle_x$ on each fiber $E_x$.

Given such a metric, define
\[
O(E):=\{u\in \mathrm{Fr}(E): u:\mathbb R^n\to E_x \text{ is an isometry for the standard inner product}\}.
\]
Then:
- $O(E)\to M$ is a principal $\mathrm{O}(n)$-bundle, where $\mathrm{O}(n)$ is a {{< knowl id="lie-group" text="Lie group" >}} acting by postcomposition on frames.
- The inclusion $O(E)\subset \mathrm{Fr}(E)$ is a reduction of the principal {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} $\mathrm{Fr}(E)\to M$ from $\mathrm{GL}(n)$ to $\mathrm{O}(n)$.
- Conversely, any principal $\mathrm{O}(n)$-subbundle $Q\subset \mathrm{Fr}(E)$ determines a unique bundle metric by declaring frames in $Q$ to be orthonormal.

Specializing to $E=TM$ recovers the construction of the {{< knowl id="orthonormal-frame-bundle-o-of-a-riemannian-manifold" text="orthonormal frame bundle" >}}.

## Examples
1. **Riemannian manifolds.**  
   For $E=TM$, choosing a Riemannian metric on $M$ produces the reduction $\mathrm{Fr}(TM)\supset O(TM)$.

2. **Trivial bundle with standard metric.**  
   For the trivial bundle $M\times\mathbb R^n$, the standard Euclidean inner product yields $O(E)\cong M\times \mathrm{O}(n)$ as a reduction of $M\times \mathrm{GL}(n)$.

3. **Changing the metric changes the reduction.**  
   Two different bundle metrics on the same underlying bundle generally produce different $\mathrm{O}(n)$-subbundles of $\mathrm{Fr}(E)$, even though both reductions have the same associated bundle $E$.
