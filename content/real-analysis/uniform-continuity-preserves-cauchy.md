---
title: "Uniform continuity preserves Cauchy sequences"
description: "Uniformly continuous maps send Cauchy sequences to Cauchy sequences"
---

Let $(X,d_X)$ and $(Y,d_Y)$ be {{< knowl id="metric-space" section="topology" text="metric spaces" >}} and let $f:X\to Y$ be {{< knowl id="uniform-continuity" text="uniformly continuous" >}}.

**Proposition**: If $(x_n)$ is a {{< knowl id="cauchy-sequence" section="topology" text="Cauchy sequence" >}} in $X$, then $(f(x_n))$ is a Cauchy sequence in $Y$.

This is an important structural feature: uniform continuity is exactly the hypothesis needed to transport {{< knowl id="complete-metric-space" section="topology" text="completeness" >}} properties through a map.
