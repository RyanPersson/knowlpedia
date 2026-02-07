---
title: "Zero derivative implies constant"
description: "If f' vanishes everywhere on an interval, the function is constant"
---

Let $f:[a,b]\to\mathbb{R}$ be {{< knowl id="continuity-on-a-set" text="continuous" >}} on $[a,b]$ and {{< knowl id="differentiability-one-variable" text="differentiable" >}} on $(a,b)$.

**Corollary**: If $f'(x)=0$ for all $x\in(a,b)$, then $f$ is constant on $[a,b]$.

**Connection to parent theorem**:
Apply the {{< knowl id="mean-value-theorem" text="mean value theorem" >}}: for any $x<y$, there exists $c\in(x,y)$ with $f(y)-f(x)=f'(c)(y-x)=0$.
