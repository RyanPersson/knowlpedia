---
title: "Complete metric space"
description: "A metric space in which every Cauchy sequence converges to a point in the space."
---

A {{< knowl id="metric-space" text="metric space" >}} $(X,d)$ is **complete** if every {{< knowl id="cauchy-sequence" text="Cauchy sequence" >}} in $X$ {{< knowl id="convergent-sequence" text="converges" >}} to a limit in $X$. Formally:
$$
\forall (x_n)\subseteq X,\ \Bigl[(x_n)\ \text{Cauchy}\ \Rightarrow\ \exists x\in X\ \text{with}\ x_n\to x\Bigr].
$$

Completeness is a core structural property in analysis: it is needed for many fixed-point and category arguments and is the metric analogue of completeness of $\mathbb{R}$ as an ordered field.

**Examples:**
- $(\mathbb{R},|x-y|)$ is complete.
- $(\mathbb{Q},|x-y|)$ is not complete.
- Any closed subset of a complete metric space is complete (with the induced metric).
