---
title: "Darboux's theorem"
description: "Derivatives satisfy the intermediate value property even when they are not continuous."
---

**Darboux's theorem:** Let $I\subseteq\mathbb{R}$ be an {{< knowl id="interval" text="interval" >}}, and let $f:I\to\mathbb{R}$ be {{< knowl id="differentiability-1d" text="differentiable" >}} on $I$. Then the derivative $f'$ has the intermediate value property: whenever $a<b$ are in $I$ and $y$ lies between $f'(a)$ and $f'(b)$, there exists $c\in(a,b)$ such that
$$
f'(c)=y.
$$

Thus $f'$ behaves like a function satisfying the {{< knowl id="intermediate-value-theorem" text="intermediate value theorem" >}}, even though $f'$ need not be a {{< knowl id="continuous-map" section="topology" text="continuous map" >}} and may have {{< knowl id="discontinuity-point" text="points of discontinuity" >}}.
