---
title: "Basic properties of open sets"
description: "Unions of open sets are open; finite intersections of open sets are open"
---

**Theorem.**
Let $(X,d)$ be a metric space. Then:

1. $\emptyset$ is open.
2. $X$ is open.
3. The union of any collection of {{< knowl id="open-subset" text="open sets" >}} in $X$ is open.
4. The intersection of finitely many open sets in $X$ is open.

**Proof sketch.** (1)–(2) follow directly from the definition. For (3), if $x$ lies in a union, it lies in one member open set and hence has a ball contained in that member and thus in the union. For (4), intersect the finitely many balls given by each open set at a point: taking the minimum radius keeps the ball inside all sets.
