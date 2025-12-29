---
title: "Weighted arithmetic–geometric mean inequality"
description: "For a,b≥0 and θ∈(0,1): a^θ b^(1−θ) ≤ θa+(1−θ)b"
---

**Proposition (Weighted AM–GM).**
For all $a,b\ge 0$ and all $\theta\in(0,1)$,
$$
a^\theta b^{1-\theta}\le \theta a+(1-\theta)b.
$$

**Context.** This inequality can be derived from convexity of the function $x\mapsto -\ln x$ on $(0,\infty)$ and is used to prove Hölder-type inequalities.

**Proof sketch.** Assume $a,b>0$. Convexity of $-\ln$ implies
$$
-\ln(\theta a+(1-\theta)b)\le -\theta\ln(a)-(1-\theta)\ln(b).
$$
Exponentiating yields $\theta a+(1-\theta)b\ge a^\theta b^{1-\theta}$. The cases $a=0$ or $b=0$ follow by continuity or direct inspection.

**Example.** With $\theta=\tfrac12$, this becomes $\sqrt{ab}\le \tfrac{a+b}{2}$.
