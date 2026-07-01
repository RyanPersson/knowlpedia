+++
id = "fiber-bundles/trivial-principal-bundle-criterion-global-section-principal-bundle-is-trivial"
title = "Theorem: Global section implies a principal bundle is trivial"
kind = "knowl"
summary = "A principal bundle admitting a smooth global section is isomorphic to the product bundle."
aliases = ["trivial-principal-bundle-criterion-global-section-principal-bundle-is-trivial", "Theorem: Global section implies a principal bundle is trivial"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/trivial-principal-bundle-criterion-global-section-principal-bundle-is-trivial.md"
+++

Let $\pi:P\to M$ be a [[fiber-bundles/principal-g-bundle|principal G-bundle]] with structure [[fiber-bundles/lie-group|Lie group]] $G$ over a [[fiber-bundles/smooth-manifold|smooth manifold]] $M$.

## Theorem

If there exists a smooth section $s:M\to P$ (so $\pi\circ s=\mathrm{id}_M$), then $P$ is trivial: the map
\[
\Phi:M\times G \longrightarrow P,\qquad \Phi(x,g):=s(x)\cdot g
\]
is a $G$-equivariant [[fiber-bundles/diffeomorphism|diffeomorphism]] covering $\mathrm{id}_M$. Hence $P\cong M\times G$ as principal $G$-bundles.

## Examples

1. **Product bundle.** For $P=M\times G$, the map $s(x)=(x,e)$ is a global section, and $\Phi$ is the identity.

2. **Nontrivial bundles fail to have sections.** The Hopf fibration $S^3\to S^2$ (a principal $U(1)$-bundle) has no global section; otherwise it would be diffeomorphic to $S^2\times U(1)$.

3. **Triviality over contractible bases.** If $M$ is contractible and a principal bundle admits a section (e.g. produced by additional structure), this theorem upgrades that section to an explicit trivialization by the formula $\Phi(x,g)=s(x)\cdot g$.
