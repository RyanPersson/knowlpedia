+++
id = "real-analysis/power-series-analytic-on-disk"
title = "Power series is analytic on its disk of convergence"
kind = "knowl"
summary = "Within its radius of convergence, a power series defines a function with derivatives given by termwise differentiation."
aliases = ["power-series-analytic-on-disk", "Power series is analytic on its disk of convergence"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/power-series-analytic-on-disk.md"
+++

**Power series is analytic on its disk of convergence:** Let $\sum_{n=0}^\infty a_n (z-z_0)^n$ be a [[real-analysis/power-series|power series]] with radius of convergence $R>0$. Define
\[
f(z)=\sum_{n=0}^\infty a_n (z-z_0)^n
\quad\text{for }|z-z_0|<R.
\]
Then $f$ is complex differentiable on the open disk $\{z:|z-z_0|<R\}$, and for every $|z-z_0|<R$,
\[
f'(z)=\sum_{n=1}^\infty n\,a_n (z-z_0)^{n-1}.
\]

This is the fundamental analytic regularity of [[real-analysis/power-series|power series]] and is typically established via [[real-analysis/term-by-term-differentiation|term-by-term differentiation]] together with uniform convergence on compact subsets (see [[real-analysis/power-series-uniform-convergence-on-compacts|uniform convergence on compacts for power series]]).
