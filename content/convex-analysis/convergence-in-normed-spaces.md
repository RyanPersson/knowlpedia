---
title: "Convergence in normed spaces"
description: "A sequence converges if the norm of its difference to the limit goes to zero"
---

Let $(X,\|\cdot\|)$ be a {{< knowl id="norm-normed-vector-space" text="normed vector space" >}}.

A sequence $(x_n)$ in $X$ **converges** to $x\in X$ (in norm) if
$$
\|x_n-x\|\to 0 \quad \text{as } n\to\infty.
$$

Equivalently: for every $\varepsilon>0$ there exists $N$ such that $\|x_n-x\|<\varepsilon$ for all $n\ge N$.

**Context.** By {{< knowl id="norm-induces-a-metric-and-conversely" text="the metric induced by a norm" >}}, this is exactly {{< knowl id="convergence-of-a-sequence" text="convergence in the associated metric space" >}}.

**Examples:**
- In $\mathbb{R}^2$ with $\|\cdot\|_2$, the sequence $x_n=(1/n,0)$ converges to $(0,0)$.
- In $C([0,1])$ with $\|\cdot\|_\infty$, the functions $f_n(t)=t/n$ satisfy $\|f_n-0\|_\infty=1/n\to 0$, so $f_n\to 0$.
- A sequence may converge under one norm and not under another in infinite-dimensional spaces (choice of norm matters).
