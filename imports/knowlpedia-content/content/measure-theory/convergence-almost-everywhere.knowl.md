+++
id = "measure-theory/convergence-almost-everywhere"
title = "Almost everywhere convergence"
kind = "knowl"
summary = "Convergence of functions pointwise outside a null set."
aliases = ["convergence-almost-everywhere", "Almost everywhere convergence"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/convergence-almost-everywhere.md"
+++

**Almost everywhere convergence** of a [[shared-foundations/sequence|sequence]] of measurable functions means the following: a sequence $(f_n)$ of [[measure-theory/measurable-function|measurable functions]] on a [[measure-theory/measure-space|measure space]] $(X,\Sigma,\mu)$ **converges almost everywhere** to a function $f$ if there exists a [[measure-theory/null-set|null set]] $N\subseteq X$ such that for every $x\in X\setminus N$ the [[real-analysis/limit-of-a-sequence|limit of a sequence]] $f_n(x)\to f(x)$ holds as $n\to\infty$.
Equivalently,
\[
\mu\bigl(\{x\in X : f_n(x)\not\to f(x)\}\bigr)=0.
\]

Almost everywhere convergence is a central hypothesis in results such as the [[measure-theory/dominated-convergence-theorem|dominated convergence theorem]] and [[measure-theory/monotone-convergence-theorem|monotone convergence theorem]]. It is one of the standard modes of convergence alongside [[measure-theory/convergence-in-measure|convergence in measure]] and [[measure-theory/convergence-in-lp|convergence in Lp]].

**Examples:**
- On $([0,1],\mathcal{B},\lambda)$, the sequence $f_n(x)=x^n$ converges almost everywhere to $f(x)=0$ (the only exceptional point is $x=1$).
- On $((0,1),\mathcal{B},\lambda)$, the functions $f_n(x)=n\,\mathbf{1}_{(0,1/n)}(x)$ satisfy $f_n(x)\to 0$ almost everywhere, but $\|f_n\|_1=\int_0^1 f_n\,d\lambda=1$ for all $n$, so the convergence is not convergence in Lp when $p=1$.
