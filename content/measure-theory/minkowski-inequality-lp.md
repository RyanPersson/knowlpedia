---
title: "Minkowski inequality in Lp"
description: "Triangle inequality for the Lp norm."
---

**Minkowski inequality:** Let $(X,\Sigma,\mu)$ be a measure space and let $1\le p\le\infty$. For all $f,g\in L^p(\mu)$,
\[
\|f+g\|_p \le \|f\|_p + \|g\|_p.
\]
In particular, when $p=\infty$ this reads
\[
\operatorname*{ess\,sup}_{x\in X}|f(x)+g(x)|
\le
\operatorname*{ess\,sup}_{x\in X}|f(x)|
+
\operatorname*{ess\,sup}_{x\in X}|g(x)|.
\]

This is the triangle inequality for the {{< knowl id="lp-norm" text="Lp norm" >}} and is what makes {{< knowl id="lp-space" text="Lp spaces" >}} into normed linear spaces for $1\le p\le\infty$. For $p=\infty$ it is the triangle inequality for the {{< knowl id="essential-supremum" text="essential supremum" >}} norm on {{< knowl id="l-infinity-function" text="essentially bounded functions" >}}.
