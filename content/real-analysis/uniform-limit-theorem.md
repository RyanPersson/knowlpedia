---
title: "Uniform limit theorem"
description: "The uniform limit of continuous functions is continuous."
---

The **uniform limit theorem** states: if \((f_n)\) is a sequence of {{< knowl id="continuous-map" section="topology" text="continuous functions" >}} \(f_n: X \to \mathbb{R}\) on a {{< knowl id="metric-space" section="topology" text="metric space" >}} \(X\), and \(f_n \to f\) {{< knowl id="uniform-convergence" text="uniformly" >}}, then \(f\) is continuous.

## Statement
For metric spaces \(X\) and \(Y\): if \(f_n: X \to Y\) are continuous and \(f_n \rightrightarrows f\) uniformly (meaning \(\sup_{x \in X} d(f_n(x), f(x)) \to 0\)), then \(f\) is continuous.

## Counterexample for pointwise convergence
\(f_n(x) = x^n\) on \([0, 1]\) converges pointwise to a discontinuous limit:
$$
f(x) = \begin{cases} 0 & x \in [0,1) \\ 1 & x = 1 \end{cases}.
$$
The convergence is not uniform.
