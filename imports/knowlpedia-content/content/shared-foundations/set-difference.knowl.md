+++
id = "shared-foundations/set-difference"
title = "Set difference"
kind = "knowl"
summary = "The elements of one set that are not in another set."
aliases = ["set-difference", "Set difference"]
domains = ["shared-foundations"]
legacy_source_path = "shared-foundations/set-difference.md"
+++

A **set difference** (or **relative complement**) of sets $A$ and $B$ is the set
$$
A\setminus B=\{x : x\in A \text{ and } x\notin B\}.
$$

Set difference can be expressed using [[shared-foundations/intersection|intersection]] and [[shared-foundations/complement|complement]] once an ambient universe $U$ is chosen: if $B\subseteq U$, then $A\setminus B = A\cap B^{c}$.

**Examples:**
- $\{1,2,3\}\setminus\{2,4\}=\{1,3\}$.
- If $A\subseteq B$, then $A\setminus B=\varnothing$ (see [[shared-foundations/empty-set|empty set]]).
