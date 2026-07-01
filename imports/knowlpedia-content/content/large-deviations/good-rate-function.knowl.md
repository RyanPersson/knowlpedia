+++
id = "large-deviations/good-rate-function"
title = "Good rate function"
kind = "knowl"
summary = "A rate function whose sublevel sets are compact."
aliases = ["good-rate-function", "Good rate function"]
domains = ["large-deviations"]
legacy_source_path = "large-deviations/good-rate-function.md"
+++

A **good rate function** on a topological space $E$ is a [[large-deviations/rate-function|rate function]] $I:E\to[0,\infty]$ such that for every $\alpha<\infty$ the sublevel set
$$
K_\alpha=\{x\in E:\ I(x)\le \alpha\}
$$

is **compact** in $E$.

Good rate functions are the natural large-deviation analogue of coercive “energy” functionals: they ensure that the variational problems appearing in a [[large-deviations/large-deviation-principle|large deviation principle]] are attained on compact sets and interact well with [[large-deviations/exponential-tightness|exponential tightness]]. In metrizable settings (e.g. Polish spaces), goodness is often the key compactness hypothesis used to pass from bounds on nice sets to bounds on all Borel sets.

**Examples:**
- On $E=\mathbb R^d$, any function of the form $I(x)=\|x\|^2$ is good: the sets $\{x:\|x\|^2\le \alpha\}$ are closed and bounded, hence compact in $\mathbb R^d$.
- If $E$ is compact and $I$ is a rate function, then $I$ is automatically good because every closed subset of a compact space is compact.
