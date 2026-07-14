---
title: "Uniformly continuous map"
description: "A map where one delta works uniformly for all points."
---

A **uniformly continuous map** between metric spaces $(X,d_X)$ and $(Y,d_Y)$ is a function $f:X\to Y$ such that for every $\varepsilon>0$ there exists $\delta>0$ with the property that whenever $d_X(x,y)<\delta$, one has $d_Y(f(x),f(y))<\varepsilon$ for all $x,y\in X$.

Uniform continuity strengthens {{{< knowl id="continuous-map" section="topology-core" text="continuity" >}}} by requiring a single $\delta$ to work uniformly over the whole domain. Uniformly continuous maps send {{{< knowl id="cauchy-sequence" text="Cauchy sequences" >}}} to Cauchy sequences, and {{{< knowl id="lipschitz-continuity" text="Lipschitz" >}}} maps are uniformly continuous.

**Examples:**
- On $\mathbb{R}$ with the usual metric, $f(x)=x^2$ is continuous but not uniformly continuous.
