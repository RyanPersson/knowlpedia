---
title: "Monotone sequence of functions"
description: "A sequence of functions that is monotone at each point of the domain."
---

A sequence of real-valued functions $(f_n)$ on a set $X$ is a **monotone increasing sequence of functions** if
\[
f_n(x)\le f_{n+1}(x)\quad \text{for all } x\in X \text{ and all } n,
\]
and it is **monotone decreasing** if $f_n(x)\ge f_{n+1}(x)$ for all $x$ and $n$. Equivalently, for each fixed $x\in X$, the numerical sequence $(f_n(x))$ is a {{< knowl id="monotone-sequence" text="monotone sequence" >}}.

Monotone sequences of functions are typically studied together with {{< knowl id="pointwise-convergence" text="pointwise convergence" >}}, and on compact domains they feature in {{< knowl id="dinis-theorem" text="Dini's theorem" >}} (which upgrades certain monotone pointwise limits to {{< knowl id="uniform-convergence" text="uniform convergence" >}}).

**Examples:**
- On any $X\subseteq\mathbb{R}$, the functions $f_n(x)=x-\frac1n$ form a monotone increasing sequence (pointwise) with limit $f(x)=x$.
- On $[0,1]$, the functions $f_n(x)=x^n$ form a monotone decreasing sequence (pointwise) with pointwise limit $f(x)=0$ for $x<1$ and $f(1)=1$.
