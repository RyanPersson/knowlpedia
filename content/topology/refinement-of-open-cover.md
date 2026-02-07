---
title: "Refinement of an open cover"
description: "A cover that is finer than another, with each set contained in a member of the original cover."
---

A **refinement** of a cover $\mathcal U$ of a set $A\subseteq X$ is another cover $\mathcal V$ of $A$ such that for every $V\in\mathcal V$ there exists $U\in\mathcal U$ with
\[
V \subseteq U.
\]
If $\mathcal U$ and $\mathcal V$ are {{< knowl id="open-cover" text="open covers" >}}, then $\mathcal V$ is called an **open refinement** of $\mathcal U$.

Refinements compare “how fine” two covers are and are especially useful when working with a {{< knowl id="basis-of-topology" text="basis of a topology" >}}, since open covers can often be refined by basic open sets.

**Examples:**
- In $\mathbb{R}$, let $\mathcal U=\{(-1,1),(0,2)\}$, which covers $[0,1]$. Then $\mathcal V=\{(0,1/2),(1/2,1)\}$ is a refinement of $\mathcal U$.
- If $\mathcal U$ is an open cover of $X$ and $\mathcal B$ is a basis, then taking all $B\in\mathcal B$ with $B\subseteq U$ for some $U\in\mathcal U$ gives an open refinement by basis elements.
