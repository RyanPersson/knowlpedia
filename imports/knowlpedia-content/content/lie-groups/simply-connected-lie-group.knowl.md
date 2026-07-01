+++
id = "lie-groups/simply-connected-lie-group"
title = "Simply connected Lie group"
kind = "knowl"
summary = "A Lie group whose underlying manifold is simply connected (connected with trivial fundamental group)."
aliases = ["simply-connected-lie-group", "Simply connected Lie group"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/simply-connected-lie-group.md"
+++

A Lie group $G$ is **simply connected** if, as a topological space (equivalently a manifold), it is connected and has trivial fundamental group:
\[
\pi_1(G)=0.
\]
In particular, $G$ is a [[lie-groups/connected-lie-group|connected Lie group]].

Simply connected Lie groups play a special role because they are the “global objects” most faithfully represented by Lie algebra data. Concretely:

- Every connected Lie group has a [[lie-groups/universal-covering-group|universal covering group]] $\widetilde G\to G$ whose total space $\widetilde G$ is a simply connected Lie group (see [[lie-groups/universal-covering-group-existence|existence of universal covering groups]] and [[lie-groups/covering-lie-group|covering Lie group]]).
- The Lie algebra does not see discrete topology: $G$ and $\widetilde G$ have the same Lie algebra (see [[lie-groups/lie-algebra-of-a-lie-group|Lie algebra of a Lie group]]), but different global topology.

A key payoff is the uniqueness principle [[lie-groups/simply-connected-determined-by-algebra|simply connected determined by Lie algebra]]: connected simply connected Lie groups are determined up to isomorphism by their Lie algebras, and Lie algebra homomorphisms integrate uniquely to group homomorphisms in the simply connected setting.
