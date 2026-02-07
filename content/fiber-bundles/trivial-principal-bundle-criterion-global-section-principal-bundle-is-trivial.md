---
title: "Theorem: Global section implies a principal bundle is trivial"
description: "A principal bundle admitting a smooth global section is isomorphic to the product bundle."
---

Let $\pi:P\to M$ be a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} with structure {{< knowl id="lie-group" text="Lie group" >}} $G$ over a {{< knowl id="smooth-manifold" text="smooth manifold" >}} $M$.

## Theorem

If there exists a smooth section $s:M\to P$ (so $\pi\circ s=\mathrm{id}_M$), then $P$ is trivial: the map
\[
\Phi:M\times G \longrightarrow P,\qquad \Phi(x,g):=s(x)\cdot g
\]
is a $G$-equivariant {{< knowl id="diffeomorphism" text="diffeomorphism" >}} covering $\mathrm{id}_M$. Hence $P\cong M\times G$ as principal $G$-bundles.

## Examples

1. **Product bundle.** For $P=M\times G$, the map $s(x)=(x,e)$ is a global section, and $\Phi$ is the identity.

2. **Nontrivial bundles fail to have sections.** The Hopf fibration $S^3\to S^2$ (a principal $U(1)$-bundle) has no global section; otherwise it would be diffeomorphic to $S^2\times U(1)$.

3. **Triviality over contractible bases.** If $M$ is contractible and a principal bundle admits a section (e.g. produced by additional structure), this theorem upgrades that section to an explicit trivialization by the formula $\Phi(x,g)=s(x)\cdot g$.
