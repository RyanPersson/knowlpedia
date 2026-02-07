---
title: "Principal bundle morphism"
description: "A smooth equivariant map between principal bundles covering a smooth map of the bases."
---

Let $\pi:P\to M$ and $\pi':P'\to M'$ be {{< knowl id="principal-g-bundle" text="principal G-bundles" >}} with {{< knowl id="right-principal-action" text="right actions" >}} $(p,g)\mapsto p\cdot g$ and $(p',g)\mapsto p'\cdot g$.

A **principal bundle morphism** from $P$ to $P'$ is a {{< knowl id="smooth-map" text="smooth map" >}} $\Phi:P\to P'$ for which there exists a smooth map $f:M\to M'$ such that:
1. (Covers $f$) $\pi'\circ \Phi = f\circ \pi$,
2. (Equivariance) $\Phi(p\cdot g)=\Phi(p)\cdot g$ for all $p\in P$ and $g\in G$.

The map $f$ is uniquely determined by $\Phi$ (because $\pi$ is surjective).

## Examples
1. **Pulling along a base map in the trivial case.** For trivial bundles $P=M\times G$ and $P'=M'\times G$, any smooth $f:M\to M'$ defines a morphism $\Phi(x,h)=(f(x),h)$.
2. **Induced map on frame bundles.** If $f:M\to M'$ is a {{< knowl id="diffeomorphism" text="diffeomorphism" >}}, then its derivative gives a morphism between the frame bundles, covering $f$, and compatible with the induced map on the {{< knowl id="tangent-bundle" text="tangent bundle" >}}.
3. **Restriction to an invariant open set.** If $U\subset M$ is open, the inclusion $\pi^{-1}(U)\hookrightarrow P$ is a morphism of principal bundles over the inclusion $U\hookrightarrow M$.
