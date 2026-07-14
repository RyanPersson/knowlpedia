---
title: "Derived set"
description: "The set of all limit points of a subset."
---

The **derived set** of a subset $A\subseteq X$ in a {{< knowl id="topological-space" text="topological space" >}} is
\[
A'=\{\,x\in X : x \text{ is a limit point of } A\,\},
\]
where “limit point” is as in {{< knowl id="limit-point-accumulation-point-cluster-point" text="limit point" >}}.

One always has $\overline{A}=A\cup A'$, relating the derived set to the {{< knowl id="closure" text="closure" >}} of $A$. In a {{< knowl id="t1-space" section="topology-separation" text="T1 space" >}}, the derived set is closed.

**Examples:**
- In $\mathbb{R}$, if $A=\{1/n : n\in\mathbb{N}\}$ then $A'=\{0\}$.
- In $\mathbb{R}$, if $A=(0,1)$ then $A'=[0,1]$.
- In an indiscrete space with at least two points, the derived set of a singleton $\{x\}$ is $X\setminus\{x\}$.
