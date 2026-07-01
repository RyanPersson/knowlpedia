+++
id = "lie-groups/levi-decomposition-theorem"
title = "Levi decomposition"
kind = "knowl"
summary = "Any finite-dimensional Lie algebra splits as a semidirect product of semisimple part and solvable radical."
aliases = ["levi-decomposition-theorem", "Levi decomposition"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/levi-decomposition-theorem.md"
+++

Let $\mathfrak g$ be a finite-dimensional [[lie-groups/lie-algebra|Lie algebra]] over a field of characteristic $0$.

**Theorem (Levi decomposition).**
There exists a largest solvable ideal $\mathfrak r\subseteq \mathfrak g$, called the **radical** (a notion built from [[lie-groups/solvable-lie-algebra|solvability]] and ideals as in [[lie-groups/ideal-lie-algebra|ideal]]), and a semisimple subalgebra $\mathfrak s\subseteq \mathfrak g$ such that
\[
\mathfrak g \cong \mathfrak s \ltimes \mathfrak r
\]
as Lie algebras. Here $\mathfrak s$ is called a **Levi factor** and $\mathfrak r$ is the solvable radical.

Moreover, any two Levi factors are conjugate by an inner automorphism of $\mathfrak g$ (more precisely, by an automorphism arising from the exponential of an [[lie-groups/inner-derivation|inner derivation]] coming from $\mathfrak r$), so the semisimple part is essentially unique.

**Context.**
This theorem isolates the “semisimple core” of a Lie algebra and reduces many problems to understanding semisimple algebras (see [[lie-groups/semisimple-lie-algebra|semisimple Lie algebras]]) plus solvable/nilpotent structure (compare [[lie-groups/derived-series-lie-algebra|derived series]] and [[lie-groups/nilpotent-lie-algebra|nilpotent Lie algebras]]). It is also a key input in analyzing Lie algebras arising from [[lie-groups/compact-lie-group|compact Lie groups]].
