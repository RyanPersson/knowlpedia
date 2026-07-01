+++
id = "real-analysis/tagged-partition"
title = "Tagged partition"
kind = "knowl"
summary = "A partition together with a chosen sample point in each subinterval."
aliases = ["tagged-partition", "Tagged partition"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/tagged-partition.md"
+++

A **tagged partition** of $[a,b]$ is a [[real-analysis/partition-of-an-interval|partition]] $P=\{x_0,\dots,x_n\}$ together with a choice of points (tags) $t_i\in[x_{i-1},x_i]$ for each $i=1,\dots,n$. It is often denoted $(P,\{t_i\}_{i=1}^n)$.

Tagged partitions are the input data for a [[real-analysis/riemann-sum|Riemann sum]] and, more generally, for a [[real-analysis/riemann-stieltjes-integral|Riemann–Stieltjes sum]].

**Examples:**
- (Midpoint tags) For each $i$, take $t_i=\tfrac12(x_{i-1}+x_i)$.
- (Right-endpoint tags) For each $i$, take $t_i=x_i$.
