+++
id = "real-analysis/cauchy-hadamard-theorem"
title = "Cauchy–Hadamard theorem"
kind = "knowl"
summary = "A formula for the radius of convergence of a power series using a limsup of nth roots of coefficients."
aliases = ["cauchy-hadamard-theorem", "Cauchy–Hadamard theorem"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/cauchy-hadamard-theorem.md"
+++

**Cauchy–Hadamard theorem:** For a [[real-analysis/power-series|power series]] $\sum_{n=0}^\infty a_n (x-x_0)^n$ (real or complex), define
\[
L=\limsup_{n\to\infty} |a_n|^{1/n}.
\]
Set the radius of convergence
\[
R=\frac{1}{L},
\]
with the conventions $1/0=\infty$ and $1/\infty=0$. Then:

- The series converges absolutely for $|x-x_0|<R$.
- The series diverges for $|x-x_0|>R$.

This result is an application of the [[real-analysis/root-test|root test]] to the terms $a_n(x-x_0)^n$ and is the standard way to compute the radius in practice.
