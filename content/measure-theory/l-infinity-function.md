---
title: "L-infinity function"
description: "A measurable function that is essentially bounded on a measure space."
---

A **$L^\infty$ function** on a {{< knowl id="measure-space" text="measure space" >}} $(X,\Sigma,\mu)$ is a {{< knowl id="measurable-function" text="measurable function" >}} $f:X\to\overline{\mathbb{R}}$ such that
\[
\|f\|_\infty := \operatorname*{ess\,sup}_{x\in X} |f(x)| < \infty.
\]
Here $\operatorname*{ess\,sup}$ denotes the {{< knowl id="essential-supremum" text="essential supremum" >}}, and $|f(x)|$ uses the {{< knowl id="absolute-value" section="real-analysis" text="absolute value" >}}.

If $f$ and $g$ are {{< knowl id="ae-equality" text="equal almost everywhere" >}}, then $\|f\|_\infty=\|g\|_\infty$, so “being in $L^\infty$” depends only on the function up to changes on a {{< knowl id="null-set" text="null set" >}}. The collection of such functions (modulo a.e. equality) is the $p=\infty$ case of an {{< knowl id="lp-space" text="$L^p$ space" >}}.

**Examples:**
- On $([0,1],\mathcal{B},\lambda)$, the function $f(x)=x$ is in $L^\infty$ and satisfies $\|f\|_\infty=1$.
- If $A$ is a {{< knowl id="measurable-set" text="measurable set" >}} in $X$, then the indicator function $\mathbf{1}_A$ is in $L^\infty$ and $\|\mathbf{1}_A\|_\infty\le 1$ (with $\|\mathbf{1}_A\|_\infty=0$ when $A$ is a {{< knowl id="null-set" text="null set" >}}).
