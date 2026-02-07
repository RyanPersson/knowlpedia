---
title: "Cartan’s criterion for solvability"
description: "A Lie algebra over characteristic 0 is solvable iff a certain trace pairing vanishes on g × [g,g]."
---

Let $\mathfrak{g}$ be a finite-dimensional {{< knowl id="lie-algebra" text="Lie algebra" >}} over a field of characteristic $0$, and let $B$ be its {{< knowl id="killing-form" text="Killing form" >}}:
$$
B(X,Y)=\mathrm{tr}(\mathrm{ad}_X\circ \mathrm{ad}_Y).
$$

Write $\mathfrak{g}'=[\mathfrak{g},\mathfrak{g}]$ for the {{< knowl id="derived-subalgebra" text="derived subalgebra" >}}.

**Theorem (Cartan’s criterion for solvability).** $\mathfrak{g}$ is {{< knowl id="solvable-lie-algebra" text="solvable" >}} if and only if
$$
B(X,Y)=0 \quad \text{for all } X\in \mathfrak{g},\; Y\in \mathfrak{g}'.
$$
Equivalently,
$$
\mathrm{tr}(\mathrm{ad}_X\circ \mathrm{ad}_Y)=0 \quad \text{for all } X\in \mathfrak{g},\; Y\in [\mathfrak{g},\mathfrak{g}].
$$

**Motivation.** Solvability is defined in terms of the {{< knowl id="derived-series-lie-algebra" text="derived series" >}}, but Cartan’s criterion replaces an iterative bracket computation with a single trace-vanishing condition. It is particularly effective when $\mathfrak{g}$ is presented as a subalgebra of $\mathfrak{gl}(V)$, where traces can be computed concretely.

**Remark.** The criterion is compatible with the heuristic that “brackets measure noncommutativity”: the condition tests how far commutators act nontrivially through $\mathrm{ad}$. Compare also {{< knowl id="cartans-criterion-semisimplicity" text="Cartan’s semisimplicity criterion" >}}.
