+++
id = "lie-groups/transitive-action-lie"
title = "Transitive Lie group action"
kind = "knowl"
summary = "A smooth action is transitive if it has a single orbit; equivalently for a stabilizer ."
aliases = ["transitive-action-lie", "Transitive Lie group action"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/transitive-action-lie.md"
+++

### Definition
Let $G$ be a Lie group acting smoothly on a manifold $M$ (see [[lie-groups/smooth-action-lie-group|smooth Lie group actions]]). The action is **transitive** if for all $x,y\in M$ there exists $g\in G$ such that
$$
g\cdot x = y.
$$

Equivalently, for some (hence every) $x\in M$, the [[lie-groups/orbit-lie-group|orbit]] $G\cdot x$ equals all of $M$.

### Homogeneous space description
Fix $x_0\in M$ and let $H=G_{x_0}$ be the [[lie-groups/stabilizer-lie-group|stabilizer subgroup]]. Then $H$ is a Lie subgroup (by the [[lie-groups/closed-subgroup-theorem|closed subgroup theorem]]), and the orbit map induces a smooth surjection
$$
G/H \to M,\quad gH\mapsto g\cdot x_0.
$$

For transitive actions this map is a diffeomorphism under standard hypotheses, so $M$ is a [[lie-groups/homogeneous-space|homogeneous space]] (compare [[lie-groups/coset-space|coset spaces]]).

### Context
Transitive actions encode “geometries with a large symmetry group.” Many classical manifolds arise as homogeneous spaces, and questions about invariants on $M$ can often be translated into representation-theoretic questions about $H$.
