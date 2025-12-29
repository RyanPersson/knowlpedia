---
title: "Pointwise convergence"
description: "A sequence of functions f_n converges pointwise if f_n(x)→f(x) for each x."
---

Let $X$ be a {{< knowl id="set" text="set" >}} and let $(Y,d_Y)$ be a {{< knowl id="metric-space" text="metric space" >}}. A sequence of functions $f_n:X\to Y$ **converges pointwise** to a function $f:X\to Y$ if
$$\forall x\in X,\quad \lim_{n\to\infty} d_Y\bigl(f_n(x),f(x)\bigr)=0.$$
One writes $f_n(x)\to f(x)$ for each fixed $x$.

Pointwise convergence is the weakest common mode of convergence for functions. Many analytic properties ({{< knowl id="continuity-at-a-point" text="continuity" >}}, integrability, differentiation) are not preserved under pointwise limits without additional hypotheses. Compare with {{< knowl id="uniform-convergence-of-a-sequence-of-functions" text="uniform convergence" >}}.

**Examples:**
- On $[0,1]$, let $f_n(x)=x^n$. Then $f_n(x)\to f(x)$ pointwise, where $f(x)=0$ for $0\le x<1$ and $f(1)=1$.
- If $f_n(x)=\frac{1}{n}\sin x$ on $\mathbb{R}$, then $f_n\to 0$ pointwise (and uniformly).
- If $f_n=\mathbf{1}_{(0,1/n)}$ on $\mathbb{R}$, then $f_n\to 0$ pointwise, but the "mass" near $0$ illustrates why pointwise convergence can miss uniform control.
