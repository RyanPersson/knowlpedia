+++
id = "convex-analysis/completeness-implies-closedness-closed-subsets-of-complete-spaces-are-complete"
title = "Completeness and closedness"
kind = "knowl"
summary = "Complete subsets are closed; closed subsets of complete spaces are complete"
aliases = ["completeness-implies-closedness-closed-subsets-of-complete-spaces-are-complete", "Completeness and closedness"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/completeness-implies-closedness-closed-subsets-of-complete-spaces-are-complete.md"
+++

**Proposition.**
Let $(X,d)$ be a [[convex-analysis/metric-metric-space|metric space]].

1. If $E\subset X$ is [[convex-analysis/complete-metric-space-complete-subset|complete]], then $E$ is [[convex-analysis/closed-subset|closed]] in $X$.
2. If $X$ is complete and $E\subset X$ is closed, then $E$ is complete (with the restricted metric).

**Context.** This gives a practical way to recognize complete sets: inside a complete ambient space, "closed" and "complete" coincide.

**Proof sketch.**
1. Take a sequence $(x_n)\subset E$ converging in $X$ to $x$. Any [[convex-analysis/convergent-sequences-are-cauchy|convergent sequence is Cauchy]], so $(x_n)$ is Cauchy in $E$. By completeness of $E$, it converges in $E$ to some $y\in E$. By [[convex-analysis/uniqueness-of-limits-in-metric-spaces|uniqueness of limits]], $x=y\in E$, hence $E$ is closed.
2. Let $(x_n)$ be Cauchy in $E$. Then it is Cauchy in $X$ and hence converges in $X$ (since $X$ is complete) to some $x\in X$. Because $E$ is closed and $(x_n)\subset E$ converges to $x$, we have $x\in E$. Thus $(x_n)$ converges in $E$.
