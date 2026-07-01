+++
id = "convex-analysis/basic-properties-of-open-sets"
title = "Basic properties of open sets"
kind = "knowl"
summary = "Unions of open sets are open; finite intersections of open sets are open"
aliases = ["basic-properties-of-open-sets", "Basic properties of open sets"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/basic-properties-of-open-sets.md"
+++

**Theorem.**
Let $(X,d)$ be a metric space. Then:

1. $\emptyset$ is open.
2. $X$ is open.
3. The union of any collection of [[convex-analysis/open-subset|open sets]] in $X$ is open.
4. The intersection of finitely many open sets in $X$ is open.

**Proof sketch.** (1)–(2) follow directly from the definition. For (3), if $x$ lies in a union, it lies in one member open set and hence has a ball contained in that member and thus in the union. For (4), intersect the finitely many balls given by each open set at a point: taking the minimum radius keeps the ball inside all sets.
