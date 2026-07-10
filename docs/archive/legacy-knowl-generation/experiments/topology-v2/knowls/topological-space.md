---
title: "Topological space"
description: "A set equipped with a topology, specifying which subsets are open."
---

A **topological space** is a pair $(X,\tau)$ where $X$ is a {{< knowl id="set" section="shared-foundations" text="set" >}} and $\tau$ is a {{< knowl id="topology" text="topology" >}} on $X$.

The elements of $\tau$ are the {{< knowl id="open-set" text="open sets" >}} of $X$, and their complements are the {{< knowl id="closed-set" text="closed sets" >}}.

**Examples:**
- $\mathbb{R}$ with its usual topology (the one induced by the usual {{< knowl id="metric" section="topology-metric" text="metric" >}}).
- Any set $X$ with the discrete topology, where every {{< knowl id="subset" section="shared-foundations" text="subset" >}} is open.
- Any set $X$ with the indiscrete topology $\{\varnothing,X\}$, where only $\varnothing$ and $X$ are open.
