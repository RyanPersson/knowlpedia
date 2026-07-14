---
title: "Bounded set"
description: "A subset contained in a ball of some finite radius."
---

Let $(X,d)$ be a {{< knowl id="metric-space" text="metric space" >}} and let $A\subseteq X$. The set $A$ is **bounded** if there exist a point $x\in X$ and a number $R>0$ such that $A\subseteq \overline{B}_d(x,R)$, where $\overline{B}_d(x,R)$ is a {{< knowl id="closed-ball" text="closed ball" >}}.

Equivalently (when $A\neq\varnothing$), $A$ is bounded if and only if it has finite {{< knowl id="diameter" text="diameter" >}}. Boundedness is closely tied to compactness; for instance, {{< knowl id="compactness-implies-boundedness" text="compact sets are bounded" >}} in metric spaces.

**Examples:**
- Any closed ball $\overline{B}_d(x,R)$ is bounded.
- In $\mathbb{R}$ with the usual metric, the set $\{1,2,3,\dots\}$ is not bounded.
