+++
id = "lie-groups/orbit-space"
title = "Orbit space"
kind = "knowl"
summary = "The quotient of a G-manifold by the equivalence relation of lying in the same orbit."
aliases = ["orbit-space", "Orbit space"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/orbit-space.md"
+++

Let $G$ be a [[fiber-bundles/lie-group|Lie group]] acting smoothly on a manifold $M$ (see [[lie-groups/smooth-action-lie-group|smooth actions]]).

The **orbit space** (or **quotient space**) is the set
$$
M/G=\{G\cdot x \mid x\in M\}
$$
of all [[lie-groups/orbit-lie-group|orbits]], equipped with the quotient topology for the canonical projection
$$
\pi:M\to M/G,\quad \pi(x)=G\cdot x.
$$

## Smooth structure in the free and proper case
In general, $M/G$ need not be a manifold. A standard sufficient condition is:
- If the action is [[lie-groups/free-action-lie|free]] and [[lie-groups/proper-action-lie|proper]], then $M/G$ carries a unique smooth manifold structure such that $\pi$ is a smooth submersion.

In this situation, each orbit is embedded and diffeomorphic to $G$, and $\pi$ exhibits $M$ as a principal homogeneous object for $G$ along the fibers (compare [[lie-groups/principal-homogeneous-space|principal homogeneous spaces]]).

## Basic examples
- If the action is [[lie-groups/transitive-action-lie|transitive]], then $M/G$ is a single point.
- If $M=G$ acts on itself by left translation, then all orbits are all of $G$ and again $M/G$ is a point; if $G$ acts by conjugation, orbit spaces encode conjugacy classes and are typically singular.
