---
title: "Connectedness criteria in R"
description: "Equivalent ways to test whether a subset of the real line is connected"
---

**Connectedness criteria in $\mathbb{R}$:** Let $A\subseteq \mathbb{R}$ with the {{< knowl id="subspace-topology" section="topology-core" text="subspace topology" >}}. The following are equivalent:
- $A$ is {{< knowl id="connected-set" text="connected" >}}.
- $A$ has the interval property: if $a,b\in A$ and $a<b$, then every $t$ with $a<t<b$ lies in $A$.
- There is no real number $c$ such that both $A\cap(-\infty,c)$ and $A\cap(c,\infty)$ are nonempty and $A\subseteq (-\infty,c)\cup(c,\infty)$ (equivalently: $A$ has no “gap” at a point).

These equivalences summarize the content of {{< knowl id="connected-subsets-of-r-are-intervals" text="connected subsets of R are intervals" >}} in a form that is convenient for checking examples.
