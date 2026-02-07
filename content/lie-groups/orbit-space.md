---
title: "Orbit space"
description: "The quotient of a G-manifold by the equivalence relation of lying in the same orbit."
---

Let $G$ be a {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}} acting smoothly on a manifold $M$ (see {{< knowl id="smooth-action-lie-group" text="smooth actions" >}}).

The **orbit space** (or **quotient space**) is the set
$$
M/G=\{G\cdot x \mid x\in M\}
$$
of all {{< knowl id="orbit-lie-group" text="orbits" >}}, equipped with the quotient topology for the canonical projection
$$
\pi:M\to M/G,\quad \pi(x)=G\cdot x.
$$

## Smooth structure in the free and proper case
In general, $M/G$ need not be a manifold. A standard sufficient condition is:
- If the action is {{< knowl id="free-action-lie" text="free" >}} and {{< knowl id="proper-action-lie" text="proper" >}}, then $M/G$ carries a unique smooth manifold structure such that $\pi$ is a smooth submersion.

In this situation, each orbit is embedded and diffeomorphic to $G$, and $\pi$ exhibits $M$ as a principal homogeneous object for $G$ along the fibers (compare {{< knowl id="principal-homogeneous-space" text="principal homogeneous spaces" >}}).

## Basic examples
- If the action is {{< knowl id="transitive-action-lie" text="transitive" >}}, then $M/G$ is a single point.
- If $M=G$ acts on itself by left translation, then all orbits are all of $G$ and again $M/G$ is a point; if $G$ acts by conjugation, orbit spaces encode conjugacy classes and are typically singular.
