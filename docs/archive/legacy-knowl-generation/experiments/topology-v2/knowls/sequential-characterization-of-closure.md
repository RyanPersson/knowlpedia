---
title: "Sequential characterization of closure"
description: "In a metric space, a point is in the closure of a set iff it is a limit of a sequence from the set"
---

**Sequential characterization of closure:** Let $(X,d)$ be a {{< knowl id="metric-space" section="topology-metric" text="metric space" >}}, let $A\subseteq X$, and let $x\in X$. Then $x$ lies in the {{< knowl id="closure" section="topology-core" text="closure" >}} $\overline{A}$ if and only if there exists a sequence $(a_n)$ with $a_n\in A$ for all $n$ such that $\lim_{n\to\infty} a_n = x$ (as a {{< knowl id="limit-of-a-sequence" section="topology-metric" text="limit of a sequence" >}}).

This is equivalent to the {{< knowl id="sequential-characterization-of-closed-sets" text="sequential characterization of closed sets" >}} by applying it to complements: a point fails to be in $\overline{A}$ exactly when it has an open neighborhood disjoint from $A$.

For example, in $\mathbb{R}$ with the usual metric, $0\in \overline{(0,1)}$ because the sequence $a_n=1/n$ lies in $(0,1)$ and converges to $0$.
