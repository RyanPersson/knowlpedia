+++
id = "measure-theory/indicator-function"
title = "Indicator function"
kind = "knowl"
summary = "A function that equals 1 on a set and 0 outside it."
aliases = ["indicator-function", "Indicator function"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/indicator-function.md"
+++

An **indicator function** of a subset $A\subseteq X$ is the function $\mathbf 1_A:X\to\{0,1\}$ defined by $\mathbf 1_A(x)=1$ for $x\in A$ and $\mathbf 1_A(x)=0$ for $x\notin A$.

Indicator functions translate set operations into algebraic ones and are the basic building blocks of [[measure-theory/simple-function|simple functions]]. In a [[measure-theory/measurable-space|measurable space]] $(X,\Sigma)$, $\mathbf 1_A$ is [[measure-theory/measurable-function|measurable]] exactly when $A$ is a [[measure-theory/measurable-set|measurable set]] (with $\{0,1\}$ carrying its power-set sigma-algebra).

**Examples:**
- On $(\mathbb R,\mathcal B(\mathbb R))$, the indicator function $\mathbf 1_{(0,1)}$ of the open [[real-analysis/interval|interval]] $(0,1)$ is measurable.
- If $N$ is a [[measure-theory/null-set|null set]] in a measure space, then $\mathbf 1_N$ equals $0$ [[measure-theory/almost-everywhere|almost everywhere]].
