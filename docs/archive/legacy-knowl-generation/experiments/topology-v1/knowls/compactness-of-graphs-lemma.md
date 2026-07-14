---
title: "Compactness of graphs lemma"
description: "The graph of a continuous map over a compact set is compact in the product space"
---

**Compactness of graphs lemma**: Let $f:X\to Y$ be a {{< knowl id="continuous-map" text="continuous map" >}} between topological spaces, and let $K\subseteq X$ be {{< knowl id="compact-set" text="compact" >}}. Consider the graph
$$
\Gamma_f=\{(x,f(x)) : x\in K\} \subseteq K\times Y.
$$
When $K\times Y$ is equipped with the {{< knowl id="product-topology" text="product topology" >}} on the {{< knowl id="cartesian-product" text="Cartesian product" >}}, the set $\Gamma_f$ is compact.

**Proof sketch**: Define $g:K\to K\times Y$ by $g(x)=(x,f(x))$. The map $g$ is continuous (coordinate maps are continuous in the product topology). Then $\Gamma_f=g(K)$, so compactness follows from {{< knowl id="continuous-image-of-compact-set-is-compact" text="continuous images of compact sets are compact" >}}.

**Examples:**
- The graph of $f(x)=\sin x$ on $[0,2\pi]$ is a compact subset of $\mathbb{R}^2$.
- If $K$ is compact and $f$ is continuous into any space $Y$, then $\Gamma_f$ is compact even when $Y$ is not Hausdorff.
