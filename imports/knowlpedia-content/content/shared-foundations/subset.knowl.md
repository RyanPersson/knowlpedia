+++
id = "shared-foundations/subset"
title = "Subset"
kind = "knowl"
summary = "A set contained in another set, element by element."
aliases = ["subset"]
domains = ["shared-foundations"]
legacy_source_path = "shared-foundations/subset.md"
+++

A **subset** of a set $B$ is a set $A$ such that every element of $A$ is an element of $B$:
$$
A\subseteq B \;\;:\!\iff\;\; \forall x\,(x\in A \Rightarrow x\in B).
$$

The subset relation is a basic way to compare [[shared-foundations/set|sets]] and is used to define operations like [[shared-foundations/power-set|power set]] and [[shared-foundations/set-difference|set difference]]. Note that $A=B$ holds exactly when both $A\subseteq B$ and $B\subseteq A$.

**Examples:**
- $\{1,2\}\subseteq \{1,2,3\}$.
- For any set $A$, $\varnothing\subseteq A$ (see [[shared-foundations/empty-set|empty set]]).
