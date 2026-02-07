---
title: "Parallel transport for an Ehresmann connection"
description: "Transport along a base curve defined by taking the endpoint of its horizontal lift in the total space."
---

Let $\pi:E\to M$ be a surjective submersion equipped with an Ehresmann connection. For a smooth curve $\gamma:[0,1]\to M$ and an initial point $e_0\in E_{\gamma(0)}$, let $\widetilde\gamma$ denote the {{< knowl id="horizontal-lift-of-a-curve" text="horizontal lift of the curve" >}} with $\widetilde\gamma(0)=e_0$, defined (at least) on $[0,1]$ whenever the lift exists globally.

**Definition.** The parallel transport along $\gamma$ is the map
\[
P_\gamma: E_{\gamma(0)} \longrightarrow E_{\gamma(1)},\qquad
P_\gamma(e_0):=\widetilde\gamma(1),
\]
where $\widetilde\gamma$ is the horizontal lift starting at $e_0$.

When parallel transport is defined for all initial points in the fiber, $P_\gamma$ is a diffeomorphism between the fibers. If the connection comes from a vector bundle connection, $P_\gamma$ is linear on each fiber; if it comes from a principal connection, it is $G$-equivariant.

Parallel transport along loops based at $x\in M$ generates the {{< knowl id="holonomy-group" text="holonomy group" >}} at $x$, and its failure to be path-independent is governed by {{< knowl id="curvature" text="curvature" >}}.

## Examples
1. **Product bundle.** For $E=M\times F$ with the product connection, $P_\gamma$ is the identity map on the fiber $F$: it sends $(\gamma(0),f)$ to $(\gamma(1),f)$.
2. **Levi-Civita transport on tangent vectors.** For the Levi-Civita connection on the tangent bundle, $P_\gamma$ transports tangent vectors along $\gamma$ by keeping them covariantly constant; on a sphere this produces the classical “rotation” effect around a loop.
3. **Line bundle with a local 1-form.** On a complex line bundle with connection given locally by a 1-form $A$, parallel transport along $\gamma$ multiplies a vector in the fiber by a phase factor determined by integrating $A$ along $\gamma$ (after choosing a local trivialization).
