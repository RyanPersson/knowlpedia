+++
id = "real-analysis/one-sided-limit"
title = "One-sided limit"
kind = "knowl"
summary = "A limit taken from the left or from the right of a point."
aliases = ["one-sided-limit", "One-sided limit"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/one-sided-limit.md"
+++

A **one-sided limit** for a [[shared-foundations/function|function]] $f:D\to\mathbb R$ at $a\in\mathbb R$ is a number $L\in\mathbb R$ satisfying an $\varepsilon$–$\delta$ condition with $x$ restricted to one side of $a$:
- The right-hand limit $\lim_{x\to a^+} f(x)=L$ means: for every $\varepsilon>0$ there exists $\delta>0$ such that if $x\in D$ and $0<x-a<\delta$, then $|f(x)-L|<\varepsilon$.
- The left-hand limit $\lim_{x\to a^-} f(x)=L$ means: for every $\varepsilon>0$ there exists $\delta>0$ such that if $x\in D$ and $0<a-x<\delta$, then $|f(x)-L|<\varepsilon$.

One-sided limits refine the [[real-analysis/limit-at-a-point|limit at a point]] by tracking behavior on half-neighborhoods, and they are especially natural for functions defined on [[real-analysis/interval|intervals]] with endpoints. They are used to describe jump behavior at a [[real-analysis/discontinuity-point|discontinuity point]].

**Examples:**
- For $f(x)=|x|$, both $\lim_{x\to 0^-} f(x)$ and $\lim_{x\to 0^+} f(x)$ equal $0$.
- For $g(x)=\begin{cases}1,&x>0\\-1,&x<0\end{cases}$, one has $\lim_{x\to 0^+} g(x)=1$ and $\lim_{x\to 0^-} g(x)=-1$.
