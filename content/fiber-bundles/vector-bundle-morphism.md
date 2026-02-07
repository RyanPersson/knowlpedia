---
title: "Vector bundle morphism"
description: "A smooth map between total spaces of vector bundles that covers a base map and is linear on each fiber."
---

Let $\pi_E:E\to M$ and $\pi_F:F\to N$ be smooth real or complex vector bundles. A **vector bundle morphism** (also called a *fiberwise linear bundle map*) from $E$ to $F$ is a pair $(\Phi,f)$ consisting of a {{< knowl id="smooth-map" text="smooth map" >}} $\Phi:E\to F$ and a smooth map $f:M\to N$ such that:

1. **Covers the base map:** $\pi_F\circ \Phi = f\circ \pi_E$.

2. **Fiberwise linearity:** for every $x\in M$, the induced map on fibers
   \[
   \Phi_x:E_x\to F_{f(x)},\qquad \Phi_x(v):=\Phi(v),
   \]
   is $\mathbb F$-linear (with $\mathbb F=\mathbb R$ or $\mathbb C$ according to the bundles).

If $M=N$ and $f=\mathrm{id}_M$, one often says $\Phi:E\to F$ is a *bundle map over $M$*.

Composition of vector bundle morphisms is defined by composition of the total-space maps and the base maps, and yields a category of smooth vector bundles and bundle morphisms.

## Examples
1. **Differential of a smooth map.** For any smooth map $f:M\to N$, the differential
   \[
   df:TM\to TN
   \]
   is a vector bundle morphism covering $f$ between the {{< knowl id="tangent-bundle" text="tangent bundles" >}}.

2. **Projection from a direct sum.** For bundles $E,F\to M$, the projection $\mathrm{pr}_E:E\oplus F\to E$ is a bundle morphism over $\mathrm{id}_M$, fiberwise the linear projection $E_x\oplus F_x\to E_x$.

3. **Inclusion of a subbundle.** If $E\subseteq F$ is a smooth vector subbundle over the same base $M$, then the inclusion map $E\hookrightarrow F$ is a vector bundle morphism over $\mathrm{id}_M$.
