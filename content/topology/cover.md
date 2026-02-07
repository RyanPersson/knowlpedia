---
title: "Cover"
description: "A family of subsets whose union contains a given set."
---

A **cover** of a subset $A\subseteq X$ is a family $\{U_i\}_{i\in I}$ of subsets of $X$ such that
\[
A \subseteq \bigcup_{i\in I} U_i.
\]
Covers are often presented as an {{< knowl id="indexed-family-of-sets" section="shared-foundations" text="indexed family of sets" >}}, and the condition above says that the {{< knowl id="union" section="shared-foundations" text="union" >}} of the family contains $A$. In topology, one frequently restricts to an {{< knowl id="open-cover" text="open cover" >}}.

**Examples:**
- In $\mathbb{R}$, the family $\{(n-1,n+1)\}_{n\in\mathbb{Z}}$ covers $\mathbb{R}$.
- For $A=[0,1]\subseteq \mathbb{R}$, the sets $U_1=(-1,1/2)$ and $U_2=(0,2)$ form a cover of $A$.
