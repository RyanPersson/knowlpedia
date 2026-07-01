+++
id = "shared-foundations/empty-set"
title = "Empty set"
kind = "knowl"
summary = "The unique set that contains no elements."
aliases = ["empty-set", "Empty set"]
domains = ["shared-foundations"]
legacy_source_path = "shared-foundations/empty-set.md"
+++

An **empty set** is a set $\varnothing$ with no elements, meaning
$$
\forall x\,(x\notin \varnothing).
$$

By extensionality (see [[shared-foundations/set|set]]), there is only one such set: if $E$ and $F$ have no elements, then $E=F$. The empty set is the identity for [[shared-foundations/union|union]] and an absorbing element for [[shared-foundations/intersection|intersection]] when working with subsets of a fixed ambient set.

**Examples:**
- The solution set $\{x\in\mathbb{R} : x^2+1=0\}$ is $\varnothing$.
- If $A$ and $B$ are disjoint subsets of a set, then $A\cap B=\varnothing$.
