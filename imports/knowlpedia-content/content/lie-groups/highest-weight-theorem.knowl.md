+++
id = "lie-groups/highest-weight-theorem"
title = "Highest-weight theorem"
kind = "knowl"
summary = "Finite-dimensional irreducibles of a semisimple Lie algebra are classified by dominant integral highest weights."
aliases = ["highest-weight-theorem", "Highest-weight theorem"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/highest-weight-theorem.md"
+++

Fix a complex semisimple [[lie-groups/lie-algebra|Lie algebra]] $\mathfrak g$, a [[lie-groups/cartan-subalgebra|Cartan subalgebra]] $\mathfrak h$, and a choice of positive roots (hence [[lie-groups/simple-root|simple roots]] and fundamental weights).

**Theorem (Highest-weight classification, Lie algebra form).**

1. Every finite-dimensional irreducible $\mathfrak g$-module is a [[lie-groups/highest-weight-representation|highest-weight representation]] with a unique [[lie-groups/highest-weight|highest weight]] $\lambda\in\mathfrak h^*$.
2. A weight $\lambda$ occurs as the highest weight of a finite-dimensional irreducible module if and only if $\lambda$ is **dominant integral** (i.e. it pairs with all simple coroots to give nonnegative integers).
3. For each dominant integral $\lambda$, there exists (up to isomorphism) a unique finite-dimensional irreducible $\mathfrak g$-module $V(\lambda)$ with highest weight $\lambda$.

**Group form (compact groups).**
If $G$ is a compact connected [[lie-groups/compact-lie-group|Lie group]] with maximal torus $T$ (see [[lie-groups/maximal-torus-theorem|maximal tori]]), then irreducible unitary representations of $G$ are similarly classified by dominant integral weights of $T$; differentiating recovers the Lie-algebra classification (compare [[lie-groups/differential-is-lie-algebra-homomorphism|differentiation of representations]]).

**Context.**
This theorem is the conceptual reason that objects like [[lie-groups/fundamental-representation|fundamental representations]] (highest weights equal to fundamental weights) play a foundational role: they correspond to the vertices of the [[lie-groups/dynkin-diagram|Dynkin diagram]] and generate the dominant cone.
