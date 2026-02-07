---
title: "Supremum norm"
description: "A norm on bounded functions given by the supremum of absolute values."
---

The **supremum norm** of a bounded function $f:X\to\mathbb{R}$ is
\[
\|f\|_\infty=\sup_{x\in X} |f(x)|.
\]
Here $\sup$ denotes the {{< knowl id="supremum" text="supremum" >}} and $|\cdot|$ is the {{< knowl id="absolute-value" text="absolute value" >}}.

The supremum norm is the standard way to measure uniform size of functions and underlies the {{< knowl id="uniform-metric" text="uniform metric" >}}. On many domains of interest (for example, a closed interval), continuous functions lie in the {{< knowl id="space-of-continuous-functions" text="space of continuous functions" >}} and are bounded, so $\|\cdot\|_\infty$ is finite.

**Examples:**
- For $f(x)=\sin x$ on $\mathbb{R}$, $\|f\|_\infty=1$.
- For $f(x)=x^2$ on $[-1,1]$, $\|f\|_\infty=1$ (the maximum is attained at $x=\pm 1$).
