---
title: "Equivalence class"
description: "The subset of elements equivalent to a given element under an equivalence relation."
---

Let $\sim$ be an equivalence relation on a set $X$. For $x\in X$, the **equivalence class** of $x$ is
$$[x] := \{y\in X : y\sim x\}\subseteq X.$$

Equivalence classes are the "blocks" determined by $\sim$; they are pairwise disjoint and their union is all of $X$. Quotient constructions replace elements by their classes.

**Examples:**
- If $\sim$ is congruence mod $3$ on $\mathbb{Z}$, then $[1]=\{\dots,-5,-2,1,4,7,\dots\}$.
- If $\sim$ is equality on $X$, then $[x]=\{x\}$ for each $x\in X$.
- On $\mathbb{R}$ with $x\sim y \iff x-y\in\mathbb{Q}$, the class of $0$ is $[0]=\mathbb{Q}$, and the class of $\sqrt{2}$ is $\sqrt{2}+\mathbb{Q}$.
