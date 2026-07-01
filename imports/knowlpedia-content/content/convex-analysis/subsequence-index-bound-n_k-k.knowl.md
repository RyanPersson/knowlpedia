+++
id = "convex-analysis/subsequence-index-bound-n_k-k"
title = "Index bound for subsequences"
kind = "knowl"
summary = "If n1<n2<… are positive integers, then nk≥k"
aliases = ["subsequence-index-bound-n_k-k", "Index bound for subsequences"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/subsequence-index-bound-n_k-k.md"
+++

**Lemma.**
Let $(n_k)$ be a strictly increasing sequence of positive integers, i.e., $n_1<n_2<\cdots$. Then
$$
n_k\ge k \quad\text{for all }k\in\mathbb{N}.
$$

**Proof.** By induction. For $k=1$, $n_1\ge 1$. Assume $n_k\ge k$. Then $n_{k+1}>n_k\ge k$, hence $n_{k+1}\ge k+1$.

This estimate is often used when transferring "eventually" statements from a sequence to a [[analysis/subsequence|subsequence]] (e.g., to compare thresholds $N$ and $K$).
