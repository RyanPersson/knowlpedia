---
title: "Partition of an interval"
description: "A finite increasing list a=x0<⋯<xn=b subdividing [a,b] into subintervals."
---

A **partition** of a closed {{< knowl id="interval" text="interval" >}} $[a,b]\subseteq\mathbb{R}$ is a finite set of points written in increasing order
$$P:\ a=x_0<x_1<\cdots<x_n=b.$$
The associated subintervals are $[x_{i-1},x_i]$ for $i=1,\dots,n$, and their lengths are $\Delta x_i:=x_i-x_{i-1}$.

Partitions are the indexing objects for {{< knowl id="riemann-sum" text="Riemann sums" >}}, {{< knowl id="upper-sum-riemann" text="upper" >}}/{{< knowl id="lower-sum-riemann" text="lower sums" >}}, and the definition of the {{< knowl id="riemann-integral" text="Riemann integral" >}}. See also {{< knowl id="refinement-of-a-partition" text="refinement" >}} and {{< knowl id="mesh-of-a-partition" text="mesh" >}}.

**Examples:**
- $P:\ 0<\tfrac12<1$ is a partition of $[0,1]$ with two subintervals.
- The uniform partition of $[0,1]$ into $n$ pieces is $x_i=i/n$.
- The trivial partition is $a=x_0<x_1=b$ (one subinterval).
