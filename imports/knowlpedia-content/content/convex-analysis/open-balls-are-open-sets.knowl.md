+++
id = "convex-analysis/open-balls-are-open-sets"
title = "Open balls are open"
kind = "knowl"
summary = "In any metric space, every open ball is an open set"
aliases = ["open-balls-are-open-sets", "Open balls are open"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/open-balls-are-open-sets.md"
+++

**Proposition.**
In any [[convex-analysis/metric-metric-space|metric space]], every open ball $B(x_0;r)$ is an [[convex-analysis/open-subset|open set]].

**Proof sketch.** Fix $a\in B(x_0;r)$. Let $\delta:=r-d(a,x_0)>0$. If $d(x,a)<\delta$, then by the triangle inequality
$$
d(x,x_0)\le d(x,a)+d(a,x_0)<\delta+d(a,x_0)=r,
$$

so $x\in B(x_0;r)$. Hence $B(a;\delta)\subset B(x_0;r)$, which is exactly openness.
