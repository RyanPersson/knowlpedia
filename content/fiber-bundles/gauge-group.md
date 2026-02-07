---
title: "Gauge group"
description: "The gauge group of a principal G bundle is the group of principal bundle automorphisms that cover the identity map of the base."
---

Let $\pi\colon P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with right action of $G$ on $P$.

The **gauge group** of $P$ is
\[
\mathcal{G}(P):=\mathrm{Aut}_G(P),
\]
the group of {{< knowl id="principal-bundle-automorphism" text="principal bundle automorphisms" >}} $\Phi\colon P\to P$ that cover the identity on the base:
\[
\pi\circ \Phi = \pi.
\]
Composition of automorphisms is the group operation.

## Equivalent descriptions
1. (**Equivariant maps into G**) A gauge transformation can be encoded by a smooth map $u\colon P\to G$ satisfying the equivariance condition
   \[
   u(pg)=g^{-1}u(p)g,
   \]
   using the {{< knowl id="conjugation-action-of-a-lie-group-on-itself" text="conjugation action of G on itself" >}}. From such a map, define
   \[
   \Phi_u(p):=p\cdot u(p).
   \]
   Then $\Phi_u$ is a principal bundle automorphism covering $\mathrm{id}_M$, and every element of $\mathcal{G}(P)$ arises uniquely this way.

2. (**Sections of the adjoint bundle**) Using the same conjugation action, form the {{< knowl id="adjoint-bundle-p-g-g-with-conjugation-action" text="adjoint bundle" >}}
   \[
   \mathrm{Ad}(P):=P\times_G G.
   \]
   The gauge group is naturally identified with the group of smooth {{< knowl id="section-of-ad" text="sections of Ad(P)" >}}, with pointwise multiplication in the fiber.

Gauge transformations act on connections: if $\nabla$ is a {{< knowl id="principal-connection" text="principal connection" >}} on $P$, then any $\Phi\in\mathcal{G}(P)$ produces a new connection by pullback as in {{< knowl id="proposition-gauge-group-acts-on-conn-by-pullback" text="the gauge action on the space of connections" >}}. This is the global version of a {{< knowl id="gauge-transformation" text="gauge transformation" >}} in local trivializations.

## Examples
1. **Trivial principal bundle.** If $P\cong M\times G$ is trivial, then
   \[
   \mathcal{G}(P)\cong C^\infty(M,G),
   \]
   with multiplication pointwise in $G$. Under this identification, $g\in C^\infty(M,G)$ acts by $(x,h)\mapsto (x, g(x)h)$.
2. **Abelian structure group.** If $G$ is abelian, conjugation is trivial, so $\mathrm{Ad}(P)\cong M\times G$ for any $P$. Hence $\mathcal{G}(P)\cong C^\infty(M,G)$ even when $P$ is not trivial (for example, for circle bundles with $G=U(1)$).
3. **Frame bundle viewpoint.** If $E\to M$ is a rank-$n$ vector bundle and $P=\mathrm{Fr}(E)$ is its {{< knowl id="construction-frame-bundle-fr-of-a-vector-bundle-e" text="frame bundle" >}}, then $\mathcal{G}(P)$ identifies with the group of vector bundle automorphisms of $E$ covering $\mathrm{id}_M$ (equivalently, fiberwise $GL(n)$-valued “change of frame” fields).
