+++
id = "measure-theory/l-infinity-function"
title = "L-infinity function"
kind = "knowl"
summary = "A measurable function that is essentially bounded on a measure space."
aliases = ["l-infinity-function", "L-infinity function"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/l-infinity-function.md"
+++

A **$L^\infty$ function** on a [[measure-theory/measure-space|measure space]] $(X,\Sigma,\mu)$ is a [[measure-theory/measurable-function|measurable function]] $f:X\to\overline{\mathbb{R}}$ such that
\[
\|f\|_\infty := \operatorname*{ess\,sup}_{x\in X} |f(x)| < \infty.
\]
Here $\operatorname*{ess\,sup}$ denotes the [[measure-theory/essential-supremum|essential supremum]], and $|f(x)|$ uses the [[real-analysis/absolute-value|absolute value]].

If $f$ and $g$ are [[measure-theory/ae-equality|equal almost everywhere]], then $\|f\|_\infty=\|g\|_\infty$, so “being in $L^\infty$” depends only on the function up to changes on a [[measure-theory/null-set|null set]]. The collection of such functions (modulo a.e. equality) is the $p=\infty$ case of an [[measure-theory/lp-space|$L^p$ space]].

**Examples:**
- On $([0,1],\mathcal{B},\lambda)$, the function $f(x)=x$ is in $L^\infty$ and satisfies $\|f\|_\infty=1$.
- If $A$ is a [[measure-theory/measurable-set|measurable set]] in $X$, then the indicator function $\mathbf{1}_A$ is in $L^\infty$ and $\|\mathbf{1}_A\|_\infty\le 1$ (with $\|\mathbf{1}_A\|_\infty=0$ when $A$ is a [[measure-theory/null-set|null set]]).
