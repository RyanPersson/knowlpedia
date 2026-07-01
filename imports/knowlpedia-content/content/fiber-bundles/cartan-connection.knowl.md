+++
id = "fiber-bundles/cartan-connection"
title = "Cartan connection"
kind = "knowl"
summary = "A g-valued 1-form on a principal H-bundle that models the geometry of a manifold on a homogeneous space G/H."
aliases = ["cartan-connection", "Cartan connection"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/cartan-connection.md"
+++

Let $G$ be a [[fiber-bundles/lie-group|Lie group]] with [[lie-groups/lie-algebra|Lie algebra]] $\mathfrak{g}$, and let $H\subset G$ be a closed subgroup with Lie algebra $\mathfrak{h}$.

## Definition (Cartan connection)
Let $\pi\colon P\to M$ be a principal $H$-bundle over a smooth manifold $M$. A **Cartan connection** on $P$ (modeled on $(G,H)$) is a $\mathfrak{g}$-valued 1-form
\[
\omega \in \Omega^1(P;\mathfrak{g})
\]
satisfying, for every $p\in P$:

1. (**Linear isomorphism**) The map $\omega_p\colon T_pP\to \mathfrak{g}$ is a linear isomorphism.
2. (**Equivariance**) For all $h\in H$, $(R_h)^*\omega = \mathrm{Ad}(h^{-1})\omega$.
3. (**Reproduces generators**) For every $X\in \mathfrak{h}$, if $X^\#$ is the corresponding fundamental vertical vector field on $P$, then $\omega(X^\#)=X$.

The curvature of a Cartan connection is the $\mathfrak{g}$-valued 2-form
\[
\Omega := d\omega + \tfrac12[\omega,\omega],
\]
where the bracket uses the [[fiber-bundles/lie-bracket|Lie bracket]] on $\mathfrak{g}$. This generalizes the curvature of a [[fiber-bundles/principal-connection|principal connection]] but with the key strengthening that $\omega$ identifies each tangent space $T_pP$ with $\mathfrak{g}$.

## Examples
1. **Homogeneous model geometry.** On the principal $H$-bundle $G\to G/H$, the Maurer–Cartan form is a Cartan connection with zero curvature; this is the “flat” Cartan geometry modeled on $G/H$.
2. **Riemannian geometry as Cartan geometry.** On the orthonormal frame bundle of a Riemannian manifold, combining the Levi–Civita connection 1-form with the solder form produces a Cartan connection modeled on Euclidean space (with model group the Euclidean group and stabilizer $O(n)$).
3. **Projective and conformal geometries.** Standard projective or conformal structures can be encoded as Cartan geometries modeled on appropriate homogeneous spaces; the Cartan curvature measures deviation from the flat model.
