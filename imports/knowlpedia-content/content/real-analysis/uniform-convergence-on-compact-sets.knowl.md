+++
id = "real-analysis/uniform-convergence-on-compact-sets"
title = "Uniform convergence on compact sets"
kind = "knowl"
summary = "Uniform convergence on every compact subset of the domain."
aliases = ["uniform-convergence-on-compact-sets", "Uniform convergence on compact sets"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/uniform-convergence-on-compact-sets.md"
+++

A sequence of functions $(f_n):X\to Y$ (with $Y$ a [[topology/metric-space|metric space]]) **converges uniformly on compact sets** to a function $f:X\to Y$ if for every compact subset $K\subseteq X$, the restricted sequence $f_n|_K$ converges uniformly to $f|_K$ on $K$, i.e.
\[
\forall \varepsilon>0\ \exists N\ \forall n\ge N:\ \sup_{x\in K} d\bigl(f_n(x),f(x)\bigr)<\varepsilon.
\]

This is a localized version of [[real-analysis/uniform-convergence|uniform convergence]] obtained by first passing to a [[shared-foundations/restriction-of-a-function|restriction]] on each compact set. It is the natural convergence notion for families like [[real-analysis/power-series|power series]], as formalized by [[real-analysis/power-series-uniform-convergence-on-compacts|uniform convergence on compacts for power series]].

**Examples:**
- On $(-1,1)$, $f_n(x)=x^n$ converges uniformly on every closed interval $[-a,a]$ with $0<a<1$, hence uniformly on compact sets in $(-1,1)$.
- If $\sum_{n=0}^\infty a_n (x-x_0)^n$ has radius of convergence $R>0$, then its partial sums converge uniformly on compact subsets of $(x_0-R,x_0+R)$.
