+++
id = "measure-theory/essential-supremum"
title = "Essential supremum"
kind = "knowl"
summary = "Least upper bound of a measurable function after ignoring a null set."
aliases = ["essential-supremum", "Essential supremum"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/essential-supremum.md"
+++

An **essential supremum** of a [[measure-theory/measurable-function|measurable function]] $f:X\to\overline{\mathbb{R}}$ on a [[measure-theory/measure-space|measure space]] $(X,\Sigma,\mu)$ is the number
\[
\operatorname*{ess\,sup}_{x\in X} f(x)
:= \inf\Bigl\{M\in\mathbb{R} : f(x)\le M \text{ for }\mu\text{-almost every }x\in X\Bigr\}.
\]
Equivalently, $\operatorname*{ess\,sup} f$ is the [[real-analysis/infimum|infimum]] of all real numbers $M$ that are an upper bound for $f$ outside a [[measure-theory/null-set|null set]].

Unlike the pointwise [[real-analysis/supremum|supremum]], the essential supremum is unchanged if $f$ is modified on a null set; in particular it depends only on the [[measure-theory/ae-equality|a.e. equivalence class]] of $f$. This notion is used to define the $p=\infty$ case of the [[measure-theory/lp-norm|$L^p$ norm]].

**Examples:**
- On $([0,1],\mathcal{B},\lambda)$, for $f(x)=x$ one has $\operatorname*{ess\,sup} f=1$.
- On the same space, if $f(0)=1$ and $f(x)=0$ for $x\in(0,1]$, then $\sup f=1$ but $\operatorname*{ess\,sup} f=0$ since the exceptional point $\{0\}$ is a [[measure-theory/null-set|null set]].
