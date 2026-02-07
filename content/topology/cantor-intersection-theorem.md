---
title: "Cantor intersection theorem"
description: "Nested closed sets with diameters going to zero intersect in a single point in a complete metric space"
---

**Cantor intersection theorem:** Let $(X,d)$ be a {{< knowl id="complete-metric-space" text="complete metric space" >}} and let $(F_n)_{n\in\mathbb{N}}$ be a sequence of nonempty {{< knowl id="closed-set" text="closed sets" >}} with
1) $F_{n+1}\subseteq F_n$ for all $n$, and  
2) $\operatorname{diam}(F_n)\to 0$, where $\operatorname{diam}$ is the {{< knowl id="diameter" text="diameter" >}} in the metric $d$.

Then the intersection $\bigcap_{n\in\mathbb{N}} F_n$ consists of exactly one point.

This theorem is the metric-space analogue of the {{< knowl id="nested-interval-theorem" text="nested interval theorem" >}} and is a standard tool in fixed-point and completeness arguments.
