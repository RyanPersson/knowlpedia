---
title: "Limit inferior (lim inf)"
description: "For a real sequence, the limit of the tail infima, describing the minimal subsequential limit."
---

Let $(a_n)$ be a sequence in the extended real line $[-\infty,\infty]$. Define the **tail infima**
$$i_n := \inf\{a_k : k\ge n\}\in[-\infty,\infty].$$
Then the **limit inferior** of $(a_n)$ is
$$\liminf_{n\to\infty} a_n := \lim_{n\to\infty} i_n,$$
where the limit exists in $[-\infty,\infty]$ because $(i_n)$ is nondecreasing.

The number $\liminf a_n$ is the smallest value that subsequences can "accumulate at" (it equals the infimum of all subsequential limits in $[-\infty,\infty]$).

**Examples:**
- If $a_n=(-1)^n$, then $\liminf a_n = -1$.
- If $a_n=1/n$, then $\liminf a_n = 0$.
- If $a_n=-n$, then $\liminf a_n = -\infty$.
