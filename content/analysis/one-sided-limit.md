---
title: "One-sided limit"
description: "A limit as x approaches a from the left or from the right in ℝ."
---

Let $f:E\to\mathbb{R}$ (or $\mathbb{C}$) with $E\subseteq\mathbb{R}$, and let $a\in\mathbb{R}$ be a limit point of $E\cap(a,\infty)$. The **right-hand limit** of $f$ at $a$ is $L$ (written $\lim_{x\to a^+} f(x)=L$) if
$$\forall \varepsilon>0,\ \exists \delta>0\ \text{such that}\ \forall x\in E,\ \bigl(0<x-a<\delta \Rightarrow |f(x)-L|<\varepsilon\bigr).$$
Similarly, the **left-hand limit** $\lim_{x\to a^-} f(x)=L$ uses the condition $0<a-x<\delta$ (equivalently, $-\delta<x-a<0$).

One-sided limits are needed for functions defined on half-intervals and for describing jump discontinuities.

**Examples:**
- For the step function $f(x)=\mathbf{1}_{[0,\infty)}(x)$, $\lim_{x\to 0^-} f(x)=0$ and $\lim_{x\to 0^+} f(x)=1$.
- For $f(x)=1/x$, $\lim_{x\to 0^+} f(x)=+\infty$ and $\lim_{x\to 0^-} f(x)=-\infty$ in the extended real sense.
- If $f$ is continuous at $a$, then both one-sided limits exist and equal $f(a)$.
