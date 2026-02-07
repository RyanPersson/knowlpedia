---
title: "Theorem: Parallel transport defines a G-equivariant map between fibers"
description: "Parallel transport along a curve yields a right G-equivariant diffeomorphism between principal bundle fibers."
---

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with a {{< knowl id="principal-connection" text="principal connection" >}}.

Let $\gamma:[a,b]\to M$ be a smooth curve with $\gamma(a)=x$ and $\gamma(b)=y$.

## Theorem

Define $\tau_\gamma:P_x\to P_y$ by the rule: for $p\in P_x$, let $\widetilde\gamma_p$ be the unique horizontal lift of $\gamma$ with $\widetilde\gamma_p(a)=p$ (existence/uniqueness is in {{< knowl id="existenceuniqueness-of-horizontal-lift-of-a-curve" text="horizontal lift existence/uniqueness" >}}), and set
\[
\tau_\gamma(p):=\widetilde\gamma_p(b)\in P_y.
\]
Then:

1. $\tau_\gamma$ is a smooth bijection (indeed a diffeomorphism) from $P_x$ to $P_y$.
2. $\tau_\gamma$ is right $G$-equivariant:
   \[
   \tau_\gamma(p\cdot g)=\tau_\gamma(p)\cdot g\qquad \forall\,p\in P_x,\ g\in G.
   \]
3. $\tau_\gamma$ depends smoothly on $p$ and on the curve $\gamma$ under smooth variations.

This map is the principal-bundle version of {{< knowl id="parallel-transport" text="parallel transport" >}}.

## Examples

1. **Trivial bundle.** For $P=M\times G$ with connection form $A$, parallel transport along $\gamma$ acts by $(x,g_0)\mapsto (y,g(b))$, where $g(t)$ solves the ODE determined by $A$ along $\gamma$.

2. **Flat connection.** If the connection is flat (zero curvature), then $\tau_\gamma$ depends only on the homotopy class of $\gamma$ with fixed endpoints; the resulting representation of $\pi_1(M,x)$ is the holonomy representation.

3. **Circle bundle phases.** For $G=U(1)$, $\tau_\gamma$ is multiplication by a phase factor in $U(1)$; on associated complex line bundles this is the usual phase change of a transported vector.
