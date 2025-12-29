---
title: "Limit superior (lim sup)"
description: "For a real sequence, the limit of the tail suprema, describing the maximal subsequential limit."
---

Let $(a_n)$ be a sequence in the extended real line $[-\infty,\infty]$. Define the **tail suprema**
$$s_n := \sup\{a_k : k\ge n\}\in[-\infty,\infty].$$
Then the **limit superior** of $(a_n)$ is
$$\limsup_{n\to\infty} a_n := \lim_{n\to\infty} s_n,$$
where the limit exists in $[-\infty,\infty]$ because $(s_n)$ is nonincreasing.

The number $\limsup a_n$ is the largest value that subsequences can "accumulate at" (more precisely, it equals the supremum of all subsequential limits when those limits are taken in $[-\infty,\infty]$).

**Examples:**
- If $a_n=(-1)^n$, then $\limsup a_n = 1$.
- If $a_n=1/n$, then $\limsup a_n = 0$.
- If $a_n=n$, then $\limsup a_n = +\infty$.
