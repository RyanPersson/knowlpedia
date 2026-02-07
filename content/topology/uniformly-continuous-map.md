---
title: "Uniformly continuous map"
description: "A map between metric spaces where one delta works uniformly for all points for a given epsilon."
---

A **uniformly continuous map** between metric spaces $(X,d_X)$ and $(Y,d_Y)$ is a map $f\colon X\to Y$ such that for every $\varepsilon>0$ there exists $\delta>0$ with
\[
d_X(x,y)<\delta \implies d_Y\bigl(f(x),f(y)\bigr)<\varepsilon
\quad\text{for all } x,y\in X.
\]

Uniform continuity strengthens {{< knowl id="continuous-map" text="continuity" >}} by requiring $\delta$ to depend only on $\varepsilon$ (not on the point of $X$). It is implied by {{< knowl id="lipschitz-continuity" text="Lipschitz continuity" >}}, and it ensures that {{< knowl id="cauchy-sequence" text="Cauchy sequences" >}} are sent to Cauchy sequences.

**Examples:**
- The map $f(x)=\sin x$ from $\mathbb{R}$ to $\mathbb{R}$ is uniformly continuous.
- The map $f(x)=x^2$ on $\mathbb{R}$ is not uniformly continuous, but it is uniformly continuous on any bounded interval such as $[0,1]$.
