+++
id = "topology/topological-group"
title = "Topological group"
kind = "knowl"
summary = "A group with a topology making multiplication and inversion continuous."
aliases = ["topological-group", "Topological group"]
domains = ["topology"]
legacy_source_path = "topology/topological-group.md"
+++

A **topological group** is a [[algebra-groups/group|group]] \(G\) equipped with a [[topology/topological-space|topology]] such that:

1. The multiplication map \(\mu: G \times G \to G\), \((g, h) \mapsto gh\), is [[topology/continuous-map|continuous]].
2. The inversion map \(\iota: G \to G\), \(g \mapsto g^{-1}\), is continuous.

Equivalently, the single map \((g, h) \mapsto gh^{-1}\) is continuous.

## Properties
- Translation maps \(L_g: h \mapsto gh\) and \(R_g: h \mapsto hg\) are [[topology/homeomorphism|homeomorphisms]].
- The topology is determined by neighborhoods of the identity.
- Connected components form a [[algebra-groups/normal-subgroup|normal subgroup]].

## Examples
- \((\mathbb{R}, +)\) and \((\mathbb{R}^n, +)\) with the Euclidean topology.
- \((\mathbb{R}^*, \cdot)\) (nonzero reals under multiplication).
- \(GL_n(\mathbb{R})\) and \(GL_n(\mathbb{C})\) with the subspace topology.
- [[fiber-bundles/lie-group|Lie groups]] are smooth topological groups.
- Any group with the discrete topology.

## Relation to Lie groups
A Lie group is a topological group that is also a [[fiber-bundles/smooth-manifold|smooth manifold]] with smooth group operations.
