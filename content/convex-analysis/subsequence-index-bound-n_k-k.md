---
title: "Index bound for subsequences"
description: "If n1<n2<… are positive integers, then nk≥k"
---

**Lemma.**
Let $(n_k)$ be a strictly increasing sequence of positive integers, i.e., $n_1<n_2<\cdots$. Then
$$
n_k\ge k \quad\text{for all }k\in\mathbb{N}.
$$

**Proof.** By induction. For $k=1$, $n_1\ge 1$. Assume $n_k\ge k$. Then $n_{k+1}>n_k\ge k$, hence $n_{k+1}\ge k+1$.

This estimate is often used when transferring "eventually" statements from a sequence to a {{< knowl id="subsequence" text="subsequence" >}} (e.g., to compare thresholds $N$ and $K$).
