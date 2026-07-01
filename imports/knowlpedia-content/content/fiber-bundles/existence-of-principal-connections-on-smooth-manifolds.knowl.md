+++
id = "fiber-bundles/existence-of-principal-connections-on-smooth-manifolds"
title = "Theorem: Existence of principal connections on smooth manifolds"
kind = "knowl"
summary = "Every principal bundle over a smooth manifold admits a principal connection, using partitions of unity."
aliases = ["existence-of-principal-connections-on-smooth-manifolds", "Theorem: Existence of principal connections on smooth manifolds"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/existence-of-principal-connections-on-smooth-manifolds.md"
+++

Let $M$ be a [[fiber-bundles/smooth-manifold|smooth manifold]] and let $\pi:P\to M$ be a [[fiber-bundles/principal-g-bundle|principal G-bundle]] with structure group $G$.

## Theorem

There exists at least one [[fiber-bundles/principal-connection|principal connection]] on $P$.

Equivalently: every principal bundle over a smooth manifold admits a $G$-equivariant horizontal distribution $H\subset TP$ complementary to the vertical subbundle.

## Examples

1. **Trivial bundle.** On $P=M\times G$, the product distribution $T M\oplus 0$ defines a connection; in connection-form language, this is the “flat” connection.

2. **Frame bundle connections.** Applying this theorem to $P=\mathrm{Fr}(E)$ gives existence of connections on any vector bundle $E\to M$; compare [[fiber-bundles/construction-connection-on-fr-induced-by-a-vector-bundle-connection|connections on Fr(E) induced by covariant derivatives]].

3. **Hopf fibration.** The principal $U(1)$-bundle $S^3\to S^2$ admits the standard connection whose horizontal spaces are orthogonal complements of the fiber circles (with respect to the round metric on $S^3$).
