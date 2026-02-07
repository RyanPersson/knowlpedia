---
title: "Simply connected Lie group"
description: "A Lie group whose underlying manifold is simply connected (connected with trivial fundamental group)."
---

A Lie group $G$ is **simply connected** if, as a topological space (equivalently a manifold), it is connected and has trivial fundamental group:
\[
\pi_1(G)=0.
\]
In particular, $G$ is a {{< knowl id="connected-lie-group" text="connected Lie group" >}}.

Simply connected Lie groups play a special role because they are the “global objects” most faithfully represented by Lie algebra data. Concretely:

- Every connected Lie group has a {{< knowl id="universal-covering-group" text="universal covering group" >}} $\widetilde G\to G$ whose total space $\widetilde G$ is a simply connected Lie group (see {{< knowl id="universal-covering-group-existence" text="existence of universal covering groups" >}} and {{< knowl id="covering-lie-group" text="covering Lie group" >}}).
- The Lie algebra does not see discrete topology: $G$ and $\widetilde G$ have the same Lie algebra (see {{< knowl id="lie-algebra-of-a-lie-group" text="Lie algebra of a Lie group" >}}), but different global topology.

A key payoff is the uniqueness principle {{< knowl id="simply-connected-determined-by-algebra" text="simply connected determined by Lie algebra" >}}: connected simply connected Lie groups are determined up to isomorphism by their Lie algebras, and Lie algebra homomorphisms integrate uniquely to group homomorphisms in the simply connected setting.
