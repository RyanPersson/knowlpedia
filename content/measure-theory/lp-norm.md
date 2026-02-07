---
title: "L^p norm"
description: "Norm from integrating the pth power of absolute value, or essential supremum when p is infinity."
---

A **$L^p$ norm** on a {{< knowl id="measure-space" text="measure space" >}} $(X,\Sigma,\mu)$ (for $1\le p<\infty$) assigns to a {{< knowl id="measurable-function" text="measurable function" >}} $f:X\to\mathbb{R}$ the value
\[
\|f\|_p := \left(\int_X |f(x)|^p\,d\mu(x)\right)^{1/p},
\]
whenever the {{< knowl id="lebesgue-integral-nonnegative" text="Lebesgue integral of the nonnegative function" >}} $|f|^p$ is finite; here $|f(x)|$ uses the {{< knowl id="absolute-value" section="real-analysis" text="absolute value" >}}. For $p=\infty$ one defines
\[
\|f\|_\infty := \operatorname*{ess\,sup}_{x\in X} |f(x)|,
\]
using the {{< knowl id="essential-supremum" text="essential supremum" >}}.

If $f$ and $g$ are {{< knowl id="ae-equality" text="equal almost everywhere" >}}, then $\|f\|_p=\|g\|_p$, so the $L^p$ norm is naturally a norm on the corresponding {{< knowl id="lp-space" text="$L^p$ space" >}}.

**Examples:**
- On $([0,1],\mathcal{B},\lambda)$, the constant function $f(x)=1$ satisfies $\|f\|_p=1$ for every $1\le p\le\infty$.
- On $([0,1],\mathcal{B},\lambda)$, for $f(x)=x$ one has $\|f\|_p=(1/(p+1))^{1/p}$ for $1\le p<\infty$, and $\|f\|_\infty=1$.
