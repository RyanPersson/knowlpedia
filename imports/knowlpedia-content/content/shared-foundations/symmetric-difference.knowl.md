+++
id = "shared-foundations/symmetric-difference"
title = "Symmetric difference"
kind = "knowl"
summary = "The elements that lie in exactly one of two sets."
aliases = ["symmetric-difference", "Symmetric difference"]
domains = ["shared-foundations"]
legacy_source_path = "shared-foundations/symmetric-difference.md"
+++

A **symmetric difference** of sets $A$ and $B$ is the set of elements that belong to exactly one of them:
$$
A\triangle B=(A\setminus B)\cup(B\setminus A).
$$

This operation is built from [[shared-foundations/set-difference|set difference]] and [[shared-foundations/union|union]]. It is symmetric in $A$ and $B$ and measures “disagreement” between sets: $A\triangle B=\varnothing$ exactly when $A=B$.

**Examples:**
- $\{1,2,3\}\triangle\{2,3,4\}=\{1,4\}$.
- If $A$ and $B$ are disjoint, then $A\triangle B=A\cup B$.
