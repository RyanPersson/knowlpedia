---
title: "Uniform convergence on compact sets"
description: "Uniform convergence on every compact subset of the domain."
---

A sequence of functions $(f_n):X\to Y$ (with $Y$ a {{< knowl id="metric-space" section="topology" text="metric space" >}}) **converges uniformly on compact sets** to a function $f:X\to Y$ if for every compact subset $K\subseteq X$, the restricted sequence $f_n|_K$ converges uniformly to $f|_K$ on $K$, i.e.
\[
\forall \varepsilon>0\ \exists N\ \forall n\ge N:\ \sup_{x\in K} d\bigl(f_n(x),f(x)\bigr)<\varepsilon.
\]

This is a localized version of {{< knowl id="uniform-convergence" text="uniform convergence" >}} obtained by first passing to a {{< knowl id="restriction-of-a-function" section="shared-foundations" text="restriction" >}} on each compact set. It is the natural convergence notion for families like {{< knowl id="power-series" text="power series" >}}, as formalized by {{< knowl id="power-series-uniform-convergence-on-compacts" text="uniform convergence on compacts for power series" >}}.

**Examples:**
- On $(-1,1)$, $f_n(x)=x^n$ converges uniformly on every closed interval $[-a,a]$ with $0<a<1$, hence uniformly on compact sets in $(-1,1)$.
- If $\sum_{n=0}^\infty a_n (x-x_0)^n$ has radius of convergence $R>0$, then its partial sums converge uniformly on compact subsets of $(x_0-R,x_0+R)$.
