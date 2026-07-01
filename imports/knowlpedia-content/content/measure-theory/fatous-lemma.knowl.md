+++
id = "measure-theory/fatous-lemma"
title = "Fatou's lemma"
kind = "knowl"
summary = "For nonnegative measurable functions, the integral of the liminf is bounded by the liminf of the integrals."
aliases = ["fatous-lemma", "Fatou's lemma"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/fatous-lemma.md"
+++

**Fatou's lemma:** Let $(X,\Sigma,\mu)$ be a [[measure-theory/measure-space|measure space]] and let $(f_n)_{n\ge 1}$ be a sequence of nonnegative [[measure-theory/measurable-function|measurable functions]] $f_n:X\to[0,\infty]$. Then
\[
\int_X \Bigl(\liminf_{n\to\infty} f_n\Bigr)\,d\mu \;\le\; \liminf_{n\to\infty}\int_X f_n\,d\mu,
\]
where $\liminf_{n\to\infty} f_n$ is taken pointwise (and may take the value $+\infty$).

Fatou's lemma expresses a fundamental lower-semicontinuity property of the [[measure-theory/lebesgue-integral|Lebesgue integral]] and is closely related to the [[measure-theory/monotone-convergence-theorem|monotone convergence theorem]]. It is a standard ingredient in the [[measure-theory/dominated-convergence-theorem|dominated convergence theorem]] and many other limit arguments in measure theory.
