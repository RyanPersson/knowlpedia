---
title: "Topological group"
description: "A group with a topology making multiplication and inversion continuous."
---

A **topological group** is a {{< knowl id="group" section="algebra-groups" text="group" >}} \(G\) equipped with a {{< knowl id="topological-space" text="topology" >}} such that:

1. The multiplication map \(\mu: G \times G \to G\), \((g, h) \mapsto gh\), is {{< knowl id="continuous-map" text="continuous" >}}.
2. The inversion map \(\iota: G \to G\), \(g \mapsto g^{-1}\), is continuous.

Equivalently, the single map \((g, h) \mapsto gh^{-1}\) is continuous.

## Properties
- Translation maps \(L_g: h \mapsto gh\) and \(R_g: h \mapsto hg\) are {{< knowl id="homeomorphism" text="homeomorphisms" >}}.
- The topology is determined by neighborhoods of the identity.
- Connected components form a {{< knowl id="normal-subgroup" section="algebra-groups" text="normal subgroup" >}}.

## Examples
- \((\mathbb{R}, +)\) and \((\mathbb{R}^n, +)\) with the Euclidean topology.
- \((\mathbb{R}^*, \cdot)\) (nonzero reals under multiplication).
- \(GL_n(\mathbb{R})\) and \(GL_n(\mathbb{C})\) with the subspace topology.
- {{< knowl id="lie-group" section="fiber-bundles" text="Lie groups" >}} are smooth topological groups.
- Any group with the discrete topology.

## Relation to Lie groups
A Lie group is a topological group that is also a {{< knowl id="smooth-manifold" section="fiber-bundles" text="smooth manifold" >}} with smooth group operations.
