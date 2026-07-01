+++
id = "shared-foundations/lower-bound"
title = "Lower bound"
kind = "knowl"
summary = "An element that is less than or equal to every element of a subset in an ordered set."
aliases = ["lower-bound", "Lower bound"]
domains = ["shared-foundations"]
legacy_source_path = "shared-foundations/lower-bound.md"
+++

A **lower bound** of a subset $A$ of a [[shared-foundations/partial-order|partially ordered set]] $(P,\le)$ is an element $\ell\in P$ such that $\ell\le a$ for all $a\in A$. The subset $A$ is **bounded below** if it has at least one lower bound in $P$.

Lower bounds complement [[shared-foundations/upper-bound|upper bounds]] and lead to greatest lower bounds (the [[real-analysis/infimum|infimum]] in real analysis).

**Examples:**
- In $(\mathbb{Z},\le)$, the integer $-5$ is a lower bound for the subset $\{-2,0,3\}$.
- In the poset $(\mathcal P(X),\subseteq)$, the set $A\cap B$ is a lower bound for $\{A,B\}$, where $A\cap B$ is the [[shared-foundations/intersection|intersection]] of $A$ and $B$.
