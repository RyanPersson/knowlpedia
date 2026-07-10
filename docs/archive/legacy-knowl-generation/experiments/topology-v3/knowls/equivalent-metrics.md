---
title: "Equivalent metrics"
description: "Two metrics that generate the same topology on a set."
---

Two metrics $d$ and $d'$ on the same set $X$ are **equivalent metrics** if they induce the same {{{< knowl id="metric-induced-topology" text="metric-induced topology" >}}} on $X$, i.e. they generate the same collection of {{{< knowl id="open-set" section="topology-core" text="open sets" >}}}.

Equivalently, $d$ and $d'$ are equivalent precisely when they give the same notion of {{{< knowl id="continuous-map" section="topology-core" text="continuity" >}}} (and hence the same topological properties). Metric notions such as {{{< knowl id="bounded-set" text="boundedness" >}}} or {{{< knowl id="complete-metric-space" text="completeness" >}}} need not be preserved.

**Examples:**
- If $d$ is any metric on $X$, then $d'(x,y)=\min\{1,d(x,y)\}$ is a metric equivalent to $d$. With $d'$, every subset of $X$ is bounded, even if $X$ was unbounded under $d$.
