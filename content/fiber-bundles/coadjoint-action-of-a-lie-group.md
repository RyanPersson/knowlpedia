---
title: "Coadjoint action of a Lie group"
description: "The induced action of a Lie group on the dual of its Lie algebra obtained by dualizing the adjoint action."
---

Let $G$ be a Lie group with Lie algebra $\mathfrak{g}$. The {{< knowl id="adjoint-action-of-a-lie-group" text="adjoint action" section="lie-groups">}} assigns to each $g\in G$ an automorphism $\mathrm{Ad}_g:\mathfrak{g}\to\mathfrak{g}$. The **coadjoint action** is the action of $G$ on the dual vector space $\mathfrak{g}^*$ (canonically analogous to a fiber of a {{< knowl id="cotangent-bundle" text="cotangent bundle" >}}) defined by
\[
\mathrm{Ad}^*_g:\mathfrak{g}^*\to\mathfrak{g}^*,
\qquad
\mathrm{Ad}^*_g(\lambda) := \lambda\circ \mathrm{Ad}_{g^{-1}}.
\]
Equivalently, $\mathrm{Ad}^*_g$ is characterized by the pairing identity
\[
\langle \mathrm{Ad}^*_g\lambda,\, X\rangle = \langle \lambda,\, \mathrm{Ad}_{g^{-1}}X\rangle \quad (\lambda\in\mathfrak{g}^*,\, X\in\mathfrak{g}).
\]
The assignment $g\mapsto \mathrm{Ad}^*_g$ is a smooth group homomorphism $G\to \mathrm{GL}(\mathfrak{g}^*)$.

## Examples
1. **Abelian groups.** If $G$ is abelian, then $\mathrm{Ad}$ is trivial, hence $\mathrm{Ad}^*$ is also trivial: $\mathrm{Ad}^*_g=\mathrm{id}$ for all $g$.
2. **Compact rotations.** For $G=\mathrm{SO}(3)$, using the standard inner product to identify $\mathfrak{so}(3)\cong\mathfrak{so}(3)^*\cong\mathbb{R}^3$, the coadjoint action corresponds to the usual rotation action on $\mathbb{R}^3$.
3. **Matrix groups with trace pairing.** For $G=\mathrm{GL}(n,\mathbb{R})$, identifying $\mathfrak{gl}(n,\mathbb{R})^*$ with matrices via the trace pairing $\langle A,B\rangle=\mathrm{tr}(A^\top B)$, the coadjoint action corresponds (up to this identification) to a conjugation-type action.
