---
title: "Good rate function"
description: "A rate function whose sublevel sets are compact."
---

A **good rate function** on a topological space $E$ is a {{< knowl id="rate-function" text="rate function" >}} $I:E\to[0,\infty]$ such that for every $\alpha<\infty$ the sublevel set
$$
K_\alpha=\{x\in E:\ I(x)\le \alpha\}
$$

is **compact** in $E$.

Good rate functions are the natural large-deviation analogue of coercive “energy” functionals: they ensure that the variational problems appearing in a {{< knowl id="large-deviation-principle" text="large deviation principle" >}} are attained on compact sets and interact well with {{< knowl id="exponential-tightness" text="exponential tightness" >}}. In metrizable settings (e.g. Polish spaces), goodness is often the key compactness hypothesis used to pass from bounds on nice sets to bounds on all Borel sets.

**Examples:**
- On $E=\mathbb R^d$, any function of the form $I(x)=\|x\|^2$ is good: the sets $\{x:\|x\|^2\le \alpha\}$ are closed and bounded, hence compact in $\mathbb R^d$.
- If $E$ is compact and $I$ is a rate function, then $I$ is automatically good because every closed subset of a compact space is compact.
