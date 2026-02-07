---
title: "Symmetric difference"
description: "The elements that lie in exactly one of two sets."
---

A **symmetric difference** of sets $A$ and $B$ is the set of elements that belong to exactly one of them:
$$
A\triangle B=(A\setminus B)\cup(B\setminus A).
$$

This operation is built from {{< knowl id="set-difference" text="set difference" >}} and {{< knowl id="union" text="union" >}}. It is symmetric in $A$ and $B$ and measures “disagreement” between sets: $A\triangle B=\varnothing$ exactly when $A=B$.

**Examples:**
- $\{1,2,3\}\triangle\{2,3,4\}=\{1,4\}$.
- If $A$ and $B$ are disjoint, then $A\triangle B=A\cup B$.
