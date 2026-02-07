---
title: "Moment map"
description: "A map from a Hamiltonian Lie group action to the dual Lie algebra encoding infinitesimal symmetries of a symplectic form."
---

Let $G$ be a {{< knowl id="lie-group" text="Lie group" >}} acting smoothly on a manifold $M$, and let $\mathfrak{g}$ be its Lie algebra. Suppose $M$ is equipped with a symplectic form $\omega$ (a closed, nondegenerate 2-form).

For $\xi\in\mathfrak{g}$, write $\xi_M$ for the fundamental vector field on $M$.

## Definition (Moment map)
The action is **Hamiltonian** if there exists a smooth map
\[
\mu\colon M \to \mathfrak{g}^*
\]
such that for every $\xi\in\mathfrak{g}$,
\[
d\langle \mu,\xi\rangle \;=\; \iota_{\xi_M}\omega,
\]
where $d$ is the {{< knowl id="exterior-derivative" text="exterior derivative" >}} and $\iota_{\xi_M}$ denotes contraction by the vector field $\xi_M$.

Such a map $\mu$ is called a **moment map**. Often one additionally requires $G$-equivariance with respect to the coadjoint action (in particular when $G$ is connected), which makes $\mu$ essentially unique up to addition of a central constant.

A useful reformulation is that in {{< knowl id="equivariant-cohomology" text="equivariant cohomology" >}} (Cartan model), the pair $(\omega,\mu)$ combines into an equivariantly closed degree-2 element.

## Examples
1. **Rotation of the plane.** For the $S^1$-action on $\mathbb{R}^2\cong \mathbb{C}$ by rotations and $\omega=dx\wedge dy$, a moment map is $\mu(z)=\tfrac12|z|^2$ (identifying $(\mathfrak{u}(1))^*\cong \mathbb{R}$).
2. **Height on the 2-sphere.** For the standard rotation action of $S^1$ on $S^2$ around the vertical axis with the area form, a moment map is the height function (up to an additive constant).
3. **Cotangent lift.** If $G$ acts on a manifold $Q$, the induced action on $T^*Q$ with its canonical symplectic form is Hamiltonian, with moment map $\mu(q,p)(\xi)=p(\xi_Q(q))$.
