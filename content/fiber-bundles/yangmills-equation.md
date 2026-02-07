---
title: "Yang–Mills equation"
description: "The Euler–Lagrange equation for the Yang–Mills functional, expressed as a covariant divergence-free condition on curvature."
---

Let $P\to M$ be a principal $G$-bundle over an oriented Riemannian manifold, and let $A$ be a {{< knowl id="principal-connection" text="principal connection" >}} with curvature $F_A$.

## Theorem/Definition (Yang–Mills equation)
The Euler–Lagrange equation for the {{< knowl id="yangmills-functional" text="Yang–Mills functional" >}} is
\[
d_A(*F_A)=0.
\]
Here $d_A$ is the covariant exterior derivative on $\mathrm{Ad}(P)$-valued forms, which extends the {{< knowl id="exterior-derivative" text="exterior derivative" >}} on ordinary forms and satisfies the Bianchi identity $d_A F_A=0.

A connection $A$ satisfying $d_A(*F_A)=0$ is called a Yang–Mills connection.

## Examples
1. **Flat connections.** If $F_A=0$ then $d_A(*F_A)=0$ automatically.
2. **Abelian reduction.** For $G=U(1)$, the equation becomes $d(*F)=0$, the source-free Maxwell equation for the curvature 2-form $F$.
3. **Instantons in dimension 4.** On a 4-manifold, any connection with self-dual or anti-self-dual curvature satisfies the Yang–Mills equation because $*F_A=\pm F_A$ and the Bianchi identity gives $d_A(*F_A)=\pm d_AF_A=0$.
