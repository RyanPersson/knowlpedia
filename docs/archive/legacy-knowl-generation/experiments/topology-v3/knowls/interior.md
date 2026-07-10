---
title: "Interior"
description: "The largest open set contained in a given set."
---

The **interior** of a subset $A\subseteq X$ in a {{{< knowl id="topological-space" text="topological space" >}}} $X$ is the largest {{{< knowl id="open-set" text="open set" >}}} contained in $A$, denoted $\operatorname{int}(A)$, and defined by
\[
\operatorname{int}(A)=\bigcup\{U\subseteq X : U \text{ is open and } U\subseteq A\}.
\]
Equivalently, a point $x$ lies in $\operatorname{int}(A)$ if there exists a {{{< knowl id="neighborhood" text="neighborhood" >}}} of $x$ contained in $A$.

**Examples:**
- In $\mathbb{R}$ with the {{{< knowl id="metric-induced-topology" section="topology-metric" text="metric-induced topology" >}}} from the usual {{{< knowl id="metric" section="topology-metric" text="metric" >}}}, the interior of $[0,1]$ is $(0,1)$.
