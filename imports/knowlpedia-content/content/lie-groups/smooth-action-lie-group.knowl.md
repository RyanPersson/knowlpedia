+++
id = "lie-groups/smooth-action-lie-group"
title = "Smooth action of a Lie group"
kind = "knowl"
summary = "A Lie group action on a manifold given by a smooth map G×M→M satisfying the action axioms."
aliases = ["smooth-action-lie-group", "Smooth action of a Lie group"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/smooth-action-lie-group.md"
+++

Let $G$ be a Lie group and $M$ a smooth manifold. A **smooth (left) action** of $G$ on $M$ is a smooth map
\[
a: G\times M \longrightarrow M,\qquad (g,m)\mapsto g\cdot m,
\]
such that:

1. $e\cdot m = m$ for all $m\in M$ (where $e$ is the identity in $G$), and
2. $(g_1g_2)\cdot m = g_1\cdot(g_2\cdot m)$ for all $g_1,g_2\in G$ and $m\in M$.

Associated to any smooth action are the basic orbit-stabilizer constructions: the orbit $G\cdot m$ (see [[lie-groups/orbit-lie-group|orbit]]) and the stabilizer subgroup $G_m$ (see [[lie-groups/stabilizer-lie-group|stabilizer]]). If the action is transitive, $M$ becomes a [[lie-groups/homogeneous-space|homogeneous space]]; if it is free, it resembles a [[lie-groups/principal-homogeneous-space|principal homogeneous space]] (compare [[lie-groups/transitive-action-lie|transitive action]] and [[lie-groups/free-action-lie|free action]]).

Differentiating at the identity produces an infinitesimal action: each $X\in\mathfrak g=\mathrm{Lie}(G)$ defines a vector field $X_M$ on $M$ by
\[
(X_M)_m = \left.\frac{d}{dt}\right|_{t=0}\exp(tX)\cdot m,
\]
linking smooth actions to [[lie-groups/one-parameter-subgroup|one-parameter subgroups]] and the [[lie-groups/exponential-map-lie-group|exponential map]]. The kernel of the action homomorphism $G\to \mathrm{Diff}(M)$ measures whether the action is [[lie-groups/effective-action|effective]].
