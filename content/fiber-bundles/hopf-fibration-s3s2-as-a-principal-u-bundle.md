---
title: "Hopf fibration as a principal U(1)-bundle"
description: "The classic circle bundle with total space the 3-sphere and base the 2-sphere."
---

Let $S^3=\{(z_1,z_2)\in\mathbb C^2:|z_1|^2+|z_2|^2=1\}$ and let $U(1)\subset\mathbb C^\times$ act on $S^3$ by scalar multiplication:
\[
(z_1,z_2)\cdot u := (z_1u, z_2u),\qquad u\in U(1).
\]

## Definition (Hopf fibration)
The **Hopf fibration** is the quotient map
\[
\pi:S^3\longrightarrow S^3/U(1)\cong \mathbb{CP}^1 \cong S^2.
\]
With this action, $\pi$ is a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with structure group $U(1)$ (a {{< knowl id="lie-group" text="Lie group" >}}), i.e. a principal circle bundle over $S^2$.

Concretely, one can take $\pi(z_1,z_2)=[z_1:z_2]\in\mathbb{CP}^1$, and the fiber over a point is exactly the $U(1)$-orbit of any representative.

This bundle is nontrivial; in particular it has no global smooth section (compare {{< knowl id="counterexample-nontrivial-principal-bundle-admitting-no-global-section" text="the section criterion for triviality" >}}).

## Examples
1. **Local trivializations from the standard affine charts.**  
   On the open set $U_2=\{[z_1:z_2]\in\mathbb{CP}^1: z_2\neq 0\}$, write $w=z_1/z_2\in\mathbb C$. A point in $S^3$ over $w$ can be uniquely written as
   \[
   \frac{1}{\sqrt{1+|w|^2}}(w,1)\cdot u,\qquad u\in U(1),
   \]
   giving a smooth identification $\pi^{-1}(U_2)\cong U_2\times U(1)$. A similar trivialization holds on $U_1=\{z_1\neq 0\}$.

2. **Clutching function.**  
   Using the two chart trivializations, the transition function on the overlap is the map $S^1\to U(1)$ of degree $1$ (it winds once). This winding is the basic topological reason the bundle is not isomorphic to $S^2\times U(1)$.

3. **Natural connection.**  
   The Hopf bundle carries a canonical principal connection whose curvature is a multiple of the area form on the base; this is the geometric starting point for the {{< knowl id="dirac-monopole-connection-on-the-hopf-bundle" text="Dirac monopole connection" >}}.
