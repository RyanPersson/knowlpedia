+++
id = "real-analysis/total-boundedness-epsilon-nets"
title = "Total boundedness characterization via ε-nets"
kind = "knowl"
summary = "A set is totally bounded iff it has a finite ε-net for every ε>0"
aliases = ["total-boundedness-epsilon-nets", "Total boundedness characterization via ε-nets"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/total-boundedness-epsilon-nets.md"
+++

Let $(X,d)$ be a [[topology/metric-space|metric space]] and let $E\subseteq X$.

An **$\varepsilon$-net** for $E$ is a finite set $\{x_1,\dots,x_N\}\subseteq X$ such that
$
E\subseteq \bigcup_{j=1}^N B(x_j,\varepsilon),
$
where $B(x,\varepsilon)$ denotes the [[topology/open-ball|open ball]] of radius $\varepsilon$ centered at $x$.

**Proposition**: The following are equivalent:
- $E$ is **[[topology/totally-bounded-set|totally bounded]]**, meaning: for every $\varepsilon>0$ there exist $x_1,\dots,x_N\in X$ such that $E\subseteq \bigcup_{j=1}^N B(x_j,\varepsilon)$.
- For every $\varepsilon>0$, $E$ admits a finite $\varepsilon$-net.

(These are the same statement in slightly different language; "$\varepsilon$-net" is the packaging.)

Total boundedness is stronger than [[topology/bounded-set|boundedness]] and is one of the two metric ingredients (the other is [[topology/complete-metric-space|completeness]]) that together characterize [[topology/compact-set|compactness]] in metric spaces.

**Examples:**
- The interval $[0,1]\subset\mathbb{R}$ is totally bounded: cover it by finitely many intervals of length $\varepsilon$.
- The set $\mathbb{Z}\subset\mathbb{R}$ is not totally bounded: for $\varepsilon<1/2$ the balls $B(n,\varepsilon)$ are disjoint, so no finite subcover exists.
