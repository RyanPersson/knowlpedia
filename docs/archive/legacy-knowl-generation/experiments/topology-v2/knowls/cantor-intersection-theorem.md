---
title: "Cantor intersection theorem"
description: "Nested closed sets with shrinking diameters in a complete metric space intersect in one point"
---

**Cantor intersection theorem:** Let $(X,d)$ be a {{< knowl id="complete-metric-space" text="complete metric space" >}} and let $(F_n)_{n\ge 1}$ be a sequence of nonempty {{< knowl id="closed-set" section="topology-core" text="closed sets" >}} with
\[
F_{n+1}\subseteq F_n \quad\text{for all }n,
\]
and with {{< knowl id="diameter" text="diameters" >}} satisfying $\operatorname{diam}(F_n)\to 0$. Then
\[
\bigcap_{n=1}^\infty F_n
\]
consists of exactly one point.

This is a metric-space generalization of the {{< knowl id="nested-interval-theorem" text="nested interval theorem" >}} and is often applied using nested sequences of {{< knowl id="closed-ball" text="closed balls" >}}.
