---
title: "Power series is analytic on its disk of convergence"
description: "Within its radius of convergence, a power series defines a function with derivatives given by termwise differentiation."
---

**Power series is analytic on its disk of convergence:** Let $\sum_{n=0}^\infty a_n (z-z_0)^n$ be a {{< knowl id="power-series" text="power series" >}} with radius of convergence $R>0$. Define
\[
f(z)=\sum_{n=0}^\infty a_n (z-z_0)^n
\quad\text{for }|z-z_0|<R.
\]
Then $f$ is complex differentiable on the open disk $\{z:|z-z_0|<R\}$, and for every $|z-z_0|<R$,
\[
f'(z)=\sum_{n=1}^\infty n\,a_n (z-z_0)^{n-1}.
\]

This is the fundamental analytic regularity of {{< knowl id="power-series" text="power series" >}} and is typically established via {{< knowl id="term-by-term-differentiation" text="term-by-term differentiation" >}} together with uniform convergence on compact subsets (see {{< knowl id="power-series-uniform-convergence-on-compacts" text="uniform convergence on compacts for power series" >}}).
