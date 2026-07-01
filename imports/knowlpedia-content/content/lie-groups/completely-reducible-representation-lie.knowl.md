+++
id = "lie-groups/completely-reducible-representation-lie"
title = "Completely reducible representation"
kind = "knowl"
summary = "A representation that splits as a direct sum of irreducible subrepresentations."
aliases = ["completely-reducible-representation-lie", "Completely reducible representation"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/completely-reducible-representation-lie.md"
+++

Let $\rho$ be a finite-dimensional representation, either of a [[lie-groups/lie-algebra|Lie algebra]] $\mathfrak{g}$ (a [[lie-groups/representation-of-a-lie-algebra|Lie algebra representation]]) or of a [[fiber-bundles/lie-group|Lie group]] $G$ (a [[lie-groups/representation-of-a-lie-group|Lie group representation]]).

**Definition.** $\rho$ is **completely reducible** if for every invariant subspace $W\subset V$ (a [[lie-groups/subrepresentation-lie-algebra|subrepresentation]]), there exists an invariant complement $W'\subset V$ such that
$$
V = W \oplus W'
$$
as representations.

Equivalently, $V$ can be written as a finite direct sum of [[lie-groups/irreducible-representation-lie-algebra|irreducible]] subrepresentations.

**Context and key theorems.**
- If $\mathfrak{g}$ is [[lie-groups/semisimple-lie-algebra|semisimple]] over $\mathbb{C}$ (or $\mathbb{R}$ with suitable hypotheses), then every finite-dimensional representation is completely reducible; this is [[lie-groups/weyls-theorem-complete-reducibility|Weyl’s complete reducibility theorem]].
- If $G$ is [[lie-groups/compact-lie-group|compact]], then every finite-dimensional continuous representation is completely reducible, via averaging an inner product (a Lie-group analogue of Maschke’s theorem), and more globally by [[lie-groups/peter-weyl-theorem|Peter–Weyl]].

Complete reducibility is the structural reason highest-weight classifications work for compact and semisimple settings.
