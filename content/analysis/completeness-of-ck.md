---
title: "Completeness of C(K) under the sup norm"
description: "On a compact metric space K, the space of continuous functions is complete in the sup metric"
---

Let $(K,d)$ be a {{< knowl id="compact-set" text="compact" >}} {{< knowl id="metric-space" text="metric space" >}} and let $C(K,\mathbb{R})$ denote the set of {{< knowl id="continuous-function" text="continuous functions" >}} $f:K\to\mathbb{R}$.

Define the **{{< knowl id="sup-norm" text="sup norm" >}}** by
$
\|f\|_\infty=\sup_{x\in K}|f(x)|,
$
and the induced metric
$
d_\infty(f,g)=\|f-g\|_\infty=\sup_{x\in K}|f(x)-g(x)|.
$

**Theorem**: The metric space $\bigl(C(K,\mathbb{R}),d_\infty\bigr)$ is {{< knowl id="complete-metric-space" text="complete" >}}.

This is the basic Banach-space fact behind many compactness and approximation arguments: {{< knowl id="uniform-convergence" text="uniform" >}} {{< knowl id="cauchy-sequence" text="Cauchy" >}} sequences of continuous functions converge uniformly to a continuous function.

**Proof sketch**:
Let $(f_n)$ be Cauchy in $d_\infty$. Then for each fixed $x\in K$, the real sequence $(f_n(x))$ is Cauchy in $\mathbb{R}$, hence {{< knowl id="convergent-sequence" text="converges" >}}; define
$
f(x)=\lim_{n\to\infty} f_n(x).
$
The uniform Cauchy property implies uniform convergence $f_n\to f$, i.e. $\|f_n-f\|_\infty\to 0$. Since each $f_n$ is continuous and the convergence is uniform, $f$ is continuous ({{< knowl id="uniform-limit-of-continuous-is-continuous" text="uniform limit theorem" >}}). Thus $f\in C(K,\mathbb{R})$ and $f_n\to f$ in $d_\infty$.
