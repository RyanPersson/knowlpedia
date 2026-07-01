+++
id = "lie-groups/effective-action"
title = "Effective action"
kind = "knowl"
summary = "A Lie group action with trivial kernel; equivalently, the only element acting as the identity on the space is ."
aliases = ["effective-action", "Effective action"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/effective-action.md"
+++

Let $G$ be a [[fiber-bundles/lie-group|Lie group]] acting smoothly on a manifold $M$, i.e. a [[lie-groups/smooth-action-lie-group|smooth action of a Lie group]].

The **kernel** of the action is
\[
\ker(G\curvearrowright M) := \{g\in G : g\cdot x = x \text{ for all }x\in M\}.
\]
The action is **effective** if its kernel is trivial, i.e. $\ker(G\curvearrowright M)=\{e\}$.

## Basic structure
- The kernel is a closed [[lie-groups/normal-lie-subgroup|normal Lie subgroup]] of $G$.
- Every action factors through an effective action of the quotient group:
  the induced action of [[lie-groups/quotient-lie-group|$G/\ker$]] on $M$ is effective and has the same orbits (compare [[lie-groups/orbit-lie-group|orbits]]) and stabilizers up to the quotient (compare [[lie-groups/stabilizer-lie-group|stabilizer]]).

## Motivation
Effectiveness is the correct “no redundancy” condition: if an action is not effective, one can replace $G$ by the smaller group $G/\ker$ without changing the geometry of the orbit decomposition or isotropy behavior.
