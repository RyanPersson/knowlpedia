---
title: "Subsequence"
description: "A sequence obtained by restricting to an increasing index sequence"
---

Let $(x_n)$ be a sequence in a set $X$ (typically a metric space). Let $(n_k)$ be a strictly increasing sequence of positive integers:
$$
n_1<n_2<n_3<\cdots.
$$
Then the sequence $(x_{n_k})_{k\in\mathbb{N}}$ is called a **subsequence** of $(x_n)$.

Subsequences are fundamental in analyzing {{< knowl id="convergence-of-a-sequence" text="convergence" >}} and compactness-type phenomena, since they allow extraction of "better behaved" sequences from a given one.

**Examples:**
- If $x_n=(-1)^n$, then $(x_{2k})$ is the constant subsequence $1$, and $(x_{2k+1})$ is the constant subsequence $-1$.
- If $x_n=1/n$, then any subsequence $x_{n_k}=1/n_k$ still converges to $0$.
