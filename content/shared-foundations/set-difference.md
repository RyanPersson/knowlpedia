---
title: "Set difference"
description: "The elements of one set that are not in another set."
---

A **set difference** (or **relative complement**) of sets $A$ and $B$ is the set
$$
A\setminus B=\{x : x\in A \text{ and } x\notin B\}.
$$

Set difference can be expressed using {{< knowl id="intersection" text="intersection" >}} and {{< knowl id="complement" text="complement" >}} once an ambient universe $U$ is chosen: if $B\subseteq U$, then $A\setminus B = A\cap B^{c}$.

**Examples:**
- $\{1,2,3\}\setminus\{2,4\}=\{1,3\}$.
- If $A\subseteq B$, then $A\setminus B=\varnothing$ (see {{< knowl id="empty-set" text="empty set" >}}).
