---
title: "Injective function"
description: "A function that never maps two distinct inputs to the same output."
---

A function $f:X\to Y$ is **injective** (or **one-to-one**) if
$$\forall x_1,x_2\in X,\ \bigl(f(x_1)=f(x_2)\Rightarrow x_1=x_2\bigr).$$

Injectivity means that outputs uniquely determine inputs (within the domain). This is the exact condition needed for a (two-sided) inverse function to exist after restricting the codomain to the image.

**Examples:**
- $f:\mathbb{R}\to\mathbb{R}$, $f(x)=x^3$ is injective.
- $f:\mathbb{R}\to\mathbb{R}$, $f(x)=x^2$ is not injective since $f(1)=f(-1)=1$.
- The restriction $x\mapsto x^2$ on $[0,\infty)$ is injective.
