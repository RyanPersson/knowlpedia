---
title: "Totally bounded set"
description: "A set that can be covered by finitely many ε-balls for every ε>0."
---

Let $(X,d)$ be a {{< knowl id="metric-space" text="metric space" >}} and let $E\subseteq X$. The set $E$ is **totally bounded** if for every $\varepsilon>0$ there exist points $x_1,\dots,x_N\in X$ such that
$$E \subseteq \bigcup_{j=1}^N B(x_j,\varepsilon)$$
(see {{< knowl id="open-ball" text="open ball" >}}).

Equivalently: for every $\varepsilon>0$, $E$ has a finite **$\varepsilon$-net**, i.e. a finite subset $F\subseteq X$ such that every point of $E$ is within distance $<\varepsilon$ of some $f\in F$.

Total boundedness is a "precompactness" condition: in a {{< knowl id="complete-metric-space" text="complete metric space" >}}, $E$ is relatively compact (its {{< knowl id="closure" text="closure" >}} is {{< knowl id="compact-set" text="compact" >}}) iff it is totally bounded.

**Examples:**
- In $\mathbb{R}^k$, every bounded set is totally bounded.
- The set $\mathbb{Z}\subset\mathbb{R}$ is not totally bounded: for $\varepsilon<1/2$, infinitely many $\varepsilon$-balls are needed.
- Any compact set is totally bounded.
