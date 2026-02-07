---
title: "Riemann sum"
description: "A finite weighted sum approximating an integral using a tagged partition."
---

A **Riemann sum** of a bounded function $f:[a,b]\to\mathbb R$ with respect to a {{< knowl id="tagged-partition" text="tagged partition" >}} $(P,\{t_i\})$, where $P=\{x_0,\dots,x_n\}$, is the number
\[
S(f;P,\{t_i\})=\sum_{i=1}^n f(t_i)\,(x_i-x_{i-1}).
\]

Riemann sums approximate the {{< knowl id="riemann-integral" text="Riemann integral" >}}; the approximation is controlled by the {{< knowl id="mesh-of-a-partition" text="mesh" >}} $\|P\|$ becoming small.

**Examples:**
- If $f(x)=1$ on $[a,b]$, then every Riemann sum equals $b-a$.
- For $f(x)=x$ on $[0,1]$, take $P=\{0,\tfrac12,1\}$ and midpoint tags $t_1=\tfrac14$, $t_2=\tfrac34$. Then $S(f;P,\{t_i\})=\tfrac14\cdot\tfrac12+\tfrac34\cdot\tfrac12=\tfrac12$.
