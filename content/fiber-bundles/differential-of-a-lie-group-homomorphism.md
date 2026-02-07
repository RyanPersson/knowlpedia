---
title: "Differential of a Lie group homomorphism"
description: "The induced Lie algebra homomorphism obtained by differentiating a Lie group homomorphism at the identity."
---

Let $\Phi:G\to H$ be a homomorphism of Lie groups. Since $\Phi$ is a smooth map, it has a {{< knowl id="differential-of-a-smooth-map" text="differential" >}} at each point; in particular, at the identity element $e_G\in G$ one gets a linear map
\[
\mathrm{d}\Phi_{e_G}:T_{e_G}G\longrightarrow T_{e_H}H.
\]
Using the identification of these tangent spaces with the {{< knowl id="lie-algebra" text="Lie algebras" section="lie-groups">}} $\mathfrak{g}$ and $\mathfrak{h}$, the map
\[
\phi := \mathrm{d}\Phi_{e_G}:\mathfrak{g}\to\mathfrak{h}
\]
is called the **differential of the Lie group homomorphism**.

A fundamental property is that $\phi$ respects brackets:
\[
\phi([X,Y])=[\phi(X),\phi(Y)] \quad \text{for all } X,Y\in\mathfrak{g},
\]
so $\phi$ is a Lie algebra homomorphism (the bracket on each side is the one induced from the Lie group structure). This construction is functorial: if $\Psi:H\to K$ is another Lie group homomorphism, then $\mathrm{d}(\Psi\circ\Phi)_{e_G}=\mathrm{d}\Psi_{e_H}\circ \mathrm{d}\Phi_{e_G}$.

## Examples
1. **Inclusion of a Lie subgroup.** The inclusion $\iota:\mathrm{SO}(n)\hookrightarrow \mathrm{GL}(n,\mathbb{R})$ differentiates to the inclusion $\mathfrak{so}(n)\hookrightarrow \mathfrak{gl}(n,\mathbb{R})$.
2. **Determinant.** The map $\det:\mathrm{GL}(n,\mathbb{R})\to \mathbb{R}^\times$ is a Lie group homomorphism. Identifying $\mathrm{Lie}(\mathbb{R}^\times)\cong\mathbb{R}$, its differential at the identity sends a matrix $A$ to $\mathrm{tr}(A)$.
3. **Adjoint action.** The {{< knowl id="adjoint-action-of-a-lie-group" text="adjoint action" section="lie-groups">}} $\mathrm{Ad}:G\to \mathrm{GL}(\mathfrak{g})$ is a Lie group homomorphism; differentiating it at the identity yields the adjoint Lie algebra representation $\mathrm{ad}:\mathfrak{g}\to \mathrm{End}(\mathfrak{g})$.
