---
title: "Dirac monopole connection on the Hopf bundle"
description: "A principal U(1) connection on the Hopf bundle whose curvature is a nonzero two-form on the 2-sphere."
---

Consider the {{< knowl id="hopf-fibration-s3s2-as-a-principal-u-bundle" text="Hopf fibration" >}} $\pi:S^3\to S^2$, a principal $U(1)$-bundle.

## Definition (Dirac monopole connection)
A **Dirac monopole connection** is a {{< knowl id="principal-connection" text="principal connection" >}} on $\pi:S^3\to S^2$ whose curvature 2-form on the base represents the generator of $H^2(S^2;\mathbb Z)$ under the usual normalization for circle bundles.

One standard description uses local gauge potentials on the usual two-chart cover of $S^2$:

- On $U_N=S^2\setminus\{\text{south pole}\}$, choose a local section and define a 1-form $A_N$.
- On $U_S=S^2\setminus\{\text{north pole}\}$, choose a local section and define a 1-form $A_S$.

These satisfy on the overlap $U_N\cap U_S$ the gauge relation
\[
A_S = A_N - d\chi
\]
for a transition function $e^{i\chi}:U_N\cap U_S\to U(1)$ of winding number $1$.

A convenient explicit choice in spherical coordinates $(\theta,\varphi)$ on the overlap is
\[
A_N=\frac{1-\cos\theta}{2}\,d\varphi,
\qquad
A_S=-\frac{1+\cos\theta}{2}\,d\varphi,
\]
which differ by $A_S=A_N-d\varphi$ on the overlap (so $\chi=\varphi$).

## Curvature
The {{< knowl id="curvature" text="curvature" >}} 2-form is globally well-defined on $S^2$ by
\[
F = dA_N = dA_S = \frac12\sin\theta\, d\theta\wedge d\varphi.
\]
This is a nonzero multiple of the standard area form. In particular, $F$ is not exact as a globally defined 2-form with the integrality normalization for $U(1)$-bundles; geometrically, this encodes the nontriviality of the Hopf bundle.

## Examples
1. **Holonomy around latitude circles.**  
   Fix $\theta=\theta_0$. Parallel transport around the loop $\varphi\in[0,2\pi]$ produces a phase in $U(1)$ whose argument is the integral of $A_N$ (or $A_S$) along the loop; this equals half the solid angle enclosed, matching the curvature-area interpretation.

2. **Higher charge monopoles.**  
   Replacing the transition function $e^{i\varphi}$ by $e^{in\varphi}$ yields a family of principal $U(1)$-bundles and connections with curvature $nF$, corresponding to Chern number $n$.

3. **Intrinsic description on the total space.**  
   There is a canonical $U(1)$-invariant 1-form on $S^3$ (a contact form) whose kernel defines the horizontal distribution; pushing this connection down recovers the above local potentials on the base.
