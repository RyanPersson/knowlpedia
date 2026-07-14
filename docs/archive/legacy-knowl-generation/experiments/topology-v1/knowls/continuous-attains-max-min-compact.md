---
title: "Continuous attains max and min on compact"
description: "A continuous real-valued function on a compact set reaches its largest and smallest values"
---

**Continuous attains max and min on compact**: Let $K$ be a {{< knowl id="compact-set" text="compact set" >}} and let $f:K\to \mathbb{R}$ be a {{< knowl id="continuous-map" text="continuous map" >}} (with $\mathbb{R}$ given its usual topology from {{< knowl id="euclidean-space" text="Euclidean space" >}}). Then there exist points $x_{\min},x_{\max}\in K$ such that for all $x\in K$,
$$
f(x_{\min}) \le f(x) \le f(x_{\max}).
$$

**Proof sketch**: By {{< knowl id="continuous-image-of-compact-set-is-compact" text="continuous images of compact sets are compact" >}}, the set $f(K)\subset\mathbb{R}$ is compact. In $\mathbb{R}$, compact sets are closed and bounded (a special case of the {{< knowl id="heine-borel-theorem" text="Heine–Borel theorem" >}}), so $f(K)$ contains its minimum and maximum values.

**Examples:**
- On $[0,1]$, the function $f(x)=x(1-x)$ has a maximum at $x=1/2$ and a minimum at $x=0$ or $x=1$.
- On $[0,2\pi]$, the function $f(x)=\sin x$ attains maximum $1$ and minimum $-1$.
