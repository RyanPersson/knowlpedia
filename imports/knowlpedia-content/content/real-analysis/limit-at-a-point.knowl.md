+++
id = "real-analysis/limit-at-a-point"
title = "Limit at a point"
kind = "knowl"
summary = "The epsilon-delta definition of the limit of a function as x approaches a."
aliases = ["limit-at-a-point", "Limit at a point"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/limit-at-a-point.md"
+++

A **limit at a point** for a [[shared-foundations/function|function]] $f:D\to\mathbb R$ (with $D\subseteq\mathbb R$) at a point $a\in\mathbb R$ is a number $L\in\mathbb R$ such that: for every $\varepsilon>0$ there exists $\delta>0$ with the property that whenever $x\in D$ and $0<|x-a|<\delta$, one has $|f(x)-L|<\varepsilon$. Typically one assumes that $a$ is a [[topology/limit-point|limit point]] of $D$.

The inequalities use the [[real-analysis/absolute-value|absolute value]] to measure distance on the real line. One-sided variants are captured by the [[real-analysis/one-sided-limit|one-sided limit]].

**Examples:**
- If $f(x)=x^2$, then $\lim_{x\to 2} f(x)=4$.
- If $g(x)=\begin{cases}1,&x>0\\-1,&x<0\end{cases}$ on $D=\mathbb R\setminus\{0\}$, then $\lim_{x\to 0} g(x)$ does not exist.
