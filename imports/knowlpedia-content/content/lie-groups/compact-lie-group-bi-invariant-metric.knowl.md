+++
id = "lie-groups/compact-lie-group-bi-invariant-metric"
title = "Bi-invariant metrics on compact Lie groups"
kind = "knowl"
summary = "A compact Lie group always admits a bi-invariant Riemannian metric by averaging."
aliases = ["compact-lie-group-bi-invariant-metric", "Bi-invariant metrics on compact Lie groups"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/compact-lie-group-bi-invariant-metric.md"
+++

Let $G$ be a [[lie-groups/compact-lie-group|compact Lie group]] with Lie algebra $\mathfrak{g}$.

**Theorem.** $G$ admits a [[lie-groups/bi-invariant-metric|bi-invariant Riemannian metric]]. Equivalently, there exists an inner product on $\mathfrak{g}$ invariant under the [[lie-groups/adjoint-action-of-a-lie-group|adjoint action]] of $G$.

**Idea of construction (averaging).** Start with any inner product $\langle\cdot,\cdot\rangle_0$ on $\mathfrak{g}$, and define a new inner product by averaging over $G$ using Haar measure:
$$
\langle X,Y\rangle := \int_G \langle \mathrm{Ad}_g X,\, \mathrm{Ad}_g Y\rangle_0 \, dg.
$$

This averaged form is $\mathrm{Ad}(G)$-invariant by construction, and it induces a bi-invariant metric on $G$ via left translation.

**Consequences.** With a bi-invariant metric, geodesics through the identity are exactly [[lie-groups/one-parameter-subgroup|one-parameter subgroups]], making the [[lie-groups/exponential-map-lie-group|exponential map]] geometrically canonical. This also provides natural bi-invariant volume forms and simplifies curvature computations.
