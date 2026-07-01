+++
id = "real-analysis/uniform-limit-theorem"
title = "Uniform limit theorem"
kind = "knowl"
summary = "The uniform limit of continuous functions is continuous."
aliases = ["uniform-limit-theorem", "Uniform limit theorem"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/uniform-limit-theorem.md"
+++

The **uniform limit theorem** states: if \((f_n)\) is a sequence of [[topology/continuous-map|continuous functions]] \(f_n: X \to \mathbb{R}\) on a [[topology/metric-space|metric space]] \(X\), and \(f_n \to f\) [[real-analysis/uniform-convergence|uniformly]], then \(f\) is continuous.

## Statement
For metric spaces \(X\) and \(Y\): if \(f_n: X \to Y\) are continuous and \(f_n \rightrightarrows f\) uniformly (meaning \(\sup_{x \in X} d(f_n(x), f(x)) \to 0\)), then \(f\) is continuous.

## Counterexample for pointwise convergence
\(f_n(x) = x^n\) on \([0, 1]\) converges pointwise to a discontinuous limit:
$$
f(x) = \begin{cases} 0 & x \in [0,1) \\ 1 & x = 1 \end{cases}.
$$
The convergence is not uniform.
