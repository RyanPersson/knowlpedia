+++
id = "topology/cover"
title = "Cover"
kind = "knowl"
summary = "A family of subsets whose union contains a given set."
aliases = ["cover"]
domains = ["topology"]
legacy_source_path = "topology/cover.md"
+++

A **cover** of a subset $A\subseteq X$ is a family $\{U_i\}_{i\in I}$ of subsets of $X$ such that
\[
A \subseteq \bigcup_{i\in I} U_i.
\]
Covers are often presented as an [[shared-foundations/indexed-family-of-sets|indexed family of sets]], and the condition above says that the [[shared-foundations/union|union]] of the family contains $A$. In topology, one frequently restricts to an [[topology/open-cover|open cover]].

**Examples:**
- In $\mathbb{R}$, the family $\{(n-1,n+1)\}_{n\in\mathbb{Z}}$ covers $\mathbb{R}$.
- For $A=[0,1]\subseteq \mathbb{R}$, the sets $U_1=(-1,1/2)$ and $U_2=(0,2)$ form a cover of $A$.
