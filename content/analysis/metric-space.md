---
title: "Metric space"
description: "A set equipped with a metric, used to define limits and continuity abstractly."
---

A **metric space** is a pair $(X,d)$ where $X$ is a {{< knowl id="set" text="set" >}} and $d$ is a {{< knowl id="metric" text="metric" >}} on $X$, i.e. a function $d:X\times X\to[0,\infty)$ satisfying positive definiteness, symmetry, and the triangle inequality.

Metric spaces generalize {{< knowl id="euclidean-space-rk" text="Euclidean spaces" >}} and provide the setting for "analysis without coordinates." Many results in real analysis extend to general metric spaces once stated in terms of $d$.

**Examples:**
- $(\mathbb{R},|x-y|)$ is a metric space.
- $(\mathbb{R}^k,\|x-y\|_2)$ is a metric space.
- Any set $X$ with the discrete metric is a metric space in which every subset is open.
