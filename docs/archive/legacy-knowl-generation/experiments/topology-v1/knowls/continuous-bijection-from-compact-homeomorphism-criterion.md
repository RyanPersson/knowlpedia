---
title: "Continuous bijection from compact homeomorphism criterion"
description: "A continuous bijection from a compact space to a Hausdorff space is a homeomorphism"
---

**Criterion**: Let $X$ be {{< knowl id="compact-set" text="compact" >}} and let $Y$ be a {{< knowl id="hausdorff-space" text="Hausdorff space" >}}. If $f:X\to Y$ is a {{< knowl id="continuous-map" text="continuous" >}} {{< knowl id="bijective-function" text="bijection" >}}, then $f$ is a {{< knowl id="homeomorphism" text="homeomorphism" >}}.

**Proof sketch**: It suffices to show $f^{-1}$ is continuous. Let $C\subseteq X$ be closed. Then $C$ is compact (closed subset of compact is compact), so $f(C)$ is compact. In a Hausdorff space, compact sets are closed, hence $f(C)$ is closed in $Y$. Therefore $f$ is a closed map, and a bijective closed map has continuous inverse.

This criterion is frequently used to prove two spaces are homeomorphic without explicitly writing down the inverse map.

**Examples:**
- A continuous bijection from a compact subset of $\mathbb{R}^n$ onto its image in $\mathbb{R}^m$ is a homeomorphism onto its image.
- The Hausdorff assumption is essential: without it, continuous bijections from compact spaces need not have continuous inverses.
