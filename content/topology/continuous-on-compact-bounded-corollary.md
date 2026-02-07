---
title: "Continuous function on a compact set is bounded"
description: "Continuous functions on compact domains have finite upper and lower bounds"
---

**Corollary**: Let $(X,d)$ be a {{< knowl id="compact-set" text="compact" >}} {{< knowl id="metric-space" text="metric space" >}} and let $f:X\to\mathbb{R}$ be {{< knowl id="continuity-on-a-set" section="real-analysis" text="continuous" >}}. Then $f$ is {{< knowl id="bounded-set" text="bounded" >}}: there exists $M<\infty$ such that $|f(x)|\le M$ for all $x\in X$.

**Connection to parent theorem**:
By the {{< knowl id="extreme-value-theorem" text="extreme value theorem" >}}, $f$ attains a {{< knowl id="maximum" section="real-analysis" text="maximum" >}} $M_+$ and a {{< knowl id="minimum" section="real-analysis" text="minimum" >}} $M_-$. Then $|f(x)|\le \max\{|M_+|,|M_-|\}$.
