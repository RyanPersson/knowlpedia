+++
id = "real-analysis/fundamental-theorem-of-calculus-ii"
title = "Fundamental theorem of calculus II"
kind = "knowl"
summary = "A Riemann integral can be computed from any antiderivative."
aliases = ["fundamental-theorem-of-calculus-ii", "Fundamental theorem of calculus II"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/fundamental-theorem-of-calculus-ii.md"
+++

**Fundamental theorem of calculus II:** Let $a<b$ and let $f:[a,b]\to\mathbb{R}$ be a [[real-analysis/riemann-integrable-function|Riemann integrable function]]. Suppose $F:[a,b]\to\mathbb{R}$ is continuous on $[a,b]$, [[real-analysis/differentiability-1d|differentiable]] on $(a,b)$, and satisfies $F'(x)=f(x)$ for all $x\in(a,b)$. Then
$$
\int_a^b f(x)\,dx = F(b)-F(a).
$$

Combined with [[real-analysis/fundamental-theorem-of-calculus-i|fundamental theorem of calculus I]], this explains why differentiation rules can be used to evaluate definite [[real-analysis/riemann-integral|integrals]] via antiderivatives.
