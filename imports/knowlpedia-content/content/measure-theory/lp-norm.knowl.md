+++
id = "measure-theory/lp-norm"
title = "L^p norm"
kind = "knowl"
summary = "Norm from integrating the pth power of absolute value, or essential supremum when p is infinity."
aliases = ["lp-norm", "L^p norm"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/lp-norm.md"
+++

A **$L^p$ norm** on a [[measure-theory/measure-space|measure space]] $(X,\Sigma,\mu)$ (for $1\le p<\infty$) assigns to a [[measure-theory/measurable-function|measurable function]] $f:X\to\mathbb{R}$ the value
\[
\|f\|_p := \left(\int_X |f(x)|^p\,d\mu(x)\right)^{1/p},
\]
whenever the [[measure-theory/lebesgue-integral-nonnegative|Lebesgue integral of the nonnegative function]] $|f|^p$ is finite; here $|f(x)|$ uses the [[real-analysis/absolute-value|absolute value]]. For $p=\infty$ one defines
\[
\|f\|_\infty := \operatorname*{ess\,sup}_{x\in X} |f(x)|,
\]
using the [[measure-theory/essential-supremum|essential supremum]].

If $f$ and $g$ are [[measure-theory/ae-equality|equal almost everywhere]], then $\|f\|_p=\|g\|_p$, so the $L^p$ norm is naturally a norm on the corresponding [[measure-theory/lp-space|$L^p$ space]].

**Examples:**
- On $([0,1],\mathcal{B},\lambda)$, the constant function $f(x)=1$ satisfies $\|f\|_p=1$ for every $1\le p\le\infty$.
- On $([0,1],\mathcal{B},\lambda)$, for $f(x)=x$ one has $\|f\|_p=(1/(p+1))^{1/p}$ for $1\le p<\infty$, and $\|f\|_\infty=1$.
