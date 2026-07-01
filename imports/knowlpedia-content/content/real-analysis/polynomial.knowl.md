+++
id = "real-analysis/polynomial"
title = "Polynomial"
kind = "knowl"
summary = "A finite linear combination of powers of a variable with real coefficients."
aliases = ["polynomial"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/polynomial.md"
+++

A **polynomial** (in one real variable) is a function $p:\mathbb{R}\to\mathbb{R}$ of the form
\[
p(x)=a_0+a_1x+a_2x^2+\cdots+a_n x^n
\]
for some integer $n\ge 0$ and coefficients $a_0,\dots,a_n\in\mathbb{R}$. If $a_n\ne 0$, the integer $n$ is the degree of $p$.

Polynomials are basic examples of smooth functions (they have [[real-analysis/higher-derivatives|derivatives of all orders]]) and they define continuous functions on any interval, so they sit inside the [[real-analysis/space-of-continuous-functions|space of continuous functions]] on that interval. Collections of polynomials often form a [[real-analysis/subalgebra-of-continuous-functions|subalgebra of continuous functions]].

**Examples:**
- $p(x)=x^3-2x+5$ is a polynomial of degree $3$.
- $p(x)=7$ is a constant polynomial (degree $0$), and $p(x)=0$ is the zero polynomial.
