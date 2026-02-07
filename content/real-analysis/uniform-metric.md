---
title: "Uniform metric"
description: "A metric on bounded functions defined by the supremum of pointwise distances."
---

The **uniform metric** on a set of bounded real-valued functions on $X$ is defined by
\[
d_\infty(f,g)=\sup_{x\in X} |f(x)-g(x)|.
\]
Equivalently, $d_\infty(f,g)=\|f-g\|_\infty$ where $\|\cdot\|_\infty$ is the {{< knowl id="supremum-norm" text="supremum norm" >}}.

This is a {{< knowl id="metric" section="topology" text="metric" >}} on the space of bounded functions, and convergence with respect to $d_\infty$ is exactly {{< knowl id="uniform-convergence" text="uniform convergence" >}}. Many compactness and approximation results for functions are phrased in terms of this metric on {{< knowl id="space-of-continuous-functions" text="continuous functions" >}}.

**Examples:**
- On $[0,1]$, with $f(x)=x$ and $g(x)=0$, one has $d_\infty(f,g)=1$.
- On $[0,1]$, for $f_n(x)=x/n$, $d_\infty(f_n,0)=1/n\to 0$, so $f_n\to 0$ uniformly.
