---
title: "Uniform convergence of power series on compact sets"
description: "A power series converges uniformly (and absolutely) on every compact subset inside its interval of convergence."
---

**Uniform convergence on compacts:** Let $\sum_{n=0}^\infty a_n(x-x_0)^n$ be a {{< knowl id="power-series" text="power series" >}} with radius of convergence $R\in(0,\infty]$. If $K\subset (x_0-R,x_0+R)$ is compact, then the series converges absolutely and uniformly on $K$.

In particular, for every $r$ with $0<r<R$, the series converges absolutely and uniformly on the closed interval $[x_0-r,x_0+r]$.

This is the standard tool behind term-by-term operations on power series, such as {{< knowl id="term-by-term-integration" text="term-by-term integration" >}} and term-by-term differentiation, and can be proved using the {{< knowl id="weierstrass-m-test" text="Weierstrass M-test" >}}. It is a concrete instance of {{< knowl id="uniform-convergence-on-compact-sets" text="uniform convergence on compact sets" >}}.
