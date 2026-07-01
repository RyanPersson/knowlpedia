+++
id = "convex-analysis/open-subset"
title = "Open set"
kind = "knowl"
summary = "A set that contains a small open ball around each of its points"
aliases = ["open-subset", "Open set"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/open-subset.md"
+++

Let $(X,d)$ be a metric space and let $A\subset X$.

The set $A$ is **open** if for every $a\in A$ there exists $\delta>0$ such that
$$
B(a;\delta)\subset A,
$$

where $B(a;\delta)$ is the open ball in $X$.

Open sets are stable under arbitrary unions and finite intersections (see [[convex-analysis/basic-properties-of-open-sets|basic properties of open sets]]). Complements of open sets are [[convex-analysis/closed-subset|closed]].

**Examples:**
- In $\mathbb{R}$, every open interval $(a,b)$ is open.
- In any metric space, $\emptyset$ and $X$ are open.
- In a discrete metric space, every subset of $X$ is open.
