---
title: "T0 space"
description: "A topological space where any two distinct points are distinguished by an open set."
---

A **$T_0$ space** is a {{{< knowl id="topological-space" section="topology-core" text="topological space" >}}} $X$ such that for any distinct points $x\neq y$ in $X$ there exists an {{{< knowl id="open-set" section="topology-core" text="open set" >}}} $U$ with exactly one of $x,y$ in $U$.

This is the weakest of the standard separation axioms: every {{{< knowl id="t1-space" text="T1 space" >}}} is $T_0$. Equivalently, $X$ is $T_0$ if and only if for distinct $x\neq y$ the {{{< knowl id="closure" section="topology-core" text="closures" >}}} of $\{x\}$ and $\{y\}$ are different.

**Examples:**
- The Sierpiński space $X=\{0,1\}$ with topology $\{\varnothing,\{1\},X\}$ is $T_0$ but not $T_1$.
