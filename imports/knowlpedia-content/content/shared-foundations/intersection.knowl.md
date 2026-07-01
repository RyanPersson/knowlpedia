+++
id = "shared-foundations/intersection"
title = "Intersection"
kind = "knowl"
summary = "The set of elements that belong to all of the given sets."
aliases = ["intersection"]
domains = ["shared-foundations"]
legacy_source_path = "shared-foundations/intersection.md"
+++

An **intersection** is the set of elements common to every set in a given collection. For sets $A,B$,
$$
A\cap B=\{x : x\in A \text{ and } x\in B\}.
$$

More generally, for an [[shared-foundations/indexed-family-of-sets|indexed family of sets]] $(A_i)_{i\in I}$,
$$
\bigcap_{i\in I} A_i=\{x : \forall i\in I,\; x\in A_i\}.
$$

Intersection is dual to [[shared-foundations/union|union]] and is closely related to [[shared-foundations/subset|containment]]: one has $A\subseteq B$ exactly when $A\cap B=A$.

**Examples:**
- $\{1,2\}\cap\{2,3\}=\{2\}$.
- If $A=\{x\in\mathbb{R}: x<0\}$ and $B=\{x\in\mathbb{R}: x\ge 0\}$, then $A\cap B=\varnothing$ (see [[shared-foundations/empty-set|empty set]]).
