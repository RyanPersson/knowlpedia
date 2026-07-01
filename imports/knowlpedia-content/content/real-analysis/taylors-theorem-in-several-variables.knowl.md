+++
id = "real-analysis/taylors-theorem-in-several-variables"
title = "Taylor's Theorem in several variables"
kind = "knowl"
summary = "Approximates a smooth multivariable function by a polynomial in a neighborhood of a point"
aliases = ["taylors-theorem-in-several-variables", "Taylor's Theorem in several variables"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/taylors-theorem-in-several-variables.md"
+++

**Taylor's Theorem (several variables, one standard form)**: Let $U\subseteq\mathbb{R}^n$ be open and let $f:U\to\mathbb{R}$ be of [[real-analysis/class-ck-map|class]] $C^{k+1}$ on a [[topology/neighborhood|neighborhood]] of $a\in U$. Using multi-index notation, there exists a remainder $R_k(h)$ such that for $h$ sufficiently small (with $a+h\in U$),
$
f(a+h)=\sum_{|\alpha|\le k}\frac{D^\alpha f(a)}{\alpha!}\,h^\alpha + R_k(h),
$
and
$
\frac{R_k(h)}{\|h\|^k}\to 0 \quad \text{as } h\to 0.
$
Here $\alpha=(\alpha_1,\dots,\alpha_n)$, $|\alpha|=\alpha_1+\cdots+\alpha_n$, $\alpha!=\alpha_1!\cdots \alpha_n!$, and $h^\alpha=h_1^{\alpha_1}\cdots h_n^{\alpha_n}$.

Taylor's theorem is the basis for local approximation, classification of [[real-analysis/critical-point|critical points]], and higher-order error bounds in multivariable calculus.
