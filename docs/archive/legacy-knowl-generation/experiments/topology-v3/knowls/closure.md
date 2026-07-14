---
title: "Closure"
description: "The smallest closed set containing a given set."
---

The **closure** of a subset $A\subseteq X$ in a {{{< knowl id="topological-space" text="topological space" >}}} $X$ is the smallest {{{< knowl id="closed-set" text="closed set" >}}} containing $A$, denoted $\overline{A}$, and defined by
\[
\overline{A}=\bigcap\{F\subseteq X : F \text{ is closed and } A\subseteq F\}.
\]
Equivalently, $x\in\overline{A}$ if every {{{< knowl id="neighborhood" text="neighborhood" >}}} of $x$ intersects $A$.

The closure operation is central to concepts like {{{< knowl id="dense-set" text="density" >}}} and {{{< knowl id="limit-point-accumulation-point-cluster-point" text="limit points" >}}}.

**Examples:**
- In $\mathbb{R}$ with the {{{< knowl id="metric-induced-topology" section="topology-metric" text="metric-induced topology" >}}} from the usual {{{< knowl id="metric" section="topology-metric" text="metric" >}}}, the closure of $(0,1)$ is $[0,1]$.
- In the same topology, the closure of $\mathbb{Q}$ is $\mathbb{R}$.
