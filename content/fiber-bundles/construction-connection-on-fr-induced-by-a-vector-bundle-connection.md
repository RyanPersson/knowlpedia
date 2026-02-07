---
title: "Construction: Connection on Fr(E) induced by a vector bundle connection (and conversely)"
description: "Equivalence between covariant derivatives on a vector bundle and principal connections on its frame bundle."
---

Let $\pi:E\to M$ be a rank-$n$ smooth vector bundle over a {{< knowl id="smooth-manifold" text="smooth manifold" >}} $M$, and let $P=\mathrm{Fr}(E)$ be its {{< knowl id="construction-frame-bundle-fr-of-a-vector-bundle-e" text="frame bundle" >}} (a principal $\mathrm{GL}(n,\mathbb R)$-bundle).

## From a vector bundle connection to a principal connection

Let $\nabla$ be a {{< knowl id="connection-on-a-vector-bundle" text="connection on the vector bundle" >}} $E$. Define horizontality in $P$ by parallel transport of frames:

For a point $u\in P_x$ (a frame $u:\mathbb R^n\to E_x$) and a tangent vector $v_x\in T_xM$, choose a smooth curve $\gamma:(-\varepsilon,\varepsilon)\to M$ with $\gamma(0)=x$ and $\dot\gamma(0)=v_x$. Let $\tau_t:E_x\to E_{\gamma(t)}$ denote parallel transport in $E$ induced by $\nabla$ along $\gamma$. Then define a curve of frames
\[
u(t):=\tau_t\circ u \in P_{\gamma(t)}.
\]
The horizontal lift of $v_x$ at $u$ is $\dot u(0)\in T_uP$, and the span of all such vectors defines a horizontal subspace $H_u\subset T_uP$.

The assignment $u\mapsto H_u$ is $\mathrm{GL}(n,\mathbb R)$-equivariant and complementary to the vertical subspace, hence defines a {{< knowl id="principal-connection" text="principal connection" >}} on $P$.

## From a principal connection to a vector bundle connection

Conversely, suppose $P=\mathrm{Fr}(E)$ carries a principal connection. The associated bundle
\[
P\times_{\mathrm{GL}(n,\mathbb R)}\mathbb R^n
\]
is canonically isomorphic to $E$. A principal connection on $P$ induces a covariant derivative on every associated vector bundle, hence in particular a vector bundle connection $\nabla$ on $E$.

These two constructions are inverse to each other: connections on $E$ are in bijection with principal connections on $\mathrm{Fr}(E)$.

## Examples

1. **Levi-Civita connection.** For $E=TM$, a Riemannian metric gives a unique torsion-free metric connection on $TM$, and the induced principal connection on $\mathrm{Fr}(TM)$ can be described by horizontals consisting of parallel transported frames.

2. **Trivial bundle and flat connection.** If $E\cong M\times\mathbb R^n$ with the standard flat covariant derivative, then the induced principal connection on $\mathrm{Fr}(E)\cong M\times \mathrm{GL}(n,\mathbb R)$ has horizontal subspaces equal to the tangent directions along $M$.

3. **Parallel transport viewpoint.** In both directions, the induced notion of {{< knowl id="parallel-transport" text="parallel transport" >}} agrees: transporting a frame in $P$ horizontally along a curve is the same as transporting each vector in the frame by the covariant derivative on $E$.
