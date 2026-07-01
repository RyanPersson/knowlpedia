+++
id = "lie-groups/free-action-lie"
title = "Free action"
kind = "knowl"
summary = "A Lie group action is free if all stabilizers are trivial."
aliases = ["free-action-lie", "Free action"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/free-action-lie.md"
+++

Let $G$ be a [[fiber-bundles/lie-group|Lie group]] acting smoothly on a manifold $M$ via a [[lie-groups/smooth-action-lie-group|smooth action]] $G\times M\to M$, $(g,p)\mapsto g\cdot p$.

**Definition (Free action).**
The action is **free** if for every $p\in M$, the [[lie-groups/stabilizer-lie-group|stabilizer]]
\[
G_p=\{g\in G: g\cdot p=p\}
\]
is trivial, i.e. $G_p=\{e\}$.

Equivalently, for each $p\in M$, the orbit map $G\to M$, $g\mapsto g\cdot p$ is injective, so each [[lie-groups/orbit-lie-group|orbit]] is diffeomorphic to $G$ as a set. (For finer geometric conclusions, freeness is often paired with [[lie-groups/proper-action-lie|properness]].)

**Motivation.**
Free actions are the infinitesimal starting point for principal bundles: when an action is free and proper, the orbit space $M/G$ is a manifold and $M\to M/G$ becomes a principal $G$-bundle; in the special case when the action is also transitive, $M$ is a [[lie-groups/principal-homogeneous-space|principal homogeneous space]].
