---
title: "Totally bounded set"
description: "A set in a metric space that can be covered by finitely many small balls for every radius."
---

A **totally bounded set** is a subset $A\subseteq X$ of a {{< knowl id="metric-space" text="metric space" >}} $(X,d)$ such that for every $\varepsilon>0$ there exist points $x_1,\dots,x_n\in X$ with
\[
A \subseteq \bigcup_{k=1}^n B(x_k,\varepsilon),
\]
where $B(x_k,\varepsilon)$ is the {{< knowl id="open-ball" text="open ball" >}} of radius $\varepsilon$ around $x_k$.

Total boundedness is equivalent to the existence of finite {{< knowl id="epsilon-net" text="epsilon-nets" >}} at every scale, and (together with {{< knowl id="complete-metric-space" text="completeness" >}}) it characterizes {{< knowl id="compact-set" text="compactness" >}} in metric spaces.

**Examples:**
- In $\mathbb{R}$ with the usual metric, the interval $[0,1]$ is totally bounded.
- The set of integers $\mathbb{Z}\subseteq\mathbb{R}$ (usual metric) is not totally bounded.
