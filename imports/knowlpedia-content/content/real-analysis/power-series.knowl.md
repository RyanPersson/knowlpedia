+++
id = "real-analysis/power-series"
title = "Power series"
kind = "knowl"
summary = "A series in powers of (x minus a center), defining a function on an interval of convergence."
aliases = ["power-series", "Power series"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/power-series.md"
+++

A **power series** is a series of the form $\sum_{n=0}^\infty c_n (x-a)^n$ with real coefficients $c_n$ and a real center $a$.

There exists a number $R\in[0,\infty]$, called the radius of convergence, such that the series converges for $|x-a|<R$ and diverges for $|x-a|>R$ (the endpoint behavior at $|x-a|=R$ is decided separately). The radius can often be computed using the [[real-analysis/cauchy-hadamard-theorem|Cauchy–Hadamard theorem]].

**Examples:**
- The geometric power series $\sum_{n=0}^\infty x^n$ converges for $|x|<1$ and represents the function $\frac{1}{1-x}$ on that interval.
- The exponential series $\sum_{n=0}^\infty \frac{x^n}{n!}$ converges for every real $x$.
