+++
id = "real-analysis/uniform-convergence-differentiation"
title = "Uniform convergence and differentiation"
kind = "knowl"
summary = "If derivatives converge uniformly and one point converges, then the functions converge uniformly and the limit may be differentiated term by term."
aliases = ["uniform-convergence-differentiation", "Uniform convergence and differentiation"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/uniform-convergence-differentiation.md"
+++

**Uniform convergence and differentiation:** Let $f_n:[a,b]\to\mathbb{R}$ be continuous on $[a,b]$ and [[real-analysis/differentiability-1d|differentiable]] on $(a,b)$ for every $n$. Assume that the sequence of derivatives $f_n'$ converges [[real-analysis/uniform-convergence|uniformly]] on $(a,b)$ to a function $g$, and that there exists $x_0\in[a,b]$ such that the real sequence $(f_n(x_0))$ converges. Then $f_n$ converges uniformly on $[a,b]$ to a function $f$, the limit $f$ is differentiable on $(a,b)$, and
\[
f'(x)=g(x)\quad\text{for all }x\in(a,b).
\]

This provides a standard criterion for passing a limit through the [[real-analysis/derivative|derivative]] operator, complementing results like [[real-analysis/differentiability-implies-continuity|differentiability implies continuity]] and [[real-analysis/uniform-limit-of-continuous-is-continuous|uniform limits preserve continuity]].
