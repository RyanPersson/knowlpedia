---
title: "Principal G-bundle"
description: "A smooth fiber bundle with a free and transitive right action of a Lie group on each fiber and local trivializations compatible with the action."
---

Let $G$ be a {{< knowl id="lie-group" text="Lie group" >}} and let $M$ be a smooth manifold. A **principal $G$-bundle** over $M$ is a quadruple $(P,\pi,M,G)$ consisting of a {{< knowl id="smooth-manifold" text="smooth manifold" >}} $P$, a surjective submersion $\pi:P\to M$, and a smooth right action
\[
P\times G\to P,\quad (p,g)\mapsto p\cdot g,
\]
such that:

1. **Free and transitive on fibers.** For each $x\in M$, the action restricts to a free and transitive action of $G$ on the fiber $P_x:=\pi^{-1}(x)$. Equivalently, each fiber is a $G$-torsor.

2. **Local triviality (equivariant).** There exists an open cover $\{U_\alpha\}$ of $M$ and {{< knowl id="diffeomorphism" text="diffeomorphisms" >}}
   \[
   \Phi_\alpha:\pi^{-1}(U_\alpha)\to U_\alpha\times G
   \]
   such that:
   - $\mathrm{pr}_1\circ \Phi_\alpha=\pi$,
   - $\Phi_\alpha(p\cdot g) = \Phi_\alpha(p)\cdot g$, where $U_\alpha\times G$ has the right action $(x,h)\cdot g := (x,hg)$.

A morphism of principal $G$-bundles over the same base is a smooth $G$-equivariant map $\Psi:P\to P'$ commuting with projections to $M$.

Principal bundles are the natural setting for {{< knowl id="principal-connection" text="principal connections" >}}; once a connection is chosen, one can define {{< knowl id="parallel-transport" text="parallel transport" >}} along paths and the associated {{< knowl id="holonomy-group" text="holonomy group" >}}, and the curvature measures the failure of horizontal distributions to be integrable (see {{< knowl id="curvature" text="curvature" >}}).

## Examples
1. **Trivial principal bundle.** For any $M$ and $G$, the projection $M\times G\to M$ with right action $(x,h)\cdot g=(x,hg)$ is a principal $G$-bundle.

2. **Frame bundles.** If $E\to M$ is a rank-$n$ vector bundle, its {{< knowl id="frame-bundle-frame-bundle-of-a-rank-n-vector-bundle" text="frame bundle" >}} is a principal bundle with structure group $\mathrm{GL}(n,\mathbb F)$.

3. **Hopf fibration.** The map $S^3\to S^2$ can be realized as a principal $\mathrm{U}(1)$-bundle, with $\mathrm{U}(1)$ acting freely on $S^3\subset \mathbb C^2$ by scalar multiplication.
