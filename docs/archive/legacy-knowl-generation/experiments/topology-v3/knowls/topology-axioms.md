---
title: "Topology axioms"
description: "The three closure properties that characterize a topology."
---

A collection $\tau$ of subsets of a set $X$ is a {{{< knowl id="topology" text="topology" >}}} on $X$ if it satisfies:

- $\varnothing \in \tau$ and $X \in \tau$.
- If $\{U_i\}_{i\in I}$ is any family of sets in $\tau$, then the {{{< knowl id="union" section="shared-foundations" text="union" >}}} $\bigcup_{i\in I} U_i$ lies in $\tau$.
- If $U_1,\dots,U_n \in \tau$, then the {{{< knowl id="intersection" section="shared-foundations" text="intersection" >}}} $U_1\cap\cdots\cap U_n$ lies in $\tau$.

The sets in $\tau$ are precisely the {{{< knowl id="open-set" text="open sets" >}}} of the resulting {{{< knowl id="topological-space" text="topological space" >}}}.
