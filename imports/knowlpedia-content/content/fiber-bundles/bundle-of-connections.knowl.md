+++
id = "fiber-bundles/bundle-of-connections"
title = "Bundle of connections"
kind = "knowl"
summary = "An affine bundle over a manifold whose sections are connections on a fixed bundle."
aliases = ["bundle-of-connections", "Bundle of connections"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/bundle-of-connections.md"
+++

Let $\pi\colon P\to M$ be a [[fiber-bundles/principal-g-bundle|principal G-bundle]]. The set of [[fiber-bundles/principal-connection|principal connections]] on $P$ is an affine space; the “bundle of connections” packages this affineness pointwise over $M$.

## Definition (Connection bundle; principal case)
The **bundle of connections** of $P$ is the affine bundle
\[
\mathcal{C}(P) \to M
\]
defined as the quotient
\[
\mathcal{C}(P) := J^1P / G,
\]
where $J^1P$ is the [[fiber-bundles/jet-bundle|1-jet bundle]] of $P$ and $G$ acts by prolongation of the principal right action.

It has the property that:
- Sections of $\mathcal{C}(P)\to M$ are in natural bijection with principal connections on $P$.

Moreover, $\mathcal{C}(P)\to M$ is an affine bundle modeled on the vector bundle
\[
T^*M \otimes \mathrm{Ad}(P),
\]
so the difference of two connections is an $\mathrm{Ad}(P)$-valued 1-form (a section of $T^*M\otimes \mathrm{Ad}(P)$). Here $T^*M$ is the [[fiber-bundles/cotangent-bundle|cotangent bundle]] and $\mathrm{Ad}(P)$ is the adjoint bundle associated to $P$.

## Vector bundle variant
If $E\to M$ is a vector bundle, the set of [[fiber-bundles/connection-on-a-vector-bundle|connections on E]] is an affine space modeled on $\Omega^1(M;\mathrm{End}(E))$, and there is an analogous affine bundle over $M$ whose sections correspond to connections on $E$.

## Examples
1. **Trivial principal bundle.** If $P=M\times G$, then choosing the product trivialization identifies connections with $\mathfrak{g}$-valued 1-forms on $M$, so $\mathcal{C}(P)$ is (noncanonically) isomorphic to an affine bundle modeled on $T^*M\otimes (M\times \mathfrak{g})$.
2. **Line bundles.** For a principal $U(1)$-bundle, the difference of two connections is an ordinary real 1-form on $M$, reflecting that $\mathrm{Ad}(P)$ is a trivial real line bundle.
3. **Levi–Civita as a section.** The Levi–Civita connection determines a distinguished section of the connection bundle of the orthonormal frame bundle of a Riemannian manifold.
