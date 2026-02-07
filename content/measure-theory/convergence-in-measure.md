---
title: "Convergence in measure"
description: "A mode of convergence where the set of large errors has measure tending to zero."
---

A **convergence in measure** is the following notion of convergence for a {{< knowl id="sequence" section="shared-foundations" text="sequence" >}} $(f_n)$ of {{< knowl id="measurable-function" text="measurable functions" >}} on a {{< knowl id="measure-space" text="measure space" >}} $(X,\mathcal{A},\mu)$: we say that $f_n$ **converges in measure** to a measurable function $f$ if for every $\varepsilon>0$,
$$
\mu\big(\{x\in X:\ |f_n(x)-f(x)|>\varepsilon\}\big)\to 0
\quad\text{as }n\to\infty.
$$

This definition treats two functions as close whenever they differ by more than $\varepsilon$ only on a set of small measure. If $\mu(X)<\infty$, then {{< knowl id="convergence-almost-everywhere" text="convergence almost everywhere" >}} implies convergence in measure, but the converse can fail.

**Examples:**
- On $([0,1],\mathcal{B},\lambda)$ with {{< knowl id="lebesgue-measure" text="Lebesgue measure" >}} $\lambda$, the functions $f_n=\mathbf{1}_{[0,1/n]}$ satisfy $f_n\to 0$ in measure because $\lambda(\{|f_n|>1/2\})=\lambda([0,1/n])=1/n\to 0$.
- On $(\mathbb{R},\mathcal{B},\lambda)$, the functions $f_n=\mathbf{1}_{[n,n+1]}$ do **not** converge in measure to $0$ because for $\varepsilon=\tfrac12$ one has $\lambda(\{|f_n|>\varepsilon\})=\lambda([n,n+1])=1$ for all $n$.
