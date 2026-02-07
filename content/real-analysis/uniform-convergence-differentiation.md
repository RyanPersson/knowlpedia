---
title: "Uniform convergence and differentiation"
description: "If derivatives converge uniformly and one point converges, then the functions converge uniformly and the limit may be differentiated term by term."
---

**Uniform convergence and differentiation:** Let $f_n:[a,b]\to\mathbb{R}$ be continuous on $[a,b]$ and {{< knowl id="differentiability-1d" text="differentiable" >}} on $(a,b)$ for every $n$. Assume that the sequence of derivatives $f_n'$ converges {{< knowl id="uniform-convergence" text="uniformly" >}} on $(a,b)$ to a function $g$, and that there exists $x_0\in[a,b]$ such that the real sequence $(f_n(x_0))$ converges. Then $f_n$ converges uniformly on $[a,b]$ to a function $f$, the limit $f$ is differentiable on $(a,b)$, and
\[
f'(x)=g(x)\quad\text{for all }x\in(a,b).
\]

This provides a standard criterion for passing a limit through the {{< knowl id="derivative" text="derivative" >}} operator, complementing results like {{< knowl id="differentiability-implies-continuity" text="differentiability implies continuity" >}} and {{< knowl id="uniform-limit-of-continuous-is-continuous" text="uniform limits preserve continuity" >}}.
