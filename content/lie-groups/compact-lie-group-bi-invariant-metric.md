---
title: "Bi-invariant metrics on compact Lie groups"
description: "A compact Lie group always admits a bi-invariant Riemannian metric by averaging."
---

Let $G$ be a {{< knowl id="compact-lie-group" text="compact Lie group" >}} with Lie algebra $\mathfrak{g}$.

**Theorem.** $G$ admits a {{< knowl id="bi-invariant-metric" text="bi-invariant Riemannian metric" >}}. Equivalently, there exists an inner product on $\mathfrak{g}$ invariant under the {{< knowl id="adjoint-action-of-a-lie-group" text="adjoint action" >}} of $G$.

**Idea of construction (averaging).** Start with any inner product $\langle\cdot,\cdot\rangle_0$ on $\mathfrak{g}$, and define a new inner product by averaging over $G$ using Haar measure:
$$
\langle X,Y\rangle := \int_G \langle \mathrm{Ad}_g X,\, \mathrm{Ad}_g Y\rangle_0 \, dg.
$$

This averaged form is $\mathrm{Ad}(G)$-invariant by construction, and it induces a bi-invariant metric on $G$ via left translation.

**Consequences.** With a bi-invariant metric, geodesics through the identity are exactly {{< knowl id="one-parameter-subgroup" text="one-parameter subgroups" >}}, making the {{< knowl id="exponential-map-lie-group" text="exponential map" >}} geometrically canonical. This also provides natural bi-invariant volume forms and simplifies curvature computations.
