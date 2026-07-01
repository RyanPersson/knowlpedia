+++
id = "fiber-bundles/construction-curvature-of-an-induced-associated-connection-via-representation"
title = "Curvature of an induced associated connection via a representation"
kind = "knowl"
summary = "How principal curvature induces curvature on an associated vector bundle through the Lie algebra representation."
aliases = ["construction-curvature-of-an-induced-associated-connection-via-representation", "Curvature of an induced associated connection via a representation"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/construction-curvature-of-an-induced-associated-connection-via-representation.md"
+++

Let $P\to M$ be a [[fiber-bundles/principal-g-bundle|principal G-bundle]] with [[fiber-bundles/principal-connection|principal connection]] $\omega$ and curvature $\Omega\in\Omega^2(P;\mathfrak g)$. Let $E=P\times_G V$ be an associated vector bundle for a representation $\rho:G\to \mathrm{GL}(V)$, with induced covariant derivative $\nabla$ as in [[fiber-bundles/construction-induced-covariant-derivative-on-associated-vector-bundle-sections|induced covariant derivative]]. Let $\rho_*:\mathfrak g\to \mathrm{End}(V)$ be the derived representation.

**Statement.** The curvature of $\nabla$ is the $\mathrm{End}(V)$-valued 2-form obtained by applying $\rho_*$ to the principal curvature:
- On $P$, the horizontal, equivariant $\mathrm{End}(V)$-valued 2-form is $\rho_*(\Omega)$.
- On $M$, in a local gauge $s:U\to P$ with $A=s^*\omega$ and $F=s^*\Omega$, the associated curvature is
  \[
  F_V = \rho_*(F)\in \Omega^2(U;\mathrm{End}(V)).
  \]

Equivalently, for any section $s$ of $E$,
\[
\nabla^2 s = \rho_*(F)\,s
\]
in local form, expressing that the curvature acts through the infinitesimal representation.

## Examples
1. For the defining representation of $\mathrm{GL}(n)$, this recovers the usual matrix-valued curvature of a rank-$n$ vector bundle connection.
2. If the principal connection is flat (principal curvature zero), then every induced associated connection is flat.
3. For the adjoint representation on $\mathfrak g$, the induced curvature on $\mathrm{ad}(P)$ is given by the bracket action $\mathrm{ad}_{F}$ in local form.
