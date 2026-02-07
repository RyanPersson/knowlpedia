---
title: "Total variation"
description: "The supremum of sums of absolute increments over all partitions."
---

A **total variation** of a function $\alpha:[a,b]\to\mathbb R$ on $[a,b]$ is the number
\[
V_a^b(\alpha)=\sup_P \sum_{i=1}^n |\alpha(x_i)-\alpha(x_{i-1})|,
\]
where the supremum is taken over all {{< knowl id="partition-of-an-interval" text="partitions" >}} $P=\{x_0,\dots,x_n\}$ of $[a,b]$.

Total variation measures how much $\alpha$ accumulates change along the interval and is the defining quantity for a {{< knowl id="bounded-variation-function" text="function of bounded variation" >}}. For {{< knowl id="monotone-function" text="monotone" >}} functions it reduces to the net change.

**Examples:**
- If $\alpha$ is increasing on $[a,b]$, then $V_a^b(\alpha)=\alpha(b)-\alpha(a)$.
- For $\alpha(x)=\sin x$ on $[0,2\pi]$, one has $V_0^{2\pi}(\alpha)=4$.
