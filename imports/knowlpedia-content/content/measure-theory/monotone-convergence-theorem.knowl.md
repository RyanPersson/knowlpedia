+++
id = "measure-theory/monotone-convergence-theorem"
title = "Monotone convergence theorem"
kind = "knowl"
summary = "For an increasing sequence of nonnegative measurable functions, the integral of the limit equals the limit of the integrals."
aliases = ["monotone-convergence-theorem", "Monotone convergence theorem"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/monotone-convergence-theorem.md"
+++

**Monotone Convergence Theorem (Beppo Levi):** Let $(X,\Sigma,\mu)$ be a [[measure-theory/measure-space|measure space]] and let $(f_n)_{n\ge 1}$ be a [[shared-foundations/sequence|sequence]] of nonnegative [[measure-theory/measurable-function|measurable functions]] $f_n:X\to[0,\infty]$ such that $f_n(x)\le f_{n+1}(x)$ for all $x\in X$ and all $n$. Define $f(x)=\lim_{n\to\infty} f_n(x)$ (possibly $+\infty$). Then
\[
\int_X f\,d\mu \;=\; \lim_{n\to\infty}\int_X f_n\,d\mu,
\]
where the integrals are the (possibly infinite) [[measure-theory/lebesgue-integral-nonnegative|Lebesgue integrals of nonnegative functions]].

If the monotone increase and the pointwise limit hold only [[measure-theory/almost-everywhere|almost everywhere]], the conclusion is unchanged because modifying functions on a [[measure-theory/null-set|null set]] does not affect their integral (see [[measure-theory/ae-equality|a.e. equality]]). Along with [[measure-theory/fatous-lemma|Fatou's lemma]] and the [[measure-theory/dominated-convergence-theorem|dominated convergence theorem]], it is one of the main tools for exchanging limits and [[measure-theory/lebesgue-integral|Lebesgue integration]].
