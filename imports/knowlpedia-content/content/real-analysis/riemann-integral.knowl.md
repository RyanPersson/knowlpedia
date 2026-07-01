+++
id = "real-analysis/riemann-integral"
title = "Riemann integral"
kind = "knowl"
summary = "The common value determined by Riemann sums when a function is integrable."
aliases = ["riemann-integral", "Riemann integral"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/riemann-integral.md"
+++

A **Riemann integral** of a [[real-analysis/riemann-integrable-function|Riemann integrable function]] $f:[a,b]\to\mathbb R$ is the number
\[
\int_a^b f(x)\,dx
\]
defined by
\[
\int_a^b f(x)\,dx=\sup_P L(f,P)=\inf_P U(f,P),
\]
where $L(f,P)$ and $U(f,P)$ are the [[real-analysis/lower-sum|lower]] and [[real-analysis/upper-sum|upper sums]] over all partitions $P$ of $[a,b]$.

This definition matches the limit of [[real-analysis/riemann-sum|Riemann sums]] along partitions of small mesh, and it is the starting point for results such as [[real-analysis/riemann-linearity|linearity]] and the [[real-analysis/fundamental-theorem-of-calculus-i|Fundamental Theorem of Calculus]].

**Examples:**
- If $f(x)=c$ is constant on $[a,b]$, then $\int_a^b f(x)\,dx=c(b-a)$.
- For $f(x)=x$ on $[0,1]$, one has $\int_0^1 x\,dx=\tfrac12$.
