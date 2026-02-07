---
title: "Term-by-term differentiation for power series"
description: "Inside the radius of convergence, a power series can be differentiated by differentiating each term."
---

**Term-by-term differentiation for power series:** Let $\sum_{n=0}^\infty a_n (x-x_0)^n$ be a {{< knowl id="power-series" text="power series" >}} with radius of convergence $R>0$, and define
\[
f(x)=\sum_{n=0}^\infty a_n (x-x_0)^n
\quad\text{for }|x-x_0|<R.
\]
Then $f$ is differentiable for $|x-x_0|<R$, and for every $|x-x_0|<R$,
\[
f'(x)=\sum_{n=1}^\infty n\,a_n (x-x_0)^{n-1}.
\]
The differentiated power series has the same radius of convergence $R$.

This theorem underlies the fact that power series define very smooth functions (see {{< knowl id="power-series-analytic-on-disk" text="power series is analytic on its disk of convergence" >}}) and is part of the broader toolkit of {{< knowl id="term-by-term-operations" text="term-by-term operations" >}} for power series.
