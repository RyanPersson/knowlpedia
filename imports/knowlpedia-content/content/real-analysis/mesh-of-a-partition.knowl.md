+++
id = "real-analysis/mesh-of-a-partition"
title = "Mesh of a partition"
kind = "knowl"
summary = "The length of the longest subinterval in a partition."
aliases = ["mesh-of-a-partition", "Mesh of a partition"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/mesh-of-a-partition.md"
+++

A **mesh of a partition** $P=\{x_0,\dots,x_n\}$ of $[a,b]$ is the number
\[
\|P\|=\max_{1\le i\le n}(x_i-x_{i-1}).
\]
For a [[real-analysis/tagged-partition|tagged partition]], the mesh depends only on the underlying partition $P$.

The mesh quantifies how “fine” a partition is; limits in the definitions of the [[real-analysis/riemann-integral|Riemann integral]] and the [[real-analysis/riemann-stieltjes-integral|Riemann–Stieltjes integral]] are taken as $\|P\|\to 0$.

**Examples:**
- The uniform partition of $[0,1]$ into $n$ equal pieces has mesh $\|P\|=1/n$.
- For $P=\{0,0.9,1\}$, the mesh is $\|P\|=0.9$.
