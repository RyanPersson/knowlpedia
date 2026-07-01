+++
id = "shared-foundations/union"
title = "Union"
kind = "knowl"
summary = "The set of elements that belong to at least one of the given sets."
aliases = ["union"]
domains = ["shared-foundations"]
legacy_source_path = "shared-foundations/union.md"
+++

A **union** is the set obtained by collecting all elements that lie in at least one set in a given collection. For sets $A,B$,
$$
A\cup B=\{x : x\in A \text{ or } x\in B\}.
$$

More generally, for an [[shared-foundations/indexed-family-of-sets|indexed family of sets]] $(A_i)_{i\in I}$,
$$
\bigcup_{i\in I} A_i=\{x : \exists i\in I\text{ with }x\in A_i\}.
$$

Union is dual to [[shared-foundations/intersection|intersection]] and interacts with [[shared-foundations/complement|complement]] via De Morgan’s laws in an ambient universe.

**Examples:**
- $\{1,2\}\cup\{2,3\}=\{1,2,3\}$.
- If $A_n=\{n\}$ for $n\in\mathbb{N}$, then $\bigcup_{n\in\mathbb{N}} A_n=\mathbb{N}$.
