+++
id = "fiber-bundles/yangmills-equation"
title = "Yang–Mills equation"
kind = "knowl"
summary = "The Euler–Lagrange equation for the Yang–Mills functional, expressed as a covariant divergence-free condition on curvature."
aliases = ["yangmills-equation", "Yang–Mills equation"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/yangmills-equation.md"
+++

Let $P\to M$ be a principal $G$-bundle over an oriented Riemannian manifold, and let $A$ be a [[fiber-bundles/principal-connection|principal connection]] with curvature $F_A$.

## Theorem/Definition (Yang–Mills equation)
The Euler–Lagrange equation for the [[fiber-bundles/yangmills-functional|Yang–Mills functional]] is
\[
d_A(*F_A)=0.
\]
Here $d_A$ is the covariant exterior derivative on $\mathrm{Ad}(P)$-valued forms, which extends the [[fiber-bundles/exterior-derivative|exterior derivative]] on ordinary forms and satisfies the Bianchi identity $d_A F_A=0.

A connection $A$ satisfying $d_A(*F_A)=0$ is called a Yang–Mills connection.

## Examples
1. **Flat connections.** If $F_A=0$ then $d_A(*F_A)=0$ automatically.
2. **Abelian reduction.** For $G=U(1)$, the equation becomes $d(*F)=0$, the source-free Maxwell equation for the curvature 2-form $F$.
3. **Instantons in dimension 4.** On a 4-manifold, any connection with self-dual or anti-self-dual curvature satisfies the Yang–Mills equation because $*F_A=\pm F_A$ and the Bianchi identity gives $d_A(*F_A)=\pm d_AF_A=0$.
