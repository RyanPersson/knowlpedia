---
title: "Separated sets"
description: "Two subsets with positive distance between them in a metric space"
---

Two subsets $A,B$ of a {{< knowl id="metric-space" text="metric space" >}} $(X,d)$ are **separated** if their distance is positive:
\[
\operatorname{dist}(A,B)=\inf\{d(a,b): a\in A,\ b\in B\}>0.
\]

If $A$ and $B$ are separated, then they have disjoint {{< knowl id="closure" section="topology-core" text="closures" >}} in the {{< knowl id="metric-induced-topology" text="metric-induced topology" >}}.

**Examples:**
- In $\mathbb{R}$, the sets $[0,1]$ and $[2,3]$ are separated (their distance is $1$).
- In $\mathbb{R}$, the sets $(0,1)$ and $(1,2)$ are not separated (their distance is $0$).
- In the discrete metric on $X$, any two disjoint nonempty subsets are separated.
