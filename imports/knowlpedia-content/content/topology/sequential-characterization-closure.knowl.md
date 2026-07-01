+++
id = "topology/sequential-characterization-closure"
title = "Sequential characterization of closure"
kind = "knowl"
summary = "In a metric space, a point lies in the closure of a set iff it is the limit of a sequence from the set."
aliases = ["sequential-characterization-closure", "Sequential characterization of closure"]
domains = ["topology"]
legacy_source_path = "topology/sequential-characterization-closure.md"
+++

**Sequential characterization of closure:** Let $(X,d)$ be a [[topology/metric-space|metric space]], let $A\subseteq X$, and let $x\in X$. Then
\[
x\in \overline{A}
\quad\Longleftrightarrow\quad
\text{there exists a sequence }(a_n)\text{ in }A\text{ with }a_n\to x,
\]
where $\overline{A}$ denotes the [[topology/closure|closure]] of $A$.

This turns the topological notion of closure into a sequential condition in metric spaces, and it complements [[topology/sequential-characterization-closed|the sequential characterization of closed sets]].
