---
title: "Derived set"
description: "The set of all limit points of a subset."
---

The **derived set** of a subset $A\subseteq X$ in a {{< knowl id="topological-space" text="topological space" >}} is the set
\[
A'=\{x\in X : x \text{ is a limit point of } A\},
\]
where “limit point” is as in {{< knowl id="limit-point" text="limit point" >}}.

The derived set records the accumulation behavior of $A$, and it satisfies the basic relationship with {{< knowl id="closure" text="closure" >}}:
\[
\overline{A}=A\cup A'.
\]

**Examples:**
- In $\mathbb{R}$, if $A=\{1/n : n\in\mathbb{N}\}$ then $A'=\{0\}$.
- In $\mathbb{R}$, if $A=\mathbb{Z}$ then $A'=\varnothing$.
- In $\mathbb{R}$, if $A=(0,1)$ then $A'=[0,1]$.
