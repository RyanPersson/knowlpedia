---
title: "Compactness of graphs lemma"
description: "A graph of a continuous map over a compact domain is compact"
---

**Compactness of graphs lemma:** Let $X$ and $Y$ be {{{< knowl id="topological-space" section="topology-core" text="topological spaces" >}}}, let $K\subseteq X$ be {{{< knowl id="compact-set" text="compact" >}}}, and let $f\colon K\to Y$ be {{{< knowl id="continuous-map" section="topology-core" text="continuous" >}}}. Define the graph
\[
\Gamma(f)=\{(x,f(x)) : x\in K\}\subseteq X\times Y.
\]
If $X\times Y$ carries the {{{< knowl id="product-topology" section="topology-core" text="product topology" >}}}, then $\Gamma(f)$ is compact.

This follows by viewing $\Gamma(f)$ as the continuous image of $K$ under the map $x\mapsto (x,f(x))$ and applying {{{< knowl id="continuous-image-of-compact-set-is-compact" text="continuous image of compact is compact" >}}}.
