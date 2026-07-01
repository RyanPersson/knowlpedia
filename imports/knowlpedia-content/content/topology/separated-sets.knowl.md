+++
id = "topology/separated-sets"
title = "Separated sets"
kind = "knowl"
summary = "Two sets in a topological space that do not meet each other's closure."
aliases = ["separated-sets", "Separated sets"]
domains = ["topology"]
legacy_source_path = "topology/separated-sets.md"
+++

Two **separated sets** $A$ and $B$ in a [[topology/topological-space|topological space]] $X$ are subsets such that
\[
A\cap \overline{B}=\varnothing
\quad\text{and}\quad
\overline{A}\cap B=\varnothing,
\]
where $\overline{A}$ and $\overline{B}$ denote [[topology/closure|closures]] in $X$.

Separatedness is the key notion used to define [[topology/connected-set|connectedness]]: a space is disconnected exactly when it can be written as a union of two nonempty separated sets.

**Examples:**
- In $\mathbb{R}$ with the usual topology, $A=(0,1)$ and $B=(1,2)$ are separated.
- In $\mathbb{R}$, the rationals $\mathbb{Q}$ and the irrationals $\mathbb{R}\setminus\mathbb{Q}$ are not separated, since each is dense and has closure $\mathbb{R}$.
