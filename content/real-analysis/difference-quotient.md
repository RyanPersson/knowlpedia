---
title: "Difference quotient"
description: "The ratio (f(x)-f(a))/(x-a) measuring average rate of change from a to x."
---

Let $f:E\to\mathbb{R}$ (or $\mathbb{C}$) with $E\subseteq\mathbb{R}$. For $a\in E$ and $x\in E$ with $x\ne a$, the **difference quotient** of $f$ at $(a,x)$ is
$$\frac{f(x)-f(a)}{x-a}.$$

Difference quotients are the finite approximations to the derivative. The derivative $f'(a)$, when it exists, is the limit of these quotients as $x\to a$.

**Examples:**
- If $f(x)=x^2$, then $\dfrac{f(x)-f(a)}{x-a}=\dfrac{x^2-a^2}{x-a}=x+a$.
- If $f(x)=\sin x$, then $\dfrac{\sin x-\sin a}{x-a}$ is an average rate of change that tends to $\cos a$ as $x\to a$.
- For $f(x)=|x|$ at $a=0$, the quotient is $\dfrac{|x|}{x}$, which equals $1$ for $x>0$ and $-1$ for $x<0$.
