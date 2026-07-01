+++
id = "topology/sequential-characterization-closed"
title = "Sequential characterization of closed sets"
kind = "knowl"
summary = "In a metric space, a set is closed iff it contains limits of all convergent sequences from it."
aliases = ["sequential-characterization-closed", "Sequential characterization of closed sets"]
domains = ["topology"]
legacy_source_path = "topology/sequential-characterization-closed.md"
+++

**Sequential characterization of closed sets:** Let $(X,d)$ be a [[topology/metric-space|metric space]] and let $A\subseteq X$. Then $A$ is [[topology/closed-set|closed]] if and only if for every [[topology/convergent-sequence|convergent sequence]] $(a_n)$ in $A$ with $a_n\to x$ in $X$, one has $x\in A$.

This is the standard “sequentially closed equals closed” principle for metric spaces, and it pairs naturally with [[topology/sequential-characterization-closure|the sequential characterization of closure]].
