+++
id = "real-analysis/power-series-uniform-convergence-on-compacts"
title = "Uniform convergence of power series on compact sets"
kind = "knowl"
summary = "A power series converges uniformly (and absolutely) on every compact subset inside its interval of convergence."
aliases = ["power-series-uniform-convergence-on-compacts", "Uniform convergence of power series on compact sets"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/power-series-uniform-convergence-on-compacts.md"
+++

**Uniform convergence on compacts:** Let $\sum_{n=0}^\infty a_n(x-x_0)^n$ be a [[real-analysis/power-series|power series]] with radius of convergence $R\in(0,\infty]$. If $K\subset (x_0-R,x_0+R)$ is compact, then the series converges absolutely and uniformly on $K$.

In particular, for every $r$ with $0<r<R$, the series converges absolutely and uniformly on the closed interval $[x_0-r,x_0+r]$.

This is the standard tool behind term-by-term operations on power series, such as [[real-analysis/term-by-term-integration|term-by-term integration]] and term-by-term differentiation, and can be proved using the [[real-analysis/weierstrass-m-test|Weierstrass M-test]]. It is a concrete instance of [[real-analysis/uniform-convergence-on-compact-sets|uniform convergence on compact sets]].
