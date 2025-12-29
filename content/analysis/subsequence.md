---
title: "Subsequence"
description: "A sequence obtained by selecting terms along a strictly increasing index sequence."
---

Let $(x_n)_{n\in\mathbb{N}}$ be a sequence in a {{< knowl id="set" text="set" >}} $X$. A **subsequence** of $(x_n)$ is a sequence of the form $(x_{n_k})_{k\in\mathbb{N}}$, where $(n_k)_{k\in\mathbb{N}}$ is a strictly increasing sequence of natural numbers:
$$n_1<n_2<n_3<\cdots.$$

Subsequences capture partial asymptotic behavior and are indispensable in {{< knowl id="compact-set" text="compactness" >}} arguments (e.g., Bolzano–Weierstrass) and in defining {{< knowl id="limit-superior-lim-sup" text="lim sup" >}} and {{< knowl id="limit-inferior-lim-inf" text="lim inf" >}}.

**Examples:**
- From $x_n = (-1)^n$, the subsequence $x_{2k}=1$ is constant, and the subsequence $x_{2k+1}=-1$ is constant.
- If $x_n=1/n$, then $(x_{n_k})$ with $n_k=2k$ is the subsequence $1/(2k)$.
- Not every selection yields a subsequence: choosing $n_k=k$ gives the original sequence; choosing indices that do not increase strictly does not define a subsequence.
