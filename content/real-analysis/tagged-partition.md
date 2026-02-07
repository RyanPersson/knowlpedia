---
title: "Tagged partition"
description: "A partition together with a chosen sample point in each subinterval."
---

A **tagged partition** of $[a,b]$ is a {{< knowl id="partition-of-an-interval" text="partition" >}} $P=\{x_0,\dots,x_n\}$ together with a choice of points (tags) $t_i\in[x_{i-1},x_i]$ for each $i=1,\dots,n$. It is often denoted $(P,\{t_i\}_{i=1}^n)$.

Tagged partitions are the input data for a {{< knowl id="riemann-sum" text="Riemann sum" >}} and, more generally, for a {{< knowl id="riemann-stieltjes-integral" text="Riemann–Stieltjes sum" >}}.

**Examples:**
- (Midpoint tags) For each $i$, take $t_i=\tfrac12(x_{i-1}+x_i)$.
- (Right-endpoint tags) For each $i$, take $t_i=x_i$.
