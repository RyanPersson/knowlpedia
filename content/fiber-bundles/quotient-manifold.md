---
title: "Quotient manifold (for a free proper action)"
description: "The smooth manifold structure on an orbit space arising from a free and proper Lie group action."
---

Let {{< knowl id="lie-group" text="Lie group" >}} $G$ act smoothly on a {{< knowl id="smooth-manifold" text="smooth manifold" >}} $M$.

## Theorem (quotient manifold theorem)
Assume the action is a {{< knowl id="principal-action" text="principal action" >}} (equivalently, smooth, free, and proper). Then:

1. The orbit space $M/G$ admits a unique smooth manifold structure such that the quotient map
   \[
   \pi:M\to M/G
   \]
   is a {{< knowl id="smooth-map" text="smooth map" >}} and a submersion.
2. The fibers of $\pi$ are the orbits, and $\dim(M/G)=\dim(M)-\dim(G)$.
3. With this structure, $\pi:M\to M/G$ is a {{< knowl id="principal-g-bundle" text="principal G-bundle" >}} whose right action is the given action (up to the usual left/right convention).

In particular, local differential geometry on $M/G$ can be studied via $G$-invariant data upstairs on $M$.

## Examples
1. **Hopf fibration.** The free proper $S^1$-action on $S^{2n+1}$ by scalar multiplication yields the quotient manifold $S^{2n+1}/S^1 \cong \mathbb{CP}^n$.
2. **Positive scalings.** The action of $\mathbb{R}_{>0}$ on $\mathbb{R}^n\setminus\{0\}$ by $t\cdot x = tx$ is free and proper; the quotient is diffeomorphic to $S^{n-1}$.
3. **Covering space quotient.** The free proper action of $\mathbb{Z}$ on $\mathbb{R}$ by translations gives the quotient manifold $\mathbb{R}/\mathbb{Z}\cong S^1$.
