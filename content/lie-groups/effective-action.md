---
title: "Effective action"
description: "A Lie group action with trivial kernel; equivalently, the only element acting as the identity on the space is ."
---

Let $G$ be a {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}} acting smoothly on a manifold $M$, i.e. a {{< knowl id="smooth-action-lie-group" text="smooth action of a Lie group" >}}.

The **kernel** of the action is
\[
\ker(G\curvearrowright M) := \{g\in G : g\cdot x = x \text{ for all }x\in M\}.
\]
The action is **effective** if its kernel is trivial, i.e. $\ker(G\curvearrowright M)=\{e\}$.

## Basic structure
- The kernel is a closed {{< knowl id="normal-lie-subgroup" text="normal Lie subgroup" >}} of $G$.
- Every action factors through an effective action of the quotient group:
  the induced action of {{< knowl id="quotient-lie-group" text="$G/\ker$" >}} on $M$ is effective and has the same orbits (compare {{< knowl id="orbit-lie-group" text="orbits" >}}) and stabilizers up to the quotient (compare {{< knowl id="stabilizer-lie-group" text="stabilizer" >}}).

## Motivation
Effectiveness is the correct “no redundancy” condition: if an action is not effective, one can replace $G$ by the smaller group $G/\ker$ without changing the geometry of the orbit decomposition or isotropy behavior.
