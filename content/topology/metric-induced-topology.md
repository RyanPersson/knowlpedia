---
title: "Metric-induced topology"
description: "The topology on a metric space in which a set is open if it contains an open ball around each of its points."
---

The **metric-induced topology** on a metric space $(X,d)$ is the collection $\tau_d$ of subsets $U\subseteq X$ such that for every $x\in U$ there exists $r>0$ with $B_d(x,r)\subseteq U$, where $B_d(x,r)$ is the {{< knowl id="open-ball" text="open ball" >}} of radius $r$ centered at $x$.

This makes $(X,\tau_d)$ a {{< knowl id="topological-space" text="topological space" >}}; equivalently, the family of open balls forms a {{< knowl id="basis-of-topology" text="basis" >}} for $\tau_d$, and the {{< knowl id="open-set" text="open sets" >}} are precisely unions of open balls.

**Examples:**
- On $\mathbb{R}^n$ with the Euclidean metric, $\tau_d$ is the usual topology of Euclidean space.
- On a set $X$ with the discrete metric, $\tau_d$ is the discrete topology (every subset is open).
