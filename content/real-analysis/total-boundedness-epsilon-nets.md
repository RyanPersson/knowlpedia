---
title: "Total boundedness characterization via ε-nets"
description: "A set is totally bounded iff it has a finite ε-net for every ε>0"
---

Let $(X,d)$ be a {{< knowl id="metric-space" section="topology" text="metric space" >}} and let $E\subseteq X$.

An **$\varepsilon$-net** for $E$ is a finite set $\{x_1,\dots,x_N\}\subseteq X$ such that
$
E\subseteq \bigcup_{j=1}^N B(x_j,\varepsilon),
$
where $B(x,\varepsilon)$ denotes the {{< knowl id="open-ball" section="topology" text="open ball" >}} of radius $\varepsilon$ centered at $x$.

**Proposition**: The following are equivalent:
- $E$ is **{{< knowl id="totally-bounded-set" section="topology" text="totally bounded" >}}**, meaning: for every $\varepsilon>0$ there exist $x_1,\dots,x_N\in X$ such that $E\subseteq \bigcup_{j=1}^N B(x_j,\varepsilon)$.
- For every $\varepsilon>0$, $E$ admits a finite $\varepsilon$-net.

(These are the same statement in slightly different language; "$\varepsilon$-net" is the packaging.)

Total boundedness is stronger than {{< knowl id="bounded-set" section="topology" text="boundedness" >}} and is one of the two metric ingredients (the other is {{< knowl id="complete-metric-space" section="topology" text="completeness" >}}) that together characterize {{< knowl id="compact-set" section="topology" text="compactness" >}} in metric spaces.

**Examples:**
- The interval $[0,1]\subset\mathbb{R}$ is totally bounded: cover it by finitely many intervals of length $\varepsilon$.
- The set $\mathbb{Z}\subset\mathbb{R}$ is not totally bounded: for $\varepsilon<1/2$ the balls $B(n,\varepsilon)$ are disjoint, so no finite subcover exists.
