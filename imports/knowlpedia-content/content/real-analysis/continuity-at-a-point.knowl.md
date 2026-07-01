+++
id = "real-analysis/continuity-at-a-point"
title = "Continuity at a point"
kind = "knowl"
summary = "The epsilon-delta condition that a function preserves closeness near a given point."
aliases = ["continuity-at-a-point", "Continuity at a point"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/continuity-at-a-point.md"
+++

Let \(f:(X,d_X)\to(Y,d_Y)\) and let \(a\in X\).
We say \(f\) is **continuous at \(a\)** if for every \(\varepsilon>0\) there exists \(\delta>0\) such that for all \(x\in X\),
\[
d_X(x,a)<\delta \quad\Rightarrow\quad d_Y\!\bigl(f(x),f(a)\bigr)<\varepsilon.
\]

In words: points \(x\) sufficiently close to \(a\) must have images \(f(x)\) close to \(f(a)\).

Sequential characterization (metric spaces): \(f\) is continuous at \(a\) iff whenever \(x_n\to a\), we have \(f(x_n)\to f(a)\).
This reframes continuity using [[real-analysis/limit-of-a-sequence|limits of sequences]].

Examples:
- \(f(x)=x^2\) is continuous at every \(a\in\mathbb{R}\).
- The step function \(f(x)=\mathbf{1}_{(0,\infty)}(x)\) is not continuous at \(0\).

If \(f\) is continuous at every point of a set \(A\), then \(f\) is [[real-analysis/continuity-on-a-set|continuous on \(A\)]].
