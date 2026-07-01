+++
id = "lie-groups/cartans-criterion-solvability"
title = "Cartan’s criterion for solvability"
kind = "knowl"
summary = "A Lie algebra over characteristic 0 is solvable iff a certain trace pairing vanishes on g × [g,g]."
aliases = ["cartans-criterion-solvability", "Cartan’s criterion for solvability"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/cartans-criterion-solvability.md"
+++

Let $\mathfrak{g}$ be a finite-dimensional [[lie-groups/lie-algebra|Lie algebra]] over a field of characteristic $0$, and let $B$ be its [[lie-groups/killing-form|Killing form]]:
$$
B(X,Y)=\mathrm{tr}(\mathrm{ad}_X\circ \mathrm{ad}_Y).
$$

Write $\mathfrak{g}'=[\mathfrak{g},\mathfrak{g}]$ for the [[lie-groups/derived-subalgebra|derived subalgebra]].

**Theorem (Cartan’s criterion for solvability).** $\mathfrak{g}$ is [[lie-groups/solvable-lie-algebra|solvable]] if and only if
$$
B(X,Y)=0 \quad \text{for all } X\in \mathfrak{g},\; Y\in \mathfrak{g}'.
$$
Equivalently,
$$
\mathrm{tr}(\mathrm{ad}_X\circ \mathrm{ad}_Y)=0 \quad \text{for all } X\in \mathfrak{g},\; Y\in [\mathfrak{g},\mathfrak{g}].
$$

**Motivation.** Solvability is defined in terms of the [[lie-groups/derived-series-lie-algebra|derived series]], but Cartan’s criterion replaces an iterative bracket computation with a single trace-vanishing condition. It is particularly effective when $\mathfrak{g}$ is presented as a subalgebra of $\mathfrak{gl}(V)$, where traces can be computed concretely.

**Remark.** The criterion is compatible with the heuristic that “brackets measure noncommutativity”: the condition tests how far commutators act nontrivially through $\mathrm{ad}$. Compare also [[lie-groups/cartans-criterion-semisimplicity|Cartan’s semisimplicity criterion]].
