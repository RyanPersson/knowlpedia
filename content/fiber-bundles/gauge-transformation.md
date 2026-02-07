---
title: "Gauge transformation"
description: "A principal bundle automorphism that covers the identity map on the base manifold."
---

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}}. A gauge transformation is a special case of a {{< knowl id="principal-bundle-automorphism" text="principal bundle automorphism" >}}.

A **gauge transformation** of $P$ is a smooth map $\Phi:P\to P$ such that:
1. (Base-preserving) $\pi\circ\Phi=\pi$,
2. (Equivariance) $\Phi(p\cdot g)=\Phi(p)\cdot g$ for all $p\in P$ and $g\in G$,
3. (Invertibility) $\Phi$ is a diffeomorphism (equivalently, an automorphism in the principal-bundle sense).

Every gauge transformation can be written uniquely in the form
\[
\Phi(p)=p\cdot u(p)
\]
for a smooth map $u:P\to G$ satisfying the conjugation-equivariance condition
\[
u(p\cdot g)=g^{-1}u(p)g.
\]
Such maps $u$ are the same data as smooth sections of the {{< knowl id="adjoint-bundle-p-g-g-with-conjugation-action" text="adjoint bundle" >}} $\mathrm{Ad}(P)$ (often described explicitly in {{< knowl id="section-of-ad" text="sections of Ad(P)" >}}).

## Examples
1. **Trivial bundle.** For $P=M\times G$, any smooth map $g:M\to G$ defines a gauge transformation by
   \[
   \Phi(x,h)=(x,\,g(x)\,h).
   \]
2. **Abelian structure group.** If $G$ is abelian (e.g. $U(1)$), the conjugation condition on $u$ becomes $u(p\cdot g)=u(p)$, so gauge transformations correspond to smooth $G$-valued functions on $M$.
3. **Frames of a vector bundle.** For the frame bundle of a rank-$n$ vector bundle $E\to M$, gauge transformations correspond to bundle automorphisms of $E$ covering $\mathrm{id}_M$ (locally given by $GL(n)$-valued functions acting on frames).
