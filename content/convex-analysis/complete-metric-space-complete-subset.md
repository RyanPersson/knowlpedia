---
title: "Complete metric space and complete subset"
description: "A metric space is complete if every Cauchy sequence converges (in the space)"
---

A {{< knowl id="metric-metric-space" text="metric space" >}} $(X,d)$ is **complete** if every {{< knowl id="cauchy-sequence" section="topology" text="Cauchy sequence" >}} $(x_n)$ in $X$ {{< knowl id="convergence-of-a-sequence" text="converges" >}} to some point $x\in X$.

A subset $E\subset X$ is called **complete** if the restricted metric space $(E,d|_{E\times E})$ is complete; equivalently, every Cauchy sequence in $E$ converges to a point of $E$.

**Context.** Completeness is the property that "no limit points are missing." It is central in analysis (e.g., for existence theorems based on Cauchy sequences).

**Examples:**
- $(\mathbb{R}^k,d)$ with the usual Euclidean distance is complete (see {{< knowl id="completeness-of-rk" text="Completeness of R^k" >}}).
- The open interval $(0,1)\subset\mathbb{R}$ with the usual distance is *not* complete: the Cauchy sequence $x_n=1/n$ converges to $0\notin(0,1)$.
- If $X$ is complete and $E\subset X$ is {{< knowl id="closed-subset" text="closed" >}}, then $E$ is complete (see {{< knowl id="completeness-implies-closedness-closed-subsets-of-complete-spaces-are-complete" text="closed subsets of complete spaces are complete" >}}).
