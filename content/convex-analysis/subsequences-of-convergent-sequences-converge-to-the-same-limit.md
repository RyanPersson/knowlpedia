---
title: "Subsequences of convergent sequences converge to the same limit"
description: "Any subsequence of a convergent sequence converges to the same limit"
---

**Proposition (Subsequence inherits the limit).**
Let $(X,d)$ be a {{< knowl id="metric-metric-space" text="metric space" >}}, and let $(x_n)$ be a sequence in $X$ that {{< knowl id="convergence-of-a-sequence" text="converges" >}} to $a\in X$. If $(x_{n_k})$ is a {{< knowl id="subsequence" text="subsequence" >}} of $(x_n)$, then $x_{n_k}\to a$.

**Context.** This is the basic "stability" property of limits under passing to subsequences. It is used constantly in compactness arguments and in extracting limits from sequences.

**Proof sketch.** Fix $\varepsilon>0$. Since $x_n\to a$, there exists $N$ such that $d(x_n,a)<\varepsilon$ for all $n\ge N$. Because $(n_k)$ is increasing and unbounded, there exists $K$ such that $n_k\ge N$ for all $k\ge K$. Then $d(x_{n_k},a)<\varepsilon$ for all $k\ge K$, so $x_{n_k}\to a$.

**Example.** In $\mathbb{R}$, if $x_n=1/n\to 0$, then any subsequence $x_{n_k}=1/n_k$ also converges to $0$.
