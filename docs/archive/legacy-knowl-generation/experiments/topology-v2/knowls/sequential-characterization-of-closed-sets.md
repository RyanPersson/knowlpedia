---
title: "Sequential characterization of closed sets"
description: "In a metric space, a set is closed iff it contains limits of all convergent sequences in it"
---

**Sequential characterization of closed sets:** Let $(X,d)$ be a {{< knowl id="metric-space" section="topology-metric" text="metric space" >}} and let $F\subseteq X$. Then $F$ is {{< knowl id="closed-set" section="topology-core" text="closed" >}} if and only if whenever $(x_n)$ is a {{< knowl id="convergent-sequence" section="topology-metric" text="convergent sequence" >}} in $X$ with $x_n\in F$ for all $n$ and {{< knowl id="limit-of-a-sequence" section="topology-metric" text="limit" >}} $\lim_{n\to\infty} x_n = x$ exists in $X$, one has $x\in F$.

This criterion is often paired with the {{< knowl id="sequential-characterization-of-closure" text="sequential characterization of closure" >}}. In general {{< knowl id="topological-space" section="topology-core" text="topological spaces" >}} that are not metrizable, being closed need not be detectable purely from sequences.
