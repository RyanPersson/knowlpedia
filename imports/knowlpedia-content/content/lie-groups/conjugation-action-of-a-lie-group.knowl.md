+++
id = "lie-groups/conjugation-action-of-a-lie-group"
title = "Conjugation action of a Lie group"
kind = "knowl"
summary = "The smooth action of a Lie group on itself by conjugation."
aliases = ["conjugation-action-of-a-lie-group", "Conjugation action of a Lie group"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/conjugation-action-of-a-lie-group.md"
+++

Let $G$ be a [[fiber-bundles/lie-group|Lie group]].

**Definition.** The **conjugation action** is the map
$$
G\times G \to G,\quad (g,h)\mapsto ghg^{-1}.
$$

This is a [[lie-groups/smooth-action-lie-group|smooth action]] of $G$ on the manifold $G$.

**Orbits and stabilizers.**
- The orbit of $h\in G$ is its conjugacy class, an example of an [[lie-groups/orbit-lie-group|orbit]] of a Lie group action.
- The stabilizer of $h$ is its centralizer $C_G(h)=\{g\in G:gh=hg\}$, a closed subgroup; compare [[lie-groups/stabilizer-lie-group|stabilizers]] and the [[lie-groups/closed-subgroup-theorem|closed subgroup theorem]].
- The kernel of the action is the [[lie-groups/center-of-a-lie-group|center]] $Z(G)$.

**Infinitesimal picture.** Differentiating conjugation at the identity yields the [[lie-groups/adjoint-action-of-a-lie-group|adjoint action]] $\mathrm{Ad}:G\to \mathrm{Aut}(\mathfrak{g})$, so conjugation is the global geometric source of the adjoint representation.
