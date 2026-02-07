---
title: "Right derivative and left derivative"
description: "One-sided derivatives defined by one-sided limits of the difference quotient."
---

Let $f:E\to\mathbb{R}$ (or $\mathbb{C}$) with $E\subseteq\mathbb{R}$, and let $a\in E$ be a limit point of $E\cap(a,\infty)$ and of $E\cap(-\infty,a)$. The **right derivative** of $f$ at $a$ is
$$f'_+(a):=\lim_{h\downarrow 0}\frac{f(a+h)-f(a)}{h},$$
provided the limit exists. The **left derivative** is
$$f'_-(a):=\lim_{h\uparrow 0}\frac{f(a+h)-f(a)}{h},$$
provided the limit exists.

If both one-sided derivatives exist and are equal, then $f$ is differentiable at $a$ and $f'(a)=f'_+(a)=f'_-(a)$.

**Examples:**
- For $f(x)=|x|$, one has $f'_+(0)=1$ and $f'_-(0)=-1$, so $f'(0)$ does not exist.
- For $f(x)=x^2$, $f'_+(a)=f'_-(a)=2a$ for all $a$.
- For the step function $\mathbf{1}_{[0,\infty)}$, the one-sided derivatives at $0$ do not exist (difference quotient blows up).
