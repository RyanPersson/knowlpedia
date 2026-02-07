---
title: "Pointwise convergence"
description: "Convergence of a sequence of functions at each fixed point of the domain."
---

**Pointwise convergence** of a sequence of functions $(f_n)$ to a function $f$ on a set $X$ means: for every $x\in X$, the real sequence $(f_n(x))$ converges to $f(x)$, i.e.
\[
\forall x\in X,\quad \lim_{n\to\infty} f_n(x)=f(x).
\]

This is a basic mode of convergence for sequences of {{< knowl id="function" section="shared-foundations" text="functions" >}}, and it is weaker than {{< knowl id="uniform-convergence" text="uniform convergence" >}} (where one $N$ works simultaneously for all $x$). For each fixed $x$, pointwise convergence is just ordinary {{< knowl id="convergent-sequence" section="topology" text="convergence of a sequence" >}} in the codomain.

**Examples:**
- On $[0,1]$, $f_n(x)=x^n$ converges pointwise to the function $f(x)=0$ for $0\le x<1$ and $f(1)=1$.
- On $\mathbb{R}$, $f_n(x)=\sin(nx)/n$ converges pointwise to $0$ (indeed $|f_n(x)|\le 1/n$ for all $x$).
