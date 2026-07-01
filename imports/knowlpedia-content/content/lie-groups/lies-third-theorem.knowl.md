+++
id = "lie-groups/lies-third-theorem"
title = "Lie’s third theorem"
kind = "knowl"
summary = "Every finite-dimensional Lie algebra is the Lie algebra of a connected, simply connected Lie group."
aliases = ["lies-third-theorem", "Lie’s third theorem"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/lies-third-theorem.md"
+++

Let $\mathfrak g$ be a finite-dimensional [[lie-groups/lie-algebra|Lie algebra]] over $\Bbb R$ (or $\Bbb C$).

## Theorem (existence and uniqueness up to simply connected cover)
There exists a connected, [[lie-groups/simply-connected-lie-group|simply connected Lie group]] $G$ such that
$$
\operatorname{Lie}(G)\cong \mathfrak g
$$
as Lie algebras (via a [[lie-groups/lie-algebra-isomorphism|Lie algebra isomorphism]]).

Moreover, if $G_1$ and $G_2$ are connected simply connected Lie groups with Lie algebras isomorphic to $\mathfrak g$, then $G_1$ and $G_2$ are isomorphic as [[fiber-bundles/lie-group|Lie groups]]. In other words, the simply connected integration of $\mathfrak g$ is unique up to Lie group isomorphism.

## Context
Combined with the fact that every connected Lie group has a [[lie-groups/universal-covering-group|universal covering group]] which is again a Lie group (see [[lie-groups/universal-covering-group-existence|existence of universal covering groups]]), Lie’s third theorem explains why Lie algebras control the local—and, up to discrete central quotients, the global—structure of connected Lie groups (compare [[lie-groups/simply-connected-determined-by-algebra|simply connected groups are determined by their Lie algebra]]).

It also underlies the [[lie-groups/lie-correspondence|Lie correspondence]]: Lie subalgebras integrate to connected (immersed) Lie subgroups inside a given Lie group.
