+++
id = "lie-groups/weyls-theorem-complete-reducibility"
title = "Weyl’s theorem on complete reducibility"
kind = "knowl"
summary = "Finite-dimensional representations of semisimple Lie algebras (and compact Lie groups) split as direct sums of irreducibles."
aliases = ["weyls-theorem-complete-reducibility", "Weyl’s theorem on complete reducibility"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/weyls-theorem-complete-reducibility.md"
+++

### Theorem (Weyl complete reducibility)
Let $\mathfrak g$ be a finite-dimensional semisimple Lie algebra over a field of characteristic $0$ (in particular over $\mathbb C$). Then every finite-dimensional representation of $\mathfrak g$ is [[lie-groups/completely-reducible-representation-lie|completely reducible]]: if $W\subseteq V$ is a [[lie-groups/subrepresentation-lie-algebra|subrepresentation]], there exists a $\mathfrak g$-invariant subspace $W'\subseteq V$ such that
$$
V = W \oplus W'.
$$
Equivalently, every representation is a direct sum of [[lie-groups/irreducible-representation-lie-algebra|irreducible representations]].

### Compact Lie group analogue
If $G$ is a [[lie-groups/compact-lie-group|compact Lie group]], then every finite-dimensional continuous representation of $G$ on a real or complex vector space admits a $G$-invariant inner product (obtained by averaging), hence is completely reducible. This is a key input to results like the [[lie-groups/peter-weyl-theorem|Peter–Weyl theorem]].

### Context and consequences
Complete reducibility is the representation-theoretic backbone of highest-weight theory: it guarantees semisimplicity of the $\mathfrak h$-action and enables the [[lie-groups/weight-space|weight space decomposition]], which in turn supports the classification of irreducibles by [[lie-groups/highest-weight|highest weights]]. It also interacts with structural criteria for semisimplicity, such as nondegeneracy of the [[lie-groups/killing-form|Killing form]] (compare [[lie-groups/tfae-semisimplicity-lie-algebra|equivalent characterizations of semisimplicity]]).
