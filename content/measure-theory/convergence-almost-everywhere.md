---
title: "Almost everywhere convergence"
description: "Convergence of functions pointwise outside a null set."
---

**Almost everywhere convergence** of a {{< knowl id="sequence" section="shared-foundations" text="sequence" >}} of measurable functions means the following: a sequence $(f_n)$ of {{< knowl id="measurable-function" text="measurable functions" >}} on a {{< knowl id="measure-space" text="measure space" >}} $(X,\Sigma,\mu)$ **converges almost everywhere** to a function $f$ if there exists a {{< knowl id="null-set" text="null set" >}} $N\subseteq X$ such that for every $x\in X\setminus N$ the {{< knowl id="limit-of-a-sequence" section="real-analysis" text="limit of a sequence" >}} $f_n(x)\to f(x)$ holds as $n\to\infty$.
Equivalently,
\[
\mu\bigl(\{x\in X : f_n(x)\not\to f(x)\}\bigr)=0.
\]

Almost everywhere convergence is a central hypothesis in results such as the {{< knowl id="dominated-convergence-theorem" text="dominated convergence theorem" >}} and {{< knowl id="monotone-convergence-theorem" text="monotone convergence theorem" >}}. It is one of the standard modes of convergence alongside {{< knowl id="convergence-in-measure" text="convergence in measure" >}} and {{< knowl id="convergence-in-lp" text="convergence in Lp" >}}.

**Examples:**
- On $([0,1],\mathcal{B},\lambda)$, the sequence $f_n(x)=x^n$ converges almost everywhere to $f(x)=0$ (the only exceptional point is $x=1$).
- On $((0,1),\mathcal{B},\lambda)$, the functions $f_n(x)=n\,\mathbf{1}_{(0,1/n)}(x)$ satisfy $f_n(x)\to 0$ almost everywhere, but $\|f_n\|_1=\int_0^1 f_n\,d\lambda=1$ for all $n$, so the convergence is not convergence in Lp when $p=1$.
