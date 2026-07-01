+++
id = "topology/sequentially-compact-set"
title = "Sequentially compact set"
kind = "knowl"
summary = "A set where every sequence has a convergent subsequence with limit in the set."
aliases = ["sequentially-compact-set", "Sequentially compact set"]
domains = ["topology"]
legacy_source_path = "topology/sequentially-compact-set.md"
+++

A **sequentially compact set** is a subset $K\subseteq X$ of a [[topology/topological-space|topological space]] $X$ such that every sequence $(x_n)$ in $K$ has a [[real-analysis/subsequence|subsequence]] $(x_{n_k})$ that is a [[topology/convergent-sequence|convergent sequence]] in $X$ with limit $x\in K$.

Sequential compactness is phrased purely in terms of sequences, and in many important settings (notably [[topology/metric-space|metric spaces]]) it closely tracks [[topology/compact-set|compactness]].

**Examples:**
- In $\mathbb{R}$ with the usual topology, $[0,1]$ is sequentially compact.
- An infinite set with the discrete topology is not sequentially compact (a sequence of distinct points has no convergent subsequence).
