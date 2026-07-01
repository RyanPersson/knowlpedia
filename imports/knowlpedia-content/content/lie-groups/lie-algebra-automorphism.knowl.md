+++
id = "lie-groups/lie-algebra-automorphism"
title = "Lie algebra automorphism"
kind = "knowl"
summary = "An invertible linear map preserving the Lie bracket."
aliases = ["lie-algebra-automorphism", "Lie algebra automorphism"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/lie-algebra-automorphism.md"
+++

Let $\mathfrak g$ be a [[lie-groups/lie-algebra|Lie algebra]].

**Definition (Automorphism).**
A **Lie algebra automorphism** is a linear isomorphism $\phi:\mathfrak g\to\mathfrak g$ such that
\[
\phi([x,y])=[\phi(x),\phi(y)]\quad\text{for all }x,y\in\mathfrak g.
\]
Equivalently, $\phi$ is an isomorphism in the category of Lie algebras (compare [[lie-groups/lie-algebra-isomorphism|Lie algebra isomorphism]]).

The set $\mathrm{Aut}(\mathfrak g)$ is a group under composition; for many $\mathfrak g$ it carries a natural Lie group structure as a closed subgroup of $\mathrm{GL}(\mathfrak g)$.

**Inner vs outer features.**
The adjoint representation gives canonical automorphisms by exponentiating inner derivations: for $x\in\mathfrak g$, the map $\exp(\mathrm{ad}_x)$ is an automorphism (built from [[lie-groups/inner-derivation|inner derivations]] and [[lie-groups/exponential-map-lie-group|exponentials]] in $\mathrm{GL}(\mathfrak g)$). Automorphisms not generated this way are “outer” in nature, and are related to [[lie-groups/outer-derivation|outer derivations]] at the infinitesimal level.

**Context.**
Automorphisms organize symmetry of structure constants, control conjugacy of subalgebras (including Levi factors in the [[lie-groups/levi-decomposition-theorem|Levi decomposition]]), and interact with representation theory through transport of structure.
