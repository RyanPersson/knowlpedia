---
title: "Mean value estimate"
description: "A bound on the change in a function in terms of a bound on its derivative."
---

**Mean value estimate lemma:** Let $f:[a,b]\to\mathbb{R}$ be continuous on $[a,b]$ and {{< knowl id="differentiability-1d" text="differentiable" >}} on $(a,b)$. If there exists $M\ge 0$ such that $|f'(x)|\le M$ for all $x\in(a,b)$, then
$$
|f(b)-f(a)|\le M\,|b-a|.
$$

This is an immediate quantitative consequence of the {{< knowl id="mean-value-theorem" text="mean value theorem" >}} and is a standard step in results like {{< knowl id="bounded-derivative-implies-uniform-continuity" text="bounded derivative implies uniform continuity" >}}.
