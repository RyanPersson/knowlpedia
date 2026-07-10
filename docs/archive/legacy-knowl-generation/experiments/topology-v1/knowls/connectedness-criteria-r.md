---
title: "Connectedness criteria in the real line"
description: "Equivalent practical tests for when a subset of the real line is connected"
---

**Connectedness criteria in the real line**: Let $A\subseteq\mathbb{R}$ (with the usual topology). The following are equivalent:

1. $A$ is {{< knowl id="connected-set" text="connected" >}}.
2. (No gaps) Whenever $a,b\in A$ with $a<b$ and $c\in\mathbb{R}$ satisfies $a<c<b$, then $c\in A$.
3. (Interval form) $A$ is an interval (possibly empty or a singleton).
4. (Order convexity) If $a,b\in A$ and $t\in[0,1]$, then $(1-t)a+tb\in A$.

This is a convenient restatement of {{< knowl id="connected-subsets-of-r-are-intervals" text="connected subsets of the real line are intervals" >}}. The same “no gaps” intuition also underlies the {{< knowl id="intermediate-value-property-topological" text="intermediate value property" >}} for continuous real-valued maps on connected spaces.

**Examples:**
- $[0,1]$ satisfies the no-gaps condition, hence is connected.
- $(0,1)\cup(2,3)$ fails the no-gaps condition (take $a=0.5$, $b=2.5$, $c=1.5$), hence is not connected.
