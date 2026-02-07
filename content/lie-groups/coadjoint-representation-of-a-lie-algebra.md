---
title: "Coadjoint representation of a Lie algebra"
description: "The dual of the adjoint representation, acting on the dual space g*."
---

Let $\mathfrak{g}$ be a {{< knowl id="lie-algebra" text="Lie algebra" >}} and let $\mathfrak{g}^*$ be its dual vector space.

**Definition.** The **coadjoint representation** is the linear map
$$
\mathrm{ad}^*:\mathfrak{g}\to \mathrm{End}(\mathfrak{g}^*)
$$

defined by dualizing the {{< knowl id="adjoint-representation-of-a-lie-algebra" text="adjoint representation" >}} $\mathrm{ad}:\mathfrak{g}\to \mathrm{End}(\mathfrak{g})$:
for $X\in \mathfrak{g}$ and $\ell\in \mathfrak{g}^*$,
$$
\mathrm{ad}^*_X(\ell) = -\,\ell\circ \mathrm{ad}_X.
$$

Equivalently, using the natural pairing $\langle\ell,Y\rangle=\ell(Y)$,
$$
\langle \mathrm{ad}^*_X\ell,\, Y\rangle = -\langle \ell,\,[X,Y]\rangle \quad \text{for all } Y\in \mathfrak{g}.
$$

**Key point.** The minus sign ensures $\mathrm{ad}^*$ is a {{< knowl id="representation-of-a-lie-algebra" text="Lie algebra representation" >}}, i.e. $[\mathrm{ad}^*_X,\mathrm{ad}^*_Y]=\mathrm{ad}^*_{[X,Y]}$.

**Context.** Coadjoint orbits in $\mathfrak{g}^*$ (via the integrated {{< knowl id="coadjoint-action-of-a-lie-group" section="fiber-bundles" text="coadjoint action of a Lie group" >}}) carry canonical symplectic structures and play a central role in geometric representation theory (Kirillov’s orbit method). In the semisimple case, identifying $\mathfrak{g}\cong\mathfrak{g}^*$ via the {{< knowl id="killing-form" text="Killing form" >}} relates coadjoint and adjoint pictures.
