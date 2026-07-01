+++
id = "lie-groups/weight-of-a-representation"
title = "Weight of a representation"
kind = "knowl"
summary = "A functional occurring as a simultaneous eigenvalue for the action of a Cartan subalgebra."
aliases = ["weight-of-a-representation", "Weight of a representation"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/weight-of-a-representation.md"
+++

### Definition
Let $\mathfrak g$ be a finite-dimensional complex semisimple Lie algebra (see [[lie-groups/semisimple-lie-algebra|semisimple Lie algebras]]) and let $\mathfrak h\subset \mathfrak g$ be a [[lie-groups/cartan-subalgebra|Cartan subalgebra]]. For a representation $\rho:\mathfrak g\to \mathfrak{gl}(V)$, a linear functional $\lambda\in \mathfrak h^\ast$ is called a **weight** of $V$ if the corresponding [[lie-groups/weight-space|weight space]]
$$
V_\lambda=\{v\in V\mid \rho(H)v=\lambda(H)v\ \text{for all }H\in\mathfrak h\}
$$
is nonzero.

Equivalently, $\lambda$ is a weight if there exists $0\neq v\in V$ such that every $H\in\mathfrak h$ acts on $v$ by the scalar $\lambda(H)$ (so $v$ is a simultaneous eigenvector for the commuting family $\rho(\mathfrak h)$).

### Context
Weights organize the representation theory of semisimple Lie algebras: the set of weights (with multiplicities $\dim V_\lambda$) encodes much of $V$, and irreducible representations are classified by their [[lie-groups/highest-weight|highest weight]] (see [[lie-groups/highest-weight-theorem|the highest-weight theorem]]). The ambient space where weights live is explained in [[lie-groups/weights-in-dual-cartan|weights in the dual Cartan]].
