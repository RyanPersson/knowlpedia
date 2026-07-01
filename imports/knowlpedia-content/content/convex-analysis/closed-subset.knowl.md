+++
id = "convex-analysis/closed-subset"
title = "Closed set"
kind = "knowl"
summary = "A set whose complement is open"
aliases = ["closed-subset", "Closed set"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/closed-subset.md"
+++

Let $(X,d)$ be a metric space and let $F\subset X$.

The set $F$ is **closed** if its complement $F^c:=X\setminus F$ is [[convex-analysis/open-subset|open]].

Closed sets are stable under arbitrary intersections and finite unions (see [[convex-analysis/basic-properties-of-closed-sets|basic properties of closed sets]]). The [[convex-analysis/closure-of-a-set|closure]] of a set is the smallest closed set containing it.

**Examples:**
- In $\mathbb{R}$, every closed interval $[a,b]$ is closed.
- In any metric space, $\emptyset$ and $X$ are closed.
- In a discrete metric space, every subset of $X$ is closed.
