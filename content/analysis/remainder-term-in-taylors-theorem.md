---
title: "Remainder term in Taylor's theorem"
description: "The difference f(x)−T_k f(x;a), measuring Taylor approximation error."
---

Let $f$ be a function for which the Taylor polynomial $T_k f(x;a)$ is defined. The **remainder term of order $k$** (about $a$) is the function
$$R_k(x;a):= f(x)-T_k f(x;a).$$

Taylor's theorem gives hypotheses under which $R_k(x;a)$ can be bounded or represented explicitly (e.g., Lagrange form or integral form), making the approximation $f(x)\approx T_k f(x;a)$ quantitatively precise.

**Examples:**
- If $f$ is a polynomial of degree $\le k$, then $R_k(x;a)\equiv 0$ for all $x$.
- For $f(x)=e^x$ about $a=0$, $R_1(x;0)=e^x-(1+x)$.
- For $f(x)=\sin x$ about $a=0$, $R_3(x;0)=\sin x-\left(x-\frac{x^3}{6}\right)$.
