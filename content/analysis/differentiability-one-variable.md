---
title: "Differentiability at a point (one-variable)"
description: "A real/complex function is differentiable at a point if its difference quotient has a limit."
---

Let $f:E\to\mathbb{R}$ (or $\mathbb{C}$) where $E\subseteq\mathbb{R}$, and let $a\in E$ be a limit point of $E$. The function $f$ is **differentiable at $a$** if the limit
$$\lim_{x\to a}\frac{f(x)-f(a)}{x-a}$$
exists (in $\mathbb{R}$ or $\mathbb{C}$). This limit, when it exists, is the derivative $f'(a)$.

Differentiability is a strong local regularity property: it implies continuity and gives the best linear approximation near $a$.

**Examples:**
- If $f(x)=x^2$, then $f'(a)=2a$ for all $a\in\mathbb{R}$.
- If $f(x)=|x|$, then $f$ is not differentiable at $a=0$ (left and right slopes differ), but it is differentiable for $a\ne 0$ with $f'(a)=\operatorname{sgn}(a)$.
- If $f(x)=\mathbf{1}_{\mathbb{Q}}(x)$, then $f$ is nowhere differentiable (it is nowhere continuous).
