---
title: "Banach space"
description: "A complete normed vector space."
---

A **Banach space** is a {{< knowl id="normed-vector-space" text="normed vector space" >}} $(X,\|\cdot\|)$ such that every {{< knowl id="cauchy-sequence" section="topology" text="Cauchy sequence" >}} in $X$ converges (in the norm) to a point of $X$.

Equivalently, the metric $d(x,y)=\|x-y\|$ makes $X$ a {{< knowl id="complete-metric-space" section="topology" text="complete metric space" >}}. Completeness is a property of the metric induced by the {{< knowl id="norm" text="norm" >}}, and it is essential for many limit processes in analysis.

**Examples:**
- $\mathbb{R}^n$ with the {{< knowl id="euclidean-norm" text="Euclidean norm" >}} (indeed, $\mathbb{R}^n$ is Banach for any norm).
- The space $C([0,1])$ of continuous real-valued functions on $[0,1]$ with the sup norm $\|f\|_\infty=\sup_{x\in[0,1]}|f(x)|$.
