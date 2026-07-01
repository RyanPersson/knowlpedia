+++
id = "measure-theory/lp-space"
title = "L^p space"
kind = "knowl"
summary = "Measurable functions with finite Lp norm, identified up to equality almost everywhere."
aliases = ["lp-space", "L^p space"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/lp-space.md"
+++

An **$L^p$ space** (for $1\le p\le\infty$) associated to a [[measure-theory/measure-space|measure space]] $(X,\Sigma,\mu)$ is the collection
\[
L^p(X,\Sigma,\mu)
:= \{\, f:X\to\mathbb{R}\ \text{measurable} : \|f\|_p<\infty \,\}\big/\sim,
\]
where $\|f\|_p$ is the [[measure-theory/lp-norm|$L^p$ norm]] and $f\sim g$ means $f=g$ [[measure-theory/almost-everywhere|almost everywhere]] (i.e. [[measure-theory/ae-equality|a.e. equality]]).

The quotient by a.e. equality ensures that the $L^p$ norm is well-defined on $L^p(X,\Sigma,\mu)$. The cases $p=1$ and $p=\infty$ correspond to [[measure-theory/l1-function|$L^1$ functions]] and [[measure-theory/l-infinity-function|$L^\infty$ functions]], respectively.

**Examples:**
- On $((0,1),\mathcal{B},\lambda)$, the function $f(x)=x^{-1/2}$ lies in $L^1$ but not in $L^2$.
- On $(\mathbb{R},\mathcal{B},\lambda)$, the indicator function $\mathbf{1}_{[0,1]}$ lies in $L^p$ for every $1\le p\le\infty$, with $\|\mathbf{1}_{[0,1]}\|_p=1$ for $p<\infty$ and $\|\mathbf{1}_{[0,1]}\|_\infty=1$.
