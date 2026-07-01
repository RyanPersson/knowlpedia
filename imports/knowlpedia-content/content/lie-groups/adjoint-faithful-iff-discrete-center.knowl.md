+++
id = "lie-groups/adjoint-faithful-iff-discrete-center"
title = "Adjoint representation: discrete kernel iff discrete center"
kind = "knowl"
summary = "For connected Lie groups, ker(Ad)=Z(G), so Ad has discrete kernel exactly when the center is discrete."
aliases = ["adjoint-faithful-iff-discrete-center", "Adjoint representation: discrete kernel iff discrete center"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/adjoint-faithful-iff-discrete-center.md"
+++

Let $G$ be a [[lie-groups/connected-lie-group|connected Lie group]] with Lie algebra $\mathfrak{g}$, and let [[lie-groups/adjoint-action-of-a-lie-group|$\mathrm{Ad}$]] denote the adjoint representation $\mathrm{Ad}:G\to \mathrm{Aut}(\mathfrak{g})$.

**Theorem.** If $G$ is connected, then
$$
\ker(\mathrm{Ad}) = Z(G),
$$

where $Z(G)$ is the [[lie-groups/center-of-a-lie-group|center of $G$]]. In particular, $\mathrm{Ad}$ has **discrete kernel** if and only if $Z(G)$ is discrete.

This is often packaged as: the adjoint action is “almost effective” precisely when the center is discrete; compare [[lie-groups/effective-action|effective actions]] (which correspond to trivial kernel).

**Context.** The key input is that $\mathrm{Ad}(g)$ is the differential at the identity of the [[lie-groups/conjugation-action-of-a-lie-group|conjugation action]]; for connected groups, acting trivially on $\mathfrak{g}$ forces $g$ to commute with a neighborhood of the identity, hence with all of $G$. A standard formulation appears as [[lie-groups/kernel-of-ad-is-center-lemma|the kernel-of-Ad equals the center lemma]].
