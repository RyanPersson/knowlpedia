---
title: "Structure of connected abelian Lie groups"
description: "Every connected abelian Lie group is isomorphic to R^n × T^m."
---

Let $G$ be a {{< knowl id="connected-lie-group" text="connected Lie group" >}} that is {{< knowl id="abelian-lie-group" text="abelian" >}}, and let $\mathfrak{g}$ be its {{< knowl id="lie-algebra-of-a-lie-group" text="Lie algebra" >}}.

**Theorem (classification).** There exist integers $n,m\ge 0$ such that
$$
G \cong \mathbb{R}^n \times \mathbb{T}^m
\quad\text{as Lie groups},
$$

where $\mathbb{T}^m$ is an $m$-torus (isomorphic to $(S^1)^m$). In particular, $G$ is determined up to isomorphism by the pair $(n,m)$ with $\dim G = n+m$.

**Idea of proof (covering + lattice).**
- Since $G$ is connected and abelian, its universal cover $\widetilde{G}$ is a connected simply connected abelian Lie group. Such a group is isomorphic to the additive group of its Lie algebra, so $\widetilde{G}\cong (\mathfrak{g},+) \cong \mathbb{R}^{n+m}$; compare {{< knowl id="universal-covering-group" text="universal covering groups" >}}.
- The covering map $\widetilde{G}\to G$ has kernel a {{< knowl id="discrete-subgroup" text="discrete subgroup" >}} of $\widetilde{G}$, hence a lattice in $\mathbb{R}^{n+m}$ up to linear change of coordinates.
- Splitting $\mathbb{R}^{n+m}$ into directions along the lattice and transverse directions produces $\mathbb{R}^n\times (\mathbb{R}^m/\mathbb{Z}^m)$.

**Context.** This result explains why the basic connected abelian examples are $\mathbb{R}^n$, circles, and tori; see {{< knowl id="example-u1-circle" text="the circle group" >}} and {{< knowl id="example-torus" text="the torus" >}}. It also matches the infinitesimal picture: $\mathfrak{g}$ is an {{< knowl id="abelian-lie-algebra" text="abelian Lie algebra" >}}, so the {{< knowl id="exponential-map-lie-group" text="exponential map" >}} is a local group isomorphism whose global kernel records the lattice.
