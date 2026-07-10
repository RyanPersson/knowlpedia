---
title: "Compactness of graphs lemma"
description: "The graph of a continuous map on a compact set is compact in the product"
---

**Compactness of graphs lemma:** Let $X$ and $Y$ be {{< knowl id="topological-space" section="topology-core" text="topological spaces" >}}, let $K\subseteq X$ be {{< knowl id="compact-set" text="compact" >}}, and let $f:K\to Y$ be {{< knowl id="continuous-map" section="topology-core" text="continuous" >}}. Define the graph
\[
\Gamma_f=\{(x,f(x)) : x\in K\}\subseteq K\times Y,
\]
where $K\times Y$ has the {{< knowl id="product-topology" section="topology-core" text="product topology" >}}. Then $\Gamma_f$ is compact.

This follows by viewing $\Gamma_f$ as the continuous image of $K$ under the map $x\mapsto (x,f(x))$.
