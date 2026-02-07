---
title: "Conjugation action of a Lie group"
description: "The smooth action of a Lie group on itself by conjugation."
---

Let $G$ be a {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}}.

**Definition.** The **conjugation action** is the map
$$
G\times G \to G,\quad (g,h)\mapsto ghg^{-1}.
$$

This is a {{< knowl id="smooth-action-lie-group" text="smooth action" >}} of $G$ on the manifold $G$.

**Orbits and stabilizers.**
- The orbit of $h\in G$ is its conjugacy class, an example of an {{< knowl id="orbit-lie-group" text="orbit" >}} of a Lie group action.
- The stabilizer of $h$ is its centralizer $C_G(h)=\{g\in G:gh=hg\}$, a closed subgroup; compare {{< knowl id="stabilizer-lie-group" text="stabilizers" >}} and the {{< knowl id="closed-subgroup-theorem" text="closed subgroup theorem" >}}.
- The kernel of the action is the {{< knowl id="center-of-a-lie-group" text="center" >}} $Z(G)$.

**Infinitesimal picture.** Differentiating conjugation at the identity yields the {{< knowl id="adjoint-action-of-a-lie-group" text="adjoint action" >}} $\mathrm{Ad}:G\to \mathrm{Aut}(\mathfrak{g})$, so conjugation is the global geometric source of the adjoint representation.
