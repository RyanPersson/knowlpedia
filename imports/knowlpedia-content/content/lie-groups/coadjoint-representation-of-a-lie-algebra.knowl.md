+++
id = "lie-groups/coadjoint-representation-of-a-lie-algebra"
title = "Coadjoint representation of a Lie algebra"
kind = "knowl"
summary = "The dual of the adjoint representation, acting on the dual space g*."
aliases = ["coadjoint-representation-of-a-lie-algebra", "Coadjoint representation of a Lie algebra"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/coadjoint-representation-of-a-lie-algebra.md"
+++

Let $\mathfrak{g}$ be a [[lie-groups/lie-algebra|Lie algebra]] and let $\mathfrak{g}^*$ be its dual vector space.

**Definition.** The **coadjoint representation** is the linear map
$$
\mathrm{ad}^*:\mathfrak{g}\to \mathrm{End}(\mathfrak{g}^*)
$$

defined by dualizing the [[lie-groups/adjoint-representation-of-a-lie-algebra|adjoint representation]] $\mathrm{ad}:\mathfrak{g}\to \mathrm{End}(\mathfrak{g})$:
for $X\in \mathfrak{g}$ and $\ell\in \mathfrak{g}^*$,
$$
\mathrm{ad}^*_X(\ell) = -\,\ell\circ \mathrm{ad}_X.
$$

Equivalently, using the natural pairing $\langle\ell,Y\rangle=\ell(Y)$,
$$
\langle \mathrm{ad}^*_X\ell,\, Y\rangle = -\langle \ell,\,[X,Y]\rangle \quad \text{for all } Y\in \mathfrak{g}.
$$

**Key point.** The minus sign ensures $\mathrm{ad}^*$ is a [[lie-groups/representation-of-a-lie-algebra|Lie algebra representation]], i.e. $[\mathrm{ad}^*_X,\mathrm{ad}^*_Y]=\mathrm{ad}^*_{[X,Y]}$.

**Context.** Coadjoint orbits in $\mathfrak{g}^*$ (via the integrated [[fiber-bundles/coadjoint-action-of-a-lie-group|coadjoint action of a Lie group]]) carry canonical symplectic structures and play a central role in geometric representation theory (Kirillov’s orbit method). In the semisimple case, identifying $\mathfrak{g}\cong\mathfrak{g}^*$ via the [[lie-groups/killing-form|Killing form]] relates coadjoint and adjoint pictures.
