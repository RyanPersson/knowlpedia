---
title: "Bi-invariant metric"
description: "A Riemannian metric on a Lie group invariant under left and right translations."
---

Let $G$ be a {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}} with {{< knowl id="left-translation" text="left translations" >}} $L_g$ and {{< knowl id="right-translation" text="right translations" >}} $R_g$.

**Definition.** A Riemannian metric $\langle\cdot,\cdot\rangle$ on $G$ is **bi-invariant** if
$$
L_g^*\langle\cdot,\cdot\rangle = \langle\cdot,\cdot\rangle
\quad\text{and}\quad
R_g^*\langle\cdot,\cdot\rangle = \langle\cdot,\cdot\rangle
\qquad \text{for all } g\in G.
$$

**Lie algebra formulation.** A left-invariant metric is determined by an inner product $\langle\cdot,\cdot\rangle_e$ on $\mathfrak{g}=\mathrm{Lie}(G)$. For connected $G$, this metric is bi-invariant if and only if $\langle\cdot,\cdot\rangle_e$ is invariant under the {{< knowl id="adjoint-action-of-a-lie-group" text="adjoint representation" >}}:
$$
\langle \mathrm{Ad}_g X,\mathrm{Ad}_g Y\rangle_e = \langle X,Y\rangle_e
\quad\text{for all } g\in G,\; X,Y\in \mathfrak{g}.
$$

**Consequences.** For a bi-invariant metric, geodesics through the identity are precisely {{< knowl id="one-parameter-subgroup" text="one-parameter subgroups" >}} $t\mapsto \exp(tX)$ (compare {{< knowl id="exponential-one-parameter-subgroup-lemma" text="the exponential/one-parameter subgroup lemma" >}}). Existence is special: every {{< knowl id="compact-lie-group" text="compact Lie group" >}} admits one (see {{< knowl id="compact-lie-group-bi-invariant-metric" text="bi-invariant metrics on compact Lie groups" >}}), while many non-compact groups do not.

**Example of a canonical source.** On a semisimple Lie algebra, the {{< knowl id="killing-form" text="Killing form" >}} provides an $\mathrm{Ad}$-invariant bilinear form; for compact semisimple groups, its negative is positive definite and yields a bi-invariant metric.
