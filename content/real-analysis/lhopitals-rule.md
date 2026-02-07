---
title: "L'Hôpital's rule"
description: "A method for evaluating certain indeterminate limits by comparing derivatives."
---

**L'Hôpital's rule (0/0 form, one-sided):** Let $f$ and $g$ be continuous on $[a,b)$ and differentiable on $(a,b)$, and assume that $g'(x)\neq 0$ for all $x\in(a,b)$. Suppose
$$
\lim_{x\to a^+} f(x)=0
\quad\text{and}\quad
\lim_{x\to a^+} g(x)=0,
$$

and that $g(x)\neq 0$ for all $x$ sufficiently close to $a$ with $x>a$. If the limit
$$
L=\lim_{x\to a^+}\frac{f'(x)}{g'(x)}
$$

exists (as a finite number or as $\pm\infty$), then the limit
$$
\lim_{x\to a^+}\frac{f(x)}{g(x)}
$$

also exists and equals $L$.

Analogous statements hold for left-hand limits and for the $\infty/\infty$ indeterminate form, and there are versions for {{< knowl id="limit-at-infinity" text="limits at infinity" >}}. The proof is based on the {{< knowl id="cauchy-mean-value-theorem" text="Cauchy mean value theorem" >}} and is formulated in terms of {{< knowl id="one-sided-limit" text="one-sided limits" >}}.
