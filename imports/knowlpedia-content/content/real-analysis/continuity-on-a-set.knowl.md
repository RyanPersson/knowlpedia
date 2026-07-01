+++
id = "real-analysis/continuity-on-a-set"
title = "Continuity on a set"
kind = "knowl"
summary = "A function is continuous on a set if it is continuous at every point of that set."
aliases = ["continuity-on-a-set", "Continuity on a set"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/continuity-on-a-set.md"
+++

Let \(f:(X,d_X)\to(Y,d_Y)\) be a function between metric spaces, and let \(A\subseteq X\).
We say \(f\) is **continuous on \(A\)** if \(f\) is [[real-analysis/continuity-at-a-point|continuous at every point]] \(a\in A\) (equivalently, the restriction \(f|_A:A\to Y\) is continuous).

Spelled out: for every \(a\in A\) and every \(\varepsilon>0\), there exists \(\delta>0\) such that for all \(x\in A\),
\[
d_X(x,a)<\delta \quad\Rightarrow\quad d_Y\!\bigl(f(x),f(a)\bigr)<\varepsilon.
\]

Equivalent viewpoints (metric spaces):
- **Sequential**: if \(x_n\in A\) and \(x_n\to a\), then \(f(x_n)\to f(a)\) (see [[real-analysis/limit-of-a-sequence|limit of a sequence]]).
- **Open-set**: for every open \(V\subseteq Y\), the preimage \(f^{-1}(V)\) is open in \(A\) (i.e., \(f^{-1}(V)=A\cap U\) for some open \(U\subseteq X\)).

Examples:
- Any polynomial \(p:\mathbb{R}\to\mathbb{R}\) is continuous on every \(A\subseteq\mathbb{R}\).
- \(f(x)=1/x\) is continuous on \((0,\infty)\) but not continuous on a set containing \(0\).

Connection: if \(f\) is differentiable (see [[real-analysis/derivative|derivative]]), then \(f\) is continuous on its domain.
