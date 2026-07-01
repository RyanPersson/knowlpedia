+++
id = "measure-theory/minkowski-inequality-lp"
title = "Minkowski inequality in Lp"
kind = "knowl"
summary = "Triangle inequality for the Lp norm."
aliases = ["minkowski-inequality-lp", "Minkowski inequality in Lp"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/minkowski-inequality-lp.md"
+++

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

This is the triangle inequality for the [[measure-theory/lp-norm|Lp norm]] and is what makes [[measure-theory/lp-space|Lp spaces]] into normed linear spaces for $1\le p\le\infty$. For $p=\infty$ it is the triangle inequality for the [[measure-theory/essential-supremum|essential supremum]] norm on [[measure-theory/l-infinity-function|essentially bounded functions]].
