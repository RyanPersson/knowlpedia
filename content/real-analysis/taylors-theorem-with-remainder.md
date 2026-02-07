---
title: "Taylor's theorem with remainder"
description: "Taylor expansion with an explicit remainder term for a smooth real function."
---

**Taylor's theorem with remainder:** Let $I\subseteq\mathbb R$ be an {{< knowl id="interval" text="interval" >}}, let $a\in I$, and let $f:I\to\mathbb R$ have continuous {{< knowl id="higher-derivatives" text="derivatives up to order" >}} $n+1$ on $I$. For each $x\in I$ there exists a point $\xi$ between $a$ and $x$ such that
$$
f(x)=\sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^k+\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}.
$$

The polynomial part is the {{< knowl id="taylor-polynomial" text="Taylor polynomial" >}} of degree $n$ at $a$, and the final term is the Lagrange-form remainder, which provides effective error bounds when $f^{(n+1)}$ is bounded.
