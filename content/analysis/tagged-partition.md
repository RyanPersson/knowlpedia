---
title: "Tagged partition"
description: "A partition together with a chosen sample point in each subinterval."
---

A **tagged partition** of $[a,b]$ is a pair $(P,T)$ where:
- $P:a=x_0<\cdots<x_n=b$ is a partition, and
- $T=(t_1,\dots,t_n)$ is a choice of **tags** with
  $$t_i\in[x_{i-1},x_i]\quad\text{for each }i=1,\dots,n.$$

Tagged partitions specify where a function is sampled to form Riemann sums. Different tagging conventions (e.g., left endpoints, right endpoints, midpoints) yield different approximations for finite partitions.

**Examples:**
- Left-endpoint tags: $t_i=x_{i-1}$ for all $i$.
- Right-endpoint tags: $t_i=x_i$ for all $i$.
- Midpoint tags: $t_i=\frac{x_{i-1}+x_i}{2}$.
