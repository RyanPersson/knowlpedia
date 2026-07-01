+++
id = "real-analysis/upper-sum"
title = "Upper sum"
kind = "knowl"
summary = "A Riemann upper sum built from suprema on each subinterval."
aliases = ["upper-sum", "Upper sum"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/upper-sum.md"
+++

An **upper sum** of a bounded function $f:[a,b]\to\mathbb R$ with respect to a [[real-analysis/partition-of-an-interval|partition]] $P=\{x_0,\dots,x_n\}$ is the number
\[
U(f,P)=\sum_{i=1}^n M_i\,(x_i-x_{i-1}),
\]
where $M_i=\sup\{f(x):x\in[x_{i-1},x_i]\}$ is the [[real-analysis/supremum|supremum]] of $f$ on the $i$th subinterval.

Upper sums, together with [[real-analysis/lower-sum|lower sums]], give the standard criterion for a [[real-analysis/riemann-integrable-function|Riemann integrable function]]: upper and lower sums can be made arbitrarily close by choosing a suitable partition.

**Examples:**
- For $f(x)=x$ on $[0,1]$ and $P=\{0,\tfrac12,1\}$, one gets $U(f,P)=\tfrac12\cdot\tfrac12+1\cdot\tfrac12=\tfrac34$.
- If $f(x)=c$ is constant on $[a,b]$, then $U(f,P)=c(b-a)$ for every partition $P$.
