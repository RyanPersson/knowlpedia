+++
id = "fiber-bundles/yangmills-connection"
title = "Yang–Mills connection"
kind = "knowl"
summary = "A connection whose curvature is a critical point of the Yang–Mills functional, equivalently satisfying the Yang–Mills equation."
aliases = ["yangmills-connection", "Yang–Mills connection"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/yangmills-connection.md"
+++

Let $P\to M$ be a principal $G$-bundle over an oriented Riemannian manifold.

## Definition (Yang–Mills connection)
A [[fiber-bundles/principal-connection|principal connection]] $A$ on $P$ is called a **Yang–Mills connection** if it satisfies the [[fiber-bundles/yangmills-equation|Yang–Mills equation]]
\[
d_A(*F_A)=0,
\]
where $F_A$ is its [[fiber-bundles/curvature|curvature]].

Equivalently, $A$ is a Yang–Mills connection if it is a critical point of the [[fiber-bundles/yangmills-functional|Yang–Mills functional]] with respect to compactly supported variations.

## Examples
1. **Flat connections.** Any flat connection is Yang–Mills, since its curvature vanishes.
2. **Anti-self-dual connections.** On an oriented 4-manifold, ASD (or SD) connections are Yang–Mills; these are the basic instanton solutions in gauge theory.
3. **Constant central curvature on surfaces.** On a closed oriented surface, Yang–Mills connections are precisely those whose curvature is covariantly constant and takes values in the center of the Lie algebra (a two-dimensional special feature).
