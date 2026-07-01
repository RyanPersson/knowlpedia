+++
id = "lie-groups/connected-abelian-lie-group-structure"
title = "Structure of connected abelian Lie groups"
kind = "knowl"
summary = "Every connected abelian Lie group is isomorphic to R^n × T^m."
aliases = ["connected-abelian-lie-group-structure", "Structure of connected abelian Lie groups"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/connected-abelian-lie-group-structure.md"
+++

Let $G$ be a [[lie-groups/connected-lie-group|connected Lie group]] that is [[lie-groups/abelian-lie-group|abelian]], and let $\mathfrak{g}$ be its [[lie-groups/lie-algebra-of-a-lie-group|Lie algebra]].

**Theorem (classification).** There exist integers $n,m\ge 0$ such that
$$
G \cong \mathbb{R}^n \times \mathbb{T}^m
\quad\text{as Lie groups},
$$

where $\mathbb{T}^m$ is an $m$-torus (isomorphic to $(S^1)^m$). In particular, $G$ is determined up to isomorphism by the pair $(n,m)$ with $\dim G = n+m$.

**Idea of proof (covering + lattice).**
- Since $G$ is connected and abelian, its universal cover $\widetilde{G}$ is a connected simply connected abelian Lie group. Such a group is isomorphic to the additive group of its Lie algebra, so $\widetilde{G}\cong (\mathfrak{g},+) \cong \mathbb{R}^{n+m}$; compare [[lie-groups/universal-covering-group|universal covering groups]].
- The covering map $\widetilde{G}\to G$ has kernel a [[lie-groups/discrete-subgroup|discrete subgroup]] of $\widetilde{G}$, hence a lattice in $\mathbb{R}^{n+m}$ up to linear change of coordinates.
- Splitting $\mathbb{R}^{n+m}$ into directions along the lattice and transverse directions produces $\mathbb{R}^n\times (\mathbb{R}^m/\mathbb{Z}^m)$.

**Context.** This result explains why the basic connected abelian examples are $\mathbb{R}^n$, circles, and tori; see [[lie-groups/example-u1-circle|the circle group]] and [[lie-groups/example-torus|the torus]]. It also matches the infinitesimal picture: $\mathfrak{g}$ is an [[lie-groups/abelian-lie-algebra|abelian Lie algebra]], so the [[lie-groups/exponential-map-lie-group|exponential map]] is a local group isomorphism whose global kernel records the lattice.
