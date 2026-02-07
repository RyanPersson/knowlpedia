---
title: "Measure space"
description: "A measurable space equipped with a measure."
---

A **measure space** is a triple $(X,\Sigma,\mu)$ where $(X,\Sigma)$ is a {{< knowl id="measurable-space" text="measurable space" >}} and $\mu$ is a {{< knowl id="measure" text="measure" >}} on $\Sigma$.

Measure spaces provide the basic setting for integration, convergence theorems, and statements that hold {{< knowl id="almost-everywhere" text="almost everywhere" >}} rather than pointwise.

**Examples:**
- For any set $X$, $(X,\mathcal P(X),\mu)$ with $\mu$ the counting measure is a measure space.
- On the unit {{< knowl id="interval" section="real-analysis" text="interval" >}} $[0,1]$, the triple $([0,1],\mathcal B([0,1]),\lambda)$ (Borel sets with a Lebesgue-type length measure $\lambda$) is a standard measure space used in probability and analysis.
