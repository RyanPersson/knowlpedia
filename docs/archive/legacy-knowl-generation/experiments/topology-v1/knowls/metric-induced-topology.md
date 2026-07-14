---
title: "Metric-induced topology"
description: "The topology whose open sets are determined by a metric."
---

Let $(X,d)$ be a {{< knowl id="metric-space" text="metric space" >}}. The **metric-induced topology** on $X$ is the {{< knowl id="topology" text="topology" >}} in which a subset $U\subseteq X$ is an {{< knowl id="open-set" text="open set" >}} if and only if:

For every $x\in U$, there exists $\varepsilon>0$ such that $B_d(x,\varepsilon)\subseteq U$.

Equivalently, the collection of all {{< knowl id="open-ball" text="open balls" >}} forms a {{< knowl id="basis-of-a-topology" text="basis for this topology" >}}.

This is the standard way to pass from metric notions to topological ones; for example, continuity can be checked via {{< knowl id="continuity-via-open-sets" text="open sets" >}} in this topology.

**Examples:**
- On $\mathbb{R}^n$ with the Euclidean metric, the metric-induced topology is the usual “Euclidean topology.”
- For the discrete metric on $X$, every subset is open (the discrete topology).
