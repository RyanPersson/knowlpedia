+++
id = "lie-groups/bi-invariant-metric"
title = "Bi-invariant metric"
kind = "knowl"
summary = "A Riemannian metric on a Lie group invariant under left and right translations."
aliases = ["bi-invariant-metric", "Bi-invariant metric"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/bi-invariant-metric.md"
+++

Let $G$ be a [[fiber-bundles/lie-group|Lie group]] with [[lie-groups/left-translation|left translations]] $L_g$ and [[lie-groups/right-translation|right translations]] $R_g$.

**Definition.** A Riemannian metric $\langle\cdot,\cdot\rangle$ on $G$ is **bi-invariant** if
$$
L_g^*\langle\cdot,\cdot\rangle = \langle\cdot,\cdot\rangle
\quad\text{and}\quad
R_g^*\langle\cdot,\cdot\rangle = \langle\cdot,\cdot\rangle
\qquad \text{for all } g\in G.
$$

**Lie algebra formulation.** A left-invariant metric is determined by an inner product $\langle\cdot,\cdot\rangle_e$ on $\mathfrak{g}=\mathrm{Lie}(G)$. For connected $G$, this metric is bi-invariant if and only if $\langle\cdot,\cdot\rangle_e$ is invariant under the [[lie-groups/adjoint-action-of-a-lie-group|adjoint representation]]:
$$
\langle \mathrm{Ad}_g X,\mathrm{Ad}_g Y\rangle_e = \langle X,Y\rangle_e
\quad\text{for all } g\in G,\; X,Y\in \mathfrak{g}.
$$

**Consequences.** For a bi-invariant metric, geodesics through the identity are precisely [[lie-groups/one-parameter-subgroup|one-parameter subgroups]] $t\mapsto \exp(tX)$ (compare [[lie-groups/exponential-one-parameter-subgroup-lemma|the exponential/one-parameter subgroup lemma]]). Existence is special: every [[lie-groups/compact-lie-group|compact Lie group]] admits one (see [[lie-groups/compact-lie-group-bi-invariant-metric|bi-invariant metrics on compact Lie groups]]), while many non-compact groups do not.

**Example of a canonical source.** On a semisimple Lie algebra, the [[lie-groups/killing-form|Killing form]] provides an $\mathrm{Ad}$-invariant bilinear form; for compact semisimple groups, its negative is positive definite and yields a bi-invariant metric.
