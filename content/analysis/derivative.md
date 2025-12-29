---
title: "Derivative"
description: "The limit of the difference quotient, giving the best linear approximation at a point."
---

Let $f:E\to\mathbb{R}$ (or $\mathbb{C}$) with $E\subseteq\mathbb{R}$ and let $a\in E$ be a limit point of $E$. If the limit
$$\lim_{x\to a}\frac{f(x)-f(a)}{x-a}$$
exists, it is called the **derivative** of $f$ at $a$ and is denoted $f'(a)$.

Equivalently, $f$ is differentiable at $a$ iff there exists a number $L$ such that
$$f(a+h)=f(a)+Lh+o(h)\quad\text{as }h\to 0,$$
and then $L=f'(a)$.

**Examples:**
- If $f(x)=x^n$ with $n\in\mathbb{N}$, then $f'(a)=n a^{n-1}$.
- If $f(x)=e^x$, then $f'(a)=e^a$.
- If $f(x)=|x|$, then $f'(0)$ does not exist.
