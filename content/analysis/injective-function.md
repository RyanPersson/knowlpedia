---
title: "Injective function"
description: "A function that never maps two distinct inputs to the same output."
---

A {{< knowl id="function-map" text="function" >}} $f:X\to Y$ is **injective** (or **one-to-one**) if
$$\forall x_1,x_2\in X,\ \bigl(f(x_1)=f(x_2)\Rightarrow x_1=x_2\bigr).$$

Injectivity means that outputs uniquely determine inputs (within the {{< knowl id="domain" text="domain" >}}). This is the exact condition needed for a (two-sided) {{< knowl id="inverse-function" text="inverse function" >}} to exist after restricting the {{< knowl id="codomain" text="codomain" >}} to the {{< knowl id="image-range" text="image" >}}.

**Examples:**
- $f:\mathbb{R}\to\mathbb{R}$, $f(x)=x^3$ is injective.
- $f:\mathbb{R}\to\mathbb{R}$, $f(x)=x^2$ is not injective since $f(1)=f(-1)=1$.
- The restriction $x\mapsto x^2$ on $[0,\infty)$ is injective.
