---
title: "Open and closed balls"
description: "Basic neighborhoods defined by a metric"
---

Let $(X,d)$ be a {{< knowl id="metric-metric-space" text="metric space" >}}, let $x_0\in X$, and let $r>0$.

- The **open ball** of center $x_0$ and radius $r$ is
  $$
  B(x_0;r):=\{x\in X\mid d(x,x_0)<r\}.
  $$
- The **closed ball** of center $x_0$ and radius $r$ is
  $$
  B'(x_0;r):=\{x\in X\mid d(x,x_0)\le r\}.
  $$

Open balls generate the topology of the metric space: a set is {{< knowl id="open-subset" text="open" >}} iff it contains an open ball around each of its points.

**Examples:**
- In $\mathbb{R}$ with $d(x,y)=|x-y|$, $B(x_0;r)=(x_0-r,x_0+r)$ and $B'(x_0;r)=[x_0-r,x_0+r]$.
- In the discrete metric, $B(x_0;r)=\{x_0\}$ whenever $0<r\le 1$.
