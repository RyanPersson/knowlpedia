---
title: "Connectedness criteria in R"
description: "Equivalent characterizations of connected subsets of the real line."
---

**Connectedness criteria in $\mathbb{R}$:** Let $A\subseteq\mathbb{R}$, where $\mathbb{R}$ has its {{{< knowl id="metric-induced-topology" section="topology-metric" text="usual topology" >}}}. The following are equivalent:
- (1) $A$ is {{{< knowl id="connected-set" text="connected" >}}}.
- (2) (Order-convexity) For all $a,b\in A$ with $a<b$, one has $[a,b]\subseteq A$.
- (3) (No separating cut) There is no $c\in\mathbb{R}$ such that $A\subseteq(-\infty,c)\cup(c,\infty)$ and both $A\cap(-\infty,c)$ and $A\cap(c,\infty)$ are nonempty.

These criteria repackage {{{< knowl id="connected-subsets-of-r-are-intervals" text="the fact that connected subsets of $\mathbb{R}$ are intervals" >}}} into convenient testable forms.
