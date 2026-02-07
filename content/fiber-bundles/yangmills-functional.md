---
title: "Yang–Mills functional"
description: "The energy of a connection defined as the L2 norm of its curvature on a Riemannian manifold."
---

Let $M$ be an oriented Riemannian manifold, let $G$ be a Lie group with an $\mathrm{Ad}$-invariant inner product on its Lie algebra, and let $\pi\colon P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}}.

Fix a {{< knowl id="principal-connection" text="principal connection" >}} $A$ on $P$ with {{< knowl id="curvature" text="curvature" >}} $F_A\in \Omega^2(M;\mathrm{Ad}(P))$.

## Definition (Yang–Mills functional)
The **Yang–Mills functional** is
\[
\mathrm{YM}(A) := \frac12\int_M |F_A|^2\,\mathrm{vol}_g,
\]
equivalently $\mathrm{YM}(A)=\frac12\int_M \langle F_A\wedge *F_A\rangle$ using the Hodge star of the Riemannian metric and the chosen inner product.

It is invariant under gauge transformations of $P$, so it descends to a functional on the moduli space of connections modulo gauge.

Critical points of this functional are precisely {{< knowl id="yangmills-connection" text="Yang–Mills connections" >}}, characterized by the {{< knowl id="yangmills-equation" text="Yang–Mills equation" >}}.

## Examples
1. **Flat connections.** If $F_A=0$ then $\mathrm{YM}(A)=0$, which is the minimum possible value.
2. **Abelian case (Maxwell energy).** For $G=U(1)$, the curvature is an ordinary closed 2-form, and $\mathrm{YM}(A)$ reduces to the classical electromagnetic energy $\frac12\int |F|^2$.
3. **Four dimensions and self-duality.** On an oriented 4-manifold, connections with self-dual or anti-self-dual curvature minimize $\mathrm{YM}$ within their topological class (the functional splits into a topological term plus a nonnegative remainder).
